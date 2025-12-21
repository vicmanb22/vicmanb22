#!/usr/bin/env python3
"""Respond to a calendar invitation (RSVP).

Usage:
    python3 calendar_rsvp.py --email victor@verifiedmetrics.com --event-id abc123 --response accepted
    python3 calendar_rsvp.py --email victor.lang22@gmail.com --event-id xyz789 --response declined

Output:
    JSON confirmation of response.
"""

import argparse
import sys

from auth import get_calendar_service
from utils import output_success, output_error, retry_with_backoff


VALID_RESPONSES = ['accepted', 'declined', 'tentative', 'needsAction']


def get_event(service, calendar_id: str, event_id: str) -> dict:
    """Get event details."""
    def fetch():
        return service.events().get(
            calendarId=calendar_id,
            eventId=event_id
        ).execute()

    return retry_with_backoff(fetch)


def rsvp_event(
    service,
    email: str,
    event_id: str,
    response: str,
    calendar_id: str = 'primary'
) -> dict:
    """Respond to a calendar invitation.

    Args:
        service: Calendar API service
        email: Your email address (to identify your attendee entry)
        event_id: Event to respond to
        response: Response status ('accepted', 'declined', 'tentative')
        calendar_id: Calendar containing the event

    Returns:
        Updated event
    """
    if response not in VALID_RESPONSES:
        raise ValueError(f"Invalid response: {response}. Must be one of: {', '.join(VALID_RESPONSES)}")

    # Get current event
    event = get_event(service, calendar_id, event_id)

    # Find and update your attendee entry
    attendees = event.get('attendees', [])
    found = False

    for attendee in attendees:
        if attendee.get('email', '').lower() == email.lower() or attendee.get('self', False):
            attendee['responseStatus'] = response
            found = True
            break

    if not found:
        raise ValueError(f"You ({email}) are not an attendee of this event")

    # Update the event with new response
    def update():
        return service.events().patch(
            calendarId=calendar_id,
            eventId=event_id,
            body={'attendees': attendees}
        ).execute()

    return retry_with_backoff(update)


def format_event_result(event: dict, email: str) -> dict:
    """Format event for output."""
    result = {
        'id': event.get('id'),
        'summary': event.get('summary', '(No title)'),
        'html_link': event.get('htmlLink', '')
    }

    start = event.get('start', {})
    if 'dateTime' in start:
        result['start'] = start['dateTime']
    else:
        result['start'] = start.get('date')

    # Find your response status
    for attendee in event.get('attendees', []):
        if attendee.get('email', '').lower() == email.lower() or attendee.get('self', False):
            result['your_response'] = attendee.get('responseStatus')
            break

    # Show organizer
    organizer = event.get('organizer', {})
    result['organizer'] = organizer.get('email', organizer.get('displayName', 'Unknown'))

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Respond to a calendar invitation'
    )
    parser.add_argument(
        '--email',
        required=True,
        help='Your Google account email address'
    )
    parser.add_argument(
        '--event-id',
        required=True,
        help='ID of the event to respond to'
    )
    parser.add_argument(
        '--response',
        required=True,
        choices=['accepted', 'declined', 'tentative'],
        help='Your response to the invitation'
    )
    parser.add_argument(
        '--calendar-id',
        default='primary',
        help='Calendar containing the event (default: primary)'
    )

    args = parser.parse_args()

    try:
        service = get_calendar_service(args.email)

        event = rsvp_event(
            service,
            email=args.email,
            event_id=args.event_id,
            response=args.response,
            calendar_id=args.calendar_id
        )

        result = {
            'responded': True,
            'response': args.response,
            'event': format_event_result(event, args.email),
            'account': args.email
        }

        output_success(result)

    except ValueError as e:
        output_error(str(e), 'INVALID_INPUT', 1)

    except Exception as e:
        error_msg = str(e)

        if '404' in error_msg or 'not found' in error_msg.lower():
            output_error(f"Event not found: {args.event_id}", 'NOT_FOUND', 1)
        else:
            output_error(error_msg, 'API_ERROR', 2)


if __name__ == '__main__':
    main()
