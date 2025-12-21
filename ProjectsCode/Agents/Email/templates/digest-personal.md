# Personal Email Digest Template

Specialized digest for victor.lang22@gmail.com

## Account
- **Email:** victor.lang22@gmail.com
- **Type:** Personal
- **Timezone:** Auto-detect (default: Asia/Hong_Kong)

---

## Categories

### 1. Attention Required
**Priority:** Highest
**Scope:** 14 days

Items needing immediate attention:

#### Needs Response
Emails from known contacts requiring a reply:
- Contains questions directed at you
- Requests action or information
- Has unanswered thread
- Mentions deadlines

**Detection:**
1. Scan Sent folder (90 days) for known contacts
2. Search for emails from those contacts
3. Analyze for response indicators

**Exclude:** noreply@, no-reply@, notifications@, alerts@, automated senders

#### Starred
```
is:starred newer_than:14d
```

#### Overdue
Unread for 3+ days:
```
older_than:3d newer_than:14d is:unread
```

---

### 2. Payments & Receipts
**Priority:** High
**Scope:** 14 days

Financial transactions:
- Payment confirmations
- Receipts from purchases
- Billing statements
- Invoice notifications

**Search:**
```
newer_than:14d (receipt OR payment OR invoice OR "order confirmation" OR "payment received" OR billing)
```

---

### 3. Daughter (Nara) Updates
**Priority:** High
**Scope:** 14 days

School and child-related:

**Seesaw:**
```
from:seesaw
```

**Schools:**
- HKIS (Hong Kong International School)
- CIS (Chinese International School)
- PIPS (Peak Independent Preschool)
- ESF (English Schools Foundation)

**Search:**
```
newer_than:14d (from:seesaw OR from:hkis OR from:cis OR from:pips OR from:esf OR subject:nara OR admissions)
```

---

### 4. Healthcare & Appointments
**Priority:** Medium
**Scope:** 14 days

Medical and therapy:

**Providers:**
- Freudly
- Spruce
- Erica Liu Woolin
- Sheena Karnani

**Search:**
```
newer_than:14d (from:freudly OR from:spruce OR from:woolin OR from:karnani OR appointment OR psychologist OR therapy)
```

---

### 5. Orders & Shipping
**Priority:** Low
**Scope:** 14 days

E-commerce tracking:
- Order confirmations
- Shipping notifications
- Delivery updates
- Tracking numbers

**Search:**
```
newer_than:14d (subject:shipped OR subject:delivery OR "tracking number" OR "out for delivery" OR "order confirmed")
```

---

## Output Format

### Table Formats

Two formats available - Complete (default) and Light:

#### Light Format
6 columns for quick scanning:
```
| # | Date | Time Ago | From | Subject | Status |
|---|------|----------|------|---------|--------|
| 1 | Dec 20 | 2h ago | HKIS | [School Update](https://mail.google.com/mail/u/0/#inbox/{messageId}) | [Unread] |
```

#### Complete Format (Default)
10 columns with LLM-enriched data:
```
| # | Date | Time Ago | From | Company | To | Subject | Domain | Summary | Status |
|---|------|----------|------|---------|-----|---------|--------|---------|--------|
| 1 | Dec 20 | 2h ago | HKIS Admin | HKIS | victor@ | [School Update](https://mail.google.com/mail/u/0/#inbox/{messageId}) | Family | Winter break schedule announced. Pick-up at 12pm Dec 20. | [Unread] |
```

**Gmail Links:**
- Subject column contains clickable Gmail link
- Format: `[Subject Text](https://mail.google.com/mail/u/0/#inbox/{messageId})`
- Requires being logged into Gmail in the browser

**Sequential Numbering:**
- `#` column contains sequential number for each email
- Numbers are sequential across entire digest (not per-category)
- Used for action references (e.g., "archive 3")

**Complete Format - Additional Columns:**
- **Company**: School, healthcare provider, or merchant name
- **To**: Recipient address
- **Domain**: Life domain classification:
  - `Family` - Daughter/school related
  - `Personal Finance` - Payments, receipts
  - `Recovery` - Healthcare, therapy
  - `Life and Fun` - Personal, hobbies
  - `Organization` - Appointments, scheduling
  - `Other` - Default
- **Summary**: LLM-generated 2-sentence summary (max 120 chars)

### Full Output Structure

```markdown
# Email Digest - Personal
**Account:** victor.lang22@gmail.com
**Period:** {start_date} - {end_date}
**Generated:** {timestamp}
**Format:** Light | Complete

## Quick Stats
| Category | Count | Unread |
|----------|-------|--------|
| Attention Required | X | X |
| Payments & Receipts | X | X |
| Daughter (Nara) | X | X |
| Healthcare | X | X |
| Orders & Shipping | X | X |

**Total:** X emails | **Unread:** X

---

## 1. Attention Required

### Needs Response
[Table in selected format]

### Starred
[Table in selected format]

### Overdue (Unread 3+ days)
[Table in selected format]

---

## 2. Payments & Receipts
[Table in selected format]

...
```

---

## Deduplication

- Each email appears in ONE category only
- Priority order: Attention Required > Payments > Daughter > Healthcare > Orders
- First match wins

## Status Column

- `[Unread]` for unread emails
- Blank for read emails
