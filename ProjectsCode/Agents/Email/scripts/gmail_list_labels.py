#!/usr/bin/env python3
"""List Gmail labels.

Replaces: mcp__gmail-workspace__list_gmail_labels

Usage:
    python3 gmail_list_labels.py --email victor.lang22@gmail.com
"""

import argparse
import json
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


def list_labels(service) -> dict:
    """List all labels in the account.

    Args:
        service: Gmail API service

    Returns:
        Dict with labels list
    """
    request = service.users().labels().list(userId='me')
    result = retry_with_backoff(request.execute)

    labels = []
    for label in result.get('labels', []):
        labels.append({
            'id': label.get('id'),
            'name': label.get('name'),
            'type': label.get('type', 'user'),
            'messageListVisibility': label.get('messageListVisibility'),
            'labelListVisibility': label.get('labelListVisibility')
        })

    # Sort: system labels first, then user labels alphabetically
    labels.sort(key=lambda x: (0 if x['type'] == 'system' else 1, x['name']))

    return {
        'labels': labels,
        'count': len(labels)
    }


def main():
    parser = argparse.ArgumentParser(
        description='List Gmail labels'
    )
    add_common_args(parser)

    args = parser.parse_args()

    try:
        service = get_gmail_service(args.email)
        result = list_labels(service)
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
