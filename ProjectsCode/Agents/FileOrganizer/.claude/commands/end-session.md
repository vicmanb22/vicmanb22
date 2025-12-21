# End FileOrganizer Session

Run this command when ending a file organization session.

## Trigger Phrases
User says: "end session", "done", "finished", "that's all", "wrap up"

## MANDATORY Steps (Do All)

### 1. Update action-log.md

Read the current action-log.md and add ALL file operations from this session:

```markdown
| Date | Time | Action | Source | Destination | Status | Notes |
|------|------|--------|--------|-------------|--------|-------|
| MM-DD | HH:MM | Move/Rename/Stage-Delete | [source path] | [dest path] | Success/Failed | [notes] |
```

Update the Statistics section at the bottom:
- Total Operations: [new count]
- Files Organized: [new count]
- Files Renamed: [new count]
- Files Staged for Deletion: [new count]
- Files Sent to Review: [new count]

### 2. Update reliability-log.md

Add session entry:

```markdown
### YYYY-MM-DD - [Brief task description]

**Outcome:** [Success/Partial/Failure]
**Task Type:** [Triage/Audit/Rename/Cleanup/Review]
**Files Processed:** [count]
**What Happened:** [1-2 sentence description]
**Root Cause (if not success):** [what went wrong]
**Pattern Detected:** [describe if any]
```

Update Summary Statistics:
- Total Tasks: [+1]
- Successes/Partials/Failures: [update]
- Success Rate: [recalculate]

### 3. Check for learnings

If user provided corrections during session:
- Add new Entity Aliases if domain mapping learned
- Note filing corrections in reliability-log.md
- Propose agent updates if 3+ similar corrections

### 4. Present session summary

```
## Session Complete

**Session:** YYYY-MM-DD HH:MM - HH:MM
**Files Processed:** [count]
**Outcome:** [Success/Partial/Failure]

### Actions Taken
- Organized: [count] files
- Renamed: [count] files
- Staged for deletion: [count] files
- Sent to review: [count] files

### Learnings Applied
- [any new entity aliases]
- [any rule corrections]

**Logs updated:** action-log.md, reliability-log.md
```
