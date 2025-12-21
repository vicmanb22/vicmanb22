# Calendar Agent

Google Calendar management with full read/write capabilities. **Default: Consolidated view across all accounts.**

## Overview

Multi-account calendar agent using the same Google API credentials as the Email agent. Provides calendar schedules, event creation/editing, RSVP, and search.

## Architecture

```
Calendar/
├── CLAUDE.md                 # This file
├── CHANGELOG.md              # Version history
├── .claude/
│   ├── agents/
│   │   ├── calendar.md       # Orchestrator
│   │   └── schedule.md       # Schedule subagent
│   ├── commands/
│   │   ├── calendar.md       # /calendar command
│   │   └── schedule.md       # /schedule command
│   └── settings.json         # Bash permissions
└── scripts/
    ├── auth.py               # OAuth management
    ├── reauth.py             # Re-authentication
    ├── utils.py              # Shared utilities
    ├── calendar_get_consolidated_events.py  # All accounts (default)
    ├── calendar_get_all_events.py           # Single account
    ├── calendar_list_calendars.py
    ├── calendar_get_events.py
    ├── calendar_search_events.py
    ├── calendar_quick_add.py       # Natural language event creation
    ├── calendar_create_event.py    # Full event creation
    ├── calendar_update_event.py    # Update event
    ├── calendar_delete_event.py    # Delete event
    ├── calendar_rsvp.py            # RSVP to invites
    ├── calendar_move_event.py      # Move between calendars
    ├── calendar_sync_ooo.py        # Sync OOO blockers Personal→VM
    └── requirements.txt
```

## Accounts

| Account | Label |
|---------|-------|
| victor.lang22@gmail.com | Personal |
| victor@verifiedmetrics.com | VM |

Credentials stored at: `~/.google_workspace_mcp/credentials/{email}.json`

Uses same OAuth tokens as Email agent (Calendar scopes already included).

## Commands

| Command | Description |
|---------|-------------|
| `/calendar` | Quick calendar operations |
| `/schedule` | Generate calendar schedule (consolidated by default) |

## Agents

| Agent | Purpose |
|-------|---------|
| `@calendar` | Main orchestrator, routes to subagents |
| `@schedule` | Calendar schedule generation |

## Read Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `calendar_get_consolidated_events.py` | Get events from ALL accounts | `--range week` |
| `calendar_get_all_events.py` | Get events from one account | `--email {account} --range week` |
| `calendar_list_calendars.py` | List all calendars | `--email {account}` |
| `calendar_get_events.py` | Get events from one calendar | `--email {account} --range week` |
| `calendar_search_events.py` | Search events | `--email {account} --query "meeting"` |

## Write Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `calendar_quick_add.py` | Natural language event creation | `--email {account} --text "Lunch tomorrow at noon"` |
| `calendar_create_event.py` | Full event creation | `--email {account} --title "Meeting" --start "2025-12-23T09:00"` |
| `calendar_update_event.py` | Update existing event | `--email {account} --event-id {id} --title "New Title"` |
| `calendar_delete_event.py` | Delete event | `--email {account} --event-id {id}` |
| `calendar_rsvp.py` | RSVP to invitation | `--email {account} --event-id {id} --response accepted` |
| `calendar_move_event.py` | Move between calendars | `--email {account} --event-id {id} --destination {cal_id}` |
| `calendar_sync_ooo.py` | Sync OOO blockers Personal→VM | `--range week --buffer 15` |

### Common Options

| Option | Description |
|--------|-------------|
| `--range` | Date range: today, tomorrow, week, month |
| `--group-by` | Grouping: date (default), account |
| `--timezone` | Override timezone (auto-detected) |

## Write Operations

| Action | Example Command |
|--------|-----------------|
| Quick add | "Add lunch with Sarah tomorrow at noon" |
| Create with details | "Create meeting titled X at 2pm with Y" |
| Create from email | "Create event from email #22" |
| Update | "Move event #5 to 3pm" |
| Delete | "Delete event #7" |
| RSVP | "Accept event #5" |
| Move | "Move event #3 to Work calendar" |
| Sync OOO | "Sync my OOO blockers for this week" |

## OOO Sync

Automatically creates OOO blockers in VM calendar for Personal calendar events.

**Features:**
- Scans Personal calendar for events during work hours (8am-7pm Mon-Fri)
- Creates OOO blockers in VM calendar with 15-minute buffer
- Detects orphaned OOO events (where Personal event was deleted)
- Interactive confirmation before changes

**Usage:**
```bash
# Preview what would be synced
python3 scripts/calendar_sync_ooo.py --range week --dry-run

# Sync with confirmation prompts
python3 scripts/calendar_sync_ooo.py --range week

# Auto-confirm (for automation)
python3 scripts/calendar_sync_ooo.py --range week --auto-confirm
```

### Write Behavior

- **Google Meet**: Ask before adding (not automatic)
- **Notifications**: Use Google default behavior
- **Account selection**: Ask when creating if not specified
- **Event references**: Use sequential numbers from schedule (e.g., "event #5")

## Create Event from Email

Create calendar events by extracting details from emails in the digest.

**Trigger phrases:**
- "Create event from email #22"
- "Add email #5 to calendar"
- "Schedule the meeting from email #3"

**Process:**
1. Reads `/tmp/email-digest-context.json` (written by Email digest)
2. Fetches full email content using Email scripts
3. LLM extracts: title, date, time, timezone, duration, location, attendees
4. Shows preview for confirmation
5. Creates event after user confirms

**Timezone detection priority:**
1. Explicit in email body: "9:45am CST", "3pm Pacific Time"
2. Email header timezone from `date_iso`
3. User's local timezone (default)

**Example:** Email from Lisa Glista saying "Dr Reichlin has tomorrow at 9:45am CST" → Creates event titled "Follow-Up with Dr Reichlin" at 9:45 AM CST.

## Schedule Features

- **Consolidated view (default)**: All accounts in one view
- **Single account view**: One account only with `--account`
- **Group by date**: Events organized by day (default)
- **Group by account**: Events organized by account
- **Conflict detection**: Highlights overlapping events
- **Video meeting links**: Shows Meet/Zoom links
- **Sequential numbering**: Reference events by number

## Integration

Part of the MainOrchestrator personal life system. Access via:
- Direct: `@calendar` or `/calendar`
- Via MainOrchestrator: `/life` → Calendar

## Error Handling

| Error | Solution |
|-------|----------|
| Credentials not found | Run `reauth.py --email {account}` |
| Token expired | Auto-refreshes, or run `reauth.py` |
| API rate limit | Auto-retries with backoff |
| Calendar access denied | Check calendar sharing settings |
| Event not found | Verify event ID from schedule |
