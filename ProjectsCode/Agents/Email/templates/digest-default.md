# Default Email Digest Template

Generic digest format for any Gmail account.

## Categories

### 1. Attention Required
**Priority:** Highest
**Scope:** 14 days

Items needing immediate attention:
- **Starred** - Flagged as important
- **Overdue** - Unread for 3+ days
- **Needs Response** - From known contacts with questions/requests

**Searches:**
```
is:starred newer_than:14d
older_than:3d newer_than:14d is:unread
```

### 2. Important
**Priority:** High
**Scope:** 14 days

Emails from people you've corresponded with:
- From known contacts (based on Sent folder scan)
- Excludes automated senders

**Detection:**
- Scan Sent folder (90 days) for known contacts
- Search for emails from those contacts

### 3. Transactions
**Priority:** Medium
**Scope:** 14 days

Financial and commerce emails:
- Receipts and confirmations
- Payment notifications
- Invoices and billing
- Order confirmations

**Search:**
```
newer_than:14d (receipt OR payment OR invoice OR "order confirmation" OR billing)
```

### 4. Notifications
**Priority:** Low
**Scope:** 14 days

Automated updates and alerts:
- System notifications
- Service alerts
- Automated reports
- Newsletter-style content in Primary

**Search:**
```
newer_than:14d (from:noreply OR from:no-reply OR from:notifications OR from:alerts)
```

### 5. Other
**Priority:** Lowest
**Scope:** 14 days

Catch-all for remaining Primary inbox emails not matching above categories.

---

## Output Format

### Table Formats

Two formats available - Complete (default) and Light:

#### Light Format
6 columns for quick scanning:
```
| # | Date | Time Ago | From | Subject | Status |
|---|------|----------|------|---------|--------|
| 1 | Dec 20 | 2h ago | John Smith | [Q4 Report](https://mail.google.com/mail/u/0/#inbox/{messageId}) | [Unread] |
```

#### Complete Format (Default)
10 columns with LLM-enriched data:
```
| # | Date | Time Ago | From | Company | To | Subject | Domain | Summary | Status |
|---|------|----------|------|---------|-----|---------|--------|---------|--------|
| 1 | Dec 20 | 2h ago | John Smith | Acme Inc | user@ | [Q4 Report](https://mail.google.com/mail/u/0/#inbox/{messageId}) | Work | Quarterly report with action items. | [Unread] |
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
- **Company**: Extracted from email domain or signature (LLM-detected)
- **To**: Recipient address
- **Domain**: Life domain classification:
  - Work: `Verified Metrics`, `Argonaut Expeditions`, `IDEA/CIMUN`, `Cloudview Real Estate`
  - Personal: `Family`, `Life and Fun`
  - Foundation: `Recovery`, `Personal Finance`, `Organization`
  - Default: `Other`
- **Summary**: LLM-generated 2-sentence summary (max 120 chars)

### Full Output Structure

```markdown
# Email Digest - {account}
**Period:** {start_date} - {end_date}
**Generated:** {timestamp}
**Format:** Light | Complete

## Quick Stats
| Category | Count | Unread |
|----------|-------|--------|
| Attention Required | X | X |
| Important | X | X |
| Transactions | X | X |
| Notifications | X | X |
| Other | X | X |

**Total:** X emails | **Unread:** X

---

## 1. Attention Required
[Table in selected format]

## 2. Important
...
```

---

## Deduplication

- Each email appears in ONE category only
- Priority order: Attention Required > Important > Transactions > Notifications > Other
- First match wins

## Inbox Filtering

All searches include:
```
-category:promotions -category:social -category:updates -category:forums -is:spam
```
