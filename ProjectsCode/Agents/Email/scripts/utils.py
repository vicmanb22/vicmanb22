#!/usr/bin/env python3
"""Shared utilities for Gmail API scripts.

Provides:
- Timezone auto-detection and date formatting
- MIME parsing and body extraction
- Base64url decoding
- Header extraction
- JSON output helpers
"""

import base64
import json
import sys
import time
from datetime import datetime, timezone
from email.utils import parseaddr
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


def format_datetime(timestamp_ms: Union[int, str], tz: Optional[ZoneInfo] = None) -> dict:
    """Format epoch milliseconds to human-readable and ISO formats.

    Args:
        timestamp_ms: Epoch time in milliseconds (as string or int)
        tz: Timezone for formatting (defaults to system timezone)

    Returns:
        Dict with 'display' (human-readable) and 'iso' (ISO 8601) keys
    """
    if tz is None:
        tz = get_timezone()

    ts = int(timestamp_ms) / 1000
    dt = datetime.fromtimestamp(ts, tz=timezone.utc).astimezone(tz)

    # Get timezone abbreviation
    tz_abbr = dt.strftime('%Z')

    return {
        'display': dt.strftime(f"%b %d, %Y %I:%M %p {tz_abbr}"),
        'iso': dt.isoformat()
    }


def format_date(timestamp_ms: Union[int, str], tz: Optional[ZoneInfo] = None) -> str:
    """Format epoch milliseconds to date only (e.g., 'Dec 20, 2024').

    Args:
        timestamp_ms: Epoch time in milliseconds
        tz: Timezone for formatting

    Returns:
        Formatted date string
    """
    if tz is None:
        tz = get_timezone()

    ts = int(timestamp_ms) / 1000
    dt = datetime.fromtimestamp(ts, tz=timezone.utc).astimezone(tz)
    return dt.strftime("%b %d, %Y")


def format_date_short(timestamp_ms: Union[int, str], tz: Optional[ZoneInfo] = None) -> str:
    """Format epoch milliseconds to short date (e.g., 'Dec 20').

    Args:
        timestamp_ms: Epoch time in milliseconds
        tz: Timezone for formatting

    Returns:
        Short formatted date string
    """
    if tz is None:
        tz = get_timezone()

    ts = int(timestamp_ms) / 1000
    dt = datetime.fromtimestamp(ts, tz=timezone.utc).astimezone(tz)
    return dt.strftime("%b %d")


def time_ago(timestamp_ms: Union[int, str], tz: Optional[ZoneInfo] = None) -> str:
    """Convert epoch milliseconds to human-readable relative time.

    Examples: '2h ago', '1d ago', '3w ago', '2mo ago'

    Args:
        timestamp_ms: Epoch time in milliseconds
        tz: Timezone for reference (defaults to system timezone)

    Returns:
        Human-readable relative time string
    """
    if tz is None:
        tz = get_timezone()

    ts = int(timestamp_ms) / 1000
    dt = datetime.fromtimestamp(ts, tz=timezone.utc).astimezone(tz)
    now = datetime.now(tz)

    diff = now - dt
    seconds = diff.total_seconds()

    if seconds < 0:
        return "just now"

    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    weeks = days / 7
    months = days / 30

    if seconds < 60:
        return "just now"
    elif minutes < 60:
        m = int(minutes)
        return f"{m}m ago"
    elif hours < 24:
        h = int(hours)
        return f"{h}h ago"
    elif days < 7:
        d = int(days)
        return f"{d}d ago"
    elif weeks < 4:
        w = int(weeks)
        return f"{w}w ago"
    else:
        mo = int(months)
        return f"{mo}mo ago"


# --- Email Parsing Utilities ---

def parse_email_address(header: str) -> dict:
    """Extract name and email from header like 'Name <email@example.com>'.

    Args:
        header: Email header value

    Returns:
        Dict with 'name' and 'email' keys
    """
    name, email = parseaddr(header)
    return {
        'name': name if name else (email.split('@')[0] if email else ''),
        'email': email
    }


def decode_base64url(data: str) -> str:
    """Decode base64url encoded content (Gmail API format).

    Args:
        data: Base64url encoded string

    Returns:
        Decoded UTF-8 string
    """
    if not data:
        return ''

    # Add padding if needed
    padding = 4 - len(data) % 4
    if padding != 4:
        data += '=' * padding

    # Replace URL-safe characters
    data = data.replace('-', '+').replace('_', '/')

    try:
        return base64.b64decode(data).decode('utf-8', errors='replace')
    except Exception:
        return ''


def extract_headers(headers: list) -> dict:
    """Extract common headers from Gmail message headers list.

    Args:
        headers: List of {'name': ..., 'value': ...} dicts

    Returns:
        Dict with common headers (From, To, Cc, Subject, Date, etc.)
    """
    result = {}
    header_names = [
        'From', 'To', 'Cc', 'Bcc', 'Subject', 'Date',
        'Message-ID', 'In-Reply-To', 'References', 'Reply-To'
    ]

    for h in headers:
        name = h.get('name', '')
        if name in header_names:
            result[name] = h.get('value', '')

    return result


def extract_body_from_payload(payload: dict) -> dict:
    """Recursively extract plain text and HTML body from MIME payload.

    Args:
        payload: Gmail message payload dict

    Returns:
        Dict with 'plain' and 'html' keys containing decoded body text
    """
    result = {'plain': '', 'html': ''}

    mime_type = payload.get('mimeType', '')
    body = payload.get('body', {})
    parts = payload.get('parts', [])

    # If this part has data directly
    if body.get('data'):
        decoded = decode_base64url(body['data'])
        if 'text/plain' in mime_type:
            result['plain'] = decoded
        elif 'text/html' in mime_type:
            result['html'] = decoded

    # Recursively process parts
    for part in parts:
        part_result = extract_body_from_payload(part)
        if part_result['plain'] and not result['plain']:
            result['plain'] = part_result['plain']
        if part_result['html'] and not result['html']:
            result['html'] = part_result['html']

    return result


def extract_attachments_info(payload: dict) -> list:
    """Extract attachment metadata from MIME payload.

    Args:
        payload: Gmail message payload dict

    Returns:
        List of attachment info dicts with filename, mimeType, size
    """
    attachments = []

    def process_part(part):
        body = part.get('body', {})
        filename = part.get('filename', '')

        if filename and body.get('attachmentId'):
            attachments.append({
                'filename': filename,
                'mimeType': part.get('mimeType', ''),
                'size': body.get('size', 0),
                'attachmentId': body.get('attachmentId', '')
            })

        for subpart in part.get('parts', []):
            process_part(subpart)

    process_part(payload)
    return attachments


# --- Label Utilities ---

def is_unread(label_ids: list) -> bool:
    """Check if message is unread based on label IDs."""
    return 'UNREAD' in (label_ids or [])


def is_starred(label_ids: list) -> bool:
    """Check if message is starred based on label IDs."""
    return 'STARRED' in (label_ids or [])


def is_in_inbox(label_ids: list) -> bool:
    """Check if message is in inbox based on label IDs."""
    return 'INBOX' in (label_ids or [])


# --- Query Utilities ---

def expand_category_primary(query: str) -> str:
    """Expand 'category:primary' to explicit exclusions.

    Gmail API's category:primary filter is unreliable. This expands it to:
    -category:promotions -category:social -category:updates -category:forums -is:spam

    Args:
        query: Gmail search query

    Returns:
        Query with category:primary expanded
    """
    if 'category:primary' in query:
        expansion = '-category:promotions -category:social -category:updates -category:forums -is:spam'
        query = query.replace('category:primary', expansion)
    return query


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
    print(json.dumps(response, ensure_ascii=False, indent=2))
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
        help='Gmail account email address'
    )
    parser.add_argument(
        '--timezone',
        default=None,
        help='Timezone for date formatting (e.g., Asia/Hong_Kong). Auto-detects if not specified.'
    )


if __name__ == '__main__':
    # Test timezone detection
    print(f"Detected timezone: {get_system_timezone()}")

    # Test date formatting
    now_ms = int(time.time() * 1000)
    formatted = format_datetime(now_ms)
    print(f"Current time: {formatted['display']}")
    print(f"ISO format: {formatted['iso']}")
