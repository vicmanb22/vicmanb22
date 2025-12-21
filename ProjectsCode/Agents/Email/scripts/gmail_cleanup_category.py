#!/usr/bin/env python3
"""Scan Gmail category and aggregate emails by sender for cleanup.

Scans Promotions, Social, or Updates category and returns sender aggregation
with counts, domains, latest message IDs, and Gmail links for review.

Usage:
    python3 gmail_cleanup_category.py --email vlang@cloudviewre.com --category promotions
    python3 gmail_cleanup_category.py --email vlang@cloudviewre.com --category updates --max-results 500
    python3 gmail_cleanup_category.py --email vlang@cloudviewre.com --category social --min-count 2
"""

# Suppress warnings before any other imports
import warnings
warnings.filterwarnings('ignore')

import argparse
import json
import logging
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# Suppress Google API discovery cache warnings
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from auth import get_gmail_service
from utils import (
    get_timezone,
    parse_email_address,
    format_date_short,
    time_ago,
    output_success,
    output_error,
    retry_with_backoff,
    add_common_args
)


def normalize_domain(domain: str) -> str:
    """Normalize domain to parent domain for searching.

    Examples:
        shared1.ccsend.com -> ccsend.com
        learn.mail.monday.com -> monday.com
        mail.feedback.xero.com -> xero.com
        essexrealtygroup.com -> essexrealtygroup.com
    """
    if not domain:
        return domain

    parts = domain.lower().split('.')

    # Common marketing/email subdomains to strip
    marketing_prefixes = [
        'mail', 'email', 'news', 'newsletter', 'updates', 'notifications',
        'info', 'noreply', 'no-reply', 'marketing', 'promo', 'shared1',
        'shared2', 'learn', 'feedback', 'messaging', 'send', 'bounce'
    ]

    # Strip known prefixes
    while len(parts) > 2 and parts[0] in marketing_prefixes:
        parts = parts[1:]

    # Handle special cases like ccsend.com (Constant Contact)
    if len(parts) >= 2:
        return '.'.join(parts[-2:])

    return domain


def get_gmail_link(email: str, message_id: str) -> str:
    """Generate Gmail web link for a message.

    Args:
        email: Email account (to determine user index)
        message_id: Gmail message ID

    Returns:
        Gmail web URL
    """
    # For simplicity, use u/0 - could enhance to detect user index
    return f"https://mail.google.com/mail/u/0/#inbox/{message_id}"


def scan_category(
    service,
    category: str,
    max_results: int = 200,
    tz=None
) -> dict:
    """Scan a Gmail category and return message details.

    Args:
        service: Gmail API service
        category: 'promotions', 'social', or 'updates'
        max_results: Maximum messages to scan
        tz: Timezone for date formatting

    Returns:
        Dict with messages list
    """
    query = f"category:{category}"

    messages = []
    page_token = None

    while len(messages) < max_results:
        result = retry_with_backoff(
            service.users().messages().list(
                userId='me',
                q=query,
                maxResults=min(100, max_results - len(messages)),
                pageToken=page_token
            ).execute
        )

        batch_messages = result.get('messages', [])
        if not batch_messages:
            break

        messages.extend(batch_messages)

        page_token = result.get('nextPageToken')
        if not page_token:
            break

    return {
        'messages': messages,
        'total': len(messages)
    }


def fetch_message_metadata(service, message_ids: list) -> list:
    """Batch fetch message metadata.

    Args:
        service: Gmail API service
        message_ids: List of message IDs

    Returns:
        List of message metadata dicts
    """
    messages = []

    # Process in batches of 100
    for i in range(0, len(message_ids), 100):
        batch_ids = message_ids[i:i + 100]
        batch_results = {}
        batch_errors = {}

        def callback(request_id, response, exception):
            if exception:
                batch_errors[request_id] = str(exception)
            else:
                batch_results[request_id] = response

        batch = service.new_batch_http_request(callback=callback)

        for msg_id in batch_ids:
            batch.add(
                service.users().messages().get(
                    userId='me',
                    id=msg_id,
                    format='metadata',
                    metadataHeaders=['From', 'Subject', 'Date']
                ),
                request_id=msg_id
            )

        batch.execute()

        for msg_id in batch_ids:
            if msg_id in batch_results:
                msg = batch_results[msg_id]
                headers = {h['name']: h['value'] for h in msg.get('payload', {}).get('headers', [])}

                from_header = headers.get('From', '')
                parsed = parse_email_address(from_header)
                from_name = parsed.get('name', '')
                from_email = parsed.get('email', '')

                messages.append({
                    'id': msg_id,
                    'from_name': from_name or from_email,
                    'from_email': from_email,
                    'subject': headers.get('Subject', ''),
                    'date': headers.get('Date', ''),
                    'labels': msg.get('labelIds', [])
                })

    return messages


def aggregate_by_sender(messages: list, email: str, min_count: int = 1) -> list:
    """Aggregate messages by sender domain.

    Args:
        messages: List of message metadata
        email: Account email for Gmail links
        min_count: Minimum count to include sender

    Returns:
        List of sender aggregations sorted by count descending
    """
    senders = defaultdict(lambda: {
        'count': 0,
        'from_name': '',
        'from_email': '',
        'domain': '',
        'normalized_domain': '',
        'message_ids': [],
        'latest_id': '',
        'latest_date': '',
        'latest_subject': ''
    })

    for msg in messages:
        from_email = msg.get('from_email', '')
        if not from_email or '@' not in from_email:
            continue

        domain = from_email.split('@')[-1].lower()
        normalized = normalize_domain(domain)

        sender = senders[normalized]
        sender['count'] += 1
        sender['message_ids'].append(msg['id'])

        # Keep first (most recent) message details
        if not sender['latest_id']:
            sender['from_name'] = msg.get('from_name', '')
            sender['from_email'] = from_email
            sender['domain'] = domain
            sender['normalized_domain'] = normalized
            sender['latest_id'] = msg['id']
            sender['latest_date'] = msg.get('date', '')
            sender['latest_subject'] = msg.get('subject', '')

    # Convert to list and filter by min_count
    result = []
    for domain, info in senders.items():
        if info['count'] >= min_count:
            info['gmail_link'] = get_gmail_link(email, info['latest_id'])
            result.append(info)

    # Sort by count descending
    result.sort(key=lambda x: -x['count'])

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Scan Gmail category and aggregate by sender for cleanup'
    )
    add_common_args(parser)

    parser.add_argument(
        '--category',
        required=True,
        choices=['promotions', 'social', 'updates'],
        help='Gmail category to scan'
    )
    parser.add_argument(
        '--max-results',
        type=int,
        default=200,
        help='Maximum messages to scan (default: 200)'
    )
    parser.add_argument(
        '--min-count',
        type=int,
        default=1,
        help='Minimum email count to include sender (default: 1)'
    )

    args = parser.parse_args()

    try:
        service = get_gmail_service(args.email)
        tz = get_timezone(args.timezone)

        # Scan category
        scan_result = scan_category(
            service,
            args.category,
            max_results=args.max_results,
            tz=tz
        )

        if not scan_result['messages']:
            output_success({
                'category': args.category,
                'senders': [],
                'total_messages': 0,
                'total_senders': 0
            })
            return

        # Fetch metadata
        message_ids = [m['id'] for m in scan_result['messages']]
        messages = fetch_message_metadata(service, message_ids)

        # Aggregate by sender
        senders = aggregate_by_sender(messages, args.email, args.min_count)

        output_success({
            'category': args.category,
            'senders': senders,
            'total_messages': scan_result['total'],
            'total_senders': len(senders)
        })

    except Exception as e:
        output_error(str(e))
        sys.exit(1)


if __name__ == '__main__':
    main()
