#!/usr/bin/env python3
"""Extract known contacts from sent emails.

This script searches the sent folder and extracts unique recipient email addresses.
Used to identify "known contacts" for the "Needs Response" detection in email digest.

New capability (not in MCP).

Usage:
    python3 gmail_get_known_contacts.py --email victor.lang22@gmail.com
    python3 gmail_get_known_contacts.py --email victor.lang22@gmail.com --days 90
"""

import argparse
import json
import re
import sys
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from auth import get_gmail_service
from utils import (
    output_success,
    output_error,
    retry_with_backoff,
    add_common_args
)

# Email addresses to exclude (automated/noreply)
EXCLUDED_PATTERNS = [
    r'^noreply@',
    r'^no-reply@',
    r'^notifications?@',
    r'^alerts?@',
    r'^mailer-daemon@',
    r'^postmaster@',
    r'^donotreply@',
    r'^do-not-reply@',
    r'^bounce@',
    r'^feedback@',
    r'^support@.*\.zendesk\.com$',
    r'^.*@.*\.intercom-mail\.com$',
]


def is_excluded_email(email: str) -> bool:
    """Check if an email address should be excluded."""
    email_lower = email.lower()
    for pattern in EXCLUDED_PATTERNS:
        if re.match(pattern, email_lower):
            return True
    return False


def extract_emails_from_header(header: str) -> list:
    """Extract all email addresses from a header value.

    Handles formats like:
    - "Name <email@example.com>"
    - "email@example.com"
    - "Name <a@x.com>, Other <b@x.com>"
    """
    emails = []
    # Match email patterns
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    matches = re.findall(pattern, header)
    for email in matches:
        if not is_excluded_email(email):
            emails.append(email.lower())
    return emails


def get_known_contacts(
    service,
    days: int = 90,
    max_messages: int = 500
) -> dict:
    """Extract unique recipient emails from sent messages.

    Args:
        service: Gmail API service
        days: Number of days to look back
        max_messages: Maximum sent messages to scan

    Returns:
        Dict with unique contact emails
    """
    query = f'in:sent newer_than:{days}d'

    # Search sent messages using messages.list
    all_message_ids = []
    page_token = None

    while len(all_message_ids) < max_messages:
        request = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=min(100, max_messages - len(all_message_ids)),
            pageToken=page_token
        )
        result = retry_with_backoff(request.execute)

        messages = result.get('messages', [])
        all_message_ids.extend([m['id'] for m in messages])

        page_token = result.get('nextPageToken')
        if not page_token:
            break

    # Get message headers in batches using batch requests
    contacts = set()

    for batch_start in range(0, len(all_message_ids), 100):
        batch_ids = all_message_ids[batch_start:batch_start + 100]
        batch_results = {}

        def callback(request_id, response, exception):
            if not exception:
                batch_results[request_id] = response

        batch = service.new_batch_http_request(callback=callback)

        for msg_id in batch_ids:
            batch.add(
                service.users().messages().get(
                    userId='me',
                    id=msg_id,
                    format='metadata',
                    metadataHeaders=['To', 'Cc', 'Bcc']
                ),
                request_id=msg_id
            )

        batch.execute()

        # Extract recipients from headers
        for msg_id, msg in batch_results.items():
            payload = msg.get('payload', {})
            headers = payload.get('headers', [])

            for header in headers:
                name = header.get('name', '')
                if name in ['To', 'Cc', 'Bcc']:
                    emails = extract_emails_from_header(header.get('value', ''))
                    contacts.update(emails)

    # Sort contacts alphabetically
    sorted_contacts = sorted(contacts)

    return {
        'contacts': sorted_contacts,
        'count': len(sorted_contacts),
        'messages_scanned': len(all_message_ids),
        'days': days
    }


def main():
    parser = argparse.ArgumentParser(
        description='Extract known contacts from sent emails'
    )
    add_common_args(parser)
    parser.add_argument(
        '--days',
        type=int,
        default=90,
        help='Number of days to look back (default: 90)'
    )
    parser.add_argument(
        '--max-messages',
        type=int,
        default=500,
        help='Maximum messages to scan (default: 500)'
    )

    args = parser.parse_args()

    try:
        service = get_gmail_service(args.email)
        result = get_known_contacts(
            service,
            days=args.days,
            max_messages=args.max_messages
        )
        output_success(result)

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
