# File Naming Conventions

## Standard Format

```
YYYY-MM-DD - Entity Name - Category - Type.ext
```

## Components

### 1. Date (YYYY-MM-DD)

**Format:** ISO 8601 date format
**Purpose:** Enables chronological sorting when files are listed alphabetically

| Source Priority | When to Use |
|-----------------|-------------|
| Document date | Date on the document itself (invoice date, statement date) |
| Receipt date | When document was received |
| Creation date | File metadata creation date |
| Modification date | Last resort |

**Examples:**
- `2025-12-20` - December 20, 2025
- `2025-01-15` - January 15, 2025

### 2. Entity Name

**Purpose:** Identifies the source, sender, or subject of the document

| Type | Examples |
|------|----------|
| Company | Acme Corp, Chase Bank, Amazon |
| Government | IRS, DMV, SSA |
| Person | Dr. Smith, John Doe |
| Institution | Stanford, Quest Diagnostics |
| Family | Nara, Family |

**Guidelines:**
- Use consistent spelling across all files
- Use official company names (not abbreviations unless standard)
- For personal files, use first name or "Family"

### 3. Category

**Purpose:** Maps to one of the 9 life domains (or additional categories)

| Domain | Tag | Use For |
|--------|-----|---------|
| VerifiedMetrics | Work | VM company files |
| ArgonautExpeditions | Work | Argonaut business |
| IDEACIMUN | Work | Education/conference |
| CloudviewRealEstate | Work | Real estate business |
| Family | Personal | Family documents |
| PersonalFinance | Personal | Banking, taxes, investments |
| Recovery | Personal | Therapy, health |
| LifeAndFun | Personal | Hobbies, entertainment |
| OrganizationRoutinesMaintenance | Personal | Admin, household |
| Reference | Additional | Manuals, guides |
| Media | Additional | Photos, videos |
| Archive | Additional | Historical files |

**Short Forms for Filenames:**
- Finance (for PersonalFinance)
- Medical (for Recovery health docs)
- Tax (for tax-specific finance)
- Work (generic work if not domain-specific)

### 4. Type

**Purpose:** Identifies the document type

| Type | Examples |
|------|----------|
| Invoice | Bills, invoices to pay |
| Receipt | Proof of payment |
| Statement | Bank/credit card statements |
| Contract | Legal agreements |
| Report | Analysis, reports |
| Form | Government/official forms |
| Letter | Correspondence |
| Photo | Images |
| Certificate | Diplomas, certifications |
| Manual | Product manuals |
| Guide | How-to guides |

## Complete Examples

| Original | Properly Named |
|----------|----------------|
| acme_invoice.pdf | 2025-12-20 - Acme Corp - Finance - Invoice.pdf |
| chase_dec_statement.pdf | 2025-12-31 - Chase Bank - Finance - Statement.pdf |
| 1099_2024.pdf | 2024-01-31 - IRS - Tax - Form 1099.pdf |
| dr_smith_results.pdf | 2025-12-15 - Dr Smith - Medical - Lab Results.pdf |
| nara_report_card.pdf | 2025-12-10 - School - Family - Report Card.pdf |
| amazon_order.pdf | 2025-12-18 - Amazon - Personal - Receipt.pdf |
| vm_client_contract.pdf | 2025-12-01 - ClientName - VerifiedMetrics - Contract.pdf |
| IMG_4521.jpg | 2025-12-20 - Family - Personal - Photo.jpg |

## Special Cases

### Multiple Documents Same Day
Add time or sequence:
- `2025-12-20 - Acme - Finance - Invoice.pdf`
- `2025-12-20 - Globex - Finance - Invoice.pdf`
(Different entities, no conflict)

If same entity, same type:
- `2025-12-20 - Acme - Finance - Invoice 1.pdf`
- `2025-12-20 - Acme - Finance - Invoice 2.pdf`

### Unknown Entity
Use source or leave placeholder:
- `2025-12-20 - Unknown - Finance - Receipt.pdf`
- Move to NeedsReview for later classification

### Multi-Category Documents
Use primary category:
- A work invoice is `VerifiedMetrics`, not `Finance`
- A family medical document is `Family`, not `Recovery`

### Media Files
For photos/videos, entity can be event or subject:
- `2025-12-25 - Christmas - Family - Photo.jpg`
- `2025-12-20 - Nara - Family - Video.mp4`
- `2025-12-15 - Office - VerifiedMetrics - Photo.jpg`

## Anti-patterns to Avoid

| Bad | Why | Good |
|-----|-----|------|
| `invoice.pdf` | No date, entity, or context | `2025-12-20 - Acme - Finance - Invoice.pdf` |
| `12-20-2025 - ...` | Wrong date format | `2025-12-20 - ...` |
| `2025-12-20 - invoice.pdf` | Missing entity and category | Full format |
| `2025-12-20 - Acme Corp.pdf` | Missing category and type | Full format |
| `final_final_v2.pdf` | Version chaos | Use date, delete old versions |
