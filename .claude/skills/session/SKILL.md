---
name: session
description: Create, update, and manage session logs and plans. Provides always-on logging, cross-session continuity, and context export. Works across any workspace with standard structure.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep]
---

# Session Manager

Create and manage session logs and plans with real-time updates, cross-session continuity, and context export.

**Relationship to work-tracker:**
- **work-tracker**: Browse, search, archive existing work items (navigation-focused)
- **session-manager**: Create, enrich, and manage active sessions (authoring-focused)

---

## Timezone Configuration

**CRITICAL: All session logs must use dual timezone format**

- **Primary timezone:** UTC (Coordinated Universal Time)
- **Secondary timezone:** Hong Kong Time (UTC+8, Asia/Hong_Kong)
- **Format:** `YYYY-MM-DD HH:MM UTC / HH:MM HKT`

**When to use:**
- Session Date field: `**Date:** YYYY-MM-DD (Started: HH:MM UTC / HH:MM HKT)`
- Session headers: `### Session N - YYYY-MM-DD HH:MM UTC / HH:MM HKT`
- Menu display: `Current Time: HH:MM UTC / HH:MM HKT`
- Context exports: `*Generated: YYYY-MM-DD HH:MM UTC / HH:MM HKT*`
- Resume display: `Last Active: YYYY-MM-DD HH:MM UTC / HH:MM HKT`

**Commands for timestamps:**
```bash
# Get both timezones
date -u '+%Y-%m-%d %H:%M UTC'; TZ='Asia/Hong_Kong' date '+%H:%M HKT'

# Combined format
date -u '+%Y-%m-%d %H:%M UTC' | tr '\n' ' '; echo "/ $(TZ='Asia/Hong_Kong' date '+%H:%M HKT')"
```

---

## Workspace Requirements

This skill operates on the current workspace (detected via CLAUDE.md). Required structure:

| Directory | Required | Purpose |
|-----------|----------|---------|
| `in-progress/session-logs-plans/` | Yes | Active sessions |
| `archive/sessions/` | Yes | Completed session logs |
| `archive/plans/` | Yes | Completed plans (PLAN.md) |

**If missing directories:** Run `mkdir -p in-progress/session-logs-plans archive/sessions archive/plans`

---

## Status Values

Use these standard statuses consistently across all session logs and plans:

| Status | When to Use | Location |
|--------|-------------|----------|
| `Planning` | Designing approach, not yet implementing | in-progress/ |
| `Active` | Currently being worked on | in-progress/ |
| `Paused` | On hold, will resume later | in-progress/ |
| `Complete` | Work finished, may need testing | archive/ |
| `Production` | Tested, stable, in regular use | archive/ |
| `Deprecated` | Superseded by newer work | archive/ |

**Rules:**
- Files in `in-progress/` should have status: `Planning`, `Active`, or `Paused`
- Files in `archive/` should have status: `Complete`, `Production`, or `Deprecated`
- When archiving, update status before moving the file

---

## Workspace Detection

**Before running any commands**, detect the workspace root by finding CLAUDE.md.

Run this to find workspace root:

```bash
# Find workspace root by searching upward for CLAUDE.md
dir="$(pwd)"
count=0
WORKSPACE_ROOT=""
while [ "$dir" != "/" ] && [ $count -lt 5 ]; do
  if [ -f "$dir/CLAUDE.md" ]; then
    WORKSPACE_ROOT="$dir"
    break
  fi
  dir="$(dirname "$dir")"
  count=$((count + 1))
done

if [ -z "$WORKSPACE_ROOT" ]; then
  echo "ERROR: Could not find workspace root (no CLAUDE.md found)"
  echo "Current directory: $(pwd)"
  echo "Searched 5 levels up. Are you in a Claude workspace?"
  exit 1
fi

echo "Workspace: $WORKSPACE_ROOT"
```

**All paths in this skill use `$WORKSPACE_ROOT` as the base.**

**IMPORTANT: Shell Persistence**
Each Bash tool call runs in a **new shell session** - variables do not persist between calls. You MUST include the workspace detection snippet at the top of EVERY Bash command. Use this compact one-liner version for brevity:

```bash
dir="$(pwd)"; WORKSPACE_ROOT=""; while [ "$dir" != "/" ]; do [ -f "$dir/CLAUDE.md" ] && WORKSPACE_ROOT="$dir" && break; dir="$(dirname "$dir")"; done; [ -z "$WORKSPACE_ROOT" ] && echo "ERROR: No CLAUDE.md" && exit 1
```

---

## Main Menu

When `/session` is invoked without arguments, display this menu.

**First, check INDEX.md freshness.** If INDEX.md is missing or last modified >24 hours ago, regenerate it (see INDEX.md section) before displaying the menu.

**Then, gather data:**

```bash
# Detect workspace (required - each Bash call is a new shell)
dir="$(pwd)"; WORKSPACE_ROOT=""; while [ "$dir" != "/" ]; do [ -f "$dir/CLAUDE.md" ] && WORKSPACE_ROOT="$dir" && break; dir="$(dirname "$dir")"; done; [ -z "$WORKSPACE_ROOT" ] && echo "ERROR: No CLAUDE.md" && exit 1

# Get current time in UTC and Hong Kong
date -u '+UTC: %Y-%m-%d %H:%M:%S'; TZ='Asia/Hong_Kong' date '+HKT: %Y-%m-%d %H:%M:%S'

# List sessions with modification times
for f in "$WORKSPACE_ROOT/in-progress/session-logs-plans"/*.md; do
  [ -f "$f" ] && stat -f "%Sm|%N" -t "%Y-%m-%d %H:%M" "$f" 2>/dev/null
done | sort -r
```

**Then display:**

```
==================================================
 SESSION MANAGER
==================================================
 Current Time: <UTC time> / <HKT time>

 ACTIVE SESSIONS (<count>)
------------------------------------------------------
 [1] session-2026-01-11-feature-name.md  *
     Status: Active | Agent: <agent> | Feature: <feature>
     Last updated: <relative time>

 [2] plan-2026-01-10-other-work.md
     Status: Planning | Agent: <agent> | Feature: <feature>
     Last updated: <relative time>

 [3] session-2026-01-09-paused-work.md
     Status: Paused | Agent: <agent> | Feature: <feature>
     Last updated: <relative time>

------------------------------------------------------
 * = Currently selected session

 ACTIONS (on selected session)
------------------------------------------------------
   u. Update        -> Log progress to selected session
   s. Summary       -> View selected session summary
   c. Checkpoint    -> Mark milestone reached
   x. Export        -> Generate context file
   d. Complete      -> Mark done + auto-archive

 CREATE
------------------------------------------------------
   n. New Session   -> Create new session log

 PROJECT MANAGEMENT
------------------------------------------------------
   p. Plan          -> View/manage PLAN.md

 VIEW
------------------------------------------------------
   r. Resume        -> Full context display for selected
   o. Rollup        -> View work by agent/feature

   q. Quit
------------------------------------------------------
Select session [1-N] or action:
```

**If no active sessions:**

```
==================================================
 SESSION MANAGER
==================================================

 NO ACTIVE SESSIONS
------------------------------------------------------
 No session logs found in in-progress/session-logs-plans/

 GET STARTED
------------------------------------------------------
   n. New Session   -> Create new session log

 PROJECT MANAGEMENT
------------------------------------------------------
   p. Plan          -> View/manage PLAN.md

 VIEW
------------------------------------------------------
   a. Archive       -> Browse archived sessions

   q. Quit
------------------------------------------------------
```

---

## Commands Reference

| Command | Action |
|---------|--------|
| `/session` | Main menu |
| `/session new` | Create new session log |
| `/session plan` | View/manage PLAN.md |
| `/session plan new` | Create PLAN.md with merged template |
| `/session plan add <task>` | Add task to plan |
| `/session plan update <task>` | Update task status (🟥→🟨→🟩) |
| `/session plan complete` | Archive PLAN.md when all tasks 🟩 |
| `/session resume` | Resume with context display |
| `/session update` | Update active session with progress |
| `/session update auto` | Auto-capture recent work |
| `/session checkpoint` | Mark milestone reached |
| `/session export` | Generate context file for new window |
| `/session summary` | Show current session summary |
| `/session tag <agent> <feature>` | Update session tags |
| `/session list` | List all sessions in progress |
| `/session rollup` | View work by agent/feature |
| `/session complete` | Mark session done + auto-archive |

---

## INDEX.md - Session Directory Index

An auto-generated index file that provides a scannable summary of all sessions in `in-progress/session-logs-plans/`.

**File location:** `$WORKSPACE_ROOT/in-progress/session-logs-plans/INDEX.md`

### When to Regenerate

Regenerate INDEX.md whenever:
- A new session is created (`/session new`)
- A session is completed and archived (`/session complete`)
- The main menu is displayed (`/session`) — if INDEX.md is missing or stale (>24h old)

### Regeneration Logic

```bash
# Detect workspace
dir="$(pwd)"; WORKSPACE_ROOT=""; while [ "$dir" != "/" ]; do [ -f "$dir/CLAUDE.md" ] && WORKSPACE_ROOT="$dir" && break; dir="$(dirname "$dir")"; done; [ -z "$WORKSPACE_ROOT" ] && echo "ERROR: No CLAUDE.md" && exit 1

SESSION_DIR="$WORKSPACE_ROOT/in-progress/session-logs-plans"

# List all .md files except INDEX.md, sorted by modification time (newest first)
ls -t "$SESSION_DIR"/*.md 2>/dev/null | grep -v INDEX.md
```

For each file, extract:
1. **Filename** (from the path)
2. **Title** (from the `# Session Log:` or `# Plan:` H1 header)
3. **Status** (from the `**Status:**` field)
4. **Date** (from the `**Date:**` field or filename)
5. **One-line summary** (from the `## Objective` section — first sentence only)

### INDEX.md Format

```markdown
# Session Index

*Auto-generated by /session skill. Last updated: YYYY-MM-DD HH:MM UTC / HH:MM HKT*

| File | Title | Status | Date | Summary |
|------|-------|--------|------|---------|
| [session-2026-02-22-...](session-2026-02-22-...) | Website Link Audit | Active | 2026-02-22 | Full link audit of verifiedmetrics.com |
| [plan-2026-01-13-...](plan-2026-01-13-...) | Posts Full Extraction | Paused | 2026-01-13 | Extract LinkedIn post data via Voyager API |
```

### Important

- INDEX.md is **auto-generated** — never edit it manually
- It only indexes files in `in-progress/session-logs-plans/`, not archived files
- If a file has no Status field, show "Unknown"

---

## `/session new` - Create Session

Display template selection:

```
SESSION TYPE
==================================================
  1. Feature       -> New feature implementation
  2. Debugging     -> Bug investigation and fix
  3. Refactor      -> Code restructuring
  4. Investigation -> Research/exploration
  5. General       -> Flexible template
------------------------------------------------------
Select type [1-5]:
```

Then prompt for:
1. **Title**: Brief descriptive name (becomes filename)
2. **Objective**: What this session will accomplish
3. **Agent**: Which agent this relates to (or "workspace")
4. **Feature**: Feature tag for grouping

**Create file at:** `$WORKSPACE_ROOT/in-progress/session-logs-plans/session-YYYY-MM-DD-HH-MM-<kebab-title>.md`

**After creating the file:** Regenerate INDEX.md (see [INDEX.md section](#indexmd---session-directory-index)).

### Session Log Template

**IMPORTANT: Timezone Formatting**
- All dates and times must include both UTC and Hong Kong time (UTC+8)
- Format: `YYYY-MM-DD HH:MM UTC / HH:MM HKT`
- Use `date -u` for UTC and `TZ='Asia/Hong_Kong' date` for Hong Kong time
- Session header timestamps must show both timezones
- Within-session timestamps can use local time notation `[HH:MM]` for brevity

```markdown
# Session Log: <Title>

**Date:** YYYY-MM-DD (Started: HH:MM UTC / HH:MM HKT)
**Status:** Active
**Type:** <Feature|Debugging|Refactor|Investigation|General>
**Agent:** <agent-name or "workspace">
**Feature:** <feature-tag>
**Scope:** <planning|implementation|debugging|refactoring>

## Objective

<One paragraph describing what this session will accomplish>

## Context

<Background, what prompted this work>

## Key Files

| File | Role |
|------|------|
| path | purpose |

## Key Decisions

| Decision | Choice | Rationale | Alternatives Considered |
|----------|--------|-----------|------------------------|
| <topic> | <what we chose> | <why> | <what we didn't choose> |

## Open Questions

- [ ] <question>

## Current State

**Working:** <items that are functioning>
**In Progress:** <items being actively worked on>
**Blocked:** <items blocked> (reason)

---

## Session Timeline

### Session 1 - YYYY-MM-DD HH:MM UTC / HH:MM HKT

**Focus:** <what this session is about>

#### Discoveries
- [HH:MM] <discovery>

#### Decisions
- [HH:MM] <decision> -- Rationale: <why>

#### Code Changes
- [HH:MM] `file.js` -- <description>

#### Checkpoints
- [HH:MM] <milestone>

---

## Summary (Auto-generated for Resume)

### Completed
- <item>

### In Progress
- <item>

### Next Steps
- <item>
```

### Template-Specific Sections

**Feature Template** - Add after Key Files:
```markdown
## Requirements

- <requirement from user>

## Acceptance Criteria

- [ ] <criterion>

## Dependencies

- <dependency>

## Phases

### Phase 1: Implementation
- [ ] Core functionality

### Phase 2: Testing & Verification
- [ ] Manual testing completed
- [ ] Edge cases validated

### Phase 3: Documentation & Cleanup
- [ ] CLAUDE.md updated (if applicable)
- [ ] No debug code remaining

## Definition of Done

- [ ] All acceptance criteria met
- [ ] All phases complete or explicitly [DEFERRED]
- [ ] No open blockers
```

**Debugging Template** - Add after Key Files:
```markdown
## Symptoms / Error Messages

<error text or behavior description>

## Reproduction Steps

1. <step>

## Root Cause Analysis

<analysis>

## Fix Applied

<fix description>
```

**Refactor Template** - Add after Key Files:
```markdown
## Current State

<what exists now>

## Target State

<what we want>

## Migration Steps

1. [ ] <step>

## Backward Compatibility Notes

- <note>
```

**Investigation Template** - Add after Key Files:
```markdown
## Questions to Answer

1. <question>

## Sources Consulted

- <source>

## Findings Summary

<summary>

## Recommendations

- <recommendation>
```

---

## `/session plan` - Manage Project Plan

Manage the project's PLAN.md file. Each project has a single PLAN.md for tracking implementation tasks.

**File location:** `$WORKSPACE_ROOT/PLAN.md`

### Subcommands

| Command | Action |
|---------|--------|
| `/session plan` | View PLAN.md status and menu |
| `/session plan new` | Create PLAN.md with template |
| `/session plan add <task>` | Add task to plan |
| `/session plan update <task>` | Update task status |
| `/session plan complete` | Archive when all tasks done |

### `/session plan` - View Plan

Display the plan status:

```
==================================================
 PROJECT PLAN
==================================================
 File: $WORKSPACE_ROOT/PLAN.md
 Overall Progress: 45% (5/11 tasks)

 TASKS
------------------------------------------------------
 🟩 Step 1: Setup project structure
 🟨 Step 2: Implement core features
    🟩 Add authentication
    🟨 Add user dashboard
    🟥 Add settings page
 🟥 Step 3: Testing & Documentation

------------------------------------------------------
 ACTIONS
   a. Add task      -> Add new task to plan
   u. Update task   -> Change task status
   c. Complete      -> Archive plan (all tasks must be 🟩)

   b. Back to main menu
------------------------------------------------------
```

### `/session plan new` - Create Plan

Prompt for:
1. **Title**: Brief descriptive name
2. **TLDR**: 2-3 sentences describing what we're building and why
3. **Agent**: Which agent this relates to (or "workspace")
4. **Feature**: Feature tag for grouping

**Create file at:** `$WORKSPACE_ROOT/PLAN.md`

### Plan Template

```markdown
# Plan: <Title>

**Overall Progress:** `0%`
**Date:** YYYY-MM-DD (Created: HH:MM UTC / HH:MM HKT)
**Status:** Planning
**Agent:** <agent-name or "workspace">
**Feature:** <feature-tag>

## TLDR

<2-3 sentences: what we're building and why>

## Supporting Documents

| Type | Link/Path | Notes |
|------|-----------|-------|
| Linear Issue | <url or "none"> | <brief description> |
| Exploration Doc | <path or "none"> | <what was discovered> |
| Design Doc | <path/url or "none"> | <key decisions> |
| Other | <reference or "none"> | <relevance> |

## Critical Decisions

Key choices made during exploration:

| Decision | Choice | Rationale |
|----------|--------|-----------|
| <topic> | <choice> | <why> |

## Key Files

| File | Action | Purpose |
|------|--------|---------|
| path | create/modify | description |

## Tasks

- [ ] 🟥 **Step 1: <Name>**
  - [ ] 🟥 Subtask 1
  - [ ] 🟥 Subtask 2

- [ ] 🟥 **Step 2: <Name>**
  - [ ] 🟥 Subtask 1

## Open Questions

- [ ] <question>
```

### Status Indicators

| Emoji | Meaning | When to Use |
|-------|---------|-------------|
| 🟩 | Done | Task completed |
| 🟨 | In Progress | Currently working on |
| 🟥 | To Do | Not started |

### `/session plan add <task>` - Add Task

Add a new task to the plan. Prompts for:
1. **Task name**: Brief description
2. **Parent task**: (optional) Add as subtask under existing task
3. **Initial status**: Usually 🟥 To Do

Appends to the Tasks section in PLAN.md.

### `/session plan update <task>` - Update Status

Update a task's status. Prompts for:
1. **Task to update**: Select from list or search
2. **New status**: 🟥 To Do, 🟨 In Progress, or 🟩 Done

Also updates:
- The checkbox: `[ ]` → `[x]` when marking 🟩
- **Overall Progress:** percentage at top of file

### Progress Calculation

```
Total tasks = count all lines matching "- [ ]" or "- [x]" with emoji
Done tasks = count lines with 🟩
Progress = (Done / Total) * 100
```

### `/session plan complete` - Archive Plan

**Requires all tasks to be 🟩 Done.**

If incomplete tasks exist:
```
PLAN COMPLETION BLOCKED
==================================================
 ⚠ Cannot complete - unfinished tasks

 INCOMPLETE TASKS
------------------------------------------------------
 🟨 Step 2: Implement core features
    🟥 Add settings page
 🟥 Step 3: Testing & Documentation

------------------------------------------------------
 Options:
   [f] Force complete (mark incomplete as [DEFERRED])
   [u] Update tasks first
   [c] Cancel
------------------------------------------------------
```

If all tasks complete:
1. Update status to `Complete`
2. Move to `$WORKSPACE_ROOT/archive/plans/PLAN-YYYY-MM-DD.md`
3. Display confirmation

```bash
mv "$WORKSPACE_ROOT/PLAN.md" "$WORKSPACE_ROOT/archive/plans/PLAN-$(date +%Y-%m-%d).md"
```

---

## `/session update` - Log Progress

Display update menu:

```
SESSION UPDATE
==================================================
Active: <session-filename>

What would you like to log?
------------------------------------------------------
  1. Discovery     -> Something learned/found
  2. Decision      -> Choice made with rationale
  3. Code Change   -> File modification summary
  4. Checkpoint    -> Milestone reached
  5. Question      -> Q&A to record
  6. Blocker       -> Issue preventing progress
  7. Next Steps    -> Update planned actions
  8. Auto-capture  -> Let me summarize recent work

  [b] Back / Cancel
------------------------------------------------------
Select [1-8] or [b]:
```

### Recommendation Behavior

**IMPORTANT:** When displaying the update menu:
1. Show the menu exactly as above - clean, without commentary
2. If you have a recommendation based on recent conversation context, add it as a separate line AFTER the menu:
   ```
   Recommendation: Select `8` (Auto-capture) to log recent risk analysis and validation discussion.
   ```
3. NEVER mix internal thinking ("I should log...") with the menu prompt
4. Keep recommendations brief and actionable

### Quick Update Syntax

```
/session update discovery "Found that API returns paginated results"
/session update decision "Using cursor pagination" "More efficient than offset"
/session update code "human_helpers.js" "Added validateConnection function"
/session update checkpoint "Phase 1 complete"
/session update blocker "Rate limited, waiting 1 hour"
/session update next "Test all scrapers"
```

### Append Format

When logging, append to the appropriate section with timestamp.

**For new session entries**, use full timezone format:
```markdown
### Session N - YYYY-MM-DD HH:MM UTC / HH:MM HKT

**Focus:** <what this session is about>
```

**For items within a session**, use brief time notation:
```markdown
#### Discoveries
- [HH:MM] <new discovery>

#### Decisions
- [HH:MM] <decision> -- Rationale: <rationale>

#### Code Changes
- [HH:MM] `<file>` -- <description>

#### Checkpoints
- [HH:MM] <milestone>

#### Questions & Answers
- [HH:MM] Q: <question>
  A: <answer>
```

### Enhanced Decision Updates

When logging a decision (`/session update decision`), capture full context:

1. **Prompt for details:**
   - Decision topic: What was decided?
   - Choice made: What did we choose?
   - Rationale: Why did we choose this?
   - Alternatives considered: What did we NOT choose and why?

2. **Update two locations:**
   - **Key Decisions table** (top of session): Add row with full context
   - **Session Timeline > Decisions**: Add timestamped entry

**Quick syntax:**
```
/session update decision "Auth method" "JWT tokens" "Stateless, works with microservices" "Sessions (requires state), OAuth (overkill)"
```

### Enhanced Question Updates

When logging a question (`/session update question`), track resolution:

1. **Add to Open Questions section** as checkbox item: `- [ ] <question>`
2. **When question is answered**, mark resolved: `- [x] <question> → <answer>`

**Quick syntax:**
```
/session update question "Should we use Redis for caching?"
/session update question resolve "Should we use Redis?" "Yes, for session storage"
```

### State Updates

New update type for tracking current state:

```
/session update state working "Auth flow, API endpoints"
/session update state progress "User dashboard"
/session update state blocked "Rate limiting" "Waiting for API quota reset"
```

Updates the **Current State** section at top of session.

---

### Auto-Capture Mode (`/session update auto`)

1. Review conversation history since last update
2. Extract key events (file edits, decisions, Q&A)
3. Present summary for approval:

```
AUTO-CAPTURE SUMMARY
==================================================
Since last update, I detected:

DISCOVERIES
  - <discovery 1>
  - <discovery 2>

DECISIONS
  - <decision> -- Rationale: <why>

CODE CHANGES
  - <file> -- <description>

------------------------------------------------------
[a] Accept all  [e] Edit before saving  [c] Cancel
------------------------------------------------------
```

---

## `/session resume` - Context Display

Read the selected session and display structured summary:

```
==================================================
 SESSION RESUME: <Title>
==================================================

 Last Active: YYYY-MM-DD HH:MM UTC / HH:MM HKT (X hours ago)
 Status: <status>
 Agent: <agent>
 Feature: <feature>

 OBJECTIVE
------------------------------------------------------
 <objective text>

 COMPLETED THIS SESSION
------------------------------------------------------
 [x] <completed item 1>
 [x] <completed item 2>

 IN PROGRESS
------------------------------------------------------
 -> <current work>

 NEXT STEPS
------------------------------------------------------
 1. <next step>
 2. <next step>

 KEY DECISIONS MADE
------------------------------------------------------
 - <decision 1>
 - <decision 2>

 OPEN QUESTIONS
------------------------------------------------------
 - <question>

==================================================
 Ready to continue? [y] Yes  [n] Review full log
==================================================
```

---

## `/session export` - Context File

Generate a portable context file for new windows:

**Create file at:** `$WORKSPACE_ROOT/in-progress/session-logs-plans/session-context-<name>.md`

```markdown
# Session Context: <Title>

> This file provides context for continuing work in a new window.
> Load this at session start for continuity.

## Quick Summary

<2-3 sentences summarizing the work>

## Objective

<objective>

## Current State

- **Completed:** <list>
- **In progress:** <item>
- **Blocked on:** <item or "nothing">

## Key Files

| File | Status | Notes |
|------|--------|-------|
| path | modified/pending | description |

## Critical Decisions

| Decision | Rationale | Date |
|----------|-----------|------|
| choice | why | when |

## Next Actions

1. <action>
2. <action>

## Open Questions

- <question>

## Handoff Notes

### Where We Are
<Current state summary - what's working, what's not>

### Critical Context
<What the next person/Claude needs to know that isn't obvious from the code>

### Recommended Approach
1. <First thing to do when resuming>
2. <Second step>

### Gotchas
- <Known issues or tricky areas to watch out for>

---
*Generated: YYYY-MM-DD HH:MM UTC / HH:MM HKT*
*Source: $WORKSPACE_ROOT/in-progress/session-logs-plans/session-YYYY-MM-DD-<name>.md*
```

---

## `/session complete` - Archive

**CRITICAL: Phase Completion Enforcement**

Before marking a session complete, you MUST verify all phases are done:

1. **Parse the session file** for phase markers:
   - Look for `## Phases Remaining` or `### Phase N:` sections
   - Look for unchecked items `- [ ]` in Implementation Steps, Acceptance Criteria, or Phases
   - Look for "In Progress" items in the Summary section

2. **If incomplete phases exist**, display blocker:

```
SESSION COMPLETION BLOCKED
==================================================
 ⚠ Cannot complete - unfinished work detected

 INCOMPLETE PHASES
------------------------------------------------------
 [ ] Phase 2: Testing & Validation
     - [ ] Test `/comms-org` with actual data
     - [ ] Run full workflow

 [ ] Phase 3: Additional Features
     - [ ] Add Slack task extraction

 INCOMPLETE ACCEPTANCE CRITERIA
------------------------------------------------------
 - [ ] Calendar events created from commitments

------------------------------------------------------
 Options:
   [f] Force complete (mark incomplete items as "deferred")
   [u] Update progress first
   [c] Cancel

------------------------------------------------------
```

3. **If all phases complete**, ask about final status:

```
COMPLETION STATUS
==================================================
What status should this session have?
------------------------------------------------------
  1. Complete    -> Work finished, may need testing
  2. Production  -> Tested, stable, in regular use
------------------------------------------------------
Select [1-2]:
```

Then proceed with archival:
   - Update status to selected value in session file
   - Update the Summary section with final state
   - Move file to `$WORKSPACE_ROOT/archive/sessions/`

```bash
mv "$WORKSPACE_ROOT/in-progress/session-logs-plans/session-YYYY-MM-DD-name.md" "$WORKSPACE_ROOT/archive/sessions/"
```

4. **Regenerate INDEX.md** (see INDEX.md section)

Display confirmation:

```
SESSION COMPLETED
==================================================
 [x] All phases verified complete
 [x] Status updated to Complete
 [x] Moved to archive/sessions/session-YYYY-MM-DD-name.md
 [x] INDEX.md regenerated

 Session Summary:
 - Duration: X days
 - Phases completed: N/N
 - Checkpoints: N
 - Decisions: N
 - Code changes: N files

==================================================
```

### Force Complete Option

If user selects `[f] Force complete`:
1. Update all incomplete items to include `[DEFERRED]` marker
2. Add a "Deferred Items" section to Summary
3. Proceed with archival
4. Display what was deferred

---

## `/session rollup` - Grouped View

Group sessions by agent and feature:

```
SESSION ROLLUP
==================================================

 BY AGENT
------------------------------------------------------
 data-extraction-linkedin-playwriter (3 sessions)
   - session-2026-01-11-detection-mitigations (Active)
   - session-2026-01-10-profile-views-fix (Paused)
   - plan-2026-01-09-api-refactor (Planning)

 workspace (1 session)
   - session-2026-01-11-session-manager-skill (Active)

 BY FEATURE
------------------------------------------------------
 detection (1)
   - session-2026-01-11-detection-mitigations

 scraping (1)
   - session-2026-01-10-profile-views-fix

 session-manager (1)
   - session-2026-01-11-session-manager-skill

==================================================
```

---

## Storage Locations

| Purpose | Path |
|---------|------|
| Active sessions/plans | `$WORKSPACE_ROOT/in-progress/session-logs-plans/` |
| Context exports | `$WORKSPACE_ROOT/in-progress/session-logs-plans/session-context-*.md` |
| Archived sessions | `$WORKSPACE_ROOT/archive/sessions/` |
| Archived plans | `$WORKSPACE_ROOT/archive/plans/` |

---

## File Naming

| Type | Pattern |
|------|---------|
| Session log | `session-YYYY-MM-DD-HH-MM-<kebab-title>.md` |
| Project plan | `PLAN.md` (one per project) |
| Archived plan | `PLAN-YYYY-MM-DD.md` |
| Context export | `session-context-<kebab-title>.md` |

---

## Trigger Phrases

Invoke this skill when user says:
- "/session"
- "/session new"
- "/session update"
- "start session"
- "create session"
- "update session"
- "session log"
- "log progress"
- "export context"
- "resume session"
