#!/usr/bin/env python3
"""Delete a calendar event.

Usage:
    python3 calendar_delete_event.py --email victor.lang22@gmail.com --event-id abc123
    python3 calendar_delete_event.py --email victor@verifiedmetrics.com --event-id xyz789 --send-updates none

Output:
    JSON confirmation of deletion.
"""

import argparse
import sys

from auth import get_calendar_service
from utils import output_success, output_error, retry_with_backoff


def get_event(service, calendar_id: str, event_id: str) -> dict:
    """Get an event's details before deletion."""
    def fetch():
        return service.events().get(
            calendarId=calendar_id,
            eventId=event_id
        ).execute()

    return retry_with_backoff(fetch)


def delete_event(
    service,
    event_id: str,
    calendar_id: str = 'primary',
    send_updates: str = None
) -> dict:
    """Delete a calendar event.

    Args:
        service: Calendar API service
        event_id: Event to delete
        calendar_id: Calendar containing the event
        send_updates: Notification behavior ('all', 'externalOnly', 'none')
                     If None, uses Google's default

    Returns:
        Deleted event details (fetched before deletion)
    """
    # Get event details before deleting
    event = get_event(service, calendar_id, event_id)

    def delete():
        kwargs = {
            'calendarId': calendar_id,
            'eventId': event_id
        }
        if send_updates:
            kwargs['sendUpdates'] = send_updates

        service.events().delete(**kwargs).execute()

    retry_with_backoff(delete)

    return event


def format_deleted_event(event: dict) -> dict:
    """Format deleted event for output."""
    result = {
        'id': event.get('id'),
        'summary': event.get('summary', '(No title)')
    }

    start = event.get('start', {})
    if 'dateTime' in start:
        result['start'] = start['dateTime']
    else:
        result['start'] = start.get('date')

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Delete a calendar event'
    )
    parser.add_argument(
        '--email',
        required=True,
        help='Google account email address'
    )
    parser.add_argument(
        '--event-id',
        required=True,
        help='ID of the event to delete'
    )
    parser.add_argument(
        '--calendar-id',
        default='primary',
        help='Calendar containing the event (default: primary)'
    )
    parser.add_argument(
        '--send-updates',
        choices=['all', 'externalOnly', 'none'],
        help='Who to notify about the deletion (default: Google decides)'
    )

    args = parser.parse_args()

    try:
        service = get_calendar_service(args.email)

        event = delete_event(
            service,
            event_id=args.event_id,
            calendar_id=args.calendar_id,
            send_updates=args.send_updates
        )

        result = {
            'deleted': True,
            'event': format_deleted_event(event),
            'account': args.email,
            'calendar_id': args.calendar_id
        }

        output_success(result)

    except Exception as e:
        error_msg = str(e)

        # Check for "not found" errors
        if '404' in error_msg or 'not found' in error_msg.lower():
            output_error(f"Event not found: {args.event_id}", 'NOT_FOUND', 1)
        else:
            output_error(error_msg, 'API_ERROR', 2)


if __name__ == '__main__':
    main()
