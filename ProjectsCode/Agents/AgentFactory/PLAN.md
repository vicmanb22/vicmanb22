# Plan

## Current Focus
- (empty)

## Backlog
- [ ] Pattern detection script (`scripts/pattern_detector.py`) - Analyze reliability logs and detect Phase 2 candidates
- [ ] `/analyze-reliability` command - Interactive pattern analysis and improvement proposals
- [ ] Skills integration - Package Phase 2 scripts as reusable Skills
- [ ] Migrate existing agents (VM_Transcript_Extractor) to SDK auto-logging
- [ ] TypeScript SDK agent template

## Completed
- [x] (2025-12-19) SDK Auto-Logging for Self-Improving Agents
  - `scripts/reliability_logger.py` - Core logging utility
  - `templates/sdk-self-improving-agent.template.py` - SDK agent wrapper
  - `templates/reliability-hooks.template.py` - Reusable hooks
  - `templates/reliability-log-v2.template.md` - Auto-populated format
  - `examples/sdk-self-improving-agent/` - Working example
  - Updated CLAUDE.md with SDK Auto-Logging section
- [x] Initial changelog/plan tracking system
