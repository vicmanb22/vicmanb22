# Agent Factory

A project for creating well-designed Claude Code agents following best practices.

## Purpose

This project helps users design, create, and audit Claude Code agents with proper structure, system prompts, tool permissions, and quality controls.

## What This Project Creates

When a user wants a new agent, we generate a complete project structure:

1. **CLAUDE.md** - Project context file that all agents inherit
2. **.claude/settings.json** - Permissions configuration
3. **.claude/agents/[name].md** - Agent definition with system prompt
4. **.claude/commands/*.md** - Optional custom commands
5. **references/** - Folder for research, transcripts, and source materials

## Project Structure

```
AgentFactory/
├── CLAUDE.md                    # This file
├── CHANGELOG.md                 # Track all project changes
├── PLAN.md                      # Track roadmap and tasks
├── .claude/
│   ├── settings.json            # Factory permissions
│   ├── agents/
│   │   ├── agent-architect.md   # Main agent for designing agents
│   │   └── agent-directory.md   # Central directory/launcher for all agents
│   └── commands/
│       ├── new-agent.md         # Create new agent project
│       ├── audit-agent.md       # Audit existing agent
│       ├── show-directory.md    # Show agent directory
│       ├── scan-agents.md       # Scan for all agents
│       ├── find-agent.md        # Search for agents
│       ├── register-agent.md    # Register/create agents
│       ├── update-changelog.md  # Update changelog
│       └── update-plan.md       # Update plan/roadmap
├── templates/                   # Starter templates
│   ├── CLAUDE.template.md
│   ├── agent.template.md
│   ├── self-improving-agent.template.md
│   ├── sdk-self-improving-agent.template.py  # SDK version with auto-logging
│   ├── reliability-hooks.template.py         # Reusable SDK hooks
│   ├── reliability-log-v2.template.md        # Auto-populated log format
│   ├── command.template.md
│   ├── settings.template.json
│   ├── CHANGELOG.template.md
│   └── PLAN.template.md
├── scripts/                     # Shared Python utilities
│   └── reliability_logger.py    # Core auto-logging utility
├── references/                  # Research, transcripts, source materials
└── examples/                    # Example agent projects
    ├── simple-agent/
    ├── self-improving-agent/
    ├── sdk-self-improving-agent/  # SDK version with auto-logging
    ├── tool-using-agent/
    └── multi-persona-agent/
```

## How to Use

### Browse All Available Agents
1. Run `/show-directory` command to see the central agent directory
2. Agents are organized by domain (Work/Personal/System) and function (Analysis/Creation/Planning/etc.)
3. Use `@agent-directory` to search, launch, or manage agents

### Find a Specific Agent
1. Run `/find-agent [search query]` to search by name, domain, function, or keywords
2. View agent details and launch syntax
3. Launch the agent with `@agent-name`

### Create a New Agent
1. Run `/new-agent` command
2. Answer the requirements questions
3. Receive generated files for your new agent project
4. Agent is automatically registered in the central directory

### Register an Existing Agent
1. Run `/register-agent` command
2. Provide the path to an existing agent
3. Agent is added to the central directory with proper categorization

### Scan for New Agents
1. Run `/scan-agents` to discover all agents in:
   - `/Users/vic-gini/ProjectsCode/Agents/`
   - `/Users/vic-gini/ProjectsCode/Projects/`
   - `/Users/vic-gini/Documents/Victor L Obsidian Vault/`
2. Registry is updated with any newly discovered agents

### Audit an Existing Agent
1. Run `/audit-agent` command
2. Provide the path to the agent project
3. Receive analysis and improvement suggestions

### Learn About Agents
Chat with `@agent-architect` to:
- Understand agent architecture
- Learn best practices
- Get examples for specific use cases

## Key Principles

1. **CLAUDE.md is required** - Provides global context all agents inherit
2. **Least privilege** - Agents get minimal necessary tool permissions
3. **Specific prompts** - System prompts should be specific, not generic
4. **Explicit constraints** - Always include forbidden behaviors
5. **Clear formats** - Response formats must be explicitly defined
6. **Error handling** - Define what to do when things go wrong

---

## DOE Framework

Agent systems operate on three layers (Directive-Orchestration-Execution):

### Directive Layer (What)
- **CLAUDE.md files** - Project context and constraints
- **Agent files** - Persona, process, guidelines
- Written in natural language - human-readable instructions

### Orchestration Layer (Who Decides)
- **LLM reasoning** - READ → CHOOSE → EXECUTE → EVALUATE → LOOP
- Claude decides which tools to use and what to do next
- Dynamic decisions based on context

### Execution Layer (How)
- **Tool calls** - Deterministic operations (Read, Write, Bash, etc.)
- Verifiable, reliable results
- Either works or errors cleanly

### Determinism Principle

For critical operations, prefer tool execution over raw reasoning:

| Use Tools For | Use Reasoning For |
|---------------|-------------------|
| File operations | Deciding which file |
| Data validation | Interpreting results |
| Search queries | Synthesizing information |
| Script execution | Analyzing outcomes |

### Two-Phase Agent Maturity

Agents can evolve from exploration to codification:

**Phase 1: LLM-Driven** (Building & Testing)
- Use reasoning to figure out how to do tasks
- Fast iteration, easy to adjust directives
- Accept ~75-90% reliability as starting point
- Track outcomes in `reliability-log.md`

**Phase 2: Code-Driven** (Codified & Reliable)
- Proven workflows converted to Python scripts
- Agent runs scripts instead of re-reasoning
- Scripts don't hallucinate - they work or error cleanly
- Target 99%+ reliability

See `templates/self-improving-agent.template.md` for the filesystem-based pattern.

### SDK Auto-Logging (Recommended for Self-Improving Agents)

The original self-improving agent pattern requires **manual feedback logging** after every task. In practice, this creates too much friction and logs don't get populated.

**Solution:** Use the Claude Agent SDK with hooks to **automatically log** all tool usage and session outcomes.

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, HookMatcher

options = ClaudeAgentOptions(
    hooks={
        "PreToolUse": [HookMatcher(hooks=[log_tool_use])],
        "PostToolUse": [HookMatcher(hooks=[log_tool_result])],
        "Stop": [HookMatcher(hooks=[log_session_outcome])]
    }
)
```

**What gets logged automatically:**
- Every tool invocation (name, inputs, timestamp)
- Tool outcomes (success/failure, errors)
- Session summaries (duration, turns, cost)

**Files:**
- `scripts/reliability_logger.py` - Core logging utility
- `templates/sdk-self-improving-agent.template.py` - SDK agent template
- `templates/reliability-hooks.template.py` - Reusable hook functions
- `examples/sdk-self-improving-agent/` - Complete working example

**When to use SDK vs Filesystem agents:**

| Factor | Filesystem Agent | SDK Agent |
|--------|------------------|-----------|
| Self-Improvement | Manual logging ❌ | Auto-logging ✓ |
| Multi-turn | Limited | Full support |
| Hooks | Not available | Full control |
| CI/CD | Possible | Native |

**Recommendation:** Use SDK agents for any agent that needs self-improvement tracking. The auto-logging hooks make Phase 1 → Phase 2 actually work.

---

## Core Workflow: Explore → Plan → Execute

**Never jump straight to execution.** Follow this sequence:

### 1. Explore
- Spend tokens building deep context before doing anything
- Prompt: "Prepare to discuss how [this area] works"
- Read relevant files, understand patterns, verify understanding
- If the overview is wrong, escape and start over—don't try to correct

### 2. Plan
- Create a plan appropriate to the risk level
- Use `/review-plan` command to get unbiased feedback on high-risk plans
- Break large work into PR-sized chunks

### 3. Execute
- Only after exploring and planning, generate the actual output
- Use the context you've built—don't start fresh

---

## Context Engineering

"Context is everything." Agents perform much better with:

- **Examples of good output** - Show what success looks like
- **Examples of bad output** - Show what to avoid (anti-patterns)
- **Validation criteria** - Linters, tests, and checks to run
- **Style guides** - Architectural patterns and preferences
- **Nested CLAUDE.md files** - For subfolders in larger projects

---

## The "My Developer" Technique

Claude won't critique its own work. To get honest feedback:

**Instead of:** "Review this plan I made"
**Say:** "My developer came up with this plan. What are the weaknesses?"

This triggers critical analysis instead of validation. Use `/review-plan` command.

---

## Code Quality Principles

When agents write code:

- **Prefer editing over writing new** - Look for existing code to modify
- **Avoid backwards compatibility** - No graceful fallbacks unless explicit
- **Delete unused code** - Don't comment out; remove completely
- **Keep it simple** - Don't over-engineer for hypothetical needs

---

## Context Window Management

- **Avoid `/compact`** - It produces low-quality context summaries
- **Use `/rewind`** - Go back to good context points instead
- **Use double-escape** - Fork conversations to preserve good context
- **Use `/resume`** - Resume from any previous point with full context

## Agent File Structure Best Practices

Every agent file should include:

```markdown
---
name: agent-name
description: Brief description
tools: [only what's needed]
---

# Agent Name

## Purpose
[Clear role definition]

## Context
[What the agent needs to know]

## Process
[Step-by-step workflow]

## Guidelines
### Required Behaviors
### Forbidden Actions

## Response Format
[Explicit output structure]

## Error Handling
[What to do when issues arise]
```

## Advanced Agent Patterns

Beyond the basic patterns, these advanced patterns enable more sophisticated agent behaviors:

### Pattern 6: Self-Improving Agent
- **Use case:** Agents that learn from feedback over time
- **Key feature:** Tracks reliability, proposes directive improvements, graduates proven workflows to Python scripts
- **Tools:** `Read, Write, Glob, Grep, Bash`
- **Templates:**
  - `templates/sdk-self-improving-agent.template.py` - **SDK version with auto-logging (recommended)**
  - `templates/self-improving-agent.template.md` - Filesystem version (manual logging)
- **Examples:**
  - `examples/sdk-self-improving-agent/` - **SDK version (recommended)**
  - `examples/self-improving-agent/` - Filesystem version

**How it works:**
1. Agent tracks task outcomes in `reliability-log.md` (auto or manual)
2. When 3+ similar failures occur → proposes directive improvement
3. When 3+ similar successes occur → proposes codifying to script
4. Human approves all changes before implementation
5. Agent evolves from Phase 1 (LLM-Driven) to Phase 2 (Code-Driven)

**Why SDK version is recommended:** The filesystem version requires manual feedback logging after every task, which creates friction and results in empty logs. The SDK version uses hooks to auto-log everything.

### Pattern 7: Multi-Agent Orchestrator
- **Use case:** Complex workflows requiring multiple specialized agents
- **Key feature:** Workflow state management, agent handoffs
- **Template:** `templates/orchestrator-agent.template.md` *(coming soon)*
- **Example:** `examples/orchestrator-agent/` *(coming soon)*

### Shared Scripts Library

Proven Python scripts created by self-improving agents are stored in a shared location:

**Location:** `/Users/vic-gini/ProjectsCode/Agents/scripts/`

This allows:
- Multiple agents to reuse proven scripts
- Centralized maintenance
- Consistent behavior across agents

---

## Available Tools Reference

| Tool | Purpose | Use When |
|------|---------|----------|
| `Read` | Read files | Agent needs to access file content |
| `Write` | Create/overwrite files | Agent creates new files |
| `Edit` | Modify existing files | Agent updates existing files |
| `Glob` | Find files by pattern | Agent searches for files |
| `Grep` | Search file contents | Agent searches within files |
| `Bash` | Execute commands | Agent runs system commands |
| `WebFetch` | Fetch web content | Agent needs web data |
| `WebSearch` | Search the web | Agent needs to search online |

## Templates Location

All templates are in the `templates/` directory:
- `CLAUDE.template.md` - Project context template
- `agent.template.md` - Agent definition template
- `self-improving-agent.template.md` - Self-improving agent template (filesystem, manual logging)
- `sdk-self-improving-agent.template.py` - **SDK version with auto-logging (recommended)**
- `reliability-hooks.template.py` - Reusable SDK hook functions
- `reliability-log.template.md` - Manual reliability tracking template
- `reliability-log-v2.template.md` - Auto-populated log format (for SDK agents)
- `command.template.md` - Command file template
- `settings.template.json` - Settings template
- `CHANGELOG.template.md` - Changelog template
- `PLAN.template.md` - Plan/roadmap template

**Scripts** are in the `scripts/` directory:
- `reliability_logger.py` - Core auto-logging utility used by SDK hooks

## Maintaining Changelog & Plan

Every project should have `CHANGELOG.md` and `PLAN.md` files.

### CHANGELOG.md
Track all changes to the project. After making changes:
1. Update CHANGELOG.md under `## [Unreleased]`
2. Use categories: Added, Changed, Deprecated, Removed, Fixed, Security
3. Or run `/update-changelog` to update it interactively

### PLAN.md
Track roadmap, tasks, and ideas:
- **Current Focus** - What you're actively working on (1-3 items max)
- **Backlog** - Future ideas and features
- **Completed** - Done items for reference

Run `/update-plan` to manage the plan interactively.

### Auto-maintenance

**⚠️ IMPORTANT: Always update documentation immediately and automatically after making ANY changes to project files — including templates, prompts, configuration files, system files, or any other project assets. Do NOT wait for the user to ask. This must happen automatically after every change.**

#### Files to Update After Changes

| Change Type | Files to Update |
|-------------|-----------------|
| Any code/config change | CHANGELOG.md (immediately) |
| Task completed | PLAN.md (mark complete) |
| Structure/architecture change | CLAUDE.md (directory tree, conventions) |
| New capability added | CLAUDE.md + CHANGELOG.md |

When working on this project, always:
1. Check PLAN.md at the start to see current priorities
2. **Update CHANGELOG.md immediately after completing any changes** (under `## [Unreleased]`)
3. Move completed items from Current Focus to Completed in PLAN.md
4. **Update CLAUDE.md** when directory structure or conventions change
