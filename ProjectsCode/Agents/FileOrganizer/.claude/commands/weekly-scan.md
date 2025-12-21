---
description: Weekly recurring scan of priority folders for organization status
---

# Weekly Scan

Automated weekly check on organization status of key folders.

## Usage

```
/weekly-scan
```

## Scope

Scans these priority locations:
1. **Priority Dump Folders:**
   - `~/Downloads/`
   - `~/Desktop/`
   - `~/Library/Mobile Documents/com~apple~CloudDocs/Downloads/`

2. **Deletion Staging:**
   - `~/ToDelete/` - Check for 30+ day old files

3. **Review Queue:**
   - `~/NeedsReview/` - Pending ambiguous files

## Process

1. **Scan all priority locations**
2. **Generate status for each:**
   - File count
   - Days since last organized
   - Urgency level (Low/Medium/High)
3. **Check deletion staging:**
   - Files older than 30 days
   - Total size of staged files
4. **Check review queue:**
   - Number of pending files
   - Oldest pending file
5. **Generate summary report**
6. **Recommend priority actions**

## Output Format

```
## Weekly Organization Status

**Report Date:** 2025-12-20
**Week:** 51

---

### Priority Dump Folders

| Folder | Files | Status | Last Triaged | Urgency |
|--------|-------|--------|--------------|---------|
| ~/Downloads | 23 | Needs triage | 7 days ago | Medium |
| ~/Desktop | 5 | Needs triage | 3 days ago | Low |
| iCloud Downloads | 0 | Clean | Today | None |

**Total files to triage:** 28

---

### Deletion Staging

| Folder | Files | Size | Oldest |
|--------|-------|------|--------|
| ~/ToDelete/2025-11/ | 45 | 250 MB | 45 days |
| ~/ToDelete/2025-12/ | 12 | 30 MB | 15 days |

**Files ready for purge review:** 45 (> 30 days old)
**Total staged:** 280 MB

---

### Review Queue

| Date Folder | Files | Oldest |
|-------------|-------|--------|
| 2025-12-15 | 3 | 5 days |
| 2025-12-18 | 2 | 2 days |

**Total pending review:** 5 files

---

### This Week's Recommendations

**Priority 1:** Run `/cleanup --purge-review`
- 45 files in ToDelete are 30+ days old

**Priority 2:** Run `/triage ~/Downloads`
- 23 files accumulated since last triage

**Priority 3:** Run `/review`
- 5 ambiguous files waiting for classification

---

### Trends

| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| Files triaged | 0 | 15 | -100% |
| Files audited | 0 | 0 | -- |
| Files deleted | 0 | 10 | -100% |

---

**Next weekly scan:** 2025-12-27
```

## Integration with Planning Agent

This weekly scan can be:
- Triggered as part of the Weekly Planning session
- Added to the weekly routines checklist
- Referenced in the Weekly Plan under "Organization / Routines / Maintenance"

## Urgency Levels

| Level | Criteria |
|-------|----------|
| **High** | > 50 files or > 14 days since last triage |
| **Medium** | 20-50 files or 7-14 days since last triage |
| **Low** | < 20 files and < 7 days since last triage |
| **None** | Folder is empty or fully organized |
