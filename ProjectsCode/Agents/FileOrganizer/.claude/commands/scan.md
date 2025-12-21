---
description: Scan directories and report on organization status
---

# Scan Organization Status

Analyze folders and report on how well files are organized, helping decide whether to triage or audit.

## Usage

```
/scan [folder_path]
/scan ~/Downloads
/scan ~/Documents
/scan --all-drives
/scan --priority-dumps
```

## Process

1. **Scan specified location(s)** - Find all files recursively
2. **Analyze each file:**
   - Check if follows naming convention
   - Check if in appropriate folder for its category
   - Identify potential duplicates
   - Note very old or large files
3. **Generate statistics:**
   - Compliance percentage
   - Files needing organization
   - Files needing review
   - Potential issues
4. **Recommend next actions**

## Analysis Criteria

### Naming Convention Check

| Status | Criteria |
|--------|----------|
| **Compliant** | Matches `YYYY-MM-DD - Entity - Category - Type.ext` |
| **Partial** | Has date but missing components |
| **Non-compliant** | No date prefix, wrong format |

### Folder Appropriateness

Check if file's apparent category matches its folder location.

### Flags

- **Large files:** > 100 MB
- **Old files:** > 1 year old
- **Potential duplicates:** Same name pattern or size

## Output Format

```
## Organization Status Report

**Scan Date:** 2025-12-20
**Location:** [path or "All Drives"]
**Total Files:** [count]
**Total Size:** [size]

### Compliance Summary

| Status | Count | % |
|--------|-------|---|
| Fully compliant | X | X% |
| Partially compliant | Y | Y% |
| Non-compliant | Z | Z% |

### By Location

| Location | Files | Compliant | Action Needed |
|----------|-------|-----------|---------------|
| ~/Downloads | 45 | 0% | Triage |
| ~/Desktop | 12 | 8% | Triage |
| ~/Documents/Finance | 150 | 85% | Audit |
| ~/Documents/Work | 200 | 72% | Audit |

### Top Issues

1. **Downloads:** 45 unorganized files (needs triage)
2. **Desktop:** 12 files with no naming convention
3. **Finance folder:** 15 files missing entity names

### Recommendations

1. Run `/triage ~/Downloads` - 45 files need organizing
2. Run `/triage ~/Desktop` - 12 files need organizing
3. Run `/audit ~/Documents/Finance` - 15 files need name fixes

### Large Files (> 100 MB)

| File | Size | Location |
|------|------|----------|
| [name] | 250 MB | [path] |

### Potential Duplicates

| File Pattern | Count | Total Size |
|--------------|-------|------------|
| invoice*.pdf | 3 | 2.5 MB |
```

## Priority Dumps Scan

When using `--priority-dumps`:

Only scans the designated dump folders:
- `~/Downloads/`
- `~/Desktop/`
- `~/Library/Mobile Documents/com~apple~CloudDocs/Downloads/`

```
## Priority Dump Folders Status

| Folder | Files | Last Cleaned | Status |
|--------|-------|--------------|--------|
| ~/Downloads | 45 | Never | Needs triage |
| ~/Desktop | 12 | 2025-12-01 | Needs triage |
| iCloud Downloads | 8 | 2025-12-15 | Needs triage |

**Total files to process:** 65

Run `/triage` on each folder to organize.
```

## All Drives Scan

When using `--all-drives`:

Scans all configured cloud drives and local storage:
- iCloud Drive
- Google Drive (Personal)
- Google Drive (Work)
- Dropbox (Personal)
- Dropbox (Cloudview)
- Local Documents
- Local Downloads
- Local Desktop

Excludes:
- Obsidian vaults
- ProjectsCode
- System/hidden folders
