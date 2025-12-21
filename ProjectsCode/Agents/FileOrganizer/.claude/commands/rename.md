---
description: Rename files using the standard naming convention
---

# Rename Files

Rename one or more files to follow the naming convention.

## Usage

```
/rename [file_path]
/rename ~/Downloads/invoice.pdf
/rename ~/Documents/*.pdf --date 2025-12-01
/rename "~/Downloads/Acme Invoice.pdf"
```

## Process

1. **Read the file(s)** - Understand current name, check if exists
2. **Analyze current name** - What information is present?
3. **Extract/infer components:**
   - **Date:** From filename, metadata, or ask user
   - **Entity:** From filename content or ask user
   - **Category:** Infer from content/context or ask user
   - **Type:** From document content or extension
4. **Propose new name** - Using naming convention
5. **Check for conflicts** - Ensure no duplicate at location
6. **Wait for approval**
7. **Execute rename** - Use `mv` command
8. **Log action** - Update action-log.md

## Naming Convention

**Format:** `YYYY-MM-DD - Entity Name - Category - Type.ext`

### Component Guidelines

| Component | Guidelines |
|-----------|------------|
| Date | Use document date, not download date when possible |
| Entity | Company name, person name, or source (IRS, Bank, etc.) |
| Category | One of the 9 domains or Reference/Media/Archive |
| Type | Invoice, Statement, Contract, Receipt, Report, Form, etc. |

## Examples

### Input → Output

| Original | Renamed |
|----------|---------|
| `invoice_acme.pdf` | `2025-12-20 - Acme Corp - Finance - Invoice.pdf` |
| `tax_1099.pdf` | `2025-01-31 - IRS - Tax - Form 1099.pdf` |
| `lab_results.pdf` | `2025-12-15 - Quest Diagnostics - Medical - Lab Results.pdf` |
| `nara_report.pdf` | `2025-12-10 - School - Family - Report Card.pdf` |

## Output Format

```
## Rename Proposal

**File:** [original path]
**Current name:** [current]
**Proposed name:** [new name]

### Components Identified
- **Date:** [YYYY-MM-DD] (source: [filename/metadata/inferred])
- **Entity:** [name] (source: [filename/inferred])
- **Category:** [category]
- **Type:** [type]

**Awaiting your approval.**
Reply: "proceed", "proceed with [changes]", or "cancel"
```

## Handling Ambiguity

If any component is unclear:
1. Present what you know
2. Ask user to clarify specific component
3. Suggest options when possible

Example:
```
I can identify:
- Date: 2025-12-20 (from file modification date)
- Type: Invoice (from filename)

But I'm unsure about:
- Entity: Is this from "Acme" or "Acme Corporation"?
- Category: Should this be Finance or VerifiedMetrics (work)?

Please clarify, or I can use: "2025-12-20 - Acme - Finance - Invoice.pdf"
```
