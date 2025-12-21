---
description: Review and classify ambiguous files in the NeedsReview folder
---

# Review Ambiguous Files

Process files that were moved to NeedsReview because they couldn't be automatically classified.

## Usage

```
/review
/review --date 2025-12-20
/review --batch
```

## Process

1. **Scan NeedsReview folder** - Find all pending files
2. **For each file, present:**
   - Filename and location
   - File metadata (size, dates, type)
   - Why it was flagged as ambiguous
   - Possible categories/destinations
3. **Get user decision:**
   - Organize to specific location (with name)
   - Stage for deletion
   - Leave in NeedsReview for later
   - Custom action
4. **Execute decision** - Move file accordingly
5. **Log action** - Update action-log.md
6. **Continue to next file** (or process batch)

## NeedsReview Structure

```
~/NeedsReview/
├── 2025-12-20/           # Date file was flagged
│   ├── mystery_doc.pdf
│   └── unclear_file.txt
└── 2025-12-19/
    └── unknown_image.jpg
```

## Presentation Format

For each file:

```
## File Review: [filename]

**Location:** ~/NeedsReview/2025-12-20/mystery_doc.pdf
**Size:** 1.2 MB
**Created:** 2025-12-15
**Modified:** 2025-12-18
**Type:** PDF document

### Why Flagged
[Reason - e.g., "Could not determine entity or category from filename"]

### Possible Classifications

1. **Finance** - If this is a financial document
   → Rename to: 2025-12-15 - [Entity] - Finance - [Type].pdf
   → Move to: ~/Documents/Finance/

2. **Work (VM)** - If this is work-related
   → Rename to: 2025-12-15 - [Entity] - VerifiedMetrics - [Type].pdf
   → Move to: ~/Documents/Work/VerifiedMetrics/

3. **Stage for deletion** - If not needed
   → Move to: ~/ToDelete/2025-12/[Category]/

4. **Leave for later** - Skip this file

### Your Decision
Please specify:
- Category number (1-4)
- Entity name (if organizing)
- Document type (if organizing)

Example: "1, Acme Corp, Invoice"
```

## Batch Mode

When using `--batch`:

```
## Batch Review: [X] Files

| # | File | Size | Suggestion | Your Decision |
|---|------|------|------------|---------------|
| 1 | mystery_doc.pdf | 1.2 MB | Finance? | [wait for input] |
| 2 | unclear_file.txt | 0.5 KB | Delete? | [wait for input] |

For each file, reply with: [#] [action] [details]
Examples:
- "1 organize Finance, Acme Corp, Invoice"
- "2 delete"
- "3 skip"
- "all delete" (for all files)
```

## Decision Actions

| Action | What Happens |
|--------|--------------|
| **organize** | Rename using convention, move to proper folder |
| **delete** | Move to ~/ToDelete/YYYY-MM/Category/ |
| **skip** | Leave in NeedsReview for later |
| **custom** | User specifies exact destination |

## After Processing

1. Log all actions to action-log.md
2. Report summary of decisions
3. Clean up empty date folders in NeedsReview
