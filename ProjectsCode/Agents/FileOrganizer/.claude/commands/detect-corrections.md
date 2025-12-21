---
description: Detect manual file moves made after agent/Hazel automation
---

# Detect Manual Corrections

Automatically detect when files were manually moved after agent or Hazel automation, indicating the automation was incorrect.

## Usage

```
/detect-corrections
/detect-corrections --since "2025-12-15"
/detect-corrections --folder ~/Documents/Finance
```

## How It Works

### Detection Method

1. **Read action-log.md** - Get list of recent agent-moved files
2. **Check current locations** - Verify files are still where agent put them
3. **Identify moved files** - Files no longer at logged destination
4. **Find new locations** - Search for files by name in likely locations
5. **Analyze patterns** - Group corrections by type
6. **Report findings** - Present corrections for review
7. **Propose improvements** - Suggest rule/behavior changes

### What Gets Detected

| Scenario | Detection |
|----------|-----------|
| File moved to different folder | Original location empty, file found elsewhere |
| File renamed after move | Original name gone, similar file in same folder |
| File deleted after move | File not found anywhere (may be in Trash) |
| File moved back to source | File returned to original location |

## Output Format

```
## Manual Corrections Detected

**Period:** [Date range analyzed]
**Actions Reviewed:** [Count from action-log]
**Corrections Found:** [Count]

### Corrections

| # | Original Action | File | Agent Put | You Moved To | Correction Type |
|---|-----------------|------|-----------|--------------|-----------------|
| 1 | Triage 12/18 | invoice.pdf | Finance/Invoices/ | Work/VM/Invoices/ | Wrong category |
| 2 | Triage 12/19 | report.pdf | NeedsReview/ | Finance/Reports/ | Resolved ambiguity |
| 3 | Hazel rule | statement.pdf | Finance/Banking/ | Deleted | Unwanted file |

### Pattern Analysis

**Category Errors:** 2 occurrences
- Agent categorized as Personal Finance, you moved to Work
- Suggests: Work invoices should go to Work folders, not Finance

**Hazel Over-matching:** 1 occurrence
- "Bank statement" rule caught a non-bank PDF
- Suggests: Tighten rule to require bank name in filename

### Proposed Improvements

1. **Agent directive:** When file contains work client names, prefer Work category over Finance
2. **Hazel rule:** Add condition "Name contains Chase OR Bank of America OR ..."

**Would you like me to:**
1. Implement these improvements
2. Log for later review
3. Discuss specific corrections
```

## Automatic Detection Triggers

The agent can run detection automatically:

### At Session Start
When starting FileOrganizer, optionally check for corrections:
```
"I notice 3 files were moved after my last session. Would you like to review these corrections?"
```

### After Weekly Scan
Include correction detection in `/weekly-scan`:
```
### Manual Corrections Since Last Week
- 2 files were moved after agent organization
- 1 Hazel-organized file was deleted
```

### Before Suggesting Hazel Rules
Check if previous suggestions led to corrections:
```
"Before suggesting new rules, I checked: the last invoice rule had 2 manual corrections.
Should I factor this into my new suggestion?"
```

## Integration with Reliability Log

Detected corrections are logged:

```markdown
### YYYY-MM-DD - Detected Correction

**Original Action:** [From action-log]
**File:** [filename]
**Agent Destination:** [path]
**User Moved To:** [new path]
**Correction Type:** [Category/Entity/Destination/Deleted]
**Days Until Corrected:** [N]
**Pattern Match:** [If matches previous corrections]
```

## Learning from Corrections

### 3+ Similar Corrections → Propose Change

When the same type of correction happens 3+ times:

```
## Pattern Detected: Work Invoices Miscategorized

**Occurrences:** 4 times in last 30 days
**Pattern:** Files with client names (Acme, Globex, etc.) placed in Finance instead of Work

**Proposed Directive Change:**
Add to file-organizer.md:
"When a file contains a known work client name, categorize under Work domain,
even if it's an invoice or financial document."

**Would you like me to implement this?**
```

### Hazel Rule Corrections → Suggest Refinement

```
## Hazel Rule Needs Adjustment: "Auto-organize Invoices"

**Corrections:** 3 in last 14 days
**Issue:** Rule catches expense reports, not just invoices

**Current Conditions:**
- Kind is PDF
- Name contains "invoice"

**Proposed Conditions:**
- Kind is PDF
- Name contains "invoice"
- Name does NOT contain "expense"
- Name does NOT contain "report"

**Would you like me to update the rule?**
```

## Privacy Note

Detection only checks files that were logged in action-log.md. The agent does not scan your entire filesystem or track files it didn't organize.
