---
description: Audit an existing Claude Code agent project and suggest improvements
---

# Audit Agent Project

You are auditing an existing agent project for quality and best practices.

## Step 1: Get Project Path

Ask the user for the path to the agent project they want audited.

## Step 2: Read Project Files

Use Glob and Read to examine:
- `CLAUDE.md` or `claude.md` (project context)
- `.claude/settings.json` (permissions)
- `.claude/agents/*.md` (agent definitions)
- `.claude/commands/*.md` (custom commands)

## Step 3: Analyze Against Checklist

Check each item:

### Structure
- [ ] Has CLAUDE.md with project context
- [ ] Has .claude/settings.json
- [ ] Has at least one agent in .claude/agents/
- [ ] File organization is clean

### CLAUDE.md Quality
- [ ] Clearly describes project purpose
- [ ] Includes relevant context for agents
- [ ] Documents file access requirements
- [ ] Has quality control guidelines (if needed)

### Agent File Quality
- [ ] YAML frontmatter is complete (name, description, tools)
- [ ] Purpose section is clear and specific
- [ ] Process/workflow is documented
- [ ] Required behaviors are listed
- [ ] Forbidden behaviors are explicit
- [ ] Response format is defined
- [ ] Error handling is included

### Permissions
- [ ] Tools in agent match permissions in settings
- [ ] Permissions follow least privilege principle
- [ ] No unnecessary wildcards
- [ ] File paths are specific where possible

### System Prompt Quality
- [ ] Role is clearly defined in first paragraph
- [ ] Context is specific, not generic
- [ ] Instructions are actionable
- [ ] Tone is consistent throughout

## Step 4: Generate Report

Provide a structured report:

```
# Agent Audit Report: [Project Name]

## Summary
[1-2 sentence overall assessment]

## What's Done Well
- [Positive point 1]
- [Positive point 2]

## Issues Found

### Critical (must fix)
- [Issue]: [Why it matters] → [How to fix]

### Recommended (should fix)
- [Issue]: [Why it matters] → [How to fix]

### Minor (nice to have)
- [Issue]: [Suggestion]

## Specific Recommendations

### [File name]
[Specific changes with examples]

## Improved Version (optional)
[If requested, provide corrected file contents]
```

## Common Issues to Check

1. **Vague purpose** - Agent role unclear or too broad
2. **Missing forbidden behaviors** - No constraints defined
3. **Overly permissive** - More tools/permissions than needed
4. **No error handling** - Doesn't address edge cases
5. **Unclear format** - Response structure not defined
6. **Missing context** - CLAUDE.md doesn't help the agent
7. **Duplicate files** - Same content in multiple places
