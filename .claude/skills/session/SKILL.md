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

## Workspace Requirements

This skill operates on the current workspace (detected via CLAUDE.md). Required structure:

| Directory | Required | Purpose |
|-----------|----------|---------|
| `in-progress/session-logs-plans/` | Yes | Active sessions |
| `archive/plans/` | Yes | Completed sessions |

**If missing directories:** Run `mkdir -p in-progress/session-logs-plans archive/plans`

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

**First, gather data:**

```bash
# Detect workspace (required - each Bash call is a new shell)
dir="$(pwd)"; WORKSPACE_ROOT=""; while [ "$dir" != "/" ]; do [ -f "$dir/CLAUDE.md" ] && WORKSPACE_ROOT="$dir" && break; dir="$(dirname "$dir")"; done; [ -z "$WORKSPACE_ROOT" ] && echo "ERROR: No CLAUDE.md" && exit 1

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
   p. New Plan      -> Create new plan document

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
   p. New Plan      -> Create new plan document
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
| `/session plan` | Create new plan |
| `/session resume` | Resume with context display |
| `/session update` | Update active session with progress |
| `/session update auto` | Auto-capture recent work |
| `/session checkpoint` | Mark milestone reached |
| `/session export` | Generate context file for new window |
| `/session summary` | Show current session summary |
| `/session tag <agent> <feature>` | Update session tags |
| `/session list` | List all sessions in progress |
| `/session rollup` | View work by agent/feature |
| `/session complete` | Mark done + auto-archive |

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

### Session Log Template

```markdown
# Session Log: <Title>

**Date:** YYYY-MM-DD
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

## Session Timeline

### Session 1 - YYYY-MM-DD HH:MM

**Focus:** <what this session is about>

#### Discoveries
- [HH:MM] <discovery>

#### Decisions
- [HH:MM] <decision> -- Rationale: <why>

#### Code Changes
- [HH:MM] `file.js` -- <description>

#### Checkpoints
- [HH:MM] <milestone>

#### Questions & Answers
- [HH:MM] Q: <question>
  A: <answer>

---

## Summary (Auto-generated for Resume)

### Completed
- <item>

### In Progress
- <item>

### Next Steps
- <item>

### Key Decisions Made
- <decision>

### Open Questions
- <question>
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

## `/session plan` - Create Plan

Similar to session but for standalone plans:

**Create file at:** `$WORKSPACE_ROOT/in-progress/session-logs-plans/plan-YYYY-MM-DD-<kebab-title>.md`

### Plan Template

```markdown
# Plan: <Title>

**Date:** YYYY-MM-DD
**Status:** Planning
**Agent:** <agent-name or "workspace">
**Feature:** <feature-tag>

## Objective

<What this plan achieves>

## Context

<Background information>

## Proposed Solution

<Approach description>

## Implementation Steps

1. [ ] Step 1
2. [ ] Step 2
3. [ ] Step 3

## Key Files

| File | Action | Purpose |
|------|--------|---------|
| path | create/modify | description |

## Open Questions

- <question>

## Risks & Considerations

- <risk>

## Progress Log

| Time | Action | Result |
|------|--------|--------|
| - | Plan created | Awaiting approval |
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

When logging, append to the appropriate section with timestamp:

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

 Last Active: YYYY-MM-DD HH:MM (X hours ago)
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

---
*Generated: YYYY-MM-DD HH:MM*
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
   - Move file to `$WORKSPACE_ROOT/archive/plans/`

```bash
mv "$WORKSPACE_ROOT/in-progress/session-logs-plans/session-YYYY-MM-DD-name.md" "$WORKSPACE_ROOT/archive/plans/"
```

Display confirmation:

```
SESSION COMPLETED
==================================================
 [x] All phases verified complete
 [x] Status updated to Complete
 [x] Moved to archive/plans/session-YYYY-MM-DD-name.md

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
| Archived sessions | `$WORKSPACE_ROOT/archive/plans/` |

---

## File Naming

| Type | Pattern |
|------|---------|
| Session log | `session-YYYY-MM-DD-HH-MM-<kebab-title>.md` |
| Plan | `plan-YYYY-MM-DD-HH-MM-<kebab-title>.md` |
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
