---
name: work-digest
description: Generate periodic digests of work completed across all domains, workspaces, and projects. Creates saved digest files for easy recall. Use /digest to generate.
allowed-tools: [Read, Write, Glob, Bash, Grep]
---

# Work Digest

Generate and save periodic digests of work completed across all Claude Code workspaces. Aggregates data from process-notes.md, CHANGELOG.md, and session logs to create comprehensive summaries.

## When to Use This Skill

**Invoke this skill when:**
1. User requests `/work-digest`
2. User asks "What have I been working on?"
3. User wants a summary of recent work across projects
4. User needs context before a meeting or planning session
5. End of day/week/month wrap-up

## Command Syntax

```
/work-digest [scope] [period] [options]
```

**Scope** (optional, default: all):
- `all` - All workspaces and domains
- `personal` - personal-life workspace only
- `work` - work-argo and work-verifiedmetrics workspaces
- `work-vm` or `vm` - work-verifiedmetrics only
- `work-argo` or `argo` - work-argo only
- `[agent-name]` - Specific agent (e.g., `file-organizer`, `planning`)

**Period** (optional, default: session):
- `session` - Last session only (based on process-notes.md Current Session)
- `today` - Today's work
- `3d` or `3days` - Last 3 days
- `week` - Last 7 days
- `month` - Last 30 days
- `[N]d` or `[N]days` - Last N days

**Options:**
- `--save` - Save digest to log file (default: display only)
- `--brief` - Short summary only
- `--detailed` - Include all file changes and decisions
- `--context` - Show last 3 actions for resumption context

## Examples

```
/work-digest                      # All workspaces, current session
/work-digest week                 # All workspaces, last 7 days
/work-digest work week            # Work workspaces, last 7 days
/work-digest vm 3d --save         # VM workspace, 3 days, save to file
/work-digest planning session     # Planning agent only, current session
/work-digest all month --detailed # Everything, 30 days, full detail
/work-digest --context            # Quick summary with last 3 actions
```

## Data Sources

The skill aggregates from these files across ALL workspaces in `~/claude-agents/`:

### Primary Sources

| Source | What It Provides |
|--------|------------------|
| `process-notes.md` | Current session summary, key decisions, open questions, next steps |
| `CHANGELOG.md` | Agent/tool changes (code, prompts, structure) |
| `PLAN.md` | Current plans, status, implementation progress |
| `CLAUDE.md` | Agent capabilities, commands, structure |
| `logs/sessions/*.md` | Planning session logs with outcomes |
| `logs/reliability-log.md` | Session statistics and patterns |

### Discovery Process

**IMPORTANT:** Do NOT hardcode workspace paths. Dynamically discover all workspaces:

```bash
# Find all workspaces
ls ~/claude-agents/

# Find all agents across all workspaces
find ~/claude-agents/ -name "CLAUDE.md" -type f | grep -v node_modules | grep -v .git
```

### Known Workspaces (as of 2025-12-27)

| Workspace | Path | Description |
|-----------|------|-------------|
| personal-life | `~/claude-agents/personal-life/` | Personal life management (9 agents) |
| work-argo | `~/claude-agents/work-argo/` | Argonaut Expeditions work |
| work-verifiedmetrics | `~/claude-agents/work-verifiedmetrics/` | Verified Metrics marketing & tools |
| shared | `~/claude-agents/shared/` | Shared utilities (agent-factory, etc.) |
| personal-finance | `~/claude-agents/personal-finance/` | Personal finance management |

**Note:** New workspaces may be added. Always scan `~/claude-agents/` dynamically.

## Output Format

### Standard Digest

```markdown
# Work Digest - [Date Range]

## Summary
- **Workspaces Active:** [count]
- **Agents Touched:** [list]
- **Key Accomplishments:** [count]
- **Decisions Made:** [count]
- **Open Questions:** [count]

## By Workspace

### personal-life
**Agents:** main-orchestrator, file-organizer, planning

#### main-orchestrator
**Focus:** [Current Session focus from process-notes]

**Accomplished:**
- [List from Summary section]

**Decisions:**
| Decision | Rationale |
|----------|-----------|

**Open Questions:**
- [ ] Question 1

**Next Steps:**
1. Step 1
2. Step 2

#### file-organizer
[Same format...]

### work-verifiedmetrics
[Same format...]

## Last 3 Actions (Resumption Context)
1. [Most recent action with file/agent context]
2. [Second most recent]
3. [Third most recent]

---
*Generated: [timestamp]*
*Saved to: [path if --save used]*
```

### Brief Format (--brief)

```markdown
# Work Digest - [Date Range]

**Active:** personal-life (3 agents), work-vm (1 agent)

**Key Accomplishments:**
- FileOrganizer: Added photo organization capabilities
- MainOrchestrator: Enhanced startup with context loading
- Planning: Completed Week 52 planning

**Open Items:** 2 questions, 3 next steps

**Last Action:** Enhanced /main-orchestrator startup in main-orchestrator
```

## Log Storage

When `--save` is used, digests are saved to:

```
~/claude-agents/shared/digests/
├── daily/
│   └── YYYY-MM-DD.md
├── weekly/
│   └── YYYY-WXX.md
├── monthly/
│   └── YYYY-MM.md
└── custom/
    └── YYYY-MM-DD-HH-MM-[scope].md
```

### Log File Format

```markdown
---
generated: YYYY-MM-DD HH:MM
scope: [all|personal|work|agent-name]
period: [session|today|week|month|Nd]
workspaces: [list]
agents: [list]
---

[Full digest content]
```

## Process

### Step 1: Parse Scope and Period

1. Parse command arguments
2. Determine which workspaces to scan
3. Calculate date range for period

### Step 2: Discover ALL Data Sources

**Dynamically scan `~/claude-agents/` for all workspaces and agents:**

```bash
# List all workspaces
ls ~/claude-agents/

# Find all process-notes.md files
find ~/claude-agents/ -name "process-notes.md" -type f | grep -v node_modules

# Find all CHANGELOG.md files
find ~/claude-agents/ -name "CHANGELOG.md" -type f | grep -v node_modules

# Find all PLAN.md files
find ~/claude-agents/ -name "PLAN.md" -type f | grep -v node_modules

# Find all CLAUDE.md files (to identify agents)
find ~/claude-agents/ -name "CLAUDE.md" -type f | grep -v node_modules
```

### Step 3: Extract Data

**For each `process-notes.md`:**
1. Parse Current Session section
2. Extract Summary, Key Decisions, Open Questions, Next Steps
3. Note the agent/workspace context
4. Check for Previous Sessions if looking at longer periods

**For each `CHANGELOG.md` (agent-level only):**
1. Parse entries within date range
2. Filter to Added/Changed/Fixed sections
3. Skip node_modules and vendor changelogs

**For each `PLAN.md`:**
1. Check plan status (Active, Complete, Abandoned)
2. Extract current phase or milestone
3. Note any blockers or dependencies

**For each `CLAUDE.md`:**
1. Extract agent name and description
2. List available commands
3. Note any recent structural changes

**For session logs:**
1. Parse session entries within date range
2. Extract outcomes, files updated, issues

### Step 4: Aggregate and Format

1. Group data by workspace, then by agent
2. Calculate summary statistics
3. Identify last 3 actions from most recent timestamps
4. Format according to output style (standard/brief/detailed)
5. Include plan status for any active plans

### Step 5: Save (if --save)

1. Create directory structure if needed
2. Determine filename based on period
3. Write digest with YAML frontmatter
4. Report save location to user

## Implementation Notes

### Date Parsing

- Extract dates from process-notes.md `**Started:** YYYY-MM-DD` format
- Extract dates from CHANGELOG entries `(YYYY-MM-DD)` format
- Extract dates from session log headers `[YYYY-MM-DD HH:MM]` format

### Last 3 Actions Heuristic

Identify the 3 most recent discrete actions by:
1. Looking at `### Files Changed` in process-notes.md
2. Looking at most recent CHANGELOG entries
3. Looking at most recent session log entries
4. Ranking by timestamp, taking top 3

### Filtering

- Exclude `node_modules/` from all scans
- Exclude `.git/` logs from all scans
- Only include `CHANGELOG.md` files at agent/project root level
- Skip entries outside the requested date range

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| "No process-notes found" | Workspace has no agents with notes | Skip workspace, note in output |
| "No data in date range" | No activity in requested period | Expand search or note empty |
| "Cannot parse date" | Malformed date in source | Log warning, skip entry |
| "Log directory not writable" | Permission issue | Report error, display only |

## Integration

This skill works with:
- **update-docs** - Runs after update-docs to capture what was documented
- **main-orchestrator** - Can be invoked via orchestrator for cross-domain summary
- **planning** - Useful before daily/weekly planning sessions

## Response Format

After generating a digest, show:

```
Work Digest Generated

Scope: [scope]
Period: [period]
Data Sources:
  - process-notes.md: 8 files
  - CHANGELOG.md: 3 files
  - Session logs: 5 entries

[Display digest or summary]

[If --save used]
Saved to: ~/claude-agents/shared/digests/[path]
```
