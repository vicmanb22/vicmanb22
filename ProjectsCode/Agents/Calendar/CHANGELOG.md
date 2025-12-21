# Changelog

All notable changes to the Calendar agent.

## [1.6.1] - 2025-12-20

### Changed
- Now supports 5 accounts via GoogleAccounts integration (was 2)
- New accounts: vlang@cloudviewre.com, victor@argonautexpeditions.com, victor.lang@modelun.net

## [1.6.0] - 2025-12-20

### Changed
- **Auth refactored to use GoogleAccounts**: `auth.py` and `reauth.py` now delegate to centralized `GoogleAccounts/scripts/auth.py`
- All authentication logic is now in one place for easier maintenance
- No changes to script interfaces - fully backward compatible

---

## [1.5.0] - 2025-12-20

### Added
- **Create Event from Email**: Extract event details from email content and create calendar events
  - Reads email context from `/tmp/email-digest-context.json` (written by Email digest)
  - Fetches full email content using Email agent scripts
  - LLM extracts: title, date, time, timezone, duration, location, attendees, description
  - Timezone detection priority: email body explicit → email header → local timezone
  - Shows preview for confirmation before creating
  - Trigger phrases: "create event from email #3", "add email #5 to calendar"

### Changed
- Updated bash permissions to use correct `:*` suffix syntax for prefix matching
- Added permissions to run Email agent scripts and read context file

---

## [1.4.0] - 2025-12-20

### Added
- **OOO Sync**: Automatically sync OOO blockers from Personal to VM calendar
- `calendar_sync_ooo.py` - Scans Personal calendar and creates OOO blockers
- 15-minute buffer on each side of events (configurable)
- Filters to work hours (8am-7pm Mon-Fri)
- Orphan detection: finds OOO events where Personal event was deleted
- Interactive confirmation or `--auto-confirm` for automation
- `--dry-run` mode to preview without changes

---

## [1.3.0] - 2025-12-20

### Added
- **Write operations**: Full event management capabilities
- `calendar_quick_add.py` - Natural language event creation ("Lunch tomorrow at noon")
- `calendar_create_event.py` - Full event creation with attendees, location, recurrence
- `calendar_update_event.py` - Modify existing events using PATCH
- `calendar_delete_event.py` - Remove events
- `calendar_rsvp.py` - Respond to invitations (accept/decline/tentative)
- `calendar_move_event.py` - Move events between calendars

### Write Behavior
- Google Meet links: Ask before adding (not automatic)
- Attendee notifications: Use Google default behavior
- Event references: Use sequential numbers from schedule (e.g., "event #5")

---

## [1.2.0] - 2025-12-20

### Changed
- Renamed "digest" to "schedule" throughout the agent
- `/digest` command → `/schedule`
- `@digest` subagent → `@schedule`

---

## [1.1.0] - 2025-12-20

### Added
- **Consolidated schedule view** (now default): Shows ALL events from ALL accounts in one unified view
- New script `calendar_get_consolidated_events.py` - auto-discovers accounts and fetches all events
- Account labels in consolidated view (Personal, VM)

### Changed
- Default schedule behavior is now consolidated (all accounts) instead of requiring account selection
- Renamed account label "Work" → "VM" for victor@verifiedmetrics.com
- Updated table format to include Account column in consolidated view

### Single Account Mode
- Use `--account {email}` flag to view single account only
- Previous single-account behavior still available

---

## [1.0.0] - 2025-12-20

### Added
- Initial release of Calendar agent
- Multi-account support using same credentials as Email agent
- Orchestrator pattern with subagents:
  - `@calendar` - Main orchestrator
  - `@schedule` - Calendar schedule generation
- Python scripts for Calendar API:
  - auth.py, reauth.py, utils.py
  - calendar_list_calendars.py
  - calendar_get_events.py
  - calendar_get_all_events.py
  - calendar_search_events.py
- Schedule features:
  - Group by time (day sections)
  - Group by calendar (calendar sections)
  - Sequential event numbering
  - Conflict detection
  - Video meeting link extraction
- Commands: `/calendar`, `/schedule`
- Integration with MainOrchestrator

### Accounts Supported
- victor.lang22@gmail.com (Personal)
- victor@verifiedmetrics.com (VM)

### Based On
- Email agent architecture and patterns
- Shared OAuth credentials from Google Workspace MCP

---

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
