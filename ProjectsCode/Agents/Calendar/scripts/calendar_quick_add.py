#!/usr/bin/env python3
"""Quick add a calendar event using natural language.

Uses Google Calendar's quickAdd API to parse natural language input
and create an event automatically.

Usage:
    python3 calendar_quick_add.py --email victor.lang22@gmail.com --text "Lunch with Sarah tomorrow at noon"
    python3 calendar_quick_add.py --email victor@verifiedmetrics.com --text "Team standup Monday 9am" --add-meet

Output:
    JSON with created event details.
"""

import argparse
import sys

from auth import get_calendar_service
from utils import output_success, output_error, retry_with_backoff


def quick_add_event(
    service,
    text: str,
    calendar_id: str = 'primary',
    add_meet: bool = False
) -> dict:
    """Create an event using natural language.

    Args:
        service: Calendar API service
        text: Natural language event description
        calendar_id: Target calendar (default: primary)
        add_meet: Whether to add a Google Meet link

    Returns:
        Created event details
    """
    def create():
        return service.events().quickAdd(
            calendarId=calendar_id,
            text=text
        ).execute()

    event = retry_with_backoff(create)

    # Add Google Meet if requested
    if add_meet and event.get('id'):
        event = add_google_meet(service, calendar_id, event['id'])

    return event


def add_google_meet(service, calendar_id: str, event_id: str) -> dict:
    """Add Google Meet conference to an existing event.

    Args:
        service: Calendar API service
        calendar_id: Calendar containing the event
        event_id: Event to add Meet to

    Returns:
        Updated event with conference data
    """
    def update():
        return service.events().patch(
            calendarId=calendar_id,
            eventId=event_id,
            conferenceDataVersion=1,
            body={
                'conferenceData': {
                    'createRequest': {
                        'requestId': f'meet-{event_id}',
                        'conferenceSolutionKey': {'type': 'hangoutsMeet'}
                    }
                }
            }
        ).execute()

    return retry_with_backoff(update)


def format_event_result(event: dict) -> dict:
    """Format event for output."""
    result = {
        'id': event.get('id'),
        'summary': event.get('summary', '(No title)'),
        'status': event.get('status', 'confirmed'),
        'html_link': event.get('htmlLink', '')
    }

    # Parse start/end
    start = event.get('start', {})
    end = event.get('end', {})

    if 'dateTime' in start:
        result['start'] = start['dateTime']
        result['end'] = end.get('dateTime')
        result['all_day'] = False
    else:
        result['start'] = start.get('date')
        result['end'] = end.get('date')
        result['all_day'] = True

    # Check for conference data
    conference_data = event.get('conferenceData', {})
    entry_points = conference_data.get('entryPoints', [])
    for ep in entry_points:
        if ep.get('entryPointType') == 'video':
            result['meet_link'] = ep.get('uri')
            break

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Quick add a calendar event using natural language'
    )
    parser.add_argument(
        '--email',
        required=True,
        help='Google account email address'
    )
    parser.add_argument(
        '--text',
        required=True,
        help='Natural language event description (e.g., "Lunch with Sarah tomorrow at noon")'
    )
    parser.add_argument(
        '--calendar-id',
        default='primary',
        help='Target calendar ID (default: primary)'
    )
    parser.add_argument(
        '--add-meet',
        action='store_true',
        help='Add a Google Meet link to the event'
    )

    args = parser.parse_args()

    try:
        service = get_calendar_service(args.email)

        event = quick_add_event(
            service,
            text=args.text,
            calendar_id=args.calendar_id,
            add_meet=args.add_meet
        )

        result = {
            'created': True,
            'event': format_event_result(event),
            'account': args.email,
            'calendar_id': args.calendar_id
        }

        output_success(result)

    except Exception as e:
        error_msg = str(e)
        output_error(error_msg, 'API_ERROR', 2)


if __name__ == '__main__':
    main()
