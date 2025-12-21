# Agent Logs

Central repository for all Claude Code agent and session logs.

## Purpose

This vault stores logs from planning sessions and agent executions across all projects. Logs provide:
- Session history and decisions made
- Audit trail of tasks created/completed
- Context for future sessions
- Patterns and insights over time

## Structure

```
AgentLogs/
├── sessions/
│   ├── pm/                      # Project Manager sessions
│   └── [project-name]/          # Other project sessions
└── agents/
    └── planner/                 # Planner agent execution logs
```

## Log File Naming Convention

`YYYY-MM-DD-HH-MM-{session-type}.md`

Examples:
- `2025-12-03-09-30-daily.md`
- `2025-12-03-14-00-weekly.md`
- `2025-12-01-10-00-monthly.md`
- `2025-10-01-09-00-quarterly.md`

## Session Log Template

After each planning session, create a log file with this structure:

```markdown
# Session Log: {Session Type} - {Date}

## Session Info
- **Type:** Daily / Weekly / Monthly / Quarterly
- **Date:** YYYY-MM-DD
- **Time:** HH:MM
- **Domains:** All / [specific domains]

## Goals Reviewed
- [List goals discussed with status]

## Tasks Created
- [New tasks added during session]

## Tasks Completed
- [Tasks marked complete during session]

## Tasks Updated
- [Tasks modified during session]

## Delegations
- [New delegations made]
- [Delegation status updates]

## Key Decisions
- [Important decisions made during session]

## Coach's Notes
- [Observations and recommendations generated]

## Next Actions
- [Immediate next steps identified]
```

## Instructions

### After Each Planning Session

1. Create a new log file in the appropriate folder:
   - PM sessions: `/sessions/pm/`
   - Other projects: `/sessions/{project-name}/`

2. Use the naming convention: `YYYY-MM-DD-HH-MM-{session-type}.md`

3. Fill in the template with session details

4. Include any important context or decisions for future reference

### Reviewing Logs

- Use logs to track patterns over time
- Reference previous sessions for context
- Identify recurring blockers or themes

## Maintaining Changelog & Plan

This project uses `CHANGELOG.md` and `PLAN.md` for tracking.

**⚠️ IMPORTANT: Always update CHANGELOG.md immediately and automatically after making ANY changes to project files — including templates, prompts, configuration files, system files, or any other project assets. Do NOT wait for the user to ask. This must happen automatically after every change.**

### When working on this project:
1. Check PLAN.md at the start to see current priorities
2. **Update CHANGELOG.md immediately after completing any changes** (under `## [Unreleased]`)
3. Move completed items from Current Focus to Completed in PLAN.md

### Changelog categories:
Added, Changed, Deprecated, Removed, Fixed, Security

### Entry format:
`- (YYYY-MM-DD HH:MM) Description of change`

### Plan sections:
- **Current Focus** - Active work (1-3 items max)
- **Backlog** - Future ideas
- **Completed** - Done items
