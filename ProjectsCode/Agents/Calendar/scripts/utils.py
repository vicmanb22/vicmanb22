#!/usr/bin/env python3
"""Shared utilities for Google Calendar API scripts.

Provides:
- Timezone auto-detection and date formatting
- Event parsing and formatting
- Duration calculations
- JSON output helpers
"""

import json
import sys
import time
from datetime import datetime, timedelta, timezone
from typing import Optional, Any, Union
from zoneinfo import ZoneInfo


# --- Timezone Utilities ---

def get_system_timezone() -> str:
    """Auto-detect system timezone.

    Checks in order:
    1. TZ environment variable
    2. /etc/localtime symlink
    3. Falls back to UTC

    Returns:
        IANA timezone string (e.g., 'Asia/Hong_Kong', 'America/New_York')
    """
    import os

    # Check TZ environment variable
    tz_env = os.environ.get('TZ')
    if tz_env:
        try:
            ZoneInfo(tz_env)
            return tz_env
        except Exception:
            pass

    # Try to read /etc/localtime symlink (macOS/Linux)
    try:
        import subprocess
        result = subprocess.run(
            ['readlink', '/etc/localtime'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            # Extract timezone from path like /var/db/timezone/zoneinfo/Asia/Hong_Kong
            path = result.stdout.strip()
            if 'zoneinfo/' in path:
                tz_name = path.split('zoneinfo/')[-1]
                ZoneInfo(tz_name)  # Validate it
                return tz_name
    except Exception:
        pass

    # Try macOS-specific method
    try:
        import subprocess
        result = subprocess.run(
            ['systemsetup', '-gettimezone'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            # Output like "Time Zone: Asia/Hong_Kong"
            tz_name = result.stdout.strip().replace('Time Zone: ', '')
            ZoneInfo(tz_name)  # Validate it
            return tz_name
    except Exception:
        pass

    # Fallback to UTC
    return 'UTC'


def get_timezone(tz_name: Optional[str] = None) -> ZoneInfo:
    """Get a ZoneInfo object for the specified or system timezone.

    Args:
        tz_name: IANA timezone name, or None for auto-detect

    Returns:
        ZoneInfo object
    """
    if tz_name is None:
        tz_name = get_system_timezone()
    return ZoneInfo(tz_name)


def format_datetime(dt: datetime, tz: Optional[ZoneInfo] = None) -> dict:
    """Format datetime to human-readable and ISO formats.

    Args:
        dt: datetime object
        tz: Timezone for formatting (defaults to system timezone)

    Returns:
        Dict with 'display' (human-readable) and 'iso' (ISO 8601) keys
    """
    if tz is None:
        tz = get_timezone()

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=tz)
    else:
        dt = dt.astimezone(tz)

    # Get timezone abbreviation
    tz_abbr = dt.strftime('%Z')

    return {
        'display': dt.strftime(f"%b %d, %Y %I:%M %p {tz_abbr}"),
        'iso': dt.isoformat()
    }


def format_date(dt: datetime, tz: Optional[ZoneInfo] = None) -> str:
    """Format datetime to date only (e.g., 'Dec 20, 2024').

    Args:
        dt: datetime object
        tz: Timezone for formatting

    Returns:
        Formatted date string
    """
    if tz is None:
        tz = get_timezone()

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=tz)
    else:
        dt = dt.astimezone(tz)

    return dt.strftime("%b %d, %Y")


def format_date_short(dt: datetime, tz: Optional[ZoneInfo] = None) -> str:
    """Format datetime to short date (e.g., 'Dec 20').

    Args:
        dt: datetime object
        tz: Timezone for formatting

    Returns:
        Short formatted date string
    """
    if tz is None:
        tz = get_timezone()

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=tz)
    else:
        dt = dt.astimezone(tz)

    return dt.strftime("%b %d")


def format_time(dt: datetime, tz: Optional[ZoneInfo] = None) -> str:
    """Format datetime to time only (e.g., '2:30 PM').

    Args:
        dt: datetime object
        tz: Timezone for formatting

    Returns:
        Formatted time string
    """
    if tz is None:
        tz = get_timezone()

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=tz)
    else:
        dt = dt.astimezone(tz)

    return dt.strftime("%I:%M %p").lstrip('0')


def format_time_range(start: datetime, end: datetime, tz: Optional[ZoneInfo] = None) -> str:
    """Format a time range (e.g., '2:30 PM - 3:30 PM').

    Args:
        start: Start datetime
        end: End datetime
        tz: Timezone for formatting

    Returns:
        Formatted time range string
    """
    return f"{format_time(start, tz)} - {format_time(end, tz)}"


def time_until(dt: datetime, tz: Optional[ZoneInfo] = None) -> str:
    """Get human-readable time until a datetime.

    Examples: 'in 2h', 'in 1d', 'in 3w', 'now'

    Args:
        dt: Target datetime
        tz: Timezone for reference

    Returns:
        Human-readable relative time string
    """
    if tz is None:
        tz = get_timezone()

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=tz)
    else:
        dt = dt.astimezone(tz)

    now = datetime.now(tz)
    diff = dt - now
    seconds = diff.total_seconds()

    if seconds < 0:
        return "past"

    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    weeks = days / 7

    if seconds < 60:
        return "now"
    elif minutes < 60:
        m = int(minutes)
        return f"in {m}m"
    elif hours < 24:
        h = int(hours)
        return f"in {h}h"
    elif days < 7:
        d = int(days)
        return f"in {d}d"
    else:
        w = int(weeks)
        return f"in {w}w"


# --- Event Parsing Utilities ---

def parse_event_datetime(event_time: dict) -> Optional[datetime]:
    """Parse event start/end time from Calendar API format.

    Handles both dateTime (timed events) and date (all-day events).

    Args:
        event_time: Dict with 'dateTime' or 'date' key

    Returns:
        datetime object or None
    """
    if not event_time:
        return None

    if 'dateTime' in event_time:
        # Timed event: "2024-12-20T14:00:00-08:00"
        dt_str = event_time['dateTime']
        return datetime.fromisoformat(dt_str)
    elif 'date' in event_time:
        # All-day event: "2024-12-20"
        date_str = event_time['date']
        return datetime.strptime(date_str, '%Y-%m-%d')

    return None


def is_all_day_event(event: dict) -> bool:
    """Check if event is an all-day event.

    Args:
        event: Calendar event dict

    Returns:
        True if all-day event
    """
    start = event.get('start', {})
    return 'date' in start and 'dateTime' not in start


def get_event_duration(event: dict) -> Optional[timedelta]:
    """Get the duration of an event.

    Args:
        event: Calendar event dict

    Returns:
        timedelta or None if can't be calculated
    """
    start = parse_event_datetime(event.get('start', {}))
    end = parse_event_datetime(event.get('end', {}))

    if start and end:
        return end - start
    return None


def format_duration(td: timedelta) -> str:
    """Format a timedelta as human-readable duration.

    Args:
        td: timedelta object

    Returns:
        String like '1h 30m', '2h', '30m', '1d'
    """
    total_seconds = int(td.total_seconds())

    if total_seconds < 0:
        return "0m"

    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60

    if days > 0:
        if hours > 0:
            return f"{days}d {hours}h"
        return f"{days}d"
    elif hours > 0:
        if minutes > 0:
            return f"{hours}h {minutes}m"
        return f"{hours}h"
    else:
        return f"{minutes}m"


def extract_attendees(event: dict) -> list:
    """Extract attendee information from an event.

    Args:
        event: Calendar event dict

    Returns:
        List of attendee dicts with email, name, response status
    """
    attendees = []
    for a in event.get('attendees', []):
        attendees.append({
            'email': a.get('email', ''),
            'name': a.get('displayName', a.get('email', '').split('@')[0]),
            'response': a.get('responseStatus', 'needsAction'),
            'organizer': a.get('organizer', False),
            'self': a.get('self', False)
        })
    return attendees


def get_organizer(event: dict) -> dict:
    """Get the organizer of an event.

    Args:
        event: Calendar event dict

    Returns:
        Dict with email and name
    """
    organizer = event.get('organizer', {})
    return {
        'email': organizer.get('email', ''),
        'name': organizer.get('displayName', organizer.get('email', '').split('@')[0] if organizer.get('email') else '')
    }


def get_event_status(event: dict) -> str:
    """Get the status of an event (confirmed, tentative, cancelled).

    Args:
        event: Calendar event dict

    Returns:
        Status string
    """
    return event.get('status', 'confirmed')


def has_video_conference(event: dict) -> bool:
    """Check if event has a video conference link.

    Args:
        event: Calendar event dict

    Returns:
        True if has video conference
    """
    conf_data = event.get('conferenceData', {})
    return bool(conf_data.get('entryPoints', []))


def get_video_conference_link(event: dict) -> Optional[str]:
    """Get the video conference link for an event.

    Args:
        event: Calendar event dict

    Returns:
        Video link URL or None
    """
    conf_data = event.get('conferenceData', {})
    for entry in conf_data.get('entryPoints', []):
        if entry.get('entryPointType') == 'video':
            return entry.get('uri')
    return None


# --- Date Range Utilities ---

def get_date_range(range_type: str, tz: Optional[ZoneInfo] = None) -> tuple:
    """Get start and end datetime for a named range.

    Args:
        range_type: One of 'today', 'tomorrow', 'week', 'month'
        tz: Timezone

    Returns:
        Tuple of (start_datetime, end_datetime)
    """
    if tz is None:
        tz = get_timezone()

    now = datetime.now(tz)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    if range_type == 'today':
        start = today_start
        end = start + timedelta(days=1)
    elif range_type == 'tomorrow':
        start = today_start + timedelta(days=1)
        end = start + timedelta(days=1)
    elif range_type == 'week':
        # Start from today, go 7 days
        start = today_start
        end = start + timedelta(days=7)
    elif range_type == 'month':
        # Start from today, go 30 days
        start = today_start
        end = start + timedelta(days=30)
    else:
        # Default to today
        start = today_start
        end = start + timedelta(days=1)

    return start, end


# --- Text Utilities ---

def truncate_text(text: str, max_length: int = 200) -> str:
    """Truncate text to max length with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + '...'


def clean_text(text: str) -> str:
    """Clean text by removing excess whitespace."""
    import re
    # Replace multiple whitespace with single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# --- JSON Output Utilities ---

def output_success(data: dict) -> None:
    """Output successful JSON response and exit with code 0."""
    response = {'success': True, **data}
    print(json.dumps(response, ensure_ascii=False, indent=2, default=str))
    sys.exit(0)


def output_error(message: str, error_type: str, exit_code: int = 1) -> None:
    """Output error JSON response and exit.

    Args:
        message: Error message
        error_type: Error type code (e.g., 'AUTH_ERROR', 'API_ERROR')
        exit_code: Exit code (1=user error, 2=API error, 3=auth error)
    """
    response = {
        'success': False,
        'error': message,
        'error_type': error_type
    }
    print(json.dumps(response, ensure_ascii=False, indent=2))
    sys.exit(exit_code)


# --- Retry Utilities ---

def retry_with_backoff(
    func,
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    retry_on: tuple = (429,)
):
    """Execute function with exponential backoff retry.

    Args:
        func: Function to execute
        max_retries: Maximum number of retries
        base_delay: Initial delay in seconds
        max_delay: Maximum delay in seconds
        retry_on: HTTP status codes to retry on

    Returns:
        Function result

    Raises:
        Last exception if all retries fail
    """
    from googleapiclient.errors import HttpError

    last_exception = None
    delay = base_delay

    for attempt in range(max_retries + 1):
        try:
            return func()
        except HttpError as e:
            last_exception = e
            if e.resp.status in retry_on and attempt < max_retries:
                time.sleep(delay)
                delay = min(delay * 2, max_delay)
            else:
                raise

    raise last_exception


# --- Argument Parsing Helpers ---

def add_common_args(parser) -> None:
    """Add common arguments to an argument parser.

    Args:
        parser: argparse.ArgumentParser instance
    """
    parser.add_argument(
        '--email',
        required=True,
        help='Google account email address'
    )
    parser.add_argument(
        '--timezone',
        default=None,
        help='Timezone for date formatting (e.g., America/Los_Angeles). Auto-detects if not specified.'
    )


if __name__ == '__main__':
    # Test timezone detection
    print(f"Detected timezone: {get_system_timezone()}")

    # Test date formatting
    now = datetime.now(get_timezone())
    formatted = format_datetime(now)
    print(f"Current time: {formatted['display']}")
    print(f"ISO format: {formatted['iso']}")

    # Test date ranges
    for range_type in ['today', 'tomorrow', 'week', 'month']:
        start, end = get_date_range(range_type)
        print(f"{range_type}: {start.date()} to {end.date()}")
