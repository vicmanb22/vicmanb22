---
name: update-docs
description: Update project documentation (CLAUDE.md, CHANGELOG.md, plan files) after completing work. Use when wrapping up tasks or when user requests /update-docs.
allowed-tools: [Read, Edit, Glob, Bash]
---

# Update Documentation

You ensure project documentation stays current by updating CLAUDE.md, CHANGELOG.md, plan files, and process-notes.md after significant work is completed.

## When to Use This Skill

**Invoke this skill when:**
1. User explicitly requests `/update-docs`
2. A significant task or feature is completed
3. New agents, skills, or projects are created
4. Workflow changes or new commands are added
5. At the end of a multi-step implementation
6. Session is ending or context is at risk of compaction
7. Major decisions were made that should be preserved

**Don't invoke for:**
- Minor bug fixes or typos
- Work-in-progress changes (unless context preservation needed)
- Exploratory/research tasks with no deliverables

## Files to Update

### 1. CLAUDE.md (Context-Aware)

This skill uses **context-aware** logic to determine which CLAUDE.md file(s) to update.

#### Project-Level CLAUDE.md (always check first)

**Location:** Nearest `CLAUDE.md` in current working directory or parent directories

**Always update when:**
- Changes are made to the agent/project
- New features, workflows, or behaviors are added
- Structure or configuration changes

**What to update:**
- Agent-specific documentation
- Local quick commands
- Project structure

#### Root CLAUDE.md (conditional)

**Location:** Look for root CLAUDE.md by traversing up to find the project root

**Only update when:**
- New agent is created → Add to "Current Agents" table
- New project is created → Add to "Current Projects" table
- New slash command is added → Add to "Quick Commands" list
- Agent hierarchy changes → Update the hierarchy diagram

**Decision rule:** If the change affects discovery/navigation of agents across the entire codebase, update root. If the change is internal to one agent/project, only update local CLAUDE.md.

### 2. CHANGELOG.md

**Location:** Usually in the agent/project folder (e.g., `Agents/AudioTranscriptCleanup/CHANGELOG.md`)

**CRITICAL: Agent-Level Changes Only**

CHANGELOG.md tracks changes to the **agent itself** (code, prompts, structure, behavior) — NOT content created or tasks performed using the agent.

**DO log:**
- New agents or subagents created
- Agent prompts or instructions modified
- New commands or workflows added
- Agent behavior or logic changed
- New templates or reference docs added
- Bug fixes in agent code
- Refactoring of agent structure

**DO NOT log:**
- Tasks completed using the agent (e.g., "Week 51 completed")
- Content generated through the agent (e.g., "Parking Lot processed")
- User data created or modified (e.g., "9 items archived")
- Daily/weekly/monthly planning sessions conducted
- Any operational work done with the agent's help

**The test:** Ask "Did the agent's code/prompts/structure change, or did I just use it?"
- If the agent changed → Log it
- If I just used the agent → Don't log it

**Format:**
```markdown
## [Unreleased]

### Added
- (YYYY-MM-DD) Description of what was added

### Changed
- (YYYY-MM-DD) Description of what changed

### Fixed
- (YYYY-MM-DD) Description of bug fix
```

**Categories:** Added, Changed, Deprecated, Removed, Fixed, Security

### 3. Plan Files

**Location:** `PLAN.md` in the project directory, or `~/.claude/plans/*.md` (auto-generated plan files)

**Update when:**
- Plan is completed
- Plan status changes
- Implementation deviates from original plan

**What to update:**
- Add `**Status:** Complete` at the top
- Note any deviations from the plan
- Add "Actual Implementation" section if different from plan

### 4. docs/catalog.md (Structure Changes)

**Location:** `docs/catalog.md` in the project root (if it exists)

**Update when:**
- New agents, skills, or scripts are created
- Project directory structure changes (new directories added/removed)
- New commands or workflows are added

**What to update:**
- Add new agents/skills to the appropriate table
- Update directory counts or ownership mappings
- Reflect structural changes (e.g., new archive subdirectories, new in-progress subdirectories)

**Skip if:** The file doesn't exist in the workspace or the changes are purely internal (no new agents, skills, directories, or commands).

### 5. process-notes.md (Context Preservation)

**Location:** Usually in the agent/project root folder alongside CLAUDE.md

**Purpose:** Preserve session context that would otherwise be lost to compaction. This is critical for long-running sessions or complex multi-step work.

**Update when:**
- Session is ending or user is wrapping up
- Major decisions were made (with rationale and alternatives considered)
- Significant milestones were completed
- Context is becoming complex and at risk of compaction
- User explicitly requests context preservation

**What to update:**

1. **Current Session section:**
   - Started date/time
   - Focus (what we're working on)
   - Summary of what was discussed and accomplished
   - Key Decisions table (Decision | Rationale | Alternatives Considered)
   - Open Questions (unresolved items)
   - Current State (working, in progress, blocked)
   - Next Steps

2. **Previous Sessions section:**
   - Archive the old "Current Session" here when starting fresh
   - Keep key outcomes, decisions, and context for future reference

3. **Persistent Context section:**
   - Update when fundamental understanding changes
   - Project-specific patterns, preferences, known issues

**Format:**
```markdown
## Current Session

**Started:** 2025-12-26 14:30
**Focus:** Implementing new feature X

### Summary
Explored codebase, made key architectural decisions, implemented core functionality.

### Key Decisions

| Decision | Rationale | Alternatives Considered |
|----------|-----------|------------------------|
| Use approach A | Better performance | Approach B (rejected: complexity) |

### Open Questions
- [ ] How to handle edge case Y?

### Current State

**What's working:**
- Core feature implemented

**What's in progress:**
- Edge case handling

**What's blocked:**
- Waiting on API documentation

### Next Steps
1. Resolve open question about edge case Y
2. Complete edge case handling
```

## Process

### Step 1: Assess the Work

Ask yourself:
- What was accomplished?
- What files/agents/skills were created or modified?
- Are there new commands or workflows?
- What's the user-facing impact?

### Step 2: Determine CLAUDE.md Scope

1. **Find project CLAUDE.md** - Look in current directory, then parent directories
2. **Decide if root needs updating:**
   - New agent created? → Update root "Current Agents" table
   - New project created? → Update root "Current Projects" table
   - New slash command? → Update root "Quick Commands" list
   - Otherwise → Only update project-level CLAUDE.md

### Step 3: Check for Existing Documentation

Use Glob to find relevant documentation files:
- Look for CLAUDE.md in current directory and root
- Look for CHANGELOG.md in agent/project folders
- Look for process-notes.md in agent/project folders
- Check for active plan files

### Step 4: Update Each File

For each file that needs updating:

1. **Read** the current content
2. **Determine** what needs to be added/changed
3. **Edit** using the Edit tool
4. **Verify** the update makes sense

### Step 5: Commit and Push to GitHub

After all documentation files are updated:

1. **Stage** all modified doc files:
   ```bash
   git add CLAUDE.md CHANGELOG.md PLAN.md process-notes.md
   ```

2. **Commit** with a standard message:
   ```bash
   git commit -m "docs: Update documentation via /update-docs"
   ```

3. **Push** to remote:
   ```bash
   git push
   ```

4. **Report** success or failure to user

### Step 6: Confirm with User

Show what was updated:
```
Documentation Updated

CLAUDE.md
   - Added /new-command to Quick Commands

CHANGELOG.md (Agents/FolderName/)
   - Added completion entry for Feature X

process-notes.md
   - Updated Current Session with summary and decisions
   - Archived previous session

Plan: plan-name.md
   - Marked as complete

Git
   - Committed: "docs: Update documentation via /update-docs"
   - Pushed to origin/main
```

## Guidelines

### Required Behaviors

- **Always read before editing** - Never guess file content
- **Use exact dates** - Format: `(YYYY-MM-DD)` or `(YYYY-MM-DD HH:MM)`
- **Be specific** - "Added transcript cleanup skill" not "Added new feature"
- **Maintain format** - Follow existing changelog format exactly
- **Ask if uncertain** - When unsure what to document, ask user

### Forbidden Actions

- **Never skip reading** the file before editing
- **Never remove** existing documentation without asking
- **Never guess** about features or changes you didn't see
- **Never use vague descriptions** like "Updated stuff"

## Response Format

After updating documentation, show a summary:

```
Documentation Updated

CLAUDE.md
   - Added /new-command to Quick Commands

CHANGELOG.md (Agents/FolderName/)
   - Added completion entry for Feature X

process-notes.md
   - Updated Current Session with summary and decisions
   - Archived previous session to Previous Sessions
   - Updated Persistent Context with new patterns

Plan: plan-name.md
   - Marked as complete

Git
   - Committed: "docs: Update documentation via /update-docs"
   - Pushed to origin/main
```

## Integration with Claude Code Workflow

This skill should be invoked:
1. **Automatically** by Claude Code when it detects task completion
2. **Manually** by user with `/update-docs`
3. **Suggested** when Claude notices undocumented changes
4. **Proactively** when session is ending or context is at risk of compaction

**Pro tip:** When creating new agents or skills, invoke this skill immediately after to keep docs in sync.

**Context Preservation:** For long-running sessions, prioritize updating process-notes.md to capture decisions and context that would otherwise be lost. This is especially important before the conversation compacts.
