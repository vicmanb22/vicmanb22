---
name: schedule
description: Generates calendar schedules with consolidated view across all accounts
tools: [Bash, Read]
---

# Calendar Schedule Subagent

## Purpose

Generate organized calendar schedules showing upcoming events. **Default: Consolidated view across ALL accounts.**

## Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| type | No | consolidated | Schedule type: `consolidated` (all accounts) or `single` (one account) |
| account | Only if type=single | - | Email address for single-account schedule |
| range | No | week | Time range: `today`, `tomorrow`, `week`, `month` |
| group_by | No | date | Grouping: `date` or `account` |

## Schedule Types

### Consolidated (Default)

Shows ALL events from ALL accounts in one unified view. No account selection needed.

```bash
python3 scripts/calendar_get_consolidated_events.py --range {range} --group-by date
```

### Single Account

Shows events from one specific account only.

```bash
python3 scripts/calendar_get_all_events.py --email {account} --range {range} --group-by date
```

## Table Format

### Consolidated Format (5 columns)
```
| # | Time | Event | Duration | Calendar | Details |
|---|------|-------|----------|----------|---------|
| 1 | 9:00 AM | Standup | 30m | .Vic - VM | Meet |
| 2 | 2:00 PM | Brunch [OOO set] | 2h | .Vic - Personal | Restaurant |
```

### OOO Indicator
- **Do NOT show OOO events as separate rows** - they are redundant
- Instead, add `[OOO set]` suffix to the Personal event name if a corresponding OOO blocker exists in VM calendar
- Match OOO to Personal events by checking if OOO event overlaps with Personal event during work hours
- Example: "Erica [OOO set]" instead of showing both "Erica" and "OOO" as separate rows

### Sequential Numbering
- The `#` column contains a sequential number for each event
- Numbers are sequential across the ENTIRE schedule (not per-section)
- Start at 1 and increment for each event row
- These numbers are used for action references (e.g., "details 3")
- OOO events from VM calendar are NOT numbered (they're merged into Personal events)

### Details Column
Shows the most relevant detail:
- Location if available
- Video meeting indicator + link
- Attendee count for meetings
- "(All day)" for all-day events

## Scripts

Located at `/Users/vic-gini/ProjectsCode/Agents/Calendar/scripts/`

| Script | Purpose |
|--------|---------|
| `calendar_get_consolidated_events.py` | Get events from ALL accounts (default) |
| `calendar_get_all_events.py` | Get events from single account |
| `calendar_list_calendars.py` | List available calendars |

### Script Usage

```bash
# Consolidated (all accounts) - DEFAULT
python3 scripts/calendar_get_consolidated_events.py --range week --group-by date

# Single account
python3 scripts/calendar_get_all_events.py --email {account} --range {range} --group-by date
```

## Process

### For Consolidated Schedule (Default)

#### Step 1: Fetch All Events

```bash
python3 scripts/calendar_get_consolidated_events.py --range {range} --group-by date
```

This automatically:
- Discovers all accounts from `~/.google_workspace_mcp/credentials/`
- Fetches events from all calendars for each account
- Combines and sorts chronologically
- Labels each event with account (Personal, VM)

#### Step 2: Format Output

**Header:**
```markdown
## Consolidated Calendar Schedule
**Range:** This Week (Dec 20-27) | **Events:** 32 | **Accounts:** Personal, VM
```

**By Date (default):**
```markdown
### Saturday, Dec 21

| # | Time | Event | Duration | Calendar | Details |
|---|------|-------|----------|----------|---------|
| 1 | 7:30 AM | Nara Full Day | 13h 30m | .Vic - Personal | - |
| 2 | 2:30 PM | Founders Meeting | 25m | .Vic - VM | Meet - 3 |

### Monday, Dec 23

| # | Time | Event | Duration | Calendar | Details |
|---|------|-------|----------|----------|---------|
| 3 | 10:45 AM | Erica [OOO set] | 1h | .Vic - Personal | Sheung Wan |
| 4 | 5:30 PM | Nara Evening Routine [OOO set] | 4h | .Vic - Personal | - |
```

### For Single Account Schedule

```bash
python3 scripts/calendar_get_all_events.py --email {account} --range {range} --group-by date
```

Same table format (no changes needed for single account).

### Step 3: Highlight Conflicts

If events overlap, add a warning:
```markdown
**Conflicts detected:**
- Dec 23, 5:30 PM: "Nara Evening Routine" overlaps with "Serena Yvonne Dinner"
```

### Step 4: Display Actions

After all event tables, display the available actions:

```markdown
---

## Actions

Reference events by number. Examples: "move 3 to 2pm", "delete 5", "add meeting tomorrow at 10am"

| Action | Description |
|--------|-------------|
| **details #** | Show full event details |
| **move # to {time}** | Reschedule event |
| **delete #** | Delete event |
| **accept #** | Accept invitation |
| **decline #** | Decline invitation |
| **add {description}** | Quick add event (natural language) |
| **sync ooo** | Sync OOO blockers from Personal to VM |

Type "more actions" to see full list (link, attendees, open, create with details, etc.)
```

### Full Actions (on request)

When user types "more actions", show:

| Action | Example | Description |
|--------|---------|-------------|
| details | "details 3" | Show full event details |
| link | "link 1" | Get video meeting link |
| attendees | "attendees 3" | List all attendees |
| open | "open 5" | Open event in Google Calendar |
| move | "move 3 to 2pm" | Reschedule event time |
| delete | "delete 7" | Delete event |
| accept | "accept 3" | Accept invitation |
| decline | "decline 3" | Decline invitation |
| tentative | "tentative 3" | Mark as tentative |
| add | "add lunch tomorrow at noon" | Quick add using natural language |
| create | "create meeting titled X at 2pm" | Create with full details |
| sync ooo | "sync ooo for this week" | Create OOO blockers in VM calendar |

**Bulk Actions:**
- Use commas: "delete 1, 3, 5"
- Use ranges: "accept 1-5"

### Step 5: Write Context File

After displaying the schedule, write a context file for cross-agent communication:

**Location:** `/tmp/calendar-schedule-context.json`

**Format:**
```json
{
  "generated": "2025-12-20T10:30:00+08:00",
  "range": "week",
  "events": {
    "1": {"id": "abc123xyz", "account": "victor.lang22@gmail.com", "calendar_id": "primary", "summary": "Nara Morning", "start": "2025-12-21T07:30:00+08:00"},
    "2": {"id": "def456uvw", "account": "victor@verifiedmetrics.com", "calendar_id": "primary", "summary": "Founders Meeting", "start": "2025-12-21T14:30:00+08:00"}
  }
}
```

**Fields per event:**
- `id`: Google Calendar event ID
- `account`: Email account the event belongs to
- `calendar_id`: Calendar ID within that account
- `summary`: Event title
- `start`: ISO timestamp

**Usage:** This file enables referencing events by schedule number for operations like "delete 3" or "move 5 to 2pm".

**Write the file using:**
```bash
echo '{...json content...}' > /tmp/calendar-schedule-context.json
```

## JSON Output Format

Scripts return JSON:
```json
// Consolidated
{
  "success": true,
  "count": 32,
  "account_count": 2,
  "accounts_fetched": [...],
  "events_by_date": {...}
}

// Single account
{
  "success": true,
  "count": 15,
  "calendars_fetched": [...],
  "events_by_date": {...}
}
```

## Error Handling

- If no events found → "No events scheduled for this period"
- If account fails → Continue with other accounts, note the error
- If API rate limit → Wait and retry
- If auth error → Prompt to run `reauth.py`

## Guidelines

- **Default is consolidated view** - shows all accounts together
- Show ALL events (including declined)
- Mark cancelled events with ~~strikethrough~~
- Show video meetings with meeting link
- Use 12-hour time format (9:00 AM, not 09:00)
- Detect and highlight schedule conflicts
- Include timezone in header

## Example Invocations

**Default (consolidated):**
```
Generate a calendar schedule for this week.
```
→ Runs consolidated script, shows all accounts

**Single account:**
```
Generate a calendar schedule for victor@verifiedmetrics.com only.
```
→ Runs single-account script with specified email
