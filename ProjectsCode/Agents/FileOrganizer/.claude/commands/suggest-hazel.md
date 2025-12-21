---
description: Analyze patterns and suggest Hazel automation rules
---

# Suggest Hazel Rules

Analyze organization patterns from action-log.md and suggest Hazel rules for automation.

## Usage

```
/suggest-hazel
/suggest-hazel --analyze-last-30-days
/suggest-hazel --for-folder ~/Downloads
```

## Process

1. **Review action-log.md** - Find repeated patterns
2. **Identify automation candidates:**
   - Same source folder → same destination (3+ times)
   - Same file type → same action (3+ times)
   - Same naming pattern → same rename rule
3. **Generate Hazel rule suggestion:**
   - Conditions (file type, name pattern, source)
   - Actions (move, rename, tag)
4. **Present suggestion** - Clear, actionable format
5. **Wait for user direction:**
   - "Implement it" - Modify Hazel (only if explicitly directed)
   - "Save for later" - Log to hazel-rules-reference.md
   - "Skip" - Don't implement
6. **Log suggestion** to reliability-log.md

## Pattern Detection

### Source → Destination Patterns

When 3+ files from same source go to same destination:
```
Pattern: Downloads/*.pdf invoices → Documents/Finance/Invoices/
Trigger: File type PDF, name contains "invoice"
Action: Move to Finance/Invoices, rename with date prefix
```

### File Type Patterns

When 3+ files of same type get same treatment:
```
Pattern: All bank statements → Documents/Finance/Banking/
Trigger: File type PDF, name contains "statement" or "bank"
Action: Move to Banking folder
```

### Naming Patterns

When same rename logic applied repeatedly:
```
Pattern: "invoice_*.pdf" → "YYYY-MM-DD - Entity - Finance - Invoice.pdf"
Trigger: Name matches "invoice_*.pdf"
Action: Rename with date and entity extraction
```

## Output Format

```
## Suggested Hazel Rule

### Pattern Detected

In the last 30 days, you've organized **[X] files** matching this pattern:
- Source: ~/Downloads/
- File type: PDF
- Name contains: "invoice"
- Destination: ~/Documents/Finance/Invoices/
- Rename pattern: Date prefix + entity + "Finance - Invoice"

### Proposed Hazel Rule

**Name:** Auto-organize Invoices
**Watch Folder:** ~/Downloads

**Conditions:**
- Kind is PDF
- Name contains "invoice" (case insensitive)

**Actions:**
1. Rename with pattern:
   - Use file creation date for YYYY-MM-DD
   - Extract company name from filename
   - Append " - Finance - Invoice"
2. Move to folder: ~/Documents/Finance/Invoices/

### Preview

| Before | After | Location |
|--------|-------|----------|
| acme_invoice_dec.pdf | 2025-12-20 - Acme - Finance - Invoice.pdf | Finance/Invoices/ |
| invoice_globex.pdf | 2025-12-20 - Globex - Finance - Invoice.pdf | Finance/Invoices/ |

### Options

1. **Implement in Hazel** - I'll create this rule (requires explicit direction)
2. **Save for reference** - Log to hazel-rules-reference.md for manual setup
3. **Skip** - Don't create this rule

What would you like to do?
```

## Important Constraints

- Agent can **SUGGEST** rules at any time
- Agent can only **IMPLEMENT** rules when user explicitly directs
- All suggestions are logged for future reference
- User maintains full control over Hazel configuration

## Hazel Rule Format Reference

For user's manual implementation:

```
Rule Name: [Name]
Folder: [Path to watch]
Conditions:
  - [Condition 1]
  - [Condition 2]
Actions:
  - [Action 1]
  - [Action 2]
```

## Logging Suggestions

All suggestions logged to reliability-log.md:

```markdown
## Hazel Rule Suggestions Log

| Date | Pattern | Suggested Rule | Status |
|------|---------|----------------|--------|
| 2025-12-20 | Invoices to Finance | Auto-organize Invoices | Saved for reference |
```
