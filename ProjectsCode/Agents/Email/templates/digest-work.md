# Work Email Digest Template

Specialized digest for victor@verifiedmetrics.com (Verified Metrics)

## Account
- **Email:** victor@verifiedmetrics.com
- **Type:** Work
- **Timezone:** Asia/Hong_Kong (HKT, UTC+8)

---

## Important Notes

### Gmail API Workaround
Gmail's `category:primary` filter is unreliable in the API. Instead, exclude unwanted categories explicitly:
```
-category:promotions -category:social -category:updates -category:forums -is:spam
```

### Inbox-Only
Only include emails currently in INBOX (not archived). Add `in:inbox` to all searches.

### Threading
Group emails by Thread ID. Show ONLY the most recent message per thread. Add count: `Subject (15 messages)`

---

## Categories

### Processing Order
Process in this order for deduplication:
1. Starred Emails
2. Sales & Clients
3. Operations & Admin
4. Internal Team
5. Meetings & Recaps
6. Billing & Finance
7. Events & Ecosystem
8. Unsolicited Email
9. Attention Required
10. Other / Uncategorized

### Display Order
Present in this order:
1. Attention Required
2. Starred Emails
3. Sales & Clients
4. Operations & Admin
5. Internal Team
6. Meetings & Recaps
7. Billing & Finance
8. Events & Ecosystem
9. Unsolicited Email
10. Other / Uncategorized

---

## Category Definitions

### 1. Attention Required
**Scope:** 14-day window
**Display Position:** 1

Items needing immediate attention:
- Unread meeting invitations (subject:"Invitation:")
- Unread emails
- Overdue (unread 3+ days)
- Needs response from known contacts

**Exclude:**
- "Accepted:" or "Canceled" in subject → Meetings & Recaps
- Spam moderator reports → Internal Team
- Already categorized as Unsolicited Email

**Search:**
```
in:inbox -category:promotions -category:social -category:updates -category:forums -is:spam newer_than:14d is:unread
```

---

### 2. Starred Emails
**Scope:** All time
**Display Position:** 2

All starred emails regardless of date.

**Search:**
```
in:inbox -category:promotions -category:social -category:updates -category:forums -is:spam is:starred
```

---

### 3. Sales & Clients
**Scope:** All time
**Display Position:** 3

Prospect and client communications.

**Key Contacts:**
- CBIZ
- Exbo Group
- Money Forward
- Pershing Ventures
- Nexa

**Keywords:** pilot, demo, engagement

**Search:**
```
in:inbox -category:promotions -category:social -category:updates -category:forums -is:spam (from:cbiz OR from:exbogroup OR from:moneyforward OR from:pershingventures OR from:nexa OR subject:pilot OR subject:demo OR subject:engagement)
```

**Note:** Check BEFORE Internal Team to capture sales emails from @verifiedmetrics.com

---

### 4. Operations & Admin
**Scope:** All time
**Display Position:** 4

Corporate and administrative matters.

**Keywords:**
- Share transfer
- Governance
- Corporate
- Legal
- Compliance
- ROM filings
- Registration
- Incorporation

**Search:**
```
in:inbox -category:promotions -category:social -category:updates -category:forums -is:spam (subject:"share transfer" OR subject:governance OR subject:corporate OR subject:legal OR subject:compliance OR subject:ROM OR subject:registration OR subject:incorporation)
```

---

### 5. Internal Team
**Scope:** All time
**Display Position:** 5

Team communications.

**Sources:**
- @verifiedmetrics.com colleagues
- Spam moderator reports (noreply-spamdigest)

**Exclude:** Already in Sales & Clients, Operations & Admin, or Meetings & Recaps

**Search:**
```
in:inbox -category:promotions -category:social -category:updates -category:forums -is:spam (from:@verifiedmetrics.com OR from:noreply-spamdigest)
```

---

### 6. Meetings & Recaps
**Scope:** All time
**Display Position:** 6

Meeting-related emails.

**Sources:**
- Fireflies.ai transcripts (from:fireflies.ai)
- Gemini meeting notes
- Accepted meeting invites (subject:"Accepted:")
- Canceled meetings (subject:"Canceled")
- Calendar event updates

**Search:**
```
in:inbox -category:promotions -category:social -category:updates -category:forums -is:spam (from:fireflies.ai OR from:gemini OR subject:"Accepted:" OR subject:"Canceled" OR subject:"meeting recap" OR subject:"meeting notes")
```

---

### 7. Billing & Finance
**Scope:** All time
**Display Position:** 7

Financial communications.

**Sources:**
- AWS billing
- Plaid invoices
- Payment requests
- accounting@verifiedmetrics.com

**Search:**
```
in:inbox -category:promotions -category:social -category:updates -category:forums -is:spam (invoice OR billing OR payment OR from:aws OR from:plaid OR from:accounting@verifiedmetrics.com)
```

---

### 8. Events & Ecosystem
**Scope:** All time
**Display Position:** 8

Industry and startup ecosystem.

**Sources:**
- Cyberport (YSIP, programs)
- HKICTA
- Industry events and conferences

**Search:**
```
in:inbox -category:promotions -category:social -category:updates -category:forums -is:spam (from:cyberport OR from:hkicta OR subject:YSIP OR subject:startup OR subject:event OR subject:conference)
```

---

### 9. Unsolicited Email
**Scope:** All time
**Display Position:** 9

Cold outreach and marketing.

**Patterns:**
- Partnership pitches
- Opportunity introductions
- "Reaching out"
- "Touch base"
- "Quick question"

**Search:**
```
in:inbox -category:promotions -category:social -category:updates -category:forums -is:spam (subject:partnership OR subject:opportunity OR subject:introduce OR "reaching out" OR "touch base" OR "quick question")
```

---

### 10. Other / Uncategorized
**Scope:** All time
**Display Position:** 10

Catch-all for remaining inbox emails not matching above categories.

**Search:**
```
in:inbox -category:promotions -category:social -category:updates -category:forums -is:spam
```
Then filter out emails already categorized.

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
| 1 | Dec 20 | 2h ago | John Smith | CBIZ | victor@ | [Q4 Report (3)](https://mail.google.com/mail/u/0/#inbox/{messageId}) | Verified Metrics | Sales report with revenue numbers. Action needed on budget. | [Unread] |
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
- **Company**: Organization from email domain or LLM-detected from signature
- **To**: Recipient (Victor, Team, specific person)
- **Domain**: Life domain classification (LLM-detected):
  - `Verified Metrics` - Core work, product, clients
  - `Argonaut Expeditions` - Side venture
  - `IDEA/CIMUN` - Nonprofit work
  - `Cloudview Real Estate` - Real estate matters
  - `Personal Finance` - Billing, invoices
  - `Organization` - Admin, operations
  - `Other` - Default
- **Summary**: LLM-generated 2-sentence summary (max 120 chars)

### Full Output Structure

```markdown
# Email Digest - Work
**Account:** victor@verifiedmetrics.com
**Period:** {start_date} - {end_date}
**Generated:** {timestamp} HKT
**Format:** Light | Complete

## Quick Stats
| Category | Count | Unread |
|----------|-------|--------|
| Attention Required | X | X |
| Starred Emails | X | X |
| Sales & Clients | X | X |
| Operations & Admin | X | X |
| Internal Team | X | X |
| Meetings & Recaps | X | X |
| Billing & Finance | X | X |
| Events & Ecosystem | X | X |
| Unsolicited Email | X | X |
| Other / Uncategorized | X | X |

**Total:** X emails | **Unread:** X

---

## 1. Attention Required

### Needs Response
[Table in selected format]

### Overdue (Unread 3+ days)
[Table in selected format]

### Other Unread
[Table in selected format]

---

## 2. Starred Emails
[Table in selected format]

...
```

---

## Column Guidelines

### To Column (Complete format)
- Victor in To, others CC'd → "Victor"
- Team address (sales@, support@) → "Sales Team", "Support Team"
- Multiple recipients, clear addressee → that person
- Broadcast/announcement → "Team" or "All"
- Check email opening ("Hi Victor," vs "Hi team,")

---

## Deduplication

- Each email in ONE category only
- Priority order: Starred > Sales > Operations > Internal > Meetings > Billing > Events > Unsolicited > Attention > Other
- First match wins
