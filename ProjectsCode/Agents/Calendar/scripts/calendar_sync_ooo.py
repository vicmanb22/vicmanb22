#!/usr/bin/env python3
"""Sync OOO blockers from Personal calendar to VM calendar.

Scans Personal calendar events and creates corresponding OOO blocker events
in the VM calendar with a 15-minute buffer on either side.

Features:
- Filters to work hours (8am-7pm) Monday-Friday only
- Detects orphaned OOO events (where Personal event was deleted)
- Interactive confirmation before creating/deleting
- Dry-run mode for preview

Usage:
    python3 calendar_sync_ooo.py --range week
    python3 calendar_sync_ooo.py --range month --dry-run
    python3 calendar_sync_ooo.py --buffer 30 --work-start 09:00 --work-end 18:00

Output:
    JSON with sync results or interactive preview.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, time
from zoneinfo import ZoneInfo

from auth import get_calendar_service
from utils import (
    get_date_range, get_timezone, format_time, format_date_short,
    output_success, output_error, retry_with_backoff
)

# Account configuration
PERSONAL_EMAIL = 'victor.lang22@gmail.com'
VM_EMAIL = 'victor@verifiedmetrics.com'

# Auto-sync marker in description
AUTO_SYNC_TAG = '[AUTO-SYNC]'


def parse_time(time_str: str) -> time:
    """Parse time string like '08:00' or '8:00'."""
    parts = time_str.split(':')
    return time(int(parts[0]), int(parts[1]) if len(parts) > 1 else 0)


def is_weekday(dt: datetime) -> bool:
    """Check if datetime is a weekday (Monday=0 to Friday=4)."""
    return dt.weekday() < 5


def is_in_work_hours(dt: datetime, work_start: time, work_end: time) -> bool:
    """Check if datetime is within work hours."""
    dt_time = dt.time()
    return work_start <= dt_time <= work_end


def clip_to_work_hours(
    start: datetime,
    end: datetime,
    work_start: time,
    work_end: time,
    tz: ZoneInfo
) -> tuple:
    """Clip event times to work hours, returning None if entirely outside."""
    # Check if on a weekday
    if not is_weekday(start):
        return None, None

    # Get work hours for this day
    day_start = start.replace(hour=work_start.hour, minute=work_start.minute, second=0, microsecond=0)
    day_end = start.replace(hour=work_end.hour, minute=work_end.minute, second=0, microsecond=0)

    # Clip start and end to work hours
    clipped_start = max(start, day_start)
    clipped_end = min(end, day_end)

    # If no overlap with work hours, return None
    if clipped_start >= clipped_end:
        return None, None

    return clipped_start, clipped_end


def add_buffer(start: datetime, end: datetime, buffer_minutes: int) -> tuple:
    """Add buffer to start and end times."""
    buffer = timedelta(minutes=buffer_minutes)
    return start - buffer, end + buffer


def get_events_for_range(
    service,
    calendar_id: str,
    time_min: datetime,
    time_max: datetime
) -> list:
    """Fetch all events in a date range."""
    events = []
    page_token = None

    while True:
        def fetch():
            return service.events().list(
                calendarId=calendar_id,
                timeMin=time_min.isoformat(),
                timeMax=time_max.isoformat(),
                maxResults=250,
                singleEvents=True,
                orderBy='startTime',
                pageToken=page_token
            ).execute()

        result = retry_with_backoff(fetch)
        events.extend(result.get('items', []))

        page_token = result.get('nextPageToken')
        if not page_token:
            break

    return events


def parse_event_datetime(event_time: dict, tz: ZoneInfo) -> datetime:
    """Parse event start/end time."""
    if 'dateTime' in event_time:
        dt_str = event_time['dateTime']
        return datetime.fromisoformat(dt_str)
    elif 'date' in event_time:
        # All-day event
        date_str = event_time['date']
        dt = datetime.strptime(date_str, '%Y-%m-%d')
        return dt.replace(tzinfo=tz)
    return None


def extract_synced_event_id(description: str) -> str:
    """Extract the Personal event ID from OOO description."""
    if not description or AUTO_SYNC_TAG not in description:
        return None

    # Pattern: [AUTO-SYNC] event_id_here
    match = re.search(rf'{re.escape(AUTO_SYNC_TAG)}\s+(\S+)', description)
    if match:
        return match.group(1)
    return None


def events_overlap(start1: datetime, end1: datetime, start2: datetime, end2: datetime) -> bool:
    """Check if two time ranges overlap."""
    return start1 < end2 and start2 < end1


def find_covering_ooo(
    original_start: datetime,
    original_end: datetime,
    vm_ooo_events: list,
    tz: ZoneInfo
) -> dict:
    """Find an existing OOO event that overlaps with the original event time.

    We check against original (non-buffered) time because existing OOO events
    may have been created without the buffer concept.
    """
    for ooo in vm_ooo_events:
        ooo_start = parse_event_datetime(ooo.get('start', {}), tz)
        ooo_end = parse_event_datetime(ooo.get('end', {}), tz)

        if ooo_start and ooo_end:
            # Check if OOO overlaps significantly with the original event
            # (at least 50% of the original event time is covered)
            if events_overlap(original_start, original_end, ooo_start, ooo_end):
                # Calculate overlap
                overlap_start = max(original_start, ooo_start)
                overlap_end = min(original_end, ooo_end)
                overlap_duration = (overlap_end - overlap_start).total_seconds()
                original_duration = (original_end - original_start).total_seconds()

                # If OOO covers at least 50% of original event, consider it blocked
                if original_duration > 0 and overlap_duration / original_duration >= 0.5:
                    return ooo

    return None


def analyze_sync(
    personal_events: list,
    vm_ooo_events: list,
    buffer_minutes: int,
    work_start: time,
    work_end: time,
    tz: ZoneInfo
) -> dict:
    """Analyze what needs to be synced.

    Returns:
        {
            'needs_creation': [...],  # Personal events needing OOO
            'already_blocked': [...],  # Personal events with existing OOO
            'orphaned': [...]  # OOO events without matching Personal event
        }
    """
    needs_creation = []
    already_blocked = []

    # Build set of Personal event IDs for orphan detection
    personal_event_ids = {e['id'] for e in personal_events}

    for event in personal_events:
        start = parse_event_datetime(event.get('start', {}), tz)
        end = parse_event_datetime(event.get('end', {}), tz)

        if not start or not end:
            continue

        # Handle all-day events: treat as full work day
        if 'date' in event.get('start', {}):
            start = start.replace(hour=work_start.hour, minute=work_start.minute)
            end = start.replace(hour=work_end.hour, minute=work_end.minute)

        # Clip to work hours
        clipped_start, clipped_end = clip_to_work_hours(start, end, work_start, work_end, tz)

        if clipped_start is None:
            # Event is outside work hours or on weekend
            continue

        # Add buffer and clip again
        buffered_start, buffered_end = add_buffer(clipped_start, clipped_end, buffer_minutes)
        buffered_start, buffered_end = clip_to_work_hours(buffered_start, buffered_end, work_start, work_end, tz)

        if buffered_start is None:
            continue

        # Check for existing OOO using clipped (not buffered) time
        # This catches existing OOO events that were created without buffer
        existing_ooo = find_covering_ooo(clipped_start, clipped_end, vm_ooo_events, tz)

        event_info = {
            'id': event['id'],
            'summary': event.get('summary', '(No title)'),
            'original_start': start.isoformat(),
            'original_end': end.isoformat(),
            'buffered_start': buffered_start.isoformat(),
            'buffered_end': buffered_end.isoformat(),
            'formatted_time': f"{format_date_short(start, tz)}, {format_time(start, tz)}-{format_time(end, tz)}",
            'formatted_ooo': f"{format_time(buffered_start, tz)} - {format_time(buffered_end, tz)}"
        }

        if existing_ooo:
            event_info['existing_ooo'] = {
                'id': existing_ooo['id'],
                'summary': existing_ooo.get('summary', 'OOO'),
                'start': existing_ooo.get('start', {}).get('dateTime'),
                'end': existing_ooo.get('end', {}).get('dateTime')
            }
            already_blocked.append(event_info)
        else:
            needs_creation.append(event_info)

    # Find orphaned OOO events
    orphaned = []
    for ooo in vm_ooo_events:
        description = ooo.get('description', '')
        synced_event_id = extract_synced_event_id(description)

        if synced_event_id and synced_event_id not in personal_event_ids:
            ooo_start = parse_event_datetime(ooo.get('start', {}), tz)
            orphaned.append({
                'id': ooo['id'],
                'summary': ooo.get('summary', 'OOO'),
                'start': ooo.get('start', {}).get('dateTime'),
                'end': ooo.get('end', {}).get('dateTime'),
                'formatted_time': f"{format_date_short(ooo_start, tz)}, {format_time(ooo_start, tz)}",
                'original_event_id': synced_event_id
            })

    return {
        'needs_creation': needs_creation,
        'already_blocked': already_blocked,
        'orphaned': orphaned
    }


def create_ooo_event(
    service,
    personal_event: dict,
    tz: ZoneInfo
) -> dict:
    """Create an OOO event in VM calendar."""
    event_body = {
        'summary': 'OOO',
        'start': {'dateTime': personal_event['buffered_start']},
        'end': {'dateTime': personal_event['buffered_end']},
        'description': f"{AUTO_SYNC_TAG} {personal_event['id']}\nBlocking for: {personal_event['summary']}",
        'transparency': 'opaque',
        'visibility': 'private'
    }

    def create():
        return service.events().insert(
            calendarId='primary',
            body=event_body
        ).execute()

    return retry_with_backoff(create)


def delete_ooo_event(service, event_id: str) -> None:
    """Delete an OOO event from VM calendar."""
    def delete():
        service.events().delete(
            calendarId='primary',
            eventId=event_id
        ).execute()

    retry_with_backoff(delete)


def main():
    parser = argparse.ArgumentParser(
        description='Sync OOO blockers from Personal to VM calendar'
    )
    parser.add_argument(
        '--range',
        default='week',
        choices=['today', 'tomorrow', 'week', 'month'],
        help='Date range to sync (default: week)'
    )
    parser.add_argument(
        '--buffer',
        type=int,
        default=15,
        help='Buffer minutes on each side of events (default: 15)'
    )
    parser.add_argument(
        '--work-start',
        default='08:00',
        help='Work hours start time (default: 08:00)'
    )
    parser.add_argument(
        '--work-end',
        default='19:00',
        help='Work hours end time (default: 19:00)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    parser.add_argument(
        '--auto-confirm',
        action='store_true',
        help='Create/delete without prompting for confirmation'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as JSON (for agent use)'
    )

    args = parser.parse_args()

    try:
        tz = get_timezone()
        work_start = parse_time(args.work_start)
        work_end = parse_time(args.work_end)

        # Get date range
        time_min, time_max = get_date_range(args.range, tz)

        # Get services for both accounts
        personal_service = get_calendar_service(PERSONAL_EMAIL)
        vm_service = get_calendar_service(VM_EMAIL)

        # Fetch events
        personal_events = get_events_for_range(personal_service, 'primary', time_min, time_max)
        vm_events = get_events_for_range(vm_service, 'primary', time_min, time_max)

        # Filter VM events to only OOO or auto-synced
        vm_ooo_events = [
            e for e in vm_events
            if e.get('summary', '').upper() == 'OOO' or AUTO_SYNC_TAG in e.get('description', '')
        ]

        # Analyze what needs to be done
        analysis = analyze_sync(
            personal_events,
            vm_ooo_events,
            args.buffer,
            work_start,
            work_end,
            tz
        )

        # JSON output mode for agent
        if args.json:
            result = {
                'range': {
                    'start': time_min.isoformat(),
                    'end': time_max.isoformat()
                },
                'buffer_minutes': args.buffer,
                'work_hours': f"{args.work_start}-{args.work_end}",
                'personal_account': PERSONAL_EMAIL,
                'vm_account': VM_EMAIL,
                **analysis
            }

            if args.dry_run:
                result['dry_run'] = True
                output_success(result)
                return

            # In JSON mode with auto-confirm, just do it
            if args.auto_confirm:
                created = []
                deleted = []

                for event in analysis['needs_creation']:
                    created_event = create_ooo_event(vm_service, event, tz)
                    created.append({
                        'id': created_event['id'],
                        'for_event': event['summary'],
                        'time': f"{event['formatted_ooo']}"
                    })

                for ooo in analysis['orphaned']:
                    delete_ooo_event(vm_service, ooo['id'])
                    deleted.append({
                        'id': ooo['id'],
                        'time': ooo['formatted_time']
                    })

                result['created'] = created
                result['deleted'] = deleted
                output_success(result)
                return

            output_success(result)
            return

        # Interactive mode
        print(f"\n## OOO Sync Preview\n")
        print(f"**Personal Calendar:** {PERSONAL_EMAIL}")
        print(f"**VM Calendar:** {VM_EMAIL}")
        print(f"**Range:** {format_date_short(time_min, tz)} - {format_date_short(time_max, tz)}")
        print(f"**Buffer:** {args.buffer} minutes")
        print(f"**Work Hours:** {args.work_start} - {args.work_end}\n")

        # Events needing OOO
        needs_creation = analysis['needs_creation']
        if needs_creation:
            print(f"### Events Needing OOO Blockers ({len(needs_creation)})\n")
            print("| # | Personal Event | Time | OOO Block (with buffer) |")
            print("|---|----------------|------|-------------------------|")
            for i, event in enumerate(needs_creation, 1):
                print(f"| {i} | {event['summary'][:30]} | {event['formatted_time']} | {event['formatted_ooo']} |")
            print()

        # Already blocked
        already_blocked = analysis['already_blocked']
        if already_blocked:
            print(f"### Already Blocked ({len(already_blocked)})\n")
            print("| Personal Event | Time | Existing OOO |")
            print("|----------------|------|--------------|")
            for event in already_blocked:
                ooo = event['existing_ooo']
                ooo_start = datetime.fromisoformat(ooo['start'])
                ooo_end = datetime.fromisoformat(ooo['end'])
                print(f"| {event['summary'][:30]} | {event['formatted_time']} | {format_time(ooo_start, tz)}-{format_time(ooo_end, tz)} |")
            print()

        # Orphaned OOO
        orphaned = analysis['orphaned']
        if orphaned:
            print(f"### Orphaned OOO Events ({len(orphaned)})\n")
            print("| # | OOO Event | Time | Original Event |")
            print("|---|-----------|------|----------------|")
            for i, ooo in enumerate(orphaned, 1):
                print(f"| {i} | {ooo['summary']} | {ooo['formatted_time']} | (Deleted) |")
            print()

        if not needs_creation and not orphaned:
            print("**Everything is in sync!** No actions needed.\n")
            return

        if args.dry_run:
            print("---\n**Dry run mode** - no changes made.\n")
            return

        # Confirmation
        print("---")

        created_count = 0
        deleted_count = 0

        if needs_creation:
            if args.auto_confirm:
                confirm_create = True
            else:
                response = input(f"Create {len(needs_creation)} OOO blockers? [y/N] ").strip().lower()
                confirm_create = response == 'y'

            if confirm_create:
                for event in needs_creation:
                    created_event = create_ooo_event(vm_service, event, tz)
                    print(f"  Created OOO for: {event['summary']}")
                    created_count += 1

        if orphaned:
            if args.auto_confirm:
                confirm_delete = True
            else:
                response = input(f"Delete {len(orphaned)} orphaned OOO events? [y/N] ").strip().lower()
                confirm_delete = response == 'y'

            if confirm_delete:
                for ooo in orphaned:
                    delete_ooo_event(vm_service, ooo['id'])
                    print(f"  Deleted orphaned OOO: {ooo['formatted_time']}")
                    deleted_count += 1

        print(f"\n**Done!** Created: {created_count}, Deleted: {deleted_count}\n")

    except Exception as e:
        if args.json if 'args' in dir() else False:
            output_error(str(e), 'SYNC_ERROR', 2)
        else:
            print(f"\nError: {e}\n", file=sys.stderr)
            sys.exit(2)


if __name__ == '__main__':
    main()
