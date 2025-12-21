# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- (2025-12-20) Initial project setup with CLAUDE.md, settings.json
- (2025-12-20) Created agent structure following AgentFactory patterns
- (2025-12-20) Defined naming convention: YYYY-MM-DD - Entity - Category - Type.ext
- (2025-12-20) Configured 9 domain categories aligned with Planning agent
- (2025-12-20) Set up two distinct jobs: Triage (file dumps) and Audit (organized folders)
- (2025-12-20) Created workflow commands: triage, audit, rename, cleanup, review, scan, suggest-hazel
- (2025-12-20) Configured staging folders: ~/ToDelete/ and ~/NeedsReview/
- (2025-12-20) Integrated self-improvement protocol with reliability logging
- (2025-12-20) Added `/feedback` command for user to rate actions and report Hazel rule issues
- (2025-12-20) Added `/detect-corrections` command to find manually moved files
- (2025-12-20) Added automatic correction detection at session start
- (2025-12-20) Learning from manual corrections: 3+ similar corrections trigger behavior change proposal
- (2025-12-20 12:15) Added Duplicate Detection Rules requiring file size comparison before deletion
- (2025-12-20 12:15) Added size comparison table format to Response Format section
- (2025-12-20 12:15) Added Anti-pattern 6: Assuming (1) Suffix Means Duplicate
- (2025-12-20 12:15) Added Duplicates behavior to Key Behaviors table in CLAUDE.md
- (2025-12-20 12:15) First reliability log entry documenting duplicate detection gap
- (2025-12-20 12:45) Added PDF digital signature detection script (scripts/pdf_signature_check.py)
- (2025-12-20 12:45) Added python3 permission to settings.json for signature detection
- (2025-12-20 12:45) Updated duplicate detection to check PDF signatures automatically
- (2025-12-20 12:45) Added PDF Signatures behavior to Key Behaviors table
- (2025-12-20) **Read Before Categorize**: Agent now reads file contents (PDFs, docs, spreadsheets) before assigning category
- (2025-12-20) **Table Before Action**: Agent must always show proposal table with Content Summary and wait for approval
- (2025-12-20) Updated proposal table format to include Content Summary and Reasoning columns
- (2025-12-20) Added Anti-pattern 7: Categorizing from Filename Alone
- (2025-12-20) Updated triage.md workflow with explicit file reading step
- (2025-12-20) Updated audit.md workflow with file reading for questionable categories
- (2025-12-20) **Entity Aliases**: Added learned entity-to-domain mappings (More Champ → VM, Crimson Typhoon → VM, etc.)
- (2025-12-20) **Session Logging Automation**: Made log updates MANDATORY at session end
- (2025-12-20) Added `/start-session` command - checks for manual corrections at session start
- (2025-12-20) Added `/end-session` command - updates action-log.md and reliability-log.md
- (2025-12-20) Added PostToolUse hook to auto-log mv/cp commands to .claude/file-ops.log
- (2025-12-20) Added Session Logging and Correction Detection to Key Behaviors table
- (2025-12-20) Updated agent with MANDATORY session logging protocol
