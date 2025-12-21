#!/usr/bin/env python3
"""Move an event between calendars.

Usage:
    python3 calendar_move_event.py --email victor.lang22@gmail.com --event-id abc123 --destination work_calendar_id
    python3 calendar_move_event.py --email victor@verifiedmetrics.com --event-id xyz789 --source primary --destination secondary_calendar_id

Output:
    JSON with moved event details.
"""

import argparse
import sys

from auth import get_calendar_service
from utils import output_success, output_error, retry_with_backoff


def get_event(service, calendar_id: str, event_id: str) -> dict:
    """Get event details before moving."""
    def fetch():
        return service.events().get(
            calendarId=calendar_id,
            eventId=event_id
        ).execute()

    return retry_with_backoff(fetch)


def move_event(
    service,
    event_id: str,
    destination: str,
    source: str = 'primary'
) -> dict:
    """Move an event to a different calendar.

    Note: Cannot move special event types (birthday, focus time, OOO, etc.)

    Args:
        service: Calendar API service
        event_id: Event to move
        destination: Target calendar ID
        source: Source calendar ID (default: primary)

    Returns:
        Moved event in new calendar
    """
    def move():
        return service.events().move(
            calendarId=source,
            eventId=event_id,
            destination=destination
        ).execute()

    return retry_with_backoff(move)


def format_event_result(event: dict, source: str, destination: str) -> dict:
    """Format moved event for output."""
    result = {
        'id': event.get('id'),
        'summary': event.get('summary', '(No title)'),
        'html_link': event.get('htmlLink', ''),
        'moved_from': source,
        'moved_to': destination
    }

    start = event.get('start', {})
    if 'dateTime' in start:
        result['start'] = start['dateTime']
    else:
        result['start'] = start.get('date')

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Move an event between calendars'
    )
    parser.add_argument(
        '--email',
        required=True,
        help='Google account email address'
    )
    parser.add_argument(
        '--event-id',
        required=True,
        help='ID of the event to move'
    )
    parser.add_argument(
        '--destination',
        required=True,
        help='Target calendar ID to move the event to'
    )
    parser.add_argument(
        '--source',
        default='primary',
        help='Source calendar ID (default: primary)'
    )

    args = parser.parse_args()

    try:
        service = get_calendar_service(args.email)

        event = move_event(
            service,
            event_id=args.event_id,
            destination=args.destination,
            source=args.source
        )

        result = {
            'moved': True,
            'event': format_event_result(event, args.source, args.destination),
            'account': args.email
        }

        output_success(result)

    except Exception as e:
        error_msg = str(e)

        if '404' in error_msg or 'not found' in error_msg.lower():
            output_error(f"Event not found: {args.event_id}", 'NOT_FOUND', 1)
        elif 'cannot move' in error_msg.lower():
            output_error("Cannot move this event type (birthday, focus time, OOO events cannot be moved)", 'INVALID_OPERATION', 1)
        else:
            output_error(error_msg, 'API_ERROR', 2)


if __name__ == '__main__':
    main()
