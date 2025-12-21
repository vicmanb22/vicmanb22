---
description: Update the project changelog with recent changes
---

# Update Changelog

Update CHANGELOG.md with recent changes to the project.

## Process

1. **Find the changelog**
   - Look for CHANGELOG.md in the project root
   - If it doesn't exist, create one

2. **Identify changes**
   - Check if this is a git repo and look at recent commits/diffs
   - Review files modified in the current session
   - Ask the user what changes were made if unclear

3. **Categorize the changes**
   Use these categories:
   - **Added** - New features or files
   - **Changed** - Changes to existing functionality
   - **Deprecated** - Features marked for removal
   - **Removed** - Removed features or files
   - **Fixed** - Bug fixes
   - **Security** - Security-related changes

4. **Update the changelog**
   - Add entries under the `## [Unreleased]` section
   - Include timestamp: `- (YYYY-MM-DD HH:MM) Description`
   - Use bullet points with concise descriptions
   - Group by category

## Input

The user may provide:
- A description of changes made
- A specific category to use
- Nothing (in which case, investigate recent changes)

## Output

- Updated CHANGELOG.md file
- Summary of what was added to the changelog

## Example Usage

```
/update-changelog Added new authentication system
```

```
/update-changelog
```
(Will prompt for or detect changes)

## Guidelines

- Always include date/time: `- (YYYY-MM-DD HH:MM) Description`
- Keep entries concise but descriptive
- Use past tense ("Added X" not "Add X")
- Don't duplicate existing entries
- When in doubt, ask the user for clarification
