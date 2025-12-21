# ProjectsCode

Root directory for all code projects and AI agents.

## Structure

```
ProjectsCode/
├── Agents/     # Reusable AI agent systems
└── Projects/   # Bounded work with deliverables
```

## Agents vs Projects

**Agent** — A system with instructions (prompts, workflows, CLAUDE.md) that guides Claude to help you accomplish tasks. Agents are reusable tools you invoke repeatedly. They have:
- A system prompt or CLAUDE.md that defines behavior
- Defined workflows or processes to follow
- No inherent "completion" — they're ongoing utilities

**Project** — A bounded piece of work with deliverables and an end state. Projects are what agents help you create. They have:
- Specific outputs/deliverables (website copy, reports, documents)
- A definition of "done"
- Often created or managed using an agent

**The test:**
- "Is this something I invoke to help me do work?" → Agent (goes in `Agents/`)
- "Is this work I'm doing that will be finished?" → Project (goes in `Projects/`)

## Current Agents

| Agent | Purpose | Subagents |
|-------|---------|-----------|
| **MainOrchestrator** | Central hub for personal life management | 1 |
| Planning | Project management and life organization | 7 |
| My Psychologist | Personal reflection and support | 9 |
| DecisionMaking | CBDT 5-day decision protocol | 15 |
| Email | Multi-account Gmail management | 1 |
| Calendar | Multi-account Google Calendar management | 1 |
| GoogleAccounts | Centralized OAuth for Email/Calendar | - |
| ShoppingListEmail | Weekly shopping list workflow | - |
| AgentFactory | Create and manage AI agents | - |
| AgentDirectory | Central registry and launcher for all agents | - |
| AgentLogs | Session logging system | - |
| WebsiteCopywriter | Website copy creation with specialized subagents | - |
| B2BFinancialGTMPanel | B2B financial software GTM advisory panel (47 experts) | - |

### Personal Life System (40 agents total)

The **MainOrchestrator** routes to 5 parent agents with 33 specialized subagents:

```
MainOrchestrator/
├── Planning (7 subagents)
│   ├── lno-framework-coach
│   ├── productivity-partner
│   ├── delegation-manager
│   ├── parking-lot-processor
│   ├── goal-alignment-auditor
│   ├── routines-manager
│   └── session-facilitator
│
├── My Psychologist (9 subagents)
│   ├── trauma-somatic-specialist
│   ├── rational-pragmatist
│   ├── relational-intimacy-expert
│   ├── psychodynamic-analyst
│   ├── humanistic-existential-guide
│   ├── cultural-identity-centered
│   ├── neuroscience-informed-integrator
│   ├── critical-provocateur
│   └── spirituality-transpersonal-explorer
│
├── DecisionMaking (15 subagents)
│   ├── regulation-checkpoint
│   ├── relational-position-check
│   ├── approval-seeking-detector
│   ├── opposite-action-protocol
│   ├── cognitive-distortion-identifier
│   ├── probabilistic-reasoner
│   ├── failure-anticipation-planner
│   ├── crisis-plan-generator
│   ├── body-wisdom-scanner
│   ├── prediction-calibrator
│   ├── relational-repair-communicator
│   ├── decision-window-closer
│   ├── weekly-implementation-tracker
│   ├── calibration-analyst
│   └── continuation-decision-maker
│
├── Email (1 subagent: digest)
├── Calendar (1 subagent: schedule)
└── ShoppingListEmail
```

**Quick Commands:**
- `/morning` — Morning routine workflow
- `/evening` — Evening reflection
- `/life` — Open routing menu
- `/google` — Manage Google accounts (add, reauth, list)
- `/digest` — Email digest for Gmail accounts

## Current Projects

| Project | Purpose |
|---------|---------|
| VerifiedMetricsWebsite2.0 | Website copy for Verified Metrics |
| Product Help Page reviews | Product help page content review |
| VM_Marketing | Marketing data infrastructure (Airtable, Apify, ABM) |
