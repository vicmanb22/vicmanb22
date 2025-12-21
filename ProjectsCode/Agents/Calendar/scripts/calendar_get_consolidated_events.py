#!/usr/bin/env python3
"""Get events from ALL calendars across ALL accounts.

This script auto-discovers all Google accounts from credentials directory
and fetches events from all accessible calendars, providing a consolidated view.

Usage:
    python3 calendar_get_consolidated_events.py --range today
    python3 calendar_get_consolidated_events.py --range week
    python3 calendar_get_consolidated_events.py --range week --group-by date

Output:
    JSON with consolidated list of events from all accounts and calendars.
"""

import argparse
import sys
from datetime import datetime, timedelta
from pathlib import Path

from auth import get_calendar_service, CREDENTIALS_DIR
from utils import (
    add_common_args, output_success, output_error, retry_with_backoff,
    get_timezone, get_date_range, parse_event_datetime, is_all_day_event,
    get_event_duration, format_duration, extract_attendees, get_organizer,
    has_video_conference, get_video_conference_link, format_time,
    format_date_short, time_until
)


# Account type labels
ACCOUNT_LABELS = {
    'victor.lang22@gmail.com': 'Personal',
    'victor@verifiedmetrics.com': 'VM'
}


def discover_accounts() -> list:
    """Auto-discover all accounts from credentials directory.

    Returns:
        List of email addresses with valid credentials
    """
    accounts = []

    if not CREDENTIALS_DIR.exists():
        return accounts

    for cred_file in CREDENTIALS_DIR.glob('*.json'):
        # Skip backup files
        if '.backup.' in cred_file.name:
            continue

        # Extract email from filename (e.g., "victor.lang22@gmail.com.json")
        email = cred_file.stem
        if '@' in email:
            accounts.append(email)

    return sorted(accounts)


def get_account_label(email: str) -> str:
    """Get the display label for an account."""
    return ACCOUNT_LABELS.get(email, email.split('@')[0])


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
    account_email: str,
    account_label: str,
    time_min: datetime,
    time_max: datetime,
    timezone_str: str = None
) -> list:
    """Get events from a single calendar with account info."""
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
                'account': {
                    'email': account_email,
                    'label': account_label
                },
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


def get_consolidated_events(
    time_min: datetime,
    time_max: datetime,
    timezone_str: str = None,
    include_hidden: bool = False
) -> tuple:
    """Get events from all calendars across all accounts.

    Deduplicates events that appear in multiple accounts (e.g., shared calendars).

    Returns:
        Tuple of (events_list, accounts_fetched)
    """
    accounts = discover_accounts()

    if not accounts:
        return [], []

    all_events = []
    seen_events = set()  # Track (event_id, start_datetime) to dedupe
    accounts_fetched = []

    for email in accounts:
        account_label = get_account_label(email)

        try:
            service = get_calendar_service(email)
            calendars = list_calendars(service, include_hidden)

            account_events = 0
            calendars_info = []

            for cal in calendars:
                events = get_events_for_calendar(
                    service,
                    cal['id'],
                    cal['name'],
                    cal['color'],
                    email,
                    account_label,
                    time_min,
                    time_max,
                    timezone_str
                )

                # Deduplicate events based on (id, start_datetime)
                unique_events = []
                for event in events:
                    event_key = (event['id'], event['start']['datetime'])
                    if event_key not in seen_events:
                        seen_events.add(event_key)
                        unique_events.append(event)

                if unique_events:
                    all_events.extend(unique_events)
                    account_events += len(unique_events)
                    calendars_info.append({
                        'id': cal['id'],
                        'name': cal['name'],
                        'event_count': len(unique_events)
                    })

            accounts_fetched.append({
                'email': email,
                'label': account_label,
                'event_count': account_events,
                'calendars': calendars_info
            })

        except Exception as e:
            # Log error but continue with other accounts
            accounts_fetched.append({
                'email': email,
                'label': account_label,
                'event_count': 0,
                'error': str(e)
            })

    # Sort all events by start time
    all_events.sort(key=lambda e: e['start']['datetime'] or '')

    return all_events, accounts_fetched


def group_events_by_date(events: list) -> dict:
    """Group events by date."""
    grouped = {}
    for event in events:
        date = event['start']['date']
        if date not in grouped:
            grouped[date] = []
        grouped[date].append(event)
    return grouped


def group_events_by_account(events: list) -> dict:
    """Group events by account."""
    grouped = {}
    for event in events:
        account_label = event['account']['label']
        if account_label not in grouped:
            grouped[account_label] = {
                'account': event['account'],
                'events': []
            }
        grouped[account_label]['events'].append(event)
    return grouped


def main():
    parser = argparse.ArgumentParser(
        description='Get consolidated events from all accounts and calendars'
    )
    parser.add_argument(
        '--timezone',
        default=None,
        help='Timezone for date formatting (e.g., America/Los_Angeles). Auto-detects if not specified.'
    )
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
        choices=['account', 'date', 'none'],
        default='date',
        help='How to group events in output (default: date)'
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

        events, accounts = get_consolidated_events(
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
            'accounts_fetched': accounts,
            'account_count': len([a for a in accounts if a.get('event_count', 0) > 0 or 'error' not in a])
        }

        if args.group_by == 'account':
            result['events_by_account'] = group_events_by_account(events)
        elif args.group_by == 'date':
            result['events_by_date'] = group_events_by_date(events)
        else:
            result['events'] = events

        output_success(result)

    except ValueError as e:
        output_error(f"Invalid date format: {e}", 'INVALID_INPUT', 1)

    except Exception as e:
        error_msg = str(e)
        output_error(error_msg, 'API_ERROR', 2)


if __name__ == '__main__':
    main()
