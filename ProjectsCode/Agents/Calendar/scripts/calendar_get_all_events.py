#!/usr/bin/env python3
"""Get events from ALL calendars for an account within a date range.

This script fetches events from all accessible calendars and combines them,
useful for getting a complete view of the user's schedule.

Usage:
    python3 calendar_get_all_events.py --email victor.lang22@gmail.com --range today
    python3 calendar_get_all_events.py --email victor.lang22@gmail.com --range week
    python3 calendar_get_all_events.py --email victor.lang22@gmail.com --range week --group-by calendar

Output:
    JSON with list of events from all calendars, optionally grouped.
"""

import argparse
import sys
from datetime import datetime, timedelta

from auth import get_calendar_service
from utils import (
    add_common_args, output_success, output_error, retry_with_backoff,
    get_timezone, get_date_range, parse_event_datetime, is_all_day_event,
    get_event_duration, format_duration, extract_attendees, get_organizer,
    has_video_conference, get_video_conference_link, format_time,
    format_date_short, time_until
)


def list_calendars(service, include_hidden: bool = False) -> list:
    """List all calendars for the authenticated user."""
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
            # Only include selected (visible) calendars unless include_hidden
            if item.get('selected', False) or include_hidden:
                calendars.append({
                    'id': item.get('id'),
                    'name': item.get('summary', 'Untitled'),
                    'primary': item.get('primary', False),
                    'color': item.get('backgroundColor', '#000000')
                })

        page_token = response.get('nextPageToken')
        if not page_token:
            break

    return calendars


def get_events_for_calendar(
    service,
    calendar_id: str,
    calendar_name: str,
    calendar_color: str,
    time_min: datetime,
    time_max: datetime,
    timezone_str: str = None
) -> list:
    """Get events from a single calendar."""
    tz = get_timezone(timezone_str)
    events = []
    page_token = None

    while True:
        def fetch_page():
            return service.events().list(
                calendarId=calendar_id,
                timeMin=time_min.isoformat(),
                timeMax=time_max.isoformat(),
                maxResults=250,
                singleEvents=True,
                orderBy='startTime',
                pageToken=page_token
            ).execute()

        try:
            response = retry_with_backoff(fetch_page)
        except Exception as e:
            # Skip calendars that fail (e.g., no access)
            return []

        for item in response.get('items', []):
            start_dt = parse_event_datetime(item.get('start', {}))
            end_dt = parse_event_datetime(item.get('end', {}))
            duration = get_event_duration(item)
            all_day = is_all_day_event(item)

            event_info = {
                'id': item.get('id'),
                'summary': item.get('summary', '(No title)'),
                'description': item.get('description', ''),
                'location': item.get('location', ''),
                'status': item.get('status', 'confirmed'),
                'all_day': all_day,
                'start': {
                    'datetime': start_dt.isoformat() if start_dt else None,
                    'date': format_date_short(start_dt, tz) if start_dt else None,
                    'time': format_time(start_dt, tz) if start_dt and not all_day else None,
                    'time_until': time_until(start_dt, tz) if start_dt else None
                },
                'end': {
                    'datetime': end_dt.isoformat() if end_dt else None,
                    'time': format_time(end_dt, tz) if end_dt and not all_day else None
                },
                'duration': format_duration(duration) if duration else None,
                'organizer': get_organizer(item),
                'attendees': extract_attendees(item),
                'attendee_count': len(item.get('attendees', [])),
                'has_video': has_video_conference(item),
                'video_link': get_video_conference_link(item),
                'html_link': item.get('htmlLink', ''),
                'recurring': bool(item.get('recurringEventId')),
                'calendar': {
                    'id': calendar_id,
                    'name': calendar_name,
                    'color': calendar_color
                }
            }

            events.append(event_info)

        page_token = response.get('nextPageToken')
        if not page_token:
            break

    return events


def get_all_events(
    email: str,
    time_min: datetime,
    time_max: datetime,
    timezone_str: str = None,
    include_hidden: bool = False
) -> tuple:
    """Get events from all calendars.

    Returns:
        Tuple of (events_list, calendars_fetched)
    """
    service = get_calendar_service(email)

    # Get all calendars
    calendars = list_calendars(service, include_hidden)

    all_events = []
    calendars_fetched = []

    for cal in calendars:
        events = get_events_for_calendar(
            service,
            cal['id'],
            cal['name'],
            cal['color'],
            time_min,
            time_max,
            timezone_str
        )

        if events:
            all_events.extend(events)
            calendars_fetched.append({
                'id': cal['id'],
                'name': cal['name'],
                'event_count': len(events)
            })

    # Sort all events by start time
    all_events.sort(key=lambda e: e['start']['datetime'] or '')

    return all_events, calendars_fetched


def group_events_by_calendar(events: list) -> dict:
    """Group events by calendar."""
    grouped = {}
    for event in events:
        cal_name = event['calendar']['name']
        if cal_name not in grouped:
            grouped[cal_name] = {
                'calendar': event['calendar'],
                'events': []
            }
        grouped[cal_name]['events'].append(event)
    return grouped


def group_events_by_date(events: list) -> dict:
    """Group events by date."""
    grouped = {}
    for event in events:
        date = event['start']['date']
        if date not in grouped:
            grouped[date] = []
        grouped[date].append(event)
    return grouped


def main():
    parser = argparse.ArgumentParser(
        description='Get events from all calendars for a Google account'
    )
    add_common_args(parser)
    parser.add_argument(
        '--range',
        choices=['today', 'tomorrow', 'week', 'month'],
        default='week',
        help='Named date range (default: week)'
    )
    parser.add_argument(
        '--start',
        help='Start date (YYYY-MM-DD format)'
    )
    parser.add_argument(
        '--end',
        help='End date (YYYY-MM-DD format)'
    )
    parser.add_argument(
        '--group-by',
        choices=['calendar', 'date', 'none'],
        default='none',
        help='How to group events in output'
    )
    parser.add_argument(
        '--include-hidden',
        action='store_true',
        help='Include hidden calendars'
    )

    args = parser.parse_args()

    try:
        tz = get_timezone(args.timezone)

        # Determine time range
        if args.start:
            time_min = datetime.strptime(args.start, '%Y-%m-%d').replace(tzinfo=tz)
            if args.end:
                time_max = datetime.strptime(args.end, '%Y-%m-%d').replace(tzinfo=tz)
                time_max = time_max + timedelta(days=1)
            else:
                time_max = time_min + timedelta(days=1)
        else:
            time_min, time_max = get_date_range(args.range, tz)

        events, calendars = get_all_events(
            email=args.email,
            time_min=time_min,
            time_max=time_max,
            timezone_str=args.timezone,
            include_hidden=args.include_hidden
        )

        result = {
            'count': len(events),
            'range': {
                'start': time_min.isoformat(),
                'end': time_max.isoformat()
            },
            'calendars_fetched': calendars
        }

        if args.group_by == 'calendar':
            result['events_by_calendar'] = group_events_by_calendar(events)
        elif args.group_by == 'date':
            result['events_by_date'] = group_events_by_date(events)
        else:
            result['events'] = events

        output_success(result)

    except FileNotFoundError as e:
        output_error(str(e), 'CREDENTIALS_NOT_FOUND', 3)

    except ValueError as e:
        output_error(f"Invalid date format: {e}", 'INVALID_INPUT', 1)

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
