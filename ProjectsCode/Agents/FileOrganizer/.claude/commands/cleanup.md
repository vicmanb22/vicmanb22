---
description: Identify and stage files for deletion (never deletes directly)
---

# Cleanup / Deletion Staging

Identify files that may be candidates for deletion and stage them for user review.

## Usage

```
/cleanup [folder_path]
/cleanup ~/Downloads
/cleanup ~/Documents --duplicates-only
/cleanup ~/Desktop --age-days 90
/cleanup --purge-review
```

## Process

1. **Scan location** - Find all files in specified folder
2. **Identify deletion candidates:**
   - Duplicate files (same content, different names)
   - Temporary files (.tmp, ~*, .swp, etc.)
   - Old versions superseded by newer ones
   - Empty files (0 bytes)
   - Very old files (if --age-days specified)
3. **Categorize by domain** - For proper staging folder placement
4. **Propose staging** - Show what will move to ~/ToDelete/
5. **Wait for approval** - CRITICAL: never proceed without confirmation
6. **Execute staging:**
   - Create ~/ToDelete/YYYY-MM/Category/ if needed
   - Move files to staging
   - Record original location in action-log.md
7. **Report results**

## Deletion Staging Structure

```
~/ToDelete/
├── 2025-12/
│   ├── VerifiedMetrics/
│   ├── ArgonautExpeditions/
│   ├── IDEACIMUN/
│   ├── CloudviewRealEstate/
│   ├── Family/
│   ├── PersonalFinance/
│   ├── Recovery/
│   ├── LifeAndFun/
│   ├── OrganizationRoutinesMaintenance/
│   ├── Reference/
│   └── Media/
└── permanent-delete-queue/
```

## Candidate Identification

### Temporary Files
```
*.tmp, *.temp, *~, .~*, *.swp, *.swo
.DS_Store, Thumbs.db, desktop.ini
*.bak, *.backup, *.old
```

### Duplicates
Files with same:
- File size AND
- First/last 1KB content match

### Old Versions
Files matching pattern:
- `filename (1).ext`, `filename (2).ext`
- `filename_v1.ext`, `filename_v2.ext`
- `filename_old.ext`, `filename_backup.ext`

When a newer version exists in same folder.

### Empty Files
Files with 0 bytes (unless intentionally empty like `.gitkeep`)

## Output Format

```
## Cleanup Proposal

**Location:** [Path]
**Files Scanned:** [Count]

### Deletion Candidates

| # | File | Reason | Size | Staging Location |
|---|------|--------|------|------------------|
| 1 | [name] | Duplicate of [other] | 1.2 MB | ~/ToDelete/2025-12/Work/ |
| 2 | [name] | Temporary file | 0 KB | ~/ToDelete/2025-12/Personal/ |

### Summary
- **Duplicates:** X files (Y MB)
- **Temporary:** X files
- **Old versions:** X files
- **Empty:** X files
- **Total to stage:** X files (Y MB)

**Files will be staged at ~/ToDelete/2025-12/ for 30 days.**
Original locations will be logged for recovery if needed.

**Awaiting your approval to proceed.**
```

## Purge Review Mode

When running `/cleanup --purge-review`:

1. Scan ~/ToDelete/ for files older than 30 days
2. List files eligible for permanent deletion
3. Move approved files to permanent-delete-queue/
4. User manually empties permanent-delete-queue when ready

## Safety Rules

1. **NEVER use rm or delete commands**
2. **ALWAYS move to staging, never delete**
3. **ALWAYS log original location for recovery**
4. **ALWAYS wait for user approval**
5. **NEVER touch excluded folders**
