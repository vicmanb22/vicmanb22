# Changelog

All notable changes to Agent Factory.

## [Unreleased]

### Added
- (2025-12-19) **SDK Auto-Logging for Self-Improving Agents** — Automated reliability logging via Claude Agent SDK hooks
  - New script: `scripts/reliability_logger.py` — Core logging utility that auto-populates reliability-log.md
  - New template: `templates/sdk-self-improving-agent.template.py` — SDK agent wrapper with auto-logging hooks
  - New template: `templates/reliability-hooks.template.py` — Reusable hook functions for PreToolUse, PostToolUse, Stop
  - New template: `templates/reliability-log-v2.template.md` — Auto-generated log format with session summaries
  - New example: `examples/sdk-self-improving-agent/` — Complete working Code Assistant with auto-logging
  - Updated CLAUDE.md with "SDK Auto-Logging" section explaining when to use SDK vs filesystem agents
  - Updated `templates/self-improving-agent.template.md` to reference the SDK version
  - **Key benefit:** Makes Phase 1 → Phase 2 progression actually work by removing manual feedback friction
- (2025-12-11) Created **LinkedInJason** agent (`/Users/vic-gini/ProjectsCode/LinkedInJason`)
  - LinkedIn content strategy agent acting as Jason Lemkin advising Victor
  - Features: Multiple-option output (3-5 options per request), ICP intelligence/flagging, privacy violation scanner, existing comments analysis, proactive filtering (when NOT to engage), learning feedback loop
  - Knowledge base: victor-bio.md, jason-frameworks.md, icp-profiles.md, privacy-rules.md, voice-guide.md
  - Content tracking: posts archive, comments archive, learnings.md for pattern recognition
  - Invoke with `@jason`
  - Business goal: Build credibility → profile traffic → meetings for Verified Metrics
- (2025-12-11 11:00) Created **ShoppingListEmail** agent (`/Users/vic-gini/ProjectsCode/Agents/ShoppingListEmail`)
  - Weekly shopping list email to secretary Belinda (belinda@argonautexpeditions.com)
  - `/send-shopping-list` command to send list with standing instructions
  - `/process-shopping-replies` command to process purchase confirmations and update list
  - Standing instructions: no fresh food, $500 HKD approval threshold, quality over price, account info (iHerb, HKTVMall, Amazon)
  - Reads from Obsidian vault, sends via Gmail MCP
- (2025-12-08) **Self-Improving Agent Pattern (Pattern 6)** — Agents that learn from feedback and graduate to code
  - New template: `templates/self-improving-agent.template.md`
  - New template: `templates/reliability-log.template.md`
  - New example: `examples/self-improving-agent/` with complete document-summarizer implementation
  - Two-phase maturity model: Phase 1 (LLM-Driven, ~75-90%) → Phase 2 (Code-Driven, 99%+)
  - Reliability tracking with `reliability-log.md`
  - Codification of proven workflows to Python scripts
  - Human-in-the-loop approval for all changes
- (2025-12-08) **DOE Framework** documentation in CLAUDE.md
  - Directive-Orchestration-Execution layers explained
  - Determinism Principle (prefer tools over reasoning for critical ops)
  - Two-Phase Agent Maturity model
- (2025-12-08) **Shared Scripts Library** at `/Users/vic-gini/ProjectsCode/Agents/scripts/`
  - Centralized location for codified Python scripts
  - Reusable across all agents
  - README with script template and guidelines
- (2025-12-08) **Advanced Agent Patterns** section in CLAUDE.md
  - Pattern 6: Self-Improving Agent (complete)
  - Pattern 7: Multi-Agent Orchestrator (coming soon)
- (2025-12-08) Updated agent-architect.md with Pattern 6 and Pattern 7 (coming soon)
- (2025-12-08 12:10) Created **Email Digest** agent (`/Users/vic-gini/ProjectsCode/Agents/EmailDigest`)
  - Gmail digest with 5 categories: Attention Required, Payments, Daughter (Nara), Healthcare, Orders
  - Read-only MCP permissions for Gmail search/read
  - `/digest` command for quick generation
  - Registered in agent-registry.json under Personal > OrganizationRoutinesMaintenance
- (2025-12-08 10:45) New `/review-plan` command — uses "My Developer" technique for unbiased plan reviews
- (2025-12-08 10:45) New `/deep-explore` command — forces deep context building before any work
- (2025-12-08 10:45) Examples of Good Output / Anti-patterns sections to agent.template.md
- (2025-12-08 10:45) Validation section to agent.template.md (linters, tests, self-checks)
- (2025-12-08 10:45) Code Quality guidelines to agent.template.md
- (2025-12-08 10:45) Context Management and Nested Documentation sections to CLAUDE.template.md
- (2025-12-08 10:45) Core Workflow (Explore → Plan → Execute) to main CLAUDE.md
- (2025-12-08 10:45) Context Engineering principles to main CLAUDE.md
- (2025-12-08 10:45) "My Developer" Technique section to main CLAUDE.md
- (2025-12-08 10:45) Code Quality Principles section to main CLAUDE.md
- (2025-12-08 10:45) Context Window Management guidance to main CLAUDE.md

### Changed
- (2025-12-08 10:45) agent-architect.md — added Explore phase (Step 0), Risk Assessment (Step 2), and "My Developer" review technique
- (2025-12-08 10:45) agent-architect.md — added Examples/Anti-patterns/Validation to design document template
- (2025-12-08 08:35) Moved to /ProjectsCode/Agents/AgentFactory/ — updated path references in CLAUDE.md, show-directory.md, scan-agents.md

### Added
- (2025-12-07 23:32) Added auto-update instruction to CLAUDE.md — changelog must be updated immediately after any project file changes
- (2025-12-07 22:49) CHANGELOG.md and PLAN.md tracking system
- (2025-12-07 22:49) Templates: CHANGELOG.template.md, PLAN.template.md
- (2025-12-07 22:49) Commands: /update-changelog, /update-plan
- (2025-12-07 22:49) CLAUDE.md instructions to maintain changelog/plan

---

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

Categories: Added, Changed, Deprecated, Removed, Fixed, Security

Entry format: `- (YYYY-MM-DD HH:MM) Description of change`
