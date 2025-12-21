---
description: Create a new Claude Code agent project with proper structure
---

# Create New Agent

You are helping the user create a new Claude Code agent. Follow this process:

## Step 1: Gather Requirements

Ask about:
1. **What should the agent do?** (purpose, main task)
2. **What persona should it have?** (voice, personality, expertise level)
3. **What tools does it need?**
   - File reading: `Read, Glob, Grep`
   - File writing: `Write, Edit`
   - Commands: `Bash`
   - Web access: `WebFetch, WebSearch`
4. **Does it need access to specific directories?** (paths)
5. **How should responses be formatted?** (structure, sections)
6. **Any forbidden behaviors?** (things it must NOT do)

## Step 2: Confirm Design

Present a summary:
```
Agent Name: [name]
Purpose: [one sentence]
Tools: [list]
File Access: [paths or "none"]
```

Ask user to confirm before generating.

## Step 3: Generate Files

Create a new directory under `/Users/vic-gini/ProjectsCode/` with:

1. **CLAUDE.md** - Use `templates/CLAUDE.template.md` as base
2. **.claude/settings.json** - Use `templates/settings.template.json` as base
3. **.claude/agents/[name].md** - Use `templates/agent.template.md` as base
4. **CHANGELOG.md** - Use `templates/CHANGELOG.template.md` as base
5. **PLAN.md** - Use `templates/PLAN.template.md` as base

Read the templates first, then customize them based on requirements.

## Step 4: Provide Instructions

After generating, tell the user:
- Where the files were created
- How to invoke the agent (`@agent-name`)
- Any additional setup needed

## Quality Checklist

Before finishing, verify:
- [ ] CLAUDE.md has project-specific context
- [ ] Agent file has clear purpose statement
- [ ] Tools are minimal (only what's needed)
- [ ] Forbidden behaviors are listed
- [ ] Response format is defined
- [ ] Error handling is included
- [ ] CHANGELOG.md exists with initial entry
- [ ] PLAN.md exists with project goals
