# Plan

## Current Focus

- **Phase 1 Extraction:** Process 20-25 high-value Discovery/Demo transcripts (VC, PE, Private Credit, select Advisors)
- **Create extraction templates:** Generate extraction-prompt-template.md and aggregation-prompt-template.md
- **Create directory structure:** Set up Extractions/By ICP/ and Extractions/By Page Type/ folders

## Backlog

- **Phase 1 Aggregation:** Create initial Master Insights documents (FDD, Portfolio Monitoring, Covenant Monitoring)
- **Phase 1 Validation:** Human review of 15% sample (3-4 transcripts) to validate 85%+ accuracy
- **Phase 2 Extraction:** Process 15-20 secondary Discovery/Demo transcripts (Founders, remaining Advisors, Advisors-Other)
- **Phase 3 Extraction:** Process 15-20 Check-ins, DD Debriefs, Unknown transcripts
- **Phase 4 Aggregation:** Final aggregation across all 67 transcripts
- **Phase 4 Copy Development:** Transform Master Insights into website copy for Base Case
- **Inventory Enhancement:** Add columns (Key Themes, Priority Score, Used in Pages, Extraction Quality, Notable Quotes)
- **Self-Improvement:** Track patterns in reliability-log.md, propose prompt refinements
- **Script Codification:** If extraction patterns prove reliable (3+ successes), codify to Python scripts (Phase 2 maturity)

## Completed

- [x] (2025-12-09 16:26) Agent project structure created at `/Users/vic-gini/ProjectsCode/Agents/TranscriptExtractor/`
- [x] (2025-12-09 16:26) CLAUDE.md project context written
- [x] (2025-12-09 16:26) Permissions configured in .claude/settings.json (least privilege)
- [x] (2025-12-09 16:26) transcript-extractor agent defined with 8-category extraction framework
- [x] (2025-12-09 16:26) aggregator agent defined for Master Insights synthesis
- [x] (2025-12-09 16:26) Extraction framework designed (8 categories, structured markdown template)
- [x] (2025-12-09 16:26) File structure designed (By ICP + By Page Type organization)
- [x] (2025-12-09 16:26) CHANGELOG.md created
- [x] (2025-12-09 16:26) PLAN.md created
- [x] (2025-12-09 16:26) reliability-log.md created for self-improvement tracking
- [x] (2025-12-09 17:15) Renamed project from TranscriptExtractor to VM_Transcript_Extractor (VM-specific branding)
- [x] (2025-12-09 17:15) Renamed agent from transcript-extractor to vm-transcript-extractor
- [x] (2025-12-09 17:15) Incorporated AudioTranscriptCleanup best practices for enhanced quality:
  - Core Quality Principles (Accuracy Over Perfection, Preserve Authenticity, Context is Key)
  - Domain Expertise section with PE/VC/finance/tech vocabulary
  - Common transcript error patterns (ARR, data room, covenant, EBITDA)
  - Enhanced uncertainty flagging with `[unclear]` and `[possibly: alternative]`
  - Conservative extraction approach (minimal interpretation)
  - Expanded error handling patterns
- [x] (2025-12-09 17:15) Updated CHANGELOG.md with v1.1.0 release documenting all improvements
- [x] (2025-12-09 17:30) Integrated AudioTranscriptCleanup agent as Stage 1 of extraction workflow (two-stage process)
- [x] (2025-12-09 17:30) Created two-stage workflow: Cleanup → Extraction for higher accuracy
- [x] (2025-12-09 17:30) Created `Transcripts Cleaned/` folder and added write permissions
- [x] (2025-12-09 17:30) Updated agent process documentation to reflect two-stage workflow
- [x] (2025-12-09 17:30) Updated CHANGELOG.md with v1.2.0 release documenting two-stage integration
