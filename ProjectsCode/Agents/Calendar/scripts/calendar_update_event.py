#!/usr/bin/env python3
"""Update an existing calendar event.

Uses PATCH to update only specified fields without affecting others.

Usage:
    python3 calendar_update_event.py --email victor.lang22@gmail.com --event-id abc123 --title "New Title"
    python3 calendar_update_event.py --email victor@verifiedmetrics.com --event-id xyz789 --start "2025-12-23T10:00:00"

Output:
    JSON with updated event details.
"""

import argparse
import sys
from datetime import datetime, timedelta

from auth import get_calendar_service
from utils import output_success, output_error, retry_with_backoff, get_timezone


def parse_datetime_input(dt_str: str, timezone_str: str = None) -> datetime:
    """Parse datetime input, handling various formats."""
    tz = get_timezone(timezone_str)

    try:
        if '+' in dt_str or 'Z' in dt_str:
            return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))

        dt = datetime.fromisoformat(dt_str)
        return dt.replace(tzinfo=tz)
    except ValueError:
        pass

    raise ValueError(f"Could not parse datetime: {dt_str}. Use ISO format like '2025-12-23T09:00:00'")


def get_event(service, calendar_id: str, event_id: str) -> dict:
    """Get an existing event."""
    def fetch():
        return service.events().get(
            calendarId=calendar_id,
            eventId=event_id
        ).execute()

    return retry_with_backoff(fetch)


def update_event(
    service,
    event_id: str,
    calendar_id: str = 'primary',
    title: str = None,
    start: datetime = None,
    end: datetime = None,
    location: str = None,
    description: str = None,
    add_attendees: list = None,
    remove_attendees: list = None
) -> dict:
    """Update an existing event using PATCH.

    Args:
        service: Calendar API service
        event_id: Event to update
        calendar_id: Calendar containing the event
        title: New title (optional)
        start: New start time (optional)
        end: New end time (optional)
        location: New location (optional)
        description: New description (optional)
        add_attendees: Attendees to add (optional)
        remove_attendees: Attendees to remove (optional)

    Returns:
        Updated event
    """
    patch_body = {}

    if title is not None:
        patch_body['summary'] = title

    if location is not None:
        patch_body['location'] = location

    if description is not None:
        patch_body['description'] = description

    # Handle start/end time updates
    if start is not None or end is not None:
        # Get current event to preserve the other time if only one is being updated
        current_event = get_event(service, calendar_id, event_id)
        current_start = current_event.get('start', {})

        # Determine if this is an all-day event
        is_all_day = 'date' in current_start

        if start is not None:
            if is_all_day:
                patch_body['start'] = {'date': start.strftime('%Y-%m-%d')}
            else:
                patch_body['start'] = {'dateTime': start.isoformat()}

        if end is not None:
            if is_all_day:
                patch_body['end'] = {'date': end.strftime('%Y-%m-%d')}
            else:
                patch_body['end'] = {'dateTime': end.isoformat()}

    # Handle attendee modifications
    if add_attendees or remove_attendees:
        current_event = get_event(service, calendar_id, event_id)
        current_attendees = current_event.get('attendees', [])

        # Build new attendee list
        attendee_emails = {a.get('email') for a in current_attendees}

        if remove_attendees:
            attendee_emails -= set(remove_attendees)

        if add_attendees:
            attendee_emails.update(add_attendees)

        patch_body['attendees'] = [{'email': email} for email in attendee_emails]

    if not patch_body:
        raise ValueError("No fields to update. Specify at least one field to change.")

    def patch():
        return service.events().patch(
            calendarId=calendar_id,
            eventId=event_id,
            body=patch_body
        ).execute()

    return retry_with_backoff(patch)


def format_event_result(event: dict) -> dict:
    """Format event for output."""
    result = {
        'id': event.get('id'),
        'summary': event.get('summary', '(No title)'),
        'status': event.get('status', 'confirmed'),
        'html_link': event.get('htmlLink', '')
    }

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

    if event.get('location'):
        result['location'] = event['location']

    attendees = event.get('attendees', [])
    if attendees:
        result['attendees'] = [a.get('email') for a in attendees]

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Update an existing calendar event'
    )
    parser.add_argument(
        '--email',
        required=True,
        help='Google account email address'
    )
    parser.add_argument(
        '--event-id',
        required=True,
        help='ID of the event to update'
    )
    parser.add_argument(
        '--calendar-id',
        default='primary',
        help='Calendar containing the event (default: primary)'
    )
    parser.add_argument(
        '--title',
        help='New event title'
    )
    parser.add_argument(
        '--start',
        help='New start datetime (ISO format)'
    )
    parser.add_argument(
        '--end',
        help='New end datetime (ISO format)'
    )
    parser.add_argument(
        '--location',
        help='New event location'
    )
    parser.add_argument(
        '--description',
        help='New event description'
    )
    parser.add_argument(
        '--add-attendees',
        help='Comma-separated list of attendees to add'
    )
    parser.add_argument(
        '--remove-attendees',
        help='Comma-separated list of attendees to remove'
    )
    parser.add_argument(
        '--timezone',
        help='Timezone for datetime parsing (auto-detected if not specified)'
    )

    args = parser.parse_args()

    try:
        service = get_calendar_service(args.email)

        # Parse optional datetime arguments
        start = None
        end = None

        if args.start:
            start = parse_datetime_input(args.start, args.timezone)

        if args.end:
            end = parse_datetime_input(args.end, args.timezone)

        # Parse attendee lists
        add_attendees = None
        remove_attendees = None

        if args.add_attendees:
            add_attendees = [e.strip() for e in args.add_attendees.split(',')]

        if args.remove_attendees:
            remove_attendees = [e.strip() for e in args.remove_attendees.split(',')]

        event = update_event(
            service,
            event_id=args.event_id,
            calendar_id=args.calendar_id,
            title=args.title,
            start=start,
            end=end,
            location=args.location,
            description=args.description,
            add_attendees=add_attendees,
            remove_attendees=remove_attendees
        )

        result = {
            'updated': True,
            'event': format_event_result(event),
            'account': args.email,
            'calendar_id': args.calendar_id
        }

        output_success(result)

    except ValueError as e:
        output_error(str(e), 'INVALID_INPUT', 1)

    except Exception as e:
        error_msg = str(e)
        output_error(error_msg, 'API_ERROR', 2)


if __name__ == '__main__':
    main()
