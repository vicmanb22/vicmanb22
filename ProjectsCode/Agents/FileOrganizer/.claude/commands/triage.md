---
description: Process unorganized file dumps - categorize, rename, and move files
---

# Triage Files

Process unorganized file dumps where files are loosely grouped but not properly named or filed.

## Usage

```
/triage [folder_path]
/triage ~/Downloads
/triage ~/Desktop
/triage "~/Documents/Tax Stuff"
```

## Process

1. **Validate path** - Ensure folder exists and is not excluded
2. **Scan the folder** - Use Glob to find all files (exclude hidden/system)
3. **Read each file** (CRITICAL - do not skip):
   - **PDFs**: Read to identify document type, parties involved, dates, purpose
   - **Spreadsheets/CSV**: Read to understand data structure and purpose
   - **Text/HTML/Markdown**: Scan for identifying information
   - **Skip reading**: Zips, images, binaries (note as "content not read")
   - **Record**: Create 1-sentence summary of what the file contains
   - Note if content contradicts filename-based categorization
4. **Analyze each file** (using content from step 3):
   - Extract date from content, filename, metadata, or modification date
   - Identify entity (person, company, source) from content or filename
   - Determine category based on 9 domains
   - Determine document type
5. **Generate proposed names** - Using `YYYY-MM-DD - Entity - Category - Type.ext`
6. **Determine destinations** - Based on category and folder hierarchy
7. **Present proposal table** - MUST include Content Summary column (see format below)
8. **Wait for approval** - Do NOT proceed without explicit confirmation
9. **Execute with logging** - Move/rename files, log each to action-log.md
10. **Report results** - Summary of completed actions
11. **Self-assess** - Log outcome to reliability-log.md

## File Analysis Tips

### Extracting Dates
- Check filename for date patterns (YYYY-MM-DD, MM-DD-YYYY, etc.)
- Use `mdls` to get file metadata (creation, modification dates)
- For documents, use the most relevant date (invoice date, not download date)

### Identifying Entities
- Company names often in filenames (invoice_acme.pdf → Acme Corp)
- Bank statements have bank names
- Medical documents have provider names
- Personal files may reference family members (Nara, etc.)

### Categorizing by Domain
| Signals | Domain |
|---------|--------|
| VM, client, project, work | VerifiedMetrics |
| Argonaut, expedition, travel business | ArgonautExpeditions |
| IDEA, CIMUN, MUN, conference | IDEACIMUN |
| Property, rental, Cloudview | CloudviewRealEstate |
| Nara, school, parenting | Family |
| Bank, tax, investment, insurance | PersonalFinance |
| Therapy, health, EMDR, wellness | Recovery |
| Hobby, entertainment, vacation | LifeAndFun |
| Bills, maintenance, admin | OrganizationRoutinesMaintenance |

## Excluded Folders

Never process files in:
- Obsidian vaults
- `~/ProjectsCode/`
- `.git/`, `node_modules/`, `.obsidian/`
- System folders

## Output Format

```
## File Organization Plan

**Job:** Triage
**Location:** [Path]
**Files Found:** [Count]

### Proposed Actions

| # | File | Content Summary | Proposed Name | Destination | Reasoning |
|---|------|-----------------|---------------|-------------|-----------|
| 1 | [current] | Invoice from Acme Corp dated Dec 2025 | 2025-12-15 - Acme - Finance - Invoice.pdf | ~/Documents/Finance/ | Finance domain |
| 2 | [current] | (zip - not read) | - | ~/NeedsReview/... | Cannot determine |
| 3 | [current] | Duplicate of #1 (same size) | - | ~/ToDelete/... | True duplicate |

### Summary
- **Organize:** X files
- **Stage for deletion:** Y files
- **Needs review:** Z files

**Awaiting your approval to proceed.**
```

## After Approval

1. Create destination folders if needed (`mkdir -p`)
2. Move/rename files using `mv`
3. Log each action to action-log.md
4. Report completion summary
5. Log session outcome to reliability-log.md
