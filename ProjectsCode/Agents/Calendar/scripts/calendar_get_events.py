#!/usr/bin/env python3
"""Get calendar events within a date range.

Usage:
    python3 calendar_get_events.py --email victor.lang22@gmail.com --range today
    python3 calendar_get_events.py --email victor.lang22@gmail.com --range week
    python3 calendar_get_events.py --email victor.lang22@gmail.com --start 2024-12-20 --end 2024-12-27
    python3 calendar_get_events.py --email victor.lang22@gmail.com --range week --calendar-id primary

Output:
    JSON with list of events including summary, start/end times, attendees, etc.
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


def get_events(
    email: str,
    calendar_id: str = 'primary',
    time_min: datetime = None,
    time_max: datetime = None,
    max_results: int = 250,
    timezone_str: str = None
) -> list:
    """Get events from a calendar within a time range.

    Args:
        email: Google account email
        calendar_id: Calendar ID (default 'primary')
        time_min: Start of range (defaults to now)
        time_max: End of range (defaults to 7 days from now)
        max_results: Maximum events to return
        timezone_str: Timezone for the query

    Returns:
        List of event info dicts
    """
    service = get_calendar_service(email)
    tz = get_timezone(timezone_str)

    if time_min is None:
        time_min = datetime.now(tz)
    if time_max is None:
        time_max = time_min + timedelta(days=7)

    # Ensure timezone info
    if time_min.tzinfo is None:
        time_min = time_min.replace(tzinfo=tz)
    if time_max.tzinfo is None:
        time_max = time_max.replace(tzinfo=tz)

    events = []
    page_token = None

    while True:
        def fetch_page():
            return service.events().list(
                calendarId=calendar_id,
                timeMin=time_min.isoformat(),
                timeMax=time_max.isoformat(),
                maxResults=min(max_results - len(events), 250),
                singleEvents=True,
                orderBy='startTime',
                pageToken=page_token
            ).execute()

        response = retry_with_backoff(fetch_page)

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
                'calendar_id': calendar_id
            }

            events.append(event_info)

        if len(events) >= max_results:
            break

        page_token = response.get('nextPageToken')
        if not page_token:
            break

    return events


def main():
    parser = argparse.ArgumentParser(
        description='Get calendar events within a date range'
    )
    add_common_args(parser)
    parser.add_argument(
        '--calendar-id',
        default='primary',
        help='Calendar ID (default: primary)'
    )
    parser.add_argument(
        '--range',
        choices=['today', 'tomorrow', 'week', 'month'],
        help='Named date range'
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
        '--max-results',
        type=int,
        default=250,
        help='Maximum number of events to return (default: 250)'
    )

    args = parser.parse_args()

    try:
        tz = get_timezone(args.timezone)

        # Determine time range
        if args.range:
            time_min, time_max = get_date_range(args.range, tz)
        elif args.start:
            time_min = datetime.strptime(args.start, '%Y-%m-%d').replace(tzinfo=tz)
            if args.end:
                time_max = datetime.strptime(args.end, '%Y-%m-%d').replace(tzinfo=tz)
                time_max = time_max + timedelta(days=1)  # Include the end date
            else:
                time_max = time_min + timedelta(days=1)
        else:
            # Default to this week
            time_min, time_max = get_date_range('week', tz)

        events = get_events(
            email=args.email,
            calendar_id=args.calendar_id,
            time_min=time_min,
            time_max=time_max,
            max_results=args.max_results,
            timezone_str=args.timezone
        )

        output_success({
            'events': events,
            'count': len(events),
            'range': {
                'start': time_min.isoformat(),
                'end': time_max.isoformat()
            },
            'calendar_id': args.calendar_id
        })

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
