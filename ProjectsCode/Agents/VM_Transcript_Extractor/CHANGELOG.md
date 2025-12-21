# Changelog

All notable changes to the VM Transcript Extractor agent will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [1.2.0] - 2025-12-09

### Added
- (2025-12-09 17:30) Integrated AudioTranscriptCleanup agent as Stage 1 of extraction workflow
- (2025-12-09 17:30) Two-stage workflow: Stage 1 (Transcript Cleanup) → Stage 2 (Insight Extraction)
- (2025-12-09 17:30) Created `Transcripts Cleaned/` folder for cleaned transcript outputs
- (2025-12-09 17:30) Added write permissions for Transcripts Cleaned folder in settings.json
- (2025-12-09 17:30) Updated agent process to clean transcripts before extraction for higher accuracy

### Changed
- (2025-12-09 17:30) Agent now processes raw transcript → cleaned transcript → extraction (was: raw → extraction directly)
- (2025-12-09 17:30) Extraction quotes now sourced from cleaned transcripts (grammar-corrected, technical terms verified)

## [1.1.0] - 2025-12-09

### Changed
- (2025-12-09 17:15) Renamed project from "TranscriptExtractor" to "VM_Transcript_Extractor" to signify VM-specific purpose
- (2025-12-09 17:15) Renamed agent from "transcript-extractor" to "vm-transcript-extractor"
- (2025-12-09 17:15) Updated CLAUDE.md title and description to reflect VM-specific focus

### Added
- (2025-12-09 17:15) Incorporated best practices from AudioTranscriptCleanup agent for enhanced quality:
  - Core Quality Principles section (Accuracy Over Perfection, Preserve Authenticity, Context is Key)
  - Domain Expertise section with specialized vocabulary knowledge (PE/VC, Financial Services, Technology, M&A)
  - Common transcript error patterns to watch for (ARR, data room, covenant, EBITDA, etc.)
  - Enhanced Required Behaviors with uncertainty flagging (`[unclear]`, `[possibly: alternative]`)
  - Enhanced Forbidden Actions emphasizing no guessing, no over-interpretation
  - Expanded Error Handling with patterns for corrupted transcripts, uncertain technical terms, ambiguous speakers
  - Conservative extraction approach (minimal interpretation when uncertain)
- (2025-12-09 17:15) Added quality checkboxes for uncertain corrections, authentic voice preservation, technical term verification

## [1.0.0] - 2025-12-09

### Added
- (2025-12-09 16:26) Created transcript-extractor agent for VM Website 2.0 project
- (2025-12-09 16:26) Created aggregator agent for Master Insights synthesis
- (2025-12-09 16:26) Set up project structure with CLAUDE.md, settings.json, agents
- (2025-12-09 16:26) Defined 8 insight categories for extraction (Pain Points, JTBD, Workflows, Use Cases, Value Props, Language, Metrics, Emotions)
- (2025-12-09 16:26) Established 4-phase workflow (High-Value Discovery → Secondary Discovery → Edge Cases → Aggregation & Copy Development)
- (2025-12-09 16:26) Configured least-privilege permissions (Read VM files, Write only to Extractions, Edit only Inventory)
- (2025-12-09 16:26) Created reliability-log.md for self-improvement tracking
- (2025-12-09 16:26) Set Phase 1 quality gate: 85%+ accuracy on 3-4 validation samples
