# Plan

## Current Focus
- Agent is operational and ready for use
- First context (Verified Metrics) saved and available for continuation

## Backlog

### High Priority
- [ ] `/case-study` command — Request specific case study analysis from experts
- [ ] `/benchmark` command — Get benchmark comparisons and industry metrics
- [ ] `/action-items` command — Extract and summarize key recommendations from conversation

### Medium Priority
- [ ] Add more expert categories:
  - [ ] International expansion specialists (EMEA, APAC GTM)
  - [ ] Product marketing managers
  - [ ] Sales compensation designers
  - [ ] Board/investor relations experts
- [ ] Expert voice calibration — Review and refine signature phrases for authenticity
- [ ] Temperature system documentation — Explain how temperature affects response style
- [ ] Example interactions file — Add 2-3 example panel responses for reference

### Low Priority
- [ ] Token optimization — Consider moving expert definitions to experts.json only (reduce CLAUDE.md size)
- [ ] Web research integration — Enable experts to cite recent articles/data via WebSearch
- [ ] Airtable integration — Track recommendations and action items across sessions
- [ ] Expert cross-references — Add "often disagrees with" and "complements" relationships

### Context Management
- [ ] Context template — Standardize format for saving session contexts
- [ ] Context index — Create index file listing all saved contexts
- [ ] Context merging — Ability to load multiple contexts in one session

## Completed
- [x] (2025-12-21) Initial agent creation with 47 experts
- [x] (2025-12-21) AgentFactory audit and fixes applied:
  - [x] Created `.claude/settings.json`
  - [x] Created `.claude/agents/gtm-panel.md`
  - [x] Created `/panel` command
  - [x] Created `/expert` command
  - [x] Created `/debate` command
  - [x] Created `/deep-dive` command
  - [x] Added forbidden behaviors section
  - [x] Added error handling section
- [x] (2025-12-21) First panel session with Verified Metrics
  - Conventional vs. unconventional GTM strategies
  - Discovery: Portfolio company data sharing resistance
  - Strategic options identified
  - Context saved to `.claude/contexts/verified-metrics-2025-12-21.md`

## Ideas Parking Lot
- Multi-panel debates (3+ experts with moderator)
- Expert "office hours" simulation
- GTM audit checklist generator
- Competitive battlecard generator
- Pricing calculator integration
- Sales playbook generator based on expert recommendations
