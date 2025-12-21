#!/usr/bin/env python3
"""Search calendar events by query text.

Usage:
    python3 calendar_search_events.py --email victor.lang22@gmail.com --query "meeting"
    python3 calendar_search_events.py --email victor.lang22@gmail.com --query "standup" --range month

Output:
    JSON with list of matching events.
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


def search_events(
    email: str,
    query: str,
    calendar_id: str = 'primary',
    time_min: datetime = None,
    time_max: datetime = None,
    max_results: int = 100,
    timezone_str: str = None
) -> list:
    """Search for events matching a query.

    Args:
        email: Google account email
        query: Search query text
        calendar_id: Calendar ID (default 'primary')
        time_min: Start of range
        time_max: End of range
        max_results: Maximum events to return
        timezone_str: Timezone

    Returns:
        List of matching event info dicts
    """
    service = get_calendar_service(email)
    tz = get_timezone(timezone_str)

    if time_min is None:
        time_min = datetime.now(tz) - timedelta(days=30)
    if time_max is None:
        time_max = datetime.now(tz) + timedelta(days=365)

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
                q=query,
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
                'attendee_count': len(item.get('attendees', [])),
                'has_video': has_video_conference(item),
                'video_link': get_video_conference_link(item),
                'html_link': item.get('htmlLink', ''),
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
        description='Search calendar events by query text'
    )
    add_common_args(parser)
    parser.add_argument(
        '--query',
        required=True,
        help='Search query text'
    )
    parser.add_argument(
        '--calendar-id',
        default='primary',
        help='Calendar ID (default: primary)'
    )
    parser.add_argument(
        '--range',
        choices=['week', 'month', 'year'],
        default='month',
        help='Search range from today (default: month)'
    )
    parser.add_argument(
        '--max-results',
        type=int,
        default=100,
        help='Maximum number of events to return (default: 100)'
    )

    args = parser.parse_args()

    try:
        tz = get_timezone(args.timezone)

        # Determine time range (search past and future)
        now = datetime.now(tz)
        if args.range == 'week':
            time_min = now - timedelta(days=7)
            time_max = now + timedelta(days=7)
        elif args.range == 'month':
            time_min = now - timedelta(days=30)
            time_max = now + timedelta(days=30)
        else:  # year
            time_min = now - timedelta(days=365)
            time_max = now + timedelta(days=365)

        events = search_events(
            email=args.email,
            query=args.query,
            calendar_id=args.calendar_id,
            time_min=time_min,
            time_max=time_max,
            max_results=args.max_results,
            timezone_str=args.timezone
        )

        output_success({
            'events': events,
            'count': len(events),
            'query': args.query,
            'range': {
                'start': time_min.isoformat(),
                'end': time_max.isoformat()
            }
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
