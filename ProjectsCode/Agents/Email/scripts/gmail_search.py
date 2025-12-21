#!/usr/bin/env python3
"""Search Gmail messages using Gmail API.

Replaces: mcp__gmail-workspace__search_gmail_messages

Usage:
    python3 gmail_search.py --email victor.lang22@gmail.com --query "newer_than:14d is:starred"
    python3 gmail_search.py --email victor.lang22@gmail.com --query "category:primary newer_than:14d" --max-results 50
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
    expand_category_primary,
    output_success,
    output_error,
    retry_with_backoff,
    add_common_args
)


def search_messages(
    service,
    query: str,
    max_results: int = 100,
    include_spam_trash: bool = False
) -> dict:
    """Search for messages matching the query.

    Args:
        service: Gmail API service
        query: Gmail search query
        max_results: Maximum number of results to return
        include_spam_trash: Whether to include spam and trash

    Returns:
        Dict with messages list and count
    """
    # Expand category:primary to explicit exclusions
    expanded_query = expand_category_primary(query)

    messages = []
    page_token = None

    while len(messages) < max_results:
        # Calculate how many more we need
        page_size = min(100, max_results - len(messages))

        request = service.users().messages().list(
            userId='me',
            q=expanded_query,
            maxResults=page_size,
            pageToken=page_token,
            includeSpamTrash=include_spam_trash
        )

        result = retry_with_backoff(request.execute)

        batch_messages = result.get('messages', [])
        messages.extend(batch_messages)

        page_token = result.get('nextPageToken')
        if not page_token:
            break

    return {
        'messages': messages[:max_results],
        'count': len(messages[:max_results]),
        'query': query,
        'expanded_query': expanded_query if expanded_query != query else None
    }


def main():
    parser = argparse.ArgumentParser(
        description='Search Gmail messages'
    )
    add_common_args(parser)
    parser.add_argument(
        '--query',
        required=True,
        help='Gmail search query (e.g., "newer_than:14d is:starred")'
    )
    parser.add_argument(
        '--max-results',
        type=int,
        default=100,
        help='Maximum number of results to return (default: 100)'
    )
    parser.add_argument(
        '--include-spam-trash',
        action='store_true',
        help='Include messages in spam and trash'
    )

    args = parser.parse_args()

    try:
        service = get_gmail_service(args.email)
        result = search_messages(
            service,
            args.query,
            max_results=args.max_results,
            include_spam_trash=args.include_spam_trash
        )
        output_success(result)

    except FileNotFoundError as e:
        output_error(str(e), 'CREDENTIALS_NOT_FOUND', exit_code=3)

    except Exception as e:
        error_type = 'API_ERROR'
        exit_code = 2

        # Check for specific error types
        error_str = str(e)
        if 'invalid_grant' in error_str.lower():
            error_type = 'AUTH_ERROR'
            exit_code = 3
        elif 'quota' in error_str.lower():
            error_type = 'QUOTA_ERROR'

        output_error(str(e), error_type, exit_code=exit_code)


if __name__ == '__main__':
    main()
