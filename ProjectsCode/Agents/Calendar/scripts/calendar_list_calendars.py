#!/usr/bin/env python3
"""List all calendars accessible to the user.

Usage:
    python3 calendar_list_calendars.py --email victor.lang22@gmail.com
    python3 calendar_list_calendars.py --email victor.lang22@gmail.com --include-hidden

Output:
    JSON with list of calendars including id, name, access role, and color.
"""

import argparse
import sys

from auth import get_calendar_service
from utils import add_common_args, output_success, output_error, retry_with_backoff


def list_calendars(email: str, include_hidden: bool = False) -> list:
    """List all calendars for the authenticated user.

    Args:
        email: Google account email
        include_hidden: Include hidden calendars

    Returns:
        List of calendar info dicts
    """
    service = get_calendar_service(email)

    calendars = []
    page_token = None

    while True:
        def fetch_page():
            return service.calendarList().list(
                pageToken=page_token,
                showHidden=include_hidden
            ).execute()

        response = retry_with_backoff(fetch_page)

        for item in response.get('items', []):
            calendars.append({
                'id': item.get('id'),
                'name': item.get('summary', 'Untitled'),
                'description': item.get('description', ''),
                'access_role': item.get('accessRole', 'reader'),
                'primary': item.get('primary', False),
                'selected': item.get('selected', False),
                'hidden': item.get('hidden', False),
                'color': {
                    'background': item.get('backgroundColor', '#000000'),
                    'foreground': item.get('foregroundColor', '#ffffff')
                },
                'timezone': item.get('timeZone', '')
            })

        page_token = response.get('nextPageToken')
        if not page_token:
            break

    return calendars


def main():
    parser = argparse.ArgumentParser(
        description='List all calendars for a Google account'
    )
    add_common_args(parser)
    parser.add_argument(
        '--include-hidden',
        action='store_true',
        help='Include hidden calendars in the list'
    )

    args = parser.parse_args()

    try:
        calendars = list_calendars(args.email, args.include_hidden)

        # Sort: primary first, then by name
        calendars.sort(key=lambda c: (not c['primary'], c['name'].lower()))

        output_success({
            'calendars': calendars,
            'count': len(calendars)
        })

    except FileNotFoundError as e:
        output_error(str(e), 'CREDENTIALS_NOT_FOUND', 3)

    except Exception as e:
        error_msg = str(e)
        if 'invalid_grant' in error_msg.lower() or 'token' in error_msg.lower():
            output_error(
                f"Authentication error: {error_msg}. Run reauth.py to refresh credentials.",
                'AUTH_ERROR',
                3
            )
        else:
            output_error(error_msg, 'API_ERROR', 2)


if __name__ == '__main__':
    main()
