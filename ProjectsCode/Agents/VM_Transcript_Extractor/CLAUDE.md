# VM Transcript Extractor

An expert agent system for extracting customer insights from Verified Metrics meeting transcripts to inform authentic, conversion-focused website copywriting for VM Website 2.0.

## Overview

This agent processes 67 customer meeting transcripts (Discovery calls, Demos, Check-ins, DD Debriefs) using a **two-stage workflow**:

1. **Stage 1 - Transcript Cleanup:** Clean raw transcript using AudioTranscriptCleanup agent (fix grammar, syntax, word accuracy, preserve speaker voice)
2. **Stage 2 - Insight Extraction:** Extract structured insights across 8 categories from the cleaned transcript

The extracted insights inform website copy for the VM Website 2.0 Base Case, ensuring all copy is grounded in real customer language and addresses actual pain points articulated by prospects and customers.

### Two-Stage Workflow Benefits
- **Higher accuracy:** Clean transcripts reduce misinterpretation of insights
- **Better quotes:** Corrected grammar/syntax makes quotes more copy-ready
- **Verified technical terms:** Cleanup stage catches transcription errors (ARR, covenant, EBITDA)
- **Preserved authenticity:** Both stages maintain speaker's natural voice and vocabulary

## Key Context

- **Project:** Verified Metrics Website 2.0 - Transform transcripts into website copy
- **Data Source:** 67 meeting transcripts organized by ICP (VC, PE, Private Credit, Founders, Advisors)
- **Output:** Structured markdown extraction files + Master Aggregation documents by page type
- **Brand Voice:** Confident, Accurate, Professional, Concise
- **Quality Standard:** >85% validation accuracy (quotes must be verbatim, insights traceable to source)
- **Timeline:** 4 phases over 7-9 working days (1.5-2 weeks full-time, 3-4 weeks part-time)

### Domain Expertise (Required for Accurate Extraction)

You have specialized vocabulary knowledge for:
- **Private equity and venture capital (PE/VC):** Deal flow, portfolio monitoring, due diligence, LP/GP dynamics, fund structures, carry, multiples, IRR, ARR, cap tables
- **Financial services:** FDD (Financial Due Diligence), quality of earnings, covenant compliance, EBITDA adjustments, working capital analysis, debt schedules
- **Technology sector:** SaaS metrics, API integrations, data rooms, financial data aggregation, automated reporting
- **M&A and corporate finance:** Sell-side prep, buy-side diligence, data rooms, information memorandums, teaser decks, management presentations

**Common transcript error patterns to watch for:**
- "Air R" → ARR (Annual Recurring Revenue)
- "Data room" → correctly identified (not "dataroom" or "date room")
- "Covenant" → correctly identified (not "covenant" misspellings)
- "Quality of earnings" → QofE or QoE
- "EBITDA" → correctly identified (not "EBIT DA")
- Speaker names → verify capitalization and spelling consistency

### Target Personas
1. **Equity Investors (VC/PE)** - 19 transcripts
2. **Founders** - 4 transcripts
3. **Private Credit** - 7 transcripts
4. **Advisors (Accounting firms)** - 30 transcripts

### Priority Use Cases
- Financial Due Diligence (FDD)
- Portfolio Monitoring
- Covenant Monitoring

### 8 Insight Categories to Extract
1. **Pain Points & Frustrations** (with context, intensity)
2. **Current Workflows & Alternatives** (tools, cost, time)
3. **Jobs-to-Be-Done** (frequency, success criteria)
4. **Use Case Mentions** (FDD, Portfolio, Covenant, FP&A, Valuation, Other)
5. **Value Prop Reactions** (sentiment, feature, follow-up)
6. **Language Patterns** (industry terms, metaphors)
7. **Time/Cost/Effort Quantifications** (specific numbers)
8. **Emotional Triggers** (stress, urgency, excitement, relief)

## File Access

### Read Access (Source Data)

**Meeting Transcripts:**
- **Path:** `/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/5. Projects/1. Verified Metrics/VM Website 2.0/References/Meeting Transcripts/Transcripts Downloaded/`
- **Purpose:** Source transcripts for extraction
- **Contents:** 67 markdown files with conversational dialogue from customer meetings
- **Format:** Speaker name + timestamp + dialogue

**Meeting Transcript Inventory:**
- **Path:** `/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/5. Projects/1. Verified Metrics/VM Website 2.0/References/Meeting Transcripts/Meeting Transcript Inventory.md`
- **Purpose:** Master database tracking all transcripts with metadata (ICP, Persona, Meeting Type, Status)
- **Access:** Edit-only (update Status column: Raw → Extracted → Applied)

**Base Case Document:**
- **Path:** `/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/5. Projects/1. Verified Metrics/VM Website 2.0/Base Case/VM Website 2.0 Base Case.md`
- **Purpose:** Reference for character limits, brand voice, page templates
- **Contents:** Website architecture, persona definitions, proof points

**Use Case Library:**
- **Path:** `/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/5. Projects/1. Verified Metrics/VM Website 2.0/References/Use Case Library/`
- **Purpose:** Supplement Founders insights if transcript data is thin (only 4 transcripts)
- **Contents:** 30+ detailed use case documents

### Write Access (Outputs)

**Cleaned Transcripts (Stage 1 Output):**
- **Path:** `/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/5. Projects/1. Verified Metrics/VM Website 2.0/References/Meeting Transcripts/Transcripts Cleaned/`
- **Purpose:** Store cleaned transcripts from AudioTranscriptCleanup agent before extraction
- **Naming:** Original filename with `_cleaned` suffix (e.g., `Hall-Chadwick-Verified-Metrics-Intro-ebda1b49-0152_cleaned.md`)

**Extraction Outputs (Stage 2 Output):**
- **Path:** `/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/5. Projects/1. Verified Metrics/VM Website 2.0/References/Meeting Transcripts/Extractions/`
- **Subdirectories:**
  - `By ICP/` - Individual extraction files organized by ICP (VC, PE, Private Credit, etc.)
  - `By Page Type/` - Master Aggregation documents (Homepage, Solutions-FDD, Persona-Equity-Investors, etc.)
  - `Validation Samples/` - Validation results per phase

**Processing Tool Files:**
- **Path:** `/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/5. Projects/1. Verified Metrics/VM Website 2.0/Transcript Processing Tool/`
- **Contents:** Extraction prompts, aggregation prompts, processing logs

## Quality Control

### Core Quality Principles (from AudioTranscriptCleanup best practices)

**Accuracy Over Perfection:**
- When uncertain about a quote or insight, flag it rather than guess
- Use context from surrounding conversation to inform extraction
- Be conservative - minimal interpretation is better than extensive assumptions
- Flag uncertainties with `[unclear]` or `[possibly: alternative interpretation]`

**Preserve Authenticity:**
- Maintain the speaker's natural tone and voice in quotes
- Don't change their vocabulary level or speaking style
- Keep important emphasis and emotional markers
- Preserve the original meaning and intent

**Context is Key:**
- Use surrounding transcript content to understand pain points
- Verify technical terms (PE/VC/finance/tech) are correctly identified
- Ensure speaker continuity when extracting multi-turn conversations
- Include clarifying notes in brackets when helpful `[referring to their portfolio monitoring process]`

### Required Checks

**Before Writing Extraction:**
- [ ] Quotes are verbatim (exact match from transcript - no paraphrasing)
- [ ] All 8 insight categories addressed (even if "None found" for some)
- [ ] Metadata complete (Date, ICP, Persona, Meeting Type, Participant, Company)
- [ ] Executive Summary is 2-3 sentences and accurately reflects conversation
- [ ] Use cases are tagged using standard labels (FDD, Portfolio, Covenant, FP&A, Valuation, Other)
- [ ] Time/cost metrics include specific numbers when mentioned
- [ ] Page Mapping Recommendations explain WHY insights fit specific pages
- [ ] Uncertain corrections flagged with `[unclear]` or `[possibly: interpretation]`
- [ ] Speaker's authentic voice preserved in all quotes
- [ ] Technical terms (especially PE/VC/finance) verified for accuracy

**Before Writing Aggregation:**
- [ ] All relevant extractions read (not just recent ones)
- [ ] Pain points/JTBD ranked by frequency (count mentions across transcripts)
- [ ] ICP breakdown included for each insight (which personas mentioned it)
- [ ] Representative quotes attributed to source (Company, Date)
- [ ] Coverage statistics calculated (total transcripts, by ICP)
- [ ] Top 20 quotes ranked by clarity + impact + specificity

### Forbidden Actions (Enhanced with AudioTranscriptCleanup best practices)

**DO NOT:**
- **Paraphrase quotes** - They must be verbatim from the transcript (preserve speaker's exact words)
- **Guess uncertain words** - Flag with `[unclear]` or `[possibly: word]` instead of guessing
- **Change speaker's vocabulary level** - Preserve their natural speaking style and terminology
- **Over-interpret** - Minimal interpretation; when in doubt, extract less rather than more
- **Add content not in original** - Only extract what was actually said
- **Invent insights** - All insights must be traceable to source transcript
- **Extract testimonials** - Explicitly excluded per user requirement
- **Process transcripts out of phase order** - Must follow Phase 1→2→3 sequence
- **Skip validation sampling** - Required quality gate between phases
- **Editorialize during aggregation** - Only aggregate what's in the extractions
- **Cherry-pick quotes to fit narrative** - Show actual frequency, not desired narrative
- **Create Master Insights before phase complete** - Wait for all phase extractions first

### Golden Quote Criteria (3 of 4 Required)
1. **Specific:** Includes numbers/examples ("$50k-$100k to consolidate")
2. **Emotional:** Reveals frustration/excitement ("Getting info from people who don't want to give it")
3. **Relatable:** Other customers will nod along ("FDD takes 3-6 weeks, founders are impatient")
4. **Actionable:** Can inform copy/positioning ("We'd pay $1,600/month for whole portfolio")

## Examples

### Good Output

**Pain Point Extraction:**
```markdown
## Pain Points & Frustrations

1. Pain: "Spend $50k-$100k to get all that data into one location"
   - Context: M&A data room creation for selling companies
   - Intensity: High

2. Pain: "Getting information from people who don't want to give it to us"
   - Context: Insolvency/restructuring investigations
   - Intensity: High
```

**Use Case Tagging:**
```markdown
## Use Case Mentions
- UseCase: FDD - "Very similar to having a data room... instantaneously ready to go"
- UseCase: Portfolio Monitoring - "30 portfolio companies, can't track them all manually"
- UseCase: Other (Forensic Accounting) - "Trying to get to the bottom of what's gone wrong"
```

**Copy-Ready Quote:**
```markdown
## Relevant Quotes (Copy-Ready)

1. "Spend $50k-$100k to get all that data into one location" - David Trim (Hall Chadwick), Advisors-Accounting
   - Golden Quote: ✅ Specific, ✅ Emotional, ✅ Relatable, ✅ Actionable

2. "Getting information from people who don't want to give it to us" - David Trim (Hall Chadwick), Advisors-Accounting
   - Golden Quote: ✅ Specific, ✅ Emotional, ✅ Relatable
```

### Bad Output / Anti-patterns

**❌ Generic Pain Point:**
```markdown
Pain: "Data consolidation is expensive"
Context: General workflow
Intensity: Medium
```

**✅ Specific Pain Point:**
```markdown
Pain: "Spend $50k-$100k to get all that data into one location"
Context: M&A data room creation for selling companies
Intensity: High
```

**❌ Paraphrased Quote:**
```markdown
"The participant mentioned that they have difficulty obtaining financial data from unwilling parties"
```

**✅ Verbatim Quote:**
```markdown
"Getting information from people who don't want to give it to us"
```

**❌ Missing Context:**
```markdown
Pain: "Manual work"
Intensity: High
```

**✅ Complete Context:**
```markdown
Pain: "Have somebody manually extracting and putting it all together in a separate data room"
Context: M&A transaction preparation (sell-side)
Intensity: High
```

## Additional Notes

### Character Limits (For Final Copy Reference)
- Homepage Hero H1: 45 chars
- Solutions Page H1: 40 chars
- Persona Page H1: 45 chars
- Hero Subheadline: 160-180 chars
- Body Copy: 150-200 chars
- Pain/Solution Point: 50-60 chars
- Testimonial Quote: 200 chars

### Brand Voice (Confident, Accurate, Professional, Concise)
**Confident:**
- No hedging ("can help" → "delivers")
- Direct statements
- Active voice

**Accurate:**
- Specific numbers ("500+ diligences" not "hundreds")
- Verifiable claims
- No superlatives unless backed by data

**Professional:**
- Industry terminology ("covenant compliance" not "checking rules")
- Finance language appropriate to audience

**Concise:**
- Short sentences (<20 words)
- No redundancy
- Character limits respected

### Avoid Generic Insights
❌ "We want to save time" (everyone wants this)
✅ "Manual consolidation takes 3-6 weeks" (quantified, specific)

❌ "Cost is a concern" (not specific)
✅ "We spend $50k-$100k per engagement on traditional consulting" (quantified)

### High-Quality Transcript Signals
- Participant volunteers pain points (unprompted)
- Participant gives examples ("Last quarter we...")
- Participant asks "Can you do X?" (reveals gaps)
- Participant reacts emotionally ("That's exactly what we need!")
- Participant quantifies problems ($, time, headcount)

## Context Management

For long-running sessions:
- Use `/rewind` to go back to good context points (not `/compact`)
- Use double-escape to fork conversations when you have good context
- Use `/resume` to continue from previous sessions with full context

## Nested Documentation

This project does not currently use nested CLAUDE.md files, as all work occurs in a single domain (transcript extraction).

## Maintaining Changelog & Plan

This project uses `CHANGELOG.md` and `PLAN.md` for tracking.

### When working on this project:
1. Check PLAN.md at the start to see current priorities (Current Focus section)
2. Update CHANGELOG.md after completing changes (under `## [Unreleased]`)
3. Move completed items from Current Focus to Completed in PLAN.md

### Changelog categories:
Added, Changed, Deprecated, Removed, Fixed, Security

### Plan sections:
- **Current Focus** - Active work (1-3 items max - currently Phase 1 extraction)
- **Backlog** - Future ideas (Phases 2-4, self-improvement tracking, script codification)
- **Completed** - Done items

## Self-Improvement (Phase 1 LLM-Driven → Phase 2 Code-Driven)

This agent uses the AgentFactory's self-improving pattern:

### Phase 1: LLM-Driven (75-90% reliability)
1. Execute extraction task
2. User provides validation feedback
3. Agent self-assesses outcome (Success/Partial/Failure)
4. Log to `reliability-log.md`
5. Check for patterns (3+ similar failures/successes)
6. Propose improvements

### Phase 2: Code-Driven (99%+ reliability)
- Proven workflows become deterministic Python scripts
- Scripts stored at `/Users/vic-gini/ProjectsCode/Agents/scripts/`
- Agent runs scripts instead of reasoning

**Current Phase:** 1 (LLM-Driven)
**Target:** 85%+ validation accuracy
