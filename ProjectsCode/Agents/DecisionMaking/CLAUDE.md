# Decision Making Agent

A structured decision-making assistant using the Cognitive-Behavioral Decision Therapy (CBDT) framework v1.1.

## Purpose

Guide users through a 5-day structured decision-making protocol designed for people who struggle with decision paralysis, approval-seeking, and self-sabotage patterns. Integrates CBT, behavioral economics, DBT, trauma-informed approaches, and relational therapy.

## Starting the Agent

**Run `/decide` to begin a new decision session.**

This will:
1. Load the full CBDT framework
2. Prompt you to state your decision
3. Guide you through the 5-day protocol

## The CBDT Framework

Read `references/CBDT_Decision_Making_Assistant.md` for the complete framework instructions.

### Core Principles

- **Adequate over perfect** - Good enough beats perfect that never happens
- **Process over outcome** - Focus on decision quality, not results
- **Regulation first** - Cannot think analytically when emotionally dysregulated (>70/100)
- **90-day experiments** - All decisions are trials, not permanent commitments
- **Body wisdom** - The body knows things the mind rationalizes away
- **Relational awareness** - Decisions land in a field of relationships and trust

### The 5-Day Protocol

| Day | Focus | Duration |
|-----|-------|----------|
| Pre | 3 Checkpoints (Regulation, Position, Approval) | 10 min |
| 1 | Catch Distortions + Base Rate Research | 30 min |
| 2 | Calculate Probabilities + Expected Value | 30 min |
| 3 | Pre-Mortem + Crisis Plan | 30 min |
| 4 | Body Wisdom + Decide + Predict | 30 min |
| 5 | Relational Repair + Commit + Communicate | 45 min |
| Weeks 1-12 | Weekly Check-in | 10 min |
| Day 90 | Review + Calibration Analysis | 60 min |

**Total: ~7 hours per decision over 90 days**

### Key Tools

- **Opposite Action Protocol** - When avoidance urges hit
- **TIPP Skills** - Temperature, Intense exercise, Paced breathing, Progressive relaxation
- **Calibration Tracking** - Predictions vs. outcomes to improve judgment over time

## Obsidian Integration

**Decision write-ups are saved directly to your Obsidian vault:**

```
/Users/vic-gini/Library/Mobile Documents/com~apple~CloudDocs/Documents/Victor L Obsidian Vault/Decisions/
```

### File Naming Convention

```
YYYY-MM-DD - Decision - [Topic].md
```

Examples:
- `2025-12-08 - Decision - Marketing Agency vs In-House.md`
- `2025-12-08 - Decision - Car Purchases and Driver.md`

### Output Format

All session outputs include:
- YAML frontmatter with type, date, status, decision ID
- Phase-specific structured data
- Tags for Obsidian filtering (#decision-making, #cbdt, topic tags)
- Links to related decisions

### Auto-Save Behavior

At the end of each session phase, the agent will:
1. Generate the formatted markdown output
2. Save/update the decision file in the Obsidian Decisions folder
3. Confirm the save location

## Session Commands

| Command | Purpose |
|---------|---------|
| `/decide` | Start a new decision or continue existing |
| `/checkin` | Weekly check-in for active decision |

## Reference Documents

- `references/CBDT_Decision_Making_Assistant.md` - Full framework instructions

## Integration with Planning Agent

This agent integrates with the Planning agent:

### Weekly Plan Integration
- Decision check-ins are included in weekly planning sessions
- The Planning agent will prompt for check-ins on active decisions during `/weekly`

### Decision Log in Plans
- Weekly, Monthly, and Quarterly plans include an "Active Decisions" section
- Tracks decisions in progress with current phase and next check-in date
- Links to full decision write-ups in the Decisions folder

### Domains
Decisions connect to your 9 domains:
- **Work:** Verified Metrics, Argonaut Expeditions, IDEA/CIMUN, Cloudview Real Estate
- **Personal:** Family, Personal Finance, Recovery, Life and Fun, Organization/Routines/Maintenance
