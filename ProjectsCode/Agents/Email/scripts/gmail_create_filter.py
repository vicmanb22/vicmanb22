#!/usr/bin/env python3
"""Create Gmail filter for a sender.

Creates a filter to automatically handle future emails from a sender
(e.g., delete, archive, mark as read).

Usage:
    python3 gmail_create_filter.py --email victor.lang22@gmail.com --from newsletter@example.com --action delete
    python3 gmail_create_filter.py --email victor.lang22@gmail.com --from @example.com --action archive
    python3 gmail_create_filter.py --email victor.lang22@gmail.com --from newsletter@example.com --action read
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


def create_filter(
    service,
    from_address: str,
    action: str,
    also_apply_to_existing: bool = False
) -> dict:
    """Create a Gmail filter for the specified sender.

    Args:
        service: Gmail API service
        from_address: Email address or domain to filter (e.g., "foo@bar.com" or "@bar.com")
        action: Action to take - 'delete', 'archive', 'read', 'spam', 'star'
        also_apply_to_existing: If True, also apply to existing messages

    Returns:
        Dict with filter creation result
    """
    # Build filter criteria
    criteria = {
        'from': from_address
    }

    # Build filter action based on requested action
    filter_action = {}

    if action == 'delete':
        # Add to TRASH
        filter_action['addLabelIds'] = ['TRASH']
        filter_action['removeLabelIds'] = ['INBOX']
    elif action == 'archive':
        # Remove from INBOX (archive)
        filter_action['removeLabelIds'] = ['INBOX']
    elif action == 'read':
        # Mark as read
        filter_action['removeLabelIds'] = ['UNREAD']
    elif action == 'spam':
        # Mark as spam
        filter_action['addLabelIds'] = ['SPAM']
        filter_action['removeLabelIds'] = ['INBOX']
    elif action == 'star':
        # Star the message
        filter_action['addLabelIds'] = ['STARRED']
    else:
        return {
            'success': False,
            'error': f'Unknown action: {action}. Valid actions: delete, archive, read, spam, star'
        }

    # Create the filter
    filter_body = {
        'criteria': criteria,
        'action': filter_action
    }

    request = service.users().settings().filters().create(
        userId='me',
        body=filter_body
    )

    result = retry_with_backoff(request.execute)

    response = {
        'success': True,
        'filter_id': result.get('id'),
        'criteria': criteria,
        'action': action,
        'message': f'Filter created: {action} emails from {from_address}'
    }

    # Optionally apply to existing messages
    if also_apply_to_existing:
        apply_result = apply_filter_to_existing(service, from_address, action)
        response['applied_to_existing'] = apply_result

    return response


def apply_filter_to_existing(service, from_address: str, action: str) -> dict:
    """Apply filter action to existing messages from sender.

    Args:
        service: Gmail API service
        from_address: Email address or domain to filter
        action: Action to apply

    Returns:
        Dict with number of messages affected
    """
    # Search for existing messages
    query = f'from:{from_address}'

    messages = []
    page_token = None

    while True:
        request = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=100,
            pageToken=page_token
        )
        result = retry_with_backoff(request.execute)

        batch_messages = result.get('messages', [])
        messages.extend(batch_messages)

        page_token = result.get('nextPageToken')
        if not page_token or len(messages) >= 500:  # Limit to 500
            break

    if not messages:
        return {'count': 0, 'message': 'No existing messages found'}

    message_ids = [m['id'] for m in messages[:500]]

    # Build label modification based on action
    add_labels = []
    remove_labels = []

    if action == 'delete':
        add_labels = ['TRASH']
        remove_labels = ['INBOX']
    elif action == 'archive':
        remove_labels = ['INBOX']
    elif action == 'read':
        remove_labels = ['UNREAD']
    elif action == 'spam':
        add_labels = ['SPAM']
        remove_labels = ['INBOX']
    elif action == 'star':
        add_labels = ['STARRED']

    # Batch modify
    body = {
        'ids': message_ids
    }
    if add_labels:
        body['addLabelIds'] = add_labels
    if remove_labels:
        body['removeLabelIds'] = remove_labels

    request = service.users().messages().batchModify(
        userId='me',
        body=body
    )
    retry_with_backoff(request.execute)

    return {
        'count': len(message_ids),
        'message': f'Applied {action} to {len(message_ids)} existing messages'
    }


def list_filters(service) -> list:
    """List all existing filters.

    Args:
        service: Gmail API service

    Returns:
        List of filter dicts
    """
    request = service.users().settings().filters().list(userId='me')
    result = retry_with_backoff(request.execute)

    filters = result.get('filter', [])

    return [{
        'id': f.get('id'),
        'criteria': f.get('criteria', {}),
        'action': f.get('action', {})
    } for f in filters]


def delete_filter(service, filter_id: str) -> dict:
    """Delete a filter by ID.

    Args:
        service: Gmail API service
        filter_id: Filter ID to delete

    Returns:
        Dict with deletion result
    """
    request = service.users().settings().filters().delete(
        userId='me',
        id=filter_id
    )
    retry_with_backoff(request.execute)

    return {
        'success': True,
        'message': f'Filter {filter_id} deleted'
    }


def main():
    parser = argparse.ArgumentParser(
        description='Create Gmail filter for a sender'
    )
    add_common_args(parser)

    # Subcommands
    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # Create filter command
    create_parser = subparsers.add_parser('create', help='Create a new filter')
    create_parser.add_argument(
        '--from',
        dest='from_address',
        required=True,
        help='Email address or domain to filter (e.g., "foo@bar.com" or "@bar.com")'
    )
    create_parser.add_argument(
        '--action',
        required=True,
        choices=['delete', 'archive', 'read', 'spam', 'star'],
        help='Action to take on matching emails'
    )
    create_parser.add_argument(
        '--apply-to-existing',
        action='store_true',
        help='Also apply action to existing messages from this sender'
    )

    # List filters command
    list_parser = subparsers.add_parser('list', help='List all filters')

    # Delete filter command
    delete_parser = subparsers.add_parser('delete', help='Delete a filter')
    delete_parser.add_argument(
        '--filter-id',
        required=True,
        help='Filter ID to delete'
    )

    args = parser.parse_args()

    # Default to create if no command and --from is provided
    if args.command is None:
        # Check if using legacy syntax (no subcommand)
        if hasattr(args, 'from_address') and args.from_address:
            args.command = 'create'
        else:
            parser.print_help()
            sys.exit(1)

    try:
        service = get_gmail_service(args.email)

        if args.command == 'create':
            result = create_filter(
                service,
                args.from_address,
                args.action,
                also_apply_to_existing=args.apply_to_existing
            )
            output_success(result)

        elif args.command == 'list':
            filters = list_filters(service)
            output_success({
                'filters': filters,
                'count': len(filters)
            })

        elif args.command == 'delete':
            result = delete_filter(service, args.filter_id)
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
