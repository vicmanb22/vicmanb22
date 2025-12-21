#!/usr/bin/env python3
"""Get a single Gmail message by ID.

Replaces: mcp__gmail-workspace__get_gmail_message_content

Usage:
    python3 gmail_get_message.py --email victor.lang22@gmail.com --message-id 18c123abc456
    python3 gmail_get_message.py --email victor.lang22@gmail.com --message-id 18c123abc456 --format metadata
"""

import argparse
import json
import sys
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from auth import get_gmail_service
from utils import (
    extract_headers,
    extract_body_from_payload,
    extract_attachments_info,
    parse_email_address,
    format_datetime,
    get_timezone,
    is_unread,
    is_starred,
    truncate_text,
    clean_text,
    output_success,
    output_error,
    retry_with_backoff,
    add_common_args
)


def get_message(
    service,
    message_id: str,
    format: str = 'full',
    timezone: str = None
) -> dict:
    """Get a message by ID.

    Args:
        service: Gmail API service
        message_id: Message ID
        format: Response format ('minimal', 'full', 'metadata', 'raw')
        timezone: Timezone for date formatting

    Returns:
        Formatted message dict
    """
    tz = get_timezone(timezone)

    request = service.users().messages().get(
        userId='me',
        id=message_id,
        format=format
    )

    msg = retry_with_backoff(request.execute)

    return format_message(msg, tz, include_body=(format == 'full'))


def format_message(msg: dict, tz, include_body: bool = True) -> dict:
    """Format a Gmail message into a clean structure.

    Args:
        msg: Raw Gmail message dict
        tz: Timezone for date formatting
        include_body: Whether to include the message body

    Returns:
        Formatted message dict
    """
    payload = msg.get('payload', {})
    headers = extract_headers(payload.get('headers', []))

    # Parse sender
    from_header = headers.get('From', '')
    from_parsed = parse_email_address(from_header)

    # Format date
    internal_date = msg.get('internalDate', '0')
    date_formatted = format_datetime(internal_date, tz)

    # Get labels
    label_ids = msg.get('labelIds', [])

    result = {
        'id': msg.get('id'),
        'threadId': msg.get('threadId'),
        'from': from_header,
        'from_name': from_parsed['name'],
        'from_email': from_parsed['email'],
        'to': headers.get('To', ''),
        'cc': headers.get('Cc', ''),
        'subject': headers.get('Subject', '(no subject)'),
        'date': date_formatted['display'],
        'date_iso': date_formatted['iso'],
        'snippet': clean_text(msg.get('snippet', '')),
        'labels': label_ids,
        'is_unread': is_unread(label_ids),
        'is_starred': is_starred(label_ids)
    }

    # Add body if requested
    if include_body:
        body = extract_body_from_payload(payload)
        result['body_plain'] = body.get('plain', '')
        result['body_html'] = body.get('html', '')

        # Add attachments info
        attachments = extract_attachments_info(payload)
        if attachments:
            result['attachments'] = attachments

    # Add optional headers if present
    if headers.get('Reply-To'):
        result['reply_to'] = headers['Reply-To']
    if headers.get('In-Reply-To'):
        result['in_reply_to'] = headers['In-Reply-To']

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Get a Gmail message by ID'
    )
    add_common_args(parser)
    parser.add_argument(
        '--message-id',
        required=True,
        help='Gmail message ID'
    )
    parser.add_argument(
        '--format',
        choices=['minimal', 'full', 'metadata', 'raw'],
        default='full',
        help='Response format (default: full)'
    )

    args = parser.parse_args()

    try:
        service = get_gmail_service(args.email)
        message = get_message(
            service,
            args.message_id,
            format=args.format,
            timezone=args.timezone
        )
        output_success({'message': message})

    except FileNotFoundError as e:
        output_error(str(e), 'CREDENTIALS_NOT_FOUND', exit_code=3)

    except Exception as e:
        error_type = 'API_ERROR'
        exit_code = 2

        error_str = str(e)
        if 'invalid_grant' in error_str.lower():
            error_type = 'AUTH_ERROR'
            exit_code = 3
        elif 'not found' in error_str.lower():
            error_type = 'NOT_FOUND'
            exit_code = 1

        output_error(str(e), error_type, exit_code=exit_code)


if __name__ == '__main__':
    main()
