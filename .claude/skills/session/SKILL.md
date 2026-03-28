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
| `in-progress/` | Yes | Parent for all active session/plan subdirectories |
| `archive/sessions/` | Yes | Completed session logs |

**Session scanning:** The skill scans **all subdirectories** under `in-progress/` for files matching `session-*.md` or `plan-*.md`. This automatically discovers sessions in any subdirectory (e.g., `session-logs-plans/`, `marketing-sessions/`, `marketing-plans/`). Files that don't match these patterns (e.g., daily reports, reviews, explorations) are ignored.

**If missing directories:** Run `mkdir -p in-progress/session-logs-plans archive/sessions`

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
| `Cancelled` | Work abandoned, no longer pursuing | archive/ |

**Rules:**
- Files in `in-progress/` should have status: `Planning`, `Active`, or `Paused`
- Files in `archive/` should have status: `Complete`, `Production`, `Deprecated`, or `Cancelled`
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

### Menu Input Handling

**CRITICAL: After displaying the menu, the user's next message IS a menu selection. Process it immediately — never ask for clarification.**

Recognize these inputs:
- **Numeric** (`1`–`N`): Select that session
- **Single letter** (`u`, `s`, `c`, `x`, `d`, `k`, `n`, `p`, `r`, `o`, `q`): Execute that action
- **`%`**: Sort toggle — re-sort by completion percentage (or revert to recency). This is NOT a typo or stray character; it is a deliberate menu action. Process it immediately by re-displaying the menu in the new sort order.
- **`l`**, **`f`**: Spec actions (link spec, new from spec)

If the input doesn't match any known action, say so briefly and re-show the menu — don't ask open-ended questions.

**First, check INDEX.md freshness.** If INDEX.md is missing or last modified >24 hours ago, regenerate it (see INDEX.md section) before displaying the menu.

**Then, gather data:**

Scan **all workspaces** under the common parent directory (`$WORKSPACE_ROOT/..`) that have a `CLAUDE.md` and an `in-progress/` directory. Within each workspace, scan **all subdirectories** of `in-progress/` for files matching `session-*.md` or `plan-*.md`. Group sessions by workspace.

```bash
# Detect workspace (required - each Bash call is a new shell)
dir="$(pwd)"; WORKSPACE_ROOT=""; while [ "$dir" != "/" ]; do [ -f "$dir/CLAUDE.md" ] && WORKSPACE_ROOT="$dir" && break; dir="$(dirname "$dir")"; done; [ -z "$WORKSPACE_ROOT" ] && echo "ERROR: No CLAUDE.md" && exit 1

PARENT_DIR="$(dirname "$WORKSPACE_ROOT")"

# Get current time in UTC and Hong Kong
date -u '+UTC: %Y-%m-%d %H:%M:%S'; TZ='Asia/Hong_Kong' date '+HKT: %Y-%m-%d %H:%M:%S'

# Scan all sibling workspaces for sessions across all in-progress subdirectories
for wsdir in "$PARENT_DIR"/*/; do
  ws="$(basename "$wsdir")"
  [ -f "$wsdir/CLAUDE.md" ] || continue
  [ -d "$wsdir/in-progress" ] || continue
  for subdir in "$wsdir"/in-progress/*/; do
    [ -d "$subdir" ] || continue
    for f in "$subdir"/session-*.md "$subdir"/plan-*.md; do
      [ -f "$f" ] || continue
      mod=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$f" 2>/dev/null)
      echo "$ws|$mod|$f"
    done
  done
done | sort -t'|' -k2 -r
```

For each session file, extract **Status**, **Agent**, and **Feature** from the header fields (first 15 lines).

**Then, calculate task progress** for each session file:

For each file, count task items in the `## Tasks` and `## Remaining Work` sections. Tasks are lines matching `- [ ]` or `- [x]` with emoji markers (🟥, 🟨, 🟩) OR plain checkbox lines (`- [ ]`, `- [x]`) in those sections.

```
Total tasks = lines matching "- [ ]" or "- [x]" (with or without emoji)
Done tasks = lines with 🟩 OR "- [x]" (without 🟥/🟨)
Progress = (Done / Total) * 100, displayed as percentage
```

If a session has no tasks (0 total), omit the progress indicator for that entry.

**Then scan for unlinked specs** in `.claude/plans/`:

```bash
# Find orphaned specs — .claude/plans/ files not referenced by any active session
CLAUDE_PLANS="$WORKSPACE_ROOT/.claude/plans"
if [ -d "$CLAUDE_PLANS" ]; then
  for spec in "$CLAUDE_PLANS"/*.md; do
    [ -f "$spec" ] || continue
    specname="$(basename "$spec")"
    # Search all active session/plan files for references to this spec
    found=$(grep -rl "$specname" "$WORKSPACE_ROOT/in-progress/" 2>/dev/null | head -1)
    if [ -z "$found" ]; then
      mod=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$spec" 2>/dev/null)
      title=$(head -3 "$spec" | grep "^# " | head -1 | sed 's/^# //')
      echo "SPEC|$mod|$specname|$title"
    fi
  done | sort -t'|' -k2 -r
fi
```

**Then display, grouped by workspace (current workspace first):**

```
==================================================
 SESSION MANAGER
==================================================
 Current Time: <UTC time> / <HKT time>

 ACTIVE SESSIONS (<total count>)
------------------------------------------------------

 personal-life (<count>)
 ······················································
 [1] session-2026-01-16-cloudview-vm-goals-review.md  *
     Status: Active | Agent: planning/goals-coach
     Last updated: <relative time>

 work-verifiedmetrics (<count>)
 ······················································
 [2] session-2026-02-27-morning-workflow.md
     Dir: session-logs-plans | Status: Active | Agent: workspace
     Progress: 60% (3/5) | Last updated: <relative time>

 [3] session-2026-02-22-marketing-scorecards.md
     Dir: marketing-sessions | Status: Active | Agent: marketing-reports
     Last updated: <relative time>

 [4] session-2026-02-26-vm-linear-workflow.md
     Dir: session-logs-plans | Status: Active | Feature: linear-integration
     Progress: 25% (1/4) | Last updated: <relative time>

 UNLINKED SPECS (.claude/plans/)
------------------------------------------------------
 These spec files aren't linked to any active session.
 Link to a session, or they'll be lost when context resets.

 [s1] proud-herding-iverson.md
      Linear Organization Redesign — Team Vic & Team Argonaut
      Last modified: 1 day ago

 [s2] polished-imagining-wall.md
      Refine /weekly-digest Skill
      Last modified: 1 day ago

 ... (+N older specs)

------------------------------------------------------
 * = Currently selected session

 ACTIONS (on selected session)
------------------------------------------------------
   u. Update        -> Log progress to selected session
   s. Summary       -> View selected session summary
   c. Checkpoint    -> Mark milestone reached
   x. Export        -> Generate context file
   d. Complete      -> Mark done + auto-archive
   k. Cancel        -> Abandon session + archive

 CREATE
------------------------------------------------------
   n. New Session   -> Create new session log

 PROJECT MANAGEMENT
------------------------------------------------------
   p. Tasks         -> View task progress across sessions

 SPECS
------------------------------------------------------
   l. Link spec     -> Link a spec to an existing session
   f. New from spec -> Create session from spec

 VIEW
------------------------------------------------------
   r. Resume        -> Full context display for selected
   o. Rollup        -> View work by agent/feature

 SORT
------------------------------------------------------
   %. Sort by progress  -> Re-sort by % complete (within groups)

   q. Quit
------------------------------------------------------
Select session [1-N] or action:
```

**Workspace ordering:** Current workspace appears first, then remaining workspaces alphabetically. Sessions within each workspace are sorted by last-modified (newest first). Workspaces with zero active sessions are omitted.

**Sort by progress (`%`):** When selected, re-display the menu with sessions sorted by task completion percentage (ascending — least complete first) within each workspace group. Sessions with no tasks are listed last. This is a display toggle — selecting `%` again reverts to the default last-modified sort.

**Unlinked specs display rules:**
- Only shown if orphaned specs exist (omit entire section otherwise)
- Show the 5 most recently modified orphaned specs
- If more exist, show `... (+N older specs)` with option to view all
- Only scan `.claude/plans/` in the current workspace (not sibling workspaces)

**Spec actions:**
- `l` (link): Prompt for spec number `[s1-sN]` and session number `[1-N]`, then add `**Spec:** .claude/plans/<name>.md` to the session header
- `f` (new from spec): Create a new session pre-populated with the spec's title and objective, with `**Spec:**` field set. Runs the `/session new` flow with pre-filled values.

**If no active sessions:**

```
==================================================
 SESSION MANAGER
==================================================

 NO ACTIVE SESSIONS
------------------------------------------------------
 No session or plan files found in any in-progress/ subdirectory

 UNLINKED SPECS (.claude/plans/)
------------------------------------------------------
 [s1] <spec-name>.md
      <Title>
      Last modified: <relative time>
 ...

 GET STARTED
------------------------------------------------------
   n. New Session   -> Create new session log
   f. New from spec -> Create session from spec

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
| `/session plan` | View task progress across all active sessions |
| `/session plan update <task>` | Update task status in selected session (🟥→🟨→🟩) |
| `/session resume` | Resume with context display |
| `/session update` | Update active session with progress |
| `/session update auto` | Auto-capture recent work |
| `/session checkpoint` | Mark milestone reached |
| `/session export` | Generate context file for new window |
| `/session summary` | Show current session summary |
| `/session tag <agent> <feature>` | Update session tags |
| `/session list` | List all sessions in progress |
| `/session rollup` | View work by agent/feature |
| `/session cancel` | Abandon session + archive as Cancelled |
| `/session complete` | Mark session done + auto-archive |

---

## INDEX.md - Session Directory Index

An auto-generated index file that provides a scannable summary of all sessions across all `in-progress/` subdirectories.

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

# Find all session/plan files across all in-progress subdirectories, sorted by modification time
find "$WORKSPACE_ROOT/in-progress" -mindepth 2 -maxdepth 2 \( -name "session-*.md" -o -name "plan-*.md" \) -exec stat -f "%m %N" {} \; 2>/dev/null | sort -rn | awk '{print $2}'
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

| File | Directory | Title | Status | Date | Summary |
|------|-----------|-------|--------|------|---------|
| session-2026-02-22-... | marketing-sessions | Marketing Scorecards | Active | 2026-02-22 | Fix scorecard bugs and data accuracy |
| plan-2026-02-27-... | session-logs-plans | Post Analytics | Planning | 2026-02-27 | Finish post analytics, lifecycle report |
| session-2026-02-26-... | session-logs-plans | Linear Workflow | Active | 2026-02-26 | Build VM work tracking in Linear |
```

### Important

- INDEX.md is **auto-generated** — never edit it manually
- It indexes `session-*.md` and `plan-*.md` files across **all** `in-progress/` subdirectories, not just `session-logs-plans/`
- The Directory column shows which subdirectory the file lives in (for disambiguation)
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
5. **Linear Issue** (optional): Linear issue identifier (e.g., MAR-152) or "none"
6. **Spec file** (optional): Path to a `.claude/plans/` spec file, or "none"
   - Auto-detect: if `.claude/plans/` files were recently modified (within last hour), suggest them
   - If provided, populate `**Spec:**` field in the header

### Linear Issue Validation

If user provides a Linear identifier (not "none" or blank):

1. **Fetch the issue** to validate it exists and get the URL:

```bash
dir="$(pwd)"; WORKSPACE_ROOT=""; while [ "$dir" != "/" ]; do [ -f "$dir/CLAUDE.md" ] && WORKSPACE_ROOT="$dir" && break; dir="$(dirname "$dir")"; done; [ -z "$WORKSPACE_ROOT" ] && echo "ERROR: No CLAUDE.md" && exit 1

export $(grep -v '^#' /Users/vic-gini/claude-agents/work-verifiedmetrics/.env | xargs)

IDENTIFIER="<user-input>"

curl -s --max-time 10 -X POST https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: $LINEAR_API_KEY" \
  -d "{\"query\": \"{ issue(id: \\\"$IDENTIFIER\\\") { id identifier title url } }\"}"
```

**Note:** The `issue(id:)` query accepts both human-readable identifiers (e.g., `MAR-136`) and UUIDs.

2. **If issue found** (response has `.data.issue` with non-null id): Populate `**Linear Issue:** <identifier> (<url>)` in the session file
3. **If not found or API error**: Show warning, ask "Continue without Linear link? [y/n]". If yes, use `*none*`
4. **If blank or "none"**: Use `*none*`

**Create file at:** `$WORKSPACE_ROOT/in-progress/<target-subdir>/session-YYYY-MM-DD-HH-MM-<kebab-title>.md`

**Target subdirectory selection:** When creating a new session, determine the appropriate subdirectory based on the agent:
- If agent starts with `marketing` or relates to LinkedIn/content/engagement → `marketing-sessions/`
- Otherwise → `session-logs-plans/`

The user can override this by specifying a directory explicitly.

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
**Linear Issue:** <identifier> (<url>) | *none*
**Spec:** `.claude/plans/<name>.md` | *none*

## Objective

<One paragraph describing what this session will accomplish>

## Context

<Background, what prompted this work>

## Key Files

| File | Role |
|------|------|
| path | purpose |

## Tasks

<!-- Add tasks as work emerges. Use 🟥 (to do), 🟨 (in progress), 🟩 (done) -->

- [ ] 🟥 <task>

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

**Feature Template** - Add after Key Files (replaces the base `## Tasks` section with a structured version):
```markdown
## Requirements

- <requirement from user>

## Acceptance Criteria

- [ ] <criterion>

## Dependencies

- <dependency>

## Tasks

- [ ] 🟥 **Step 1: Implementation**
  - [ ] 🟥 Core functionality

- [ ] 🟥 **Step 2: Testing & Verification**
  - [ ] 🟥 Manual testing completed
  - [ ] 🟥 Edge cases validated

- [ ] 🟥 **Step 3: Documentation & Cleanup**
  - [ ] 🟥 CLAUDE.md updated (if applicable)
  - [ ] 🟥 No debug code remaining

## Definition of Done

- [ ] All acceptance criteria met
- [ ] All tasks complete or explicitly [DEFERRED]
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

## `/session plan` - Cross-Workstream Task Viewer

View task progress across all active sessions. Tasks live inside each session's `## Tasks` section — there is no separate PLAN.md.

### Subcommands

| Command | Action |
|---------|--------|
| `/session plan` | View task progress across all active sessions |
| `/session plan update <task>` | Update task status in selected session (🟥→🟨→🟩) |

### `/session plan` - View Tasks

Scan all active session/plan files across all workspaces for `## Tasks` sections. Display aggregated progress:

```
==================================================
 TASK OVERVIEW (across all active sessions)
==================================================

 personal-life (2 sessions with tasks)
 ······················································
 [1] plan-2026-03-08-letter-to-siew-ching.md
     Progress: 0% (0/6)
     🟥 Step 1: Draft letter structure
     🟥 Step 2: Write opening section
     ...

 [2] session-2026-03-08-05-39-voice-integration.md
     Progress: 60% (3/5)
     🟩 Setup whisper-cli
     🟩 TTS integration
     🟩 Recording pipeline
     🟨 End-to-end testing
     🟥 VS Code hotkey binding

 work-verifiedmetrics (1 session with tasks)
 ······················································
 [3] session-2026-03-10-outbound-outreach-sheet.md
     Progress: 25% (1/4)
     🟩 Create sheet template
     🟥 Add data validation
     🟥 Build sync script
     🟥 Test end-to-end

------------------------------------------------------
 Select [1-N] to update tasks, or [b] back
------------------------------------------------------
```

**Only shows sessions that have a non-empty `## Tasks` section.** Sessions with only the placeholder comment are omitted.

### `/session plan update <task>` - Update Task Status

After selecting a session from the viewer:
1. Display the session's tasks with numbered list
2. Prompt for task number and new status: 🟥 To Do, 🟨 In Progress, or 🟩 Done
3. Update the task line in the session file:
   - Change emoji: 🟥 → 🟨 → 🟩
   - Update checkbox: `[ ]` → `[x]` when marking 🟩

### Status Indicators

| Emoji | Meaning | When to Use |
|-------|---------|-------------|
| 🟩 | Done | Task completed |
| 🟨 | In Progress | Currently working on |
| 🟥 | To Do | Not started |

### Progress Calculation

```
Total tasks = count all lines matching "- [ ]" or "- [x]" with emoji (🟥, 🟨, or 🟩)
Done tasks = count lines with 🟩
Progress = (Done / Total) * 100
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
 Linear: <identifier> (<url>)    # only show if linked

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

**Create file at:** Same subdirectory as the source session file (e.g., `$WORKSPACE_ROOT/in-progress/marketing-sessions/session-context-<name>.md`)

```markdown
# Session Context: <Title>

> This file provides context for continuing work in a new window.
> Load this at session start for continuity.

## Quick Summary

<2-3 sentences summarizing the work>

**Linear Issue:** <identifier> (<url>) | *none*

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
*Source: $WORKSPACE_ROOT/in-progress/<subdir>/session-YYYY-MM-DD-<name>.md*
```

---

## `/session cancel` - Abandon Session

Cancel a session that is no longer being pursued. Unlike `/session complete`, this does NOT enforce phase completion.

1. **Confirm cancellation:**

```
SESSION CANCEL
==================================================
 Cancel: <session-filename>
 Status: <current-status>

 Are you sure you want to cancel this session?
 All incomplete items will be marked [CANCELLED].
------------------------------------------------------
   [y] Yes, cancel and archive
   [n] No, go back
------------------------------------------------------
```

2. **On confirmation:**
   - Update `**Status:**` to `Cancelled`
   - Mark all unchecked items (`- [ ]`) with `[CANCELLED]` suffix
   - If session has a Linear issue linked, create a cancellation document (same as complete flow, but with `**Status:** Cancelled` and a note: `Session cancelled — work abandoned.`)
   - Move file to `$WORKSPACE_ROOT/archive/sessions/`
   - Regenerate INDEX.md

3. **Display confirmation:**

```
SESSION CANCELLED
==================================================
 [x] Status updated to Cancelled
 [x] Incomplete items marked [CANCELLED]
 [x] Moved to archive/sessions/<filename>
 [x] INDEX.md regenerated

==================================================
```

---

## `/session complete` - Archive

**CRITICAL: Phase Completion Enforcement**

Before marking a session complete, you MUST verify all tasks are done:

1. **Parse the session file** for task markers:
   - Look for `## Tasks` section with unchecked items (`- [ ]` with 🟥 or 🟨)
   - Look for unchecked items in Acceptance Criteria
   - Look for "In Progress" items in the Summary section

2. **If incomplete tasks exist**, display blocker:

```
SESSION COMPLETION BLOCKED
==================================================
 ⚠ Cannot complete - unfinished work detected

 INCOMPLETE TASKS
------------------------------------------------------
 🟨 Step 2: Implement core features
    🟥 Add settings page
 🟥 Step 3: Testing & Documentation

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

3. **If all tasks complete**, ask about final status:

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

### Linear Document Sync (on close)

**Before archival**, check if the session has a Linear issue linked:

1. **Read the session file** and look for `**Linear Issue:**` field
2. **If `*none*` or field is missing** — skip this step entirely, proceed to archival
3. **If a Linear identifier is present** (e.g., `MAR-152`):

   a. **Extract the Summary section** from the session file — everything between `## Summary (Auto-generated for Resume)` and the next `---` or end of file. This includes `### Completed`, `### In Progress`, and `### Next Steps` subsections.

   b. **Look up the internal UUID** from the identifier:

   ```bash
   dir="$(pwd)"; WORKSPACE_ROOT=""; while [ "$dir" != "/" ]; do [ -f "$dir/CLAUDE.md" ] && WORKSPACE_ROOT="$dir" && break; dir="$(dirname "$dir")"; done; [ -z "$WORKSPACE_ROOT" ] && echo "ERROR: No CLAUDE.md" && exit 1

   export $(grep -v '^#' /Users/vic-gini/claude-agents/work-verifiedmetrics/.env | xargs)

   IDENTIFIER="<extracted-from-session>"

   RESPONSE=$(curl -s --max-time 10 -X POST https://api.linear.app/graphql \
     -H "Content-Type: application/json" \
     -H "Authorization: $LINEAR_API_KEY" \
     -d "{\"query\": \"{ issue(id: \\\"$IDENTIFIER\\\") { id identifier title url } }\"}")

   ISSUE_ID=$(echo "$RESPONSE" | jq -r '.data.issue.id')
   ```

   **Note:** `issue(id:)` accepts both human-readable identifiers (e.g., `MAR-136`) and UUIDs.

   c. **Format the document content** — session summary with metadata:

   ```markdown
   **Date:** <session-date> | **Duration:** <X days> | **Status:** <Complete|Production>

   ### Completed
   - <items from Summary>

   ### In Progress
   - <items from Summary>

   ### Next Steps
   - <items from Summary>
   ```

   d. **Create the document** linked to the issue using `jq` + GraphQL variables for safe JSON escaping:

   ```bash
   # Write document content to temp file
   cat > /tmp/linear-doc-content.txt << 'CONTENT_EOF'
   <formatted content from step c>
   CONTENT_EOF

   # Build JSON payload with proper escaping using jq
   jq -n \
     --arg title "Session Log: <session-title>" \
     --arg issueId "$ISSUE_ID" \
     --rawfile content /tmp/linear-doc-content.txt \
     '{query: "mutation($title: String!, $content: String, $issueId: String) { documentCreate(input: { title: $title, content: $content, issueId: $issueId }) { success document { id title url } } }", variables: {title: $title, content: $content, issueId: $issueId}}' \
     > /tmp/linear-doc-payload.json

   curl -s --max-time 10 -X POST https://api.linear.app/graphql \
     -H "Content-Type: application/json" \
     -H "Authorization: $LINEAR_API_KEY" \
     -d @/tmp/linear-doc-payload.json

   # Clean up temp files
   rm -f /tmp/linear-doc-content.txt /tmp/linear-doc-payload.json
   ```

   e. **If the API call succeeds** — add a checkmark to the confirmation display
   f. **If the API call fails** — show a warning but do NOT block archival. Display: `[!] Linear document failed: <error>. Session archived anyway.`

### Spec Absorption (on close)

**Before archival**, check if the session has a linked spec file:

1. **Read the session file** and look for `**Spec:**` field
2. **If `*none*` or field is missing** — skip this step entirely
3. **If a `.claude/plans/` path is present** (e.g., `.claude/plans/proud-herding-iverson.md`):

   a. **Check if the spec file exists** at `$WORKSPACE_ROOT/<spec-path>`
   b. **If it exists:**
      - Read the spec file content
      - Append it to the session file as a new section at the bottom (before the final `---`):
        ```markdown
        ---

        ## Spec (Archived)

        > *Absorbed from `.claude/plans/<name>.md` on completion. This is the full spec that drove this work.*

        <full spec file content>
        ```
      - Delete the `.claude/plans/` file
   c. **If the spec file doesn't exist** (already deleted or moved): Add note to confirmation: `[!] Spec file not found — may have been cleaned up already`

Then proceed with archival:
   - Update status to selected value in session file
   - Update the Summary section with final state
   - Move file to `$WORKSPACE_ROOT/archive/sessions/`

```bash
# Move from whichever in-progress subdirectory the session lives in
mv "$WORKSPACE_ROOT/in-progress/<subdir>/session-YYYY-MM-DD-name.md" "$WORKSPACE_ROOT/archive/sessions/"
```

4. **Regenerate INDEX.md** (see INDEX.md section)

Display confirmation:

```
SESSION COMPLETED
==================================================
 [x] All tasks verified complete
 [x] Status updated to Complete
 [x] Spec absorbed from .claude/plans/<name>.md
 [x] Moved to archive/sessions/session-YYYY-MM-DD-name.md
 [x] Session document created in Linear on <identifier>
 [x] INDEX.md regenerated

 Session Summary:
 - Duration: X days
 - Tasks completed: N/N
 - Checkpoints: N
 - Decisions: N
 - Code changes: N files

==================================================
```

**Spec line variants:**
- Linked + absorbed: `[x] Spec absorbed from .claude/plans/<name>.md`
- Not linked: `[ ] No spec linked — skipped absorption`
- File missing: `[!] Spec file not found — may have been cleaned up already`

**Linear line variants:**
- Linked + success: `[x] Session document created in Linear on MAR-152`
- Not linked: `[ ] No Linear issue linked — skipped document sync`
- API failure: `[!] Linear document failed — session archived anyway`

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
| Active sessions/plans | `$WORKSPACE_ROOT/in-progress/*/` (any subdirectory containing `session-*.md` or `plan-*.md`) |
| Default session dir | `$WORKSPACE_ROOT/in-progress/session-logs-plans/` |
| Marketing sessions | `$WORKSPACE_ROOT/in-progress/marketing-sessions/` |
| Marketing plans | `$WORKSPACE_ROOT/in-progress/marketing-plans/` |
| Context exports | Same subdirectory as the source session |
| Plan-mode specs | `$WORKSPACE_ROOT/.claude/plans/` (absorbed into session on completion) |
| Archived sessions | `$WORKSPACE_ROOT/archive/sessions/` |

---

## File Naming

| Type | Pattern |
|------|---------|
| Session log | `session-YYYY-MM-DD-HH-MM-<kebab-title>.md` |
| Feature plan | `plan-YYYY-MM-DD-<kebab-title>.md` (in `in-progress/`) |
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
