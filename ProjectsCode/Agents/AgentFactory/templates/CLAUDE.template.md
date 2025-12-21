# [Project Name]

[Brief description of what this project/agent does - 1-2 sentences]

## Overview

[Detailed explanation of the project purpose. What problem does it solve? Who is it for?]

## Key Context

[Important information the agent needs to know to do its job effectively]

- [Context point 1 - e.g., "This agent helps with X"]
- [Context point 2 - e.g., "The user prefers Y approach"]
- [Context point 3 - e.g., "Important constraint: Z"]

## File Access

[If the agent needs to access specific files/directories, document them here]

- **Path:** `[/path/to/files]`
- **Purpose:** [Why the agent needs access to these files]
- **Contents:** [What kind of files are there]

## Quality Control

[Any verification steps, safeguards, or quality requirements]

### Required Checks
- [Check 1 - e.g., "Always verify X before Y"]
- [Check 2 - e.g., "Reference documents with exact quotes"]

### Forbidden Actions
- [Forbidden 1 - e.g., "Never assume X without verification"]
- [Forbidden 2 - e.g., "Do not modify files in Y directory"]

## Examples

### Good Output
[Concrete examples of what success looks like for this agent]

### Bad Output / Anti-patterns
[Examples of what the agent should NOT do]

## Additional Notes

[Any other context that helps the agent perform better]

## Context Management

For long-running sessions:
- Use `/rewind` to go back to good context points (not `/compact`)
- Use double-escape to fork conversations when you have good context
- Use `/resume` to continue from previous sessions with full context

## Nested Documentation (For Large Projects)

If this project has multiple subsystems, create CLAUDE.md files in subfolders:

```
project/
├── CLAUDE.md           # Main overview
├── frontend/
│   └── CLAUDE.md       # Frontend-specific context
├── backend/
│   └── CLAUDE.md       # Backend-specific context
└── shared/
    └── CLAUDE.md       # Shared utilities context
```

This reduces cognitive load by providing focused context for each area.

## Documentation Updates

This project uses `CHANGELOG.md`, `PLAN.md`, and `CLAUDE.md` for tracking.

**⚠️ IMPORTANT: Update documentation immediately after changes — do not wait to be asked.**

### Files to Update After Changes

| Change Type | Files to Update |
|-------------|-----------------|
| Any code/config change | CHANGELOG.md (immediately) |
| Task completed | PLAN.md (mark complete) |
| Structure/architecture change | CLAUDE.md (directory tree, conventions) |
| New capability added | CLAUDE.md + CHANGELOG.md |

### When working on this project:
1. Check PLAN.md at the start to see current priorities
2. Update CHANGELOG.md after completing changes (under `## [Unreleased]`)
3. Move completed items from Current Focus to Completed in PLAN.md
4. Update CLAUDE.md when directory structure or conventions change

### Changelog categories:
Added, Changed, Deprecated, Removed, Fixed, Security

### Plan sections:
- **Current Focus** - Active work (1-3 items max)
- **Backlog** - Future ideas
- **Completed** - Done items
