---
description: Review organized folders for naming convention and filing issues
---

# Audit Organization

Review files in "organized" folders to find naming convention violations and misfiled items.

## Usage

```
/audit [folder_path]
/audit ~/Documents/Finance
/audit ~/Documents/Work/VerifiedMetrics
/audit "~/Google Drive/Personal"
```

## Process

1. **Validate path** - Ensure folder exists and is not excluded
2. **Scan the folder** - Find all files in the location
3. **Read file contents** (when category seems questionable):
   - If filename doesn't clearly indicate content, read the file
   - Verify the file actually belongs in its current category
   - Create 1-sentence content summary for files being moved
   - This step prevents misfiling - don't skip it for unclear files
4. **Check each file:**
   - Does it follow naming convention? (`YYYY-MM-DD - Entity - Category - Type.ext`)
   - Is the date valid and properly formatted?
   - Is the entity name present and clear?
   - Is the category appropriate for this folder? (verify by reading if unclear)
   - Is the document type specified?
5. **Identify issues:**
   - Missing date prefix
   - Missing or unclear entity
   - Wrong category (misfiled - verified by reading content)
   - Missing document type
   - Inconsistent formatting
6. **Present proposal table** - Include Content Summary for any files being moved
7. **Wait for approval**
8. **Execute with logging**
9. **Self-assess**

## Naming Convention Check

**Expected format:** `YYYY-MM-DD - Entity Name - Category - Type.ext`

### Common Issues

| Issue | Example | Fix |
|-------|---------|-----|
| No date | `Acme Invoice.pdf` | Add `2025-12-20 -` prefix |
| Wrong date format | `12-20-2025 - ...` | Convert to `2025-12-20 - ...` |
| Missing entity | `2025-12-20 - Finance - Invoice.pdf` | Add entity: `2025-12-20 - Acme - Finance - Invoice.pdf` |
| No category | `2025-12-20 - Acme - Invoice.pdf` | Add category: `2025-12-20 - Acme - Finance - Invoice.pdf` |
| No type | `2025-12-20 - Acme - Finance.pdf` | Add type: `2025-12-20 - Acme - Finance - Invoice.pdf` |
| Wrong folder | Finance file in Family folder | Move to correct location |

## Compliance Scoring

Calculate and report:
- **Fully compliant:** Follows all naming convention rules
- **Partially compliant:** Has date but missing other elements
- **Non-compliant:** No date prefix or completely wrong format

## Output Format

```
## Organization Audit Report

**Job:** Audit
**Location:** [Path]
**Files Found:** [Count]

### Compliance Summary

| Status | Count | % |
|--------|-------|---|
| Fully compliant | X | X% |
| Partially compliant | Y | Y% |
| Non-compliant | Z | Z% |

### Issues Found

| # | File | Content Summary | Issue | Proposed Fix |
|---|------|-----------------|-------|--------------|
| 1 | [current] | Invoice from Acme Corp | Wrong category | Move to ~/Finance/ |
| 2 | [current] | (naming issue only) | Missing date | 2025-12-15 - [current] |

Note: Content Summary included for files being moved to verify correct destination.

### Recommendations

1. [Specific recommendation]
2. [Specific recommendation]

**Awaiting your approval to proceed with fixes.**
```

## After Approval

1. Rename files to follow convention
2. Move misfiled items to correct locations
3. Log each action to action-log.md
4. Report completion summary
5. Log session outcome to reliability-log.md
