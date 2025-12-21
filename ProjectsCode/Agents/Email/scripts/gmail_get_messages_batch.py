#!/usr/bin/env python3
"""Get multiple Gmail messages in batch.

Replaces: mcp__gmail-workspace__get_gmail_messages_content_batch

Usage:
    python3 gmail_get_messages_batch.py --email victor.lang22@gmail.com --message-ids "id1,id2,id3"
    python3 gmail_get_messages_batch.py --email victor.lang22@gmail.com --message-ids "id1,id2" --format metadata
"""

# Suppress warnings before any other imports
import warnings
warnings.filterwarnings('ignore')

import argparse
import json
import logging
import sys
from pathlib import Path

# Suppress Google API discovery cache warnings
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from auth import get_gmail_service
from gmail_get_message import format_message
from utils import (
    get_timezone,
    output_success,
    output_error,
    add_common_args
)

# Maximum messages per batch (Gmail API limit is 100)
MAX_BATCH_SIZE = 100


def get_messages_batch(
    service,
    message_ids: list,
    format: str = 'metadata',
    timezone: str = None
) -> dict:
    """Get multiple messages by ID using batch requests.

    Args:
        service: Gmail API service
        message_ids: List of message IDs
        format: Response format ('minimal', 'full', 'metadata')
        timezone: Timezone for date formatting

    Returns:
        Dict with messages list, count, and any errors
    """
    from googleapiclient.http import BatchHttpRequest

    tz = get_timezone(timezone)
    messages = []
    errors = []

    # Process in batches of MAX_BATCH_SIZE
    for batch_start in range(0, len(message_ids), MAX_BATCH_SIZE):
        batch_ids = message_ids[batch_start:batch_start + MAX_BATCH_SIZE]
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
                    format=format
                ),
                request_id=msg_id
            )

        batch.execute()

        # Process results
        for msg_id in batch_ids:
            if msg_id in batch_results:
                formatted = format_message(
                    batch_results[msg_id],
                    tz,
                    include_body=(format == 'full')
                )
                messages.append(formatted)
            elif msg_id in batch_errors:
                errors.append({
                    'id': msg_id,
                    'error': batch_errors[msg_id]
                })

    return {
        'messages': messages,
        'count': len(messages),
        'errors': errors if errors else None
    }


def main():
    parser = argparse.ArgumentParser(
        description='Get multiple Gmail messages by ID'
    )
    add_common_args(parser)
    parser.add_argument(
        '--message-ids',
        required=True,
        help='Comma-separated list of message IDs'
    )
    parser.add_argument(
        '--format',
        choices=['minimal', 'full', 'metadata'],
        default='metadata',
        help='Response format (default: metadata)'
    )

    args = parser.parse_args()

    # Parse message IDs
    message_ids = [id.strip() for id in args.message_ids.split(',') if id.strip()]

    if not message_ids:
        output_error('No message IDs provided', 'INVALID_INPUT', exit_code=1)

    try:
        service = get_gmail_service(args.email)
        result = get_messages_batch(
            service,
            message_ids,
            format=args.format,
            timezone=args.timezone
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
