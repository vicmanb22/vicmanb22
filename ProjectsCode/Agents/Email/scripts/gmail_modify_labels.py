#!/usr/bin/env python3
"""Modify labels on Gmail messages.

Replaces: mcp__gmail-workspace__modify_gmail_message_labels

Usage:
    # Mark as read
    python3 gmail_modify_labels.py --email victor.lang22@gmail.com --message-id "abc123" --remove-labels "UNREAD"

    # Archive (remove from inbox)
    python3 gmail_modify_labels.py --email victor.lang22@gmail.com --message-id "abc123" --remove-labels "INBOX"

    # Star a message
    python3 gmail_modify_labels.py --email victor.lang22@gmail.com --message-id "abc123" --add-labels "STARRED"

    # Multiple operations
    python3 gmail_modify_labels.py --email victor.lang22@gmail.com --message-id "abc123" --add-labels "STARRED" --remove-labels "UNREAD,INBOX"

    # Batch modify multiple messages
    python3 gmail_modify_labels.py --email victor.lang22@gmail.com --message-ids "id1,id2,id3" --remove-labels "UNREAD"
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
from utils import (
    output_success,
    output_error,
    retry_with_backoff,
    add_common_args
)


def modify_message_labels(
    service,
    message_id: str,
    add_labels: list = None,
    remove_labels: list = None
) -> dict:
    """Modify labels on a single message.

    Args:
        service: Gmail API service
        message_id: Message ID
        add_labels: Label IDs to add
        remove_labels: Label IDs to remove

    Returns:
        Dict with updated message info
    """
    body = {}
    if add_labels:
        body['addLabelIds'] = add_labels
    if remove_labels:
        body['removeLabelIds'] = remove_labels

    request = service.users().messages().modify(
        userId='me',
        id=message_id,
        body=body
    )

    result = retry_with_backoff(request.execute)

    return {
        'id': result.get('id'),
        'threadId': result.get('threadId'),
        'labelIds': result.get('labelIds', [])
    }


def batch_modify_labels(
    service,
    message_ids: list,
    add_labels: list = None,
    remove_labels: list = None
) -> dict:
    """Modify labels on multiple messages using batch requests.

    Args:
        service: Gmail API service
        message_ids: List of message IDs
        add_labels: Label IDs to add
        remove_labels: Label IDs to remove

    Returns:
        Dict with results and any errors
    """
    body = {}
    if add_labels:
        body['addLabelIds'] = add_labels
    if remove_labels:
        body['removeLabelIds'] = remove_labels

    results = []
    errors = []

    # Process in batches of 100
    for batch_start in range(0, len(message_ids), 100):
        batch_ids = message_ids[batch_start:batch_start + 100]
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
                service.users().messages().modify(
                    userId='me',
                    id=msg_id,
                    body=body
                ),
                request_id=msg_id
            )

        batch.execute()

        # Process results
        for msg_id in batch_ids:
            if msg_id in batch_results:
                results.append({
                    'id': batch_results[msg_id].get('id'),
                    'labelIds': batch_results[msg_id].get('labelIds', [])
                })
            elif msg_id in batch_errors:
                errors.append({
                    'id': msg_id,
                    'error': batch_errors[msg_id]
                })

    return {
        'modified': results,
        'count': len(results),
        'errors': errors if errors else None
    }


def parse_labels(label_string: str) -> list:
    """Parse comma-separated label string into list."""
    if not label_string:
        return []
    return [l.strip() for l in label_string.split(',') if l.strip()]


def main():
    parser = argparse.ArgumentParser(
        description='Modify labels on Gmail messages'
    )
    add_common_args(parser)

    # Message selection (one of these required)
    msg_group = parser.add_mutually_exclusive_group(required=True)
    msg_group.add_argument(
        '--message-id',
        help='Single message ID'
    )
    msg_group.add_argument(
        '--message-ids',
        help='Comma-separated list of message IDs for batch operation'
    )

    # Label modifications
    parser.add_argument(
        '--add-labels',
        help='Label IDs to add, comma-separated (e.g., "STARRED,IMPORTANT")'
    )
    parser.add_argument(
        '--remove-labels',
        help='Label IDs to remove, comma-separated (e.g., "UNREAD,INBOX")'
    )

    # Convenience shortcuts
    parser.add_argument(
        '--mark-read',
        action='store_true',
        help='Shortcut to remove UNREAD label'
    )
    parser.add_argument(
        '--mark-unread',
        action='store_true',
        help='Shortcut to add UNREAD label'
    )
    parser.add_argument(
        '--archive',
        action='store_true',
        help='Shortcut to remove INBOX label'
    )
    parser.add_argument(
        '--star',
        action='store_true',
        help='Shortcut to add STARRED label'
    )
    parser.add_argument(
        '--unstar',
        action='store_true',
        help='Shortcut to remove STARRED label'
    )
    parser.add_argument(
        '--trash',
        action='store_true',
        help='Shortcut to add TRASH label'
    )

    args = parser.parse_args()

    # Build label lists from arguments
    add_labels = parse_labels(args.add_labels)
    remove_labels = parse_labels(args.remove_labels)

    # Apply shortcuts
    if args.mark_read:
        remove_labels.append('UNREAD')
    if args.mark_unread:
        add_labels.append('UNREAD')
    if args.archive:
        remove_labels.append('INBOX')
    if args.star:
        add_labels.append('STARRED')
    if args.unstar:
        remove_labels.append('STARRED')
    if args.trash:
        add_labels.append('TRASH')

    # Validate we have something to do
    if not add_labels and not remove_labels:
        output_error(
            'No label modifications specified. Use --add-labels, --remove-labels, or shortcuts like --mark-read',
            'INVALID_INPUT',
            exit_code=1
        )

    try:
        service = get_gmail_service(args.email)

        if args.message_id:
            # Single message
            result = modify_message_labels(
                service,
                args.message_id,
                add_labels=add_labels if add_labels else None,
                remove_labels=remove_labels if remove_labels else None
            )
            output_success({'message': result})
        else:
            # Batch operation
            message_ids = [id.strip() for id in args.message_ids.split(',') if id.strip()]
            if not message_ids:
                output_error('No message IDs provided', 'INVALID_INPUT', exit_code=1)

            result = batch_modify_labels(
                service,
                message_ids,
                add_labels=add_labels if add_labels else None,
                remove_labels=remove_labels if remove_labels else None
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
