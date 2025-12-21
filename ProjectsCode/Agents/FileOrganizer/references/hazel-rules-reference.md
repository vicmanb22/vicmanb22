# Hazel Rules Reference

## Overview

Hazel is a macOS automation app that watches folders and applies rules automatically. FileOrganizer works alongside Hazel:
- Hazel handles automatic, rule-based organization
- FileOrganizer handles complex decisions Hazel cannot make
- FileOrganizer suggests Hazel rules for repetitive patterns

## Hazel Basics

### Rule Structure

```
Rule Name: [Descriptive name]
Folder: [Folder to watch]
Conditions:
  - [Condition 1]
  - [Condition 2]
Actions:
  - [Action 1]
  - [Action 2]
```

### Common Conditions

| Condition | Example |
|-----------|---------|
| Kind | Kind is PDF |
| Name | Name contains "invoice" |
| Extension | Extension is pdf |
| Date Added | Date Added is in the last 1 day |
| Contents | Contents contain "tax" |
| Size | Size is greater than 10 MB |

### Common Actions

| Action | Example |
|--------|---------|
| Move | Move to folder ~/Documents/Finance/ |
| Rename | Rename with pattern... |
| Tag | Add tag "Processed" |
| Delete | Move to Trash |
| Sort into subfolder | Sort into subfolder based on date |

## Suggested Rules Log

Rules suggested by FileOrganizer but not yet implemented.

### Pending Suggestions

| Date | Pattern | Suggested Rule | Status |
|------|---------|----------------|--------|
| | | | |

### Implemented Rules

| Date | Rule Name | Watch Folder | Notes |
|------|-----------|--------------|-------|
| | | | |

---

## Template Rules

### Template: Auto-organize Invoices

**Watch Folder:** ~/Downloads

**Conditions:**
- Kind is PDF
- Name contains "invoice" (case insensitive)

**Actions:**
1. Rename with pattern:
   - Date Added → YYYY-MM-DD
   - Add " - [Entity] - Finance - Invoice"
   - Note: Entity extraction may require manual naming
2. Move to: ~/Documents/Finance/Invoices/

---

### Template: Auto-organize Bank Statements

**Watch Folder:** ~/Downloads

**Conditions:**
- Kind is PDF
- Name contains "statement" OR name contains bank name

**Actions:**
1. Rename with pattern:
   - Date Added → YYYY-MM-DD
   - Add " - [Bank Name] - Finance - Statement"
2. Move to: ~/Documents/Finance/Banking/[Bank Name]/

---

### Template: Auto-stage Old Downloads

**Watch Folder:** ~/Downloads

**Conditions:**
- Date Added is not in the last 30 days
- NOT Kind is Application

**Actions:**
1. Move to: ~/ToDelete/[current month]/

**Notes:** This auto-stages old downloads for review.

---

### Template: Auto-organize Screenshots

**Watch Folder:** ~/Desktop

**Conditions:**
- Name starts with "Screenshot"
- Kind is Image

**Actions:**
1. Rename with pattern:
   - Use creation date → YYYY-MM-DD
   - Remove "Screenshot " prefix
   - Add " - Screenshot"
2. Move to: ~/Pictures/Screenshots/[Year]-[Month]/

---

### Template: Sort Photos by Date

**Watch Folder:** ~/Pictures/Imports

**Conditions:**
- Kind is Image
- Extension is jpg, jpeg, png, heic

**Actions:**
1. Sort into subfolder based on:
   - Date created → Year/Month format
2. Move to: ~/Pictures/[Year]/[Month]/

---

## Hazel + FileOrganizer Workflow

### Division of Labor

| Task | Handled By |
|------|------------|
| Simple pattern matching (invoices, statements) | Hazel |
| Complex categorization decisions | FileOrganizer |
| Date extraction from filenames | Hazel (simple) / FileOrganizer (complex) |
| Entity identification | FileOrganizer |
| Deletion decisions | FileOrganizer (staging only) |
| Ambiguous files | FileOrganizer |

### When to Use Hazel vs FileOrganizer

**Use Hazel when:**
- Pattern is simple and consistent
- No human judgment needed
- Rule has been proven reliable 3+ times

**Use FileOrganizer when:**
- File needs context analysis
- Entity must be identified from content
- Category is ambiguous
- Deletion decision required

## Adding New Rules

1. Detect pattern via `/suggest-hazel`
2. Document rule in this file under "Pending Suggestions"
3. When ready, manually create in Hazel app
4. Move to "Implemented Rules" section
5. Test with sample files

## Hazel App Location

Hazel preferences: System Preferences → Hazel
Or: Hazel app in menu bar → Preferences

---

## Notes

- Hazel rules are stored in Hazel's preferences
- Export/import via Hazel app for backup
- Test rules with "Run Rules Now" before enabling
