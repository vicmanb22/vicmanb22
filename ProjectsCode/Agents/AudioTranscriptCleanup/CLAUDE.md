# Audio Transcript Cleanup

An expert transcript editor agent for cleaning up and enhancing imperfect audio transcriptions.

## Overview

This agent transforms raw, error-filled transcripts into polished, accurate documents while preserving the speaker's original voice and meaning. It handles transcripts from various sources including Google Meet, Fireflies.ai, Otter.ai, and internet extracts.

## How to Use

1. **Invoke the agent:** `@transcript-cleanup`
2. **Provide a transcript:** Either paste text directly or provide a file path from the `transcripts/` folder
3. **Receive cleaned output:** Agent saves polished transcript to `cleaned/` folder and displays it

## Key Context

- **Domain expertise:** PE/VC, financial services, and technology terminology
- **Input sources:** Google Meet, Fireflies.ai, Otter.ai, internet extracts, other transcription services
- **Output mode:** Always full polish with summary of corrections
- **Philosophy:** Accuracy over perfection, conservative edits, preserve speaker's voice

## File Access

- **Input:** `transcripts/` - Place raw transcript files here
- **Output:** `cleaned/` - Agent saves cleaned transcripts here
- **Naming:** Cleaned files use original filename with `_cleaned` suffix

## Quality Control

### Required Checks
- Verify speaker continuity across the document
- Ensure technical terms (especially PE/VC/finance/tech) are correctly transcribed
- Flag uncertain corrections with `[unclear]` or `[possibly: word]`
- Include summary of corrections at the end

### Forbidden Actions
- Never guess uncertain words without flagging
- Never change speaker's vocabulary level or speaking style
- Never over-edit to the point of changing meaning
- Never add content that wasn't in the original

## Speaker Labeling

- **Unknown speakers:** `**Speaker 1:**`, `**Speaker 2:**`
- **Known names:** `**[Name]:**`
- **Existing labels:** Preserve and standardize format
- **Multiple unlabeled:** Ask user for names if detected

## Long Transcript Handling

For transcripts exceeding context limits:
1. Agent notifies user of length
2. Processes in logical chunks (by speaker turn or topic)
3. Maintains speaker continuity across chunks
4. Combines into single cleaned output file
5. Summary covers entire transcript

## Maintaining Changelog & Plan

This project uses `CHANGELOG.md` and `PLAN.md` for tracking.

### When working on this project:
1. Check PLAN.md at the start to see current priorities
2. Update CHANGELOG.md after completing changes (under `## [Unreleased]`)
3. Move completed items from Current Focus to Completed in PLAN.md

### Changelog categories:
Added, Changed, Deprecated, Removed, Fixed, Security

### Entry format:
`- (YYYY-MM-DD HH:MM) Description of change`

### Plan sections:
- **Current Focus** - Active work (1-3 items max)
- **Backlog** - Future ideas
- **Completed** - Done items
