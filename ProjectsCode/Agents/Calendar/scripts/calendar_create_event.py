#!/usr/bin/env python3
"""Create a calendar event with full control over all fields.

Usage:
    python3 calendar_create_event.py --email victor.lang22@gmail.com --title "Team Standup" --start "2025-12-23T09:00:00" --end "2025-12-23T09:30:00"
    python3 calendar_create_event.py --email victor@verifiedmetrics.com --title "Meeting" --start "2025-12-23T14:00:00" --duration 1h --attendees "ray@vm.com,ricardo@vm.com"

Output:
    JSON with created event details.
"""

import argparse
import re
import sys
from datetime import datetime, timedelta

from auth import get_calendar_service
from utils import output_success, output_error, retry_with_backoff, get_timezone


def parse_duration(duration_str: str) -> timedelta:
    """Parse duration string like '30m', '1h', '1h30m', '2h'.

    Args:
        duration_str: Duration string

    Returns:
        timedelta object
    """
    total_minutes = 0

    # Match hours
    hours_match = re.search(r'(\d+)h', duration_str)
    if hours_match:
        total_minutes += int(hours_match.group(1)) * 60

    # Match minutes
    minutes_match = re.search(r'(\d+)m', duration_str)
    if minutes_match:
        total_minutes += int(minutes_match.group(1))

    if total_minutes == 0:
        # Try parsing as just a number (assume minutes)
        try:
            total_minutes = int(duration_str)
        except ValueError:
            raise ValueError(f"Invalid duration format: {duration_str}")

    return timedelta(minutes=total_minutes)


def parse_datetime_input(dt_str: str, timezone_str: str = None) -> datetime:
    """Parse datetime input, handling various formats.

    Args:
        dt_str: Datetime string (ISO format)
        timezone_str: Optional timezone

    Returns:
        datetime object with timezone
    """
    tz = get_timezone(timezone_str)

    # Try ISO format first
    try:
        # If it has timezone info already
        if '+' in dt_str or 'Z' in dt_str:
            return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))

        # Parse and add local timezone
        dt = datetime.fromisoformat(dt_str)
        return dt.replace(tzinfo=tz)
    except ValueError:
        pass

    raise ValueError(f"Could not parse datetime: {dt_str}. Use ISO format like '2025-12-23T09:00:00'")


def create_event(
    service,
    title: str,
    start: datetime,
    end: datetime = None,
    all_day: bool = False,
    location: str = None,
    description: str = None,
    attendees: list = None,
    calendar_id: str = 'primary',
    add_meet: bool = False,
    recurrence: str = None
) -> dict:
    """Create a calendar event.

    Args:
        service: Calendar API service
        title: Event summary/title
        start: Start datetime
        end: End datetime (optional, defaults to 1 hour after start)
        all_day: Whether this is an all-day event
        location: Event location
        description: Event description
        attendees: List of attendee email addresses
        calendar_id: Target calendar ID
        add_meet: Whether to add Google Meet
        recurrence: RRULE string for recurring events

    Returns:
        Created event
    """
    event_body = {
        'summary': title
    }

    # Set start/end times
    if all_day:
        event_body['start'] = {'date': start.strftime('%Y-%m-%d')}
        if end:
            event_body['end'] = {'date': end.strftime('%Y-%m-%d')}
        else:
            # All-day events end the next day
            next_day = start + timedelta(days=1)
            event_body['end'] = {'date': next_day.strftime('%Y-%m-%d')}
    else:
        event_body['start'] = {'dateTime': start.isoformat()}
        if end:
            event_body['end'] = {'dateTime': end.isoformat()}
        else:
            # Default to 1 hour
            default_end = start + timedelta(hours=1)
            event_body['end'] = {'dateTime': default_end.isoformat()}

    # Optional fields
    if location:
        event_body['location'] = location

    if description:
        event_body['description'] = description

    if attendees:
        event_body['attendees'] = [{'email': email.strip()} for email in attendees]

    if recurrence:
        event_body['recurrence'] = [recurrence]

    # Add Google Meet if requested
    conference_data_version = 0
    if add_meet:
        conference_data_version = 1
        event_body['conferenceData'] = {
            'createRequest': {
                'requestId': f'meet-{datetime.now().timestamp()}',
                'conferenceSolutionKey': {'type': 'hangoutsMeet'}
            }
        }

    def create():
        return service.events().insert(
            calendarId=calendar_id,
            body=event_body,
            conferenceDataVersion=conference_data_version
        ).execute()

    return retry_with_backoff(create)


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

    # Location
    if event.get('location'):
        result['location'] = event['location']

    # Attendees
    attendees = event.get('attendees', [])
    if attendees:
        result['attendees'] = [a.get('email') for a in attendees]

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
        description='Create a calendar event'
    )
    parser.add_argument(
        '--email',
        required=True,
        help='Google account email address'
    )
    parser.add_argument(
        '--title',
        required=True,
        help='Event title/summary'
    )
    parser.add_argument(
        '--start',
        required=True,
        help='Start datetime (ISO format, e.g., "2025-12-23T09:00:00")'
    )
    parser.add_argument(
        '--end',
        help='End datetime (ISO format). If not specified, uses --duration or defaults to 1 hour.'
    )
    parser.add_argument(
        '--duration',
        help='Event duration (e.g., "30m", "1h", "1h30m"). Used if --end not specified.'
    )
    parser.add_argument(
        '--all-day',
        action='store_true',
        help='Create an all-day event'
    )
    parser.add_argument(
        '--location',
        help='Event location'
    )
    parser.add_argument(
        '--description',
        help='Event description'
    )
    parser.add_argument(
        '--attendees',
        help='Comma-separated list of attendee email addresses'
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
    parser.add_argument(
        '--recurrence',
        help='RRULE string for recurring events (e.g., "RRULE:FREQ=WEEKLY;COUNT=10")'
    )
    parser.add_argument(
        '--timezone',
        help='Timezone for the event (auto-detected if not specified)'
    )

    args = parser.parse_args()

    try:
        service = get_calendar_service(args.email)

        # Parse start time
        start = parse_datetime_input(args.start, args.timezone)

        # Parse end time
        end = None
        if args.end:
            end = parse_datetime_input(args.end, args.timezone)
        elif args.duration:
            duration = parse_duration(args.duration)
            end = start + duration

        # Parse attendees
        attendees = None
        if args.attendees:
            attendees = [e.strip() for e in args.attendees.split(',')]

        event = create_event(
            service,
            title=args.title,
            start=start,
            end=end,
            all_day=args.all_day,
            location=args.location,
            description=args.description,
            attendees=attendees,
            calendar_id=args.calendar_id,
            add_meet=args.add_meet,
            recurrence=args.recurrence
        )

        result = {
            'created': True,
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
