# Self-Improving Document Summarizer

An example agent that demonstrates the self-improving pattern - tracking reliability and proposing improvements to its own directives, with the ability to graduate proven workflows to deterministic Python scripts.

## Overview

This agent summarizes documents and tracks its own performance. When it notices patterns in failures or user corrections, it proposes improvements to its own instructions. When it notices patterns in successes, it proposes codifying the workflow into a reusable script.

## Purpose

Demonstrates the self-improving agent pattern:
- Reliability tracking with `reliability-log.md`
- Self-assessment after each task
- Pattern detection across sessions
- Improvement proposals for failures (directive changes)
- Codification proposals for successes (Python scripts)
- Human approval required for all changes

## Agent Maturity

**Current Phase:** 1 (LLM-Driven)

| Phase | Status | Description |
|-------|--------|-------------|
| Phase 1 | **ACTIVE** | LLM-driven, building & testing |
| Phase 2 | Pending | Code-driven, codified workflows |

**Scripts auto-run:** No (requires permission)

See `reliability-log.md` for task history and improvement proposals.

## When to Use This Pattern

Use this pattern when your agent:
- Performs repetitive tasks where quality varies
- Can benefit from learning from mistakes
- Should evolve its behavior over time
- Needs to maintain human oversight of changes
- Has tasks that could eventually be codified for reliability

## Key Files

| File | Purpose |
|------|---------|
| `reliability-log.md` | Tracks all task outcomes and proposals |
| `.claude/agents/document-summarizer.md` | The agent with self-improvement protocol |
| `.claude/settings.json` | Permissions and auto-run configuration |
| `scripts/` | Local scripts (links to shared library) |

## Self-Improvement Cycle

```
┌─────────────────────────────────────────────────────────────┐
│                    PHASE 1: LLM-DRIVEN                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ Execute  │───→│ Assess   │───→│   Log    │              │
│  │  Task    │    │ Outcome  │    │ Result   │              │
│  └──────────┘    └──────────┘    └────┬─────┘              │
│                                       │                     │
│                         ┌─────────────┴─────────────┐      │
│                         ▼                           ▼      │
│                  ┌────────────┐              ┌────────────┐│
│                  │  3+ Same   │              │  3+ Same   ││
│                  │  Failures  │              │ Successes  ││
│                  └─────┬──────┘              └─────┬──────┘│
│                        │                           │       │
│                        ▼                           ▼       │
│                  ┌────────────┐              ┌────────────┐│
│                  │  Propose   │              │  Propose   ││
│                  │ Directive  │              │ Codifying  ││
│                  │  Change    │              │ to Script  ││
│                  └─────┬──────┘              └─────┬──────┘│
│                        │                           │       │
│                        └───────────┬───────────────┘       │
│                                    ▼                       │
│                           ┌──────────────┐                 │
│                           │    User      │                 │
│                           │   Approval   │                 │
│                           └──────────────┘                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ (After significant codification)
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    PHASE 2: CODE-DRIVEN                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │  Check   │───→│   Run    │───→│   Log    │              │
│  │ Scripts  │    │  Script  │    │ Result   │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│                                                             │
│  Scripts don't hallucinate - they work or error cleanly    │
│  Target: 99%+ reliability                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Shared Scripts Library

Codified scripts are stored in the shared library for reuse across agents:
`/Users/vic-gini/ProjectsCode/Agents/scripts/`

The local `scripts/` folder contains a README pointing to the shared library.

## Example Usage

```
User: Summarize this quarterly report for me.

Agent: [Reads document, creates summary, presents to user]

User: Looks good!

Agent: [Logs "Success" to reliability-log.md]
       [Checks for patterns - this is the 3rd successful document summary]
       [Proposes: "I've summarized documents successfully 3 times.
        Would you like me to codify this into a reusable script?"]
```

## Related

- Template: `/Users/vic-gini/ProjectsCode/Agents/AgentFactory/templates/self-improving-agent.template.md`
- Shared Scripts: `/Users/vic-gini/ProjectsCode/Agents/scripts/`
