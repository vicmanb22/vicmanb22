#!/usr/bin/env python3
"""Get a Gmail thread by ID.

Replaces: mcp__gmail-workspace__get_gmail_thread_content

Usage:
    python3 gmail_get_thread.py --email victor.lang22@gmail.com --thread-id 18c123abc456
"""

import argparse
import json
import sys
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from auth import get_gmail_service
from gmail_get_message import format_message
from utils import (
    get_timezone,
    output_success,
    output_error,
    retry_with_backoff,
    add_common_args
)


def get_thread(
    service,
    thread_id: str,
    format: str = 'full',
    timezone: str = None
) -> dict:
    """Get a thread by ID.

    Args:
        service: Gmail API service
        thread_id: Thread ID
        format: Response format ('minimal', 'full', 'metadata')
        timezone: Timezone for date formatting

    Returns:
        Dict with thread info and messages
    """
    tz = get_timezone(timezone)

    request = service.users().threads().get(
        userId='me',
        id=thread_id,
        format=format
    )

    thread = retry_with_backoff(request.execute)

    # Format all messages in the thread
    messages = []
    for msg in thread.get('messages', []):
        formatted = format_message(msg, tz, include_body=(format == 'full'))
        messages.append(formatted)

    return {
        'id': thread.get('id'),
        'historyId': thread.get('historyId'),
        'messages': messages,
        'message_count': len(messages)
    }


def main():
    parser = argparse.ArgumentParser(
        description='Get a Gmail thread by ID'
    )
    add_common_args(parser)
    parser.add_argument(
        '--thread-id',
        required=True,
        help='Gmail thread ID'
    )
    parser.add_argument(
        '--format',
        choices=['minimal', 'full', 'metadata'],
        default='full',
        help='Response format (default: full)'
    )

    args = parser.parse_args()

    try:
        service = get_gmail_service(args.email)
        thread = get_thread(
            service,
            args.thread_id,
            format=args.format,
            timezone=args.timezone
        )
        output_success({'thread': thread})

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
