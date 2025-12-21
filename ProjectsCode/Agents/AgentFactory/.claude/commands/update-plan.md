---
description: Update the project plan with tasks and ideas
---

# Update Plan

Manage the PLAN.md file to track project tasks, ideas, and progress.

## Process

1. **Find the plan file**
   - Look for PLAN.md in the project root
   - If it doesn't exist, create one using `templates/PLAN.template.md`

2. **Determine the action**
   Based on user input:
   - **Add item** - Add to Current Focus or Backlog
   - **Move item** - Move between sections
   - **Complete item** - Mark as done and move to Completed
   - **Review** - Show current plan status

3. **Update the plan**
   - Current Focus: Active work items (keep this short, 1-3 items)
   - Backlog: Future ideas and features
   - Completed: Done items with [x] checkbox

4. **Sync with changelog (optional)**
   - When completing items, ask if they should be added to CHANGELOG.md

## Input

The user may provide:
- An action: "add", "complete", "move", "review"
- A task description
- A target section

## Output

- Updated PLAN.md file
- Summary of changes made

## Example Usage

```
/update-plan add: Implement user authentication
```

```
/update-plan complete: Setup project structure
```

```
/update-plan move "Add tests" to current
```

```
/update-plan
```
(Will show current plan and ask what to update)

## Guidelines

- Keep Current Focus limited to 1-3 active items
- Move items to Completed when done, don't delete them
- Use clear, actionable task descriptions
- Ask if completed items should also update the changelog
