#!/usr/bin/env python3
"""List email subscriptions aggregated by sender.

Scans inbox for subscription emails and aggregates them by sender,
showing frequency metrics and unsubscribe method availability.

Usage:
    python3 gmail_list_subscriptions.py --email victor.lang22@gmail.com
    python3 gmail_list_subscriptions.py --email victor.lang22@gmail.com --days 30
    python3 gmail_list_subscriptions.py --email victor.lang22@gmail.com --min-count 3
"""

# Suppress warnings before any other imports
import warnings
warnings.filterwarnings('ignore')

import argparse
import json
import logging
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

# Suppress Google API discovery cache warnings
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from auth import get_gmail_service
from utils import (
    get_timezone,
    parse_email_address,
    extract_headers,
    extract_body_from_payload,
    decode_base64url,
    format_date_short,
    time_ago,
    output_success,
    output_error,
    retry_with_backoff,
    add_common_args
)


def get_list_unsubscribe_header(headers: list) -> dict:
    """Extract List-Unsubscribe and List-Unsubscribe-Post headers.

    Args:
        headers: List of {'name': ..., 'value': ...} dicts

    Returns:
        Dict with 'url', 'mailto', 'has_one_click' keys
    """
    result = {
        'url': None,
        'mailto': None,
        'has_one_click': False
    }

    for h in headers:
        name = h.get('name', '').lower()
        value = h.get('value', '')

        if name == 'list-unsubscribe':
            # Parse URLs from header like: <mailto:unsub@example.com>, <https://example.com/unsub>
            urls = re.findall(r'<([^>]+)>', value)
            for url in urls:
                if url.startswith('mailto:'):
                    result['mailto'] = url
                elif url.startswith('http'):
                    result['url'] = url

        elif name == 'list-unsubscribe-post':
            if 'List-Unsubscribe=One-Click' in value:
                result['has_one_click'] = True

    return result


def find_unsubscribe_link_in_body(html: str) -> str:
    """Find unsubscribe link in HTML body.

    Args:
        html: HTML content of email body

    Returns:
        First unsubscribe URL found, or None
    """
    if not html:
        return None

    # Look for href attributes containing 'unsubscribe'
    pattern = r'href=["\']([^"\']*unsubscribe[^"\']*)["\']'
    matches = re.findall(pattern, html, re.IGNORECASE)

    for url in matches:
        # Validate it's a proper URL
        if url.startswith('http'):
            return url

    return None


def determine_unsubscribe_method(unsub_header: dict, body_link: str) -> str:
    """Determine the best unsubscribe method available.

    Args:
        unsub_header: Result from get_list_unsubscribe_header()
        body_link: Unsubscribe link found in body, or None

    Returns:
        One of: 'post', 'mailto', 'link', 'manual', 'none'
    """
    if unsub_header['url'] and unsub_header['has_one_click']:
        return 'post'  # RFC 8058 one-click
    elif unsub_header['mailto']:
        return 'mailto'
    elif unsub_header['url']:
        return 'link'  # GET request to URL
    elif body_link:
        return 'link'  # Body link fallback
    else:
        return 'none'


def get_gmail_web_link(email: str, message_id: str) -> str:
    """Generate Gmail web interface link for a message.

    Args:
        email: Account email address
        message_id: Gmail message ID

    Returns:
        URL to open message in Gmail web
    """
    # Determine account index (0 for primary, 1+ for additional)
    # For simplicity, use 0 - user can adjust if needed
    return f"https://mail.google.com/mail/u/0/#inbox/{message_id}"


def search_subscriptions(service, days: int = 90, max_results: int = 500) -> list:
    """Search for subscription emails.

    Args:
        service: Gmail API service
        days: Number of days to look back
        max_results: Maximum messages to retrieve

    Returns:
        List of message IDs
    """
    # Query to find subscription emails
    query = f'newer_than:{days}d (has:unsubscribe OR list:* OR from:newsletter OR from:noreply OR from:notifications)'

    messages = []
    page_token = None

    while len(messages) < max_results:
        page_size = min(100, max_results - len(messages))

        request = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=page_size,
            pageToken=page_token,
            includeSpamTrash=False
        )

        result = retry_with_backoff(request.execute)

        batch_messages = result.get('messages', [])
        messages.extend(batch_messages)

        page_token = result.get('nextPageToken')
        if not page_token:
            break

    return [m['id'] for m in messages[:max_results]]


def get_message_metadata(service, message_ids: list) -> list:
    """Batch fetch message metadata.

    Args:
        service: Gmail API service
        message_ids: List of message IDs

    Returns:
        List of message metadata dicts
    """
    messages = []

    # Process in batches of 100
    for batch_start in range(0, len(message_ids), 100):
        batch_ids = message_ids[batch_start:batch_start + 100]
        batch_results = {}

        def callback(request_id, response, exception):
            if exception is None:
                batch_results[request_id] = response

        batch = service.new_batch_http_request(callback=callback)

        for msg_id in batch_ids:
            batch.add(
                service.users().messages().get(
                    userId='me',
                    id=msg_id,
                    format='metadata',
                    metadataHeaders=['From', 'Subject', 'Date', 'List-Unsubscribe', 'List-Unsubscribe-Post']
                ),
                request_id=msg_id
            )

        batch.execute()

        for msg_id in batch_ids:
            if msg_id in batch_results:
                messages.append(batch_results[msg_id])

    return messages


def aggregate_by_sender(messages: list, email: str, tz) -> list:
    """Aggregate messages by sender domain.

    Args:
        messages: List of message metadata
        email: Account email for generating Gmail links
        tz: Timezone for date formatting

    Returns:
        List of subscription dicts, sorted by count descending
    """
    senders = defaultdict(lambda: {
        'sender_email': None,
        'sender_name': None,
        'domain': None,
        'messages': [],
        'has_list_unsubscribe': False,
        'unsubscribe_method': 'none',
        'unsubscribe_url': None,
        'unsubscribe_mailto': None,
    })

    for msg in messages:
        headers = msg.get('payload', {}).get('headers', [])
        header_dict = extract_headers(headers)

        from_header = header_dict.get('From', '')
        parsed = parse_email_address(from_header)
        sender_email = parsed['email'].lower() if parsed['email'] else ''
        sender_name = parsed['name']

        if not sender_email:
            continue

        # Extract domain
        domain = sender_email.split('@')[-1] if '@' in sender_email else sender_email

        # Get unsubscribe info
        unsub_header = get_list_unsubscribe_header(headers)

        # Use domain as key for aggregation
        key = domain

        senders[key]['sender_email'] = sender_email
        senders[key]['sender_name'] = sender_name or sender_email.split('@')[0]
        senders[key]['domain'] = domain
        senders[key]['messages'].append({
            'id': msg['id'],
            'subject': header_dict.get('Subject', '(no subject)'),
            'date_ms': int(msg.get('internalDate', 0)),
        })

        # Update unsubscribe info if better method available
        current_method = senders[key]['unsubscribe_method']
        new_method = determine_unsubscribe_method(unsub_header, None)

        method_priority = {'post': 4, 'mailto': 3, 'link': 2, 'manual': 1, 'none': 0}
        if method_priority.get(new_method, 0) > method_priority.get(current_method, 0):
            senders[key]['unsubscribe_method'] = new_method
            senders[key]['unsubscribe_url'] = unsub_header['url']
            senders[key]['unsubscribe_mailto'] = unsub_header['mailto']
            senders[key]['has_list_unsubscribe'] = bool(unsub_header['url'] or unsub_header['mailto'])

    # Convert to list and add computed fields
    now = datetime.now(timezone.utc)
    thirty_days_ago = now - timedelta(days=30)

    result = []
    for key, data in senders.items():
        messages = data['messages']

        # Sort messages by date descending
        messages.sort(key=lambda m: m['date_ms'], reverse=True)

        # Get latest message
        latest = messages[0]
        latest_date_ms = latest['date_ms']

        # Count by time period
        count_30d = sum(1 for m in messages if m['date_ms'] > thirty_days_ago.timestamp() * 1000)
        count_total = len(messages)

        result.append({
            'sender_email': data['sender_email'],
            'sender_name': data['sender_name'],
            'domain': data['domain'],
            'count_30d': count_30d,
            'count_total': count_total,
            'last_received': format_date_short(latest_date_ms, tz),
            'last_received_ago': time_ago(latest_date_ms, tz),
            'latest_subject': latest['subject'],
            'latest_message_id': latest['id'],
            'gmail_link': get_gmail_web_link(email, latest['id']),
            'has_list_unsubscribe': data['has_list_unsubscribe'],
            'unsubscribe_method': data['unsubscribe_method'],
            'unsubscribe_url': data['unsubscribe_url'],
            'unsubscribe_mailto': data['unsubscribe_mailto'],
        })

    # Sort by 30-day count descending
    result.sort(key=lambda x: x['count_30d'], reverse=True)

    return result


def main():
    parser = argparse.ArgumentParser(
        description='List email subscriptions aggregated by sender'
    )
    add_common_args(parser)
    parser.add_argument(
        '--days',
        type=int,
        default=90,
        help='Number of days to look back (default: 90)'
    )
    parser.add_argument(
        '--max-results',
        type=int,
        default=500,
        help='Maximum messages to scan (default: 500)'
    )
    parser.add_argument(
        '--min-count',
        type=int,
        default=1,
        help='Minimum message count to include sender (default: 1)'
    )

    args = parser.parse_args()

    try:
        service = get_gmail_service(args.email)
        tz = get_timezone(args.timezone)

        # Search for subscription emails
        message_ids = search_subscriptions(
            service,
            days=args.days,
            max_results=args.max_results
        )

        if not message_ids:
            output_success({
                'subscriptions': [],
                'total_senders': 0,
                'total_messages': 0,
                'days_scanned': args.days
            })

        # Fetch metadata
        messages = get_message_metadata(service, message_ids)

        # Aggregate by sender
        subscriptions = aggregate_by_sender(messages, args.email, tz)

        # Filter by minimum count
        if args.min_count > 1:
            subscriptions = [s for s in subscriptions if s['count_total'] >= args.min_count]

        output_success({
            'subscriptions': subscriptions,
            'total_senders': len(subscriptions),
            'total_messages': len(message_ids),
            'days_scanned': args.days
        })

    except FileNotFoundError as e:
        output_error(str(e), 'CREDENTIALS_NOT_FOUND', exit_code=3)

    except Exception as e:
        error_type = 'API_ERROR'
        exit_code = 2

        error_str = str(e)
        if 'invalid_grant' in error_str.lower():
            error_type = 'AUTH_ERROR'
            exit_code = 3

        output_error(str(e), error_type, exit_code=exit_code)


if __name__ == '__main__':
    main()
