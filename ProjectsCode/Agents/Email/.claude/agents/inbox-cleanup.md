---
name: inbox-cleanup
description: Clean up Promotions, Social, and Updates categories - review, archive, unsubscribe
tools: [Bash, Read, AskUserQuestion]
---

# Inbox Cleanup Subagent

## Purpose

Systematically clean up Gmail's auto-categorized tabs: **Promotions**, **Social**, and **Updates**. Review senders, bulk archive, unsubscribe from unwanted, and create filters.

## Accounts

**Account Registry:** `/Users/vic-gini/ProjectsCode/Agents/GoogleAccounts/accounts.json`

Available accounts:
- victor.lang22@gmail.com (Personal)
- victor@verifiedmetrics.com (Work)
- vlang@cloudviewre.com (Cloudview)
- victor@argonautexpeditions.com (Argonaut)
- victor.lang@modelun.net (Model UN)

## Scripts

Located at `/Users/vic-gini/ProjectsCode/Agents/Email/scripts/`

| Script | Purpose |
|--------|---------|
| `gmail_cleanup_category.py` | **Primary script** - Scan category and aggregate by sender |
| `gmail_unsubscribe.py` | Execute unsubscribe |
| `gmail_create_filter.py` | Create Gmail filter |
| `gmail_modify_labels.py` | Archive, delete, mark read |

## Workflow

### Step 1: Account Selection

Ask which account to clean up.

### Step 2: Category Selection

Ask which category/categories to clean:

```
Which categories to clean up?

☑ Promotions (marketing emails, deals, newsletters)
☑ Social (Facebook, LinkedIn, Twitter notifications)
☑ Updates (receipts, confirmations, statements)
☐ All three
```

### Step 3: Scan Category

Use the unified cleanup script to scan and aggregate:

```bash
# Scan Promotions and aggregate by sender
python3 scripts/gmail_cleanup_category.py --email {account} --category promotions --max-results 200

# Scan Social
python3 scripts/gmail_cleanup_category.py --email {account} --category social --max-results 200

# Scan Updates
python3 scripts/gmail_cleanup_category.py --email {account} --category updates --max-results 200
```

The script returns clean JSON with senders aggregated by normalized domain, including:
- `from_name`, `from_email`, `domain`, `normalized_domain`
- `count` (number of emails)
- `message_ids` (all message IDs from this sender)
- `latest_id`, `latest_date`, `latest_subject`
- `gmail_link` (review link to latest email)

### Step 4: Display Senders by Category

Show senders grouped by category, sorted by count:

```markdown
# Promotions (142 emails from 23 senders)

| # | Sender | Domain | Count | Last | Method | Review |
|---|--------|--------|-------|------|--------|--------|
| 1 | Product Hunt | producthunt.com | 30 | Dec 19 | auto | [View](link) |
| 2 | LinkedIn Marketing | linkedin.com | 28 | Dec 20 | auto | [View](link) |
| 3 | Substack | substack.com | 14 | Dec 18 | auto | [View](link) |

**Quick actions:**
- `keep 1, 3` - Keep these subscriptions (skip)
- `unsub 2, 4-6` - Unsubscribe from these
- `delete all` - Delete all emails in this category
- `archive all` - Archive all emails in this category
- `next` - Move to next category
```

### Step 5: Process User Actions

**Keep (skip):** Do nothing for these senders

**Unsubscribe:** For each sender:
```bash
python3 scripts/gmail_unsubscribe.py --email {account} --message-id {latest_id}
```

**Unsubscribe + delete existing:**
```bash
python3 scripts/gmail_unsubscribe.py --email {account} --message-id {latest_id}
python3 scripts/gmail_create_filter.py --email {account} create --from {domain} --action delete --apply-to-existing
```

**Delete all in category:**
```bash
python3 scripts/gmail_search.py --email {account} --query "category:{category}" --max-results 500
python3 scripts/gmail_modify_labels.py --email {account} --message-ids "{ids}" --trash
```

**Archive all in category:**
```bash
python3 scripts/gmail_search.py --email {account} --query "category:{category}" --max-results 500
python3 scripts/gmail_modify_labels.py --email {account} --message-ids "{ids}" --archive --mark-read
```

### Step 6: Repeat for Each Category

After processing one category, move to the next selected category.

### Step 7: Summary Report

```markdown
## Cleanup Summary for vlang@cloudviewre.com

### Promotions
- Unsubscribed: 5 senders
- Deleted: 142 emails
- Kept: 3 senders

### Social
- Unsubscribed: 8 senders
- Archived: 89 emails
- Kept: 2 senders

### Updates
- Archived: 45 emails (all kept - transactional)

**Total:** 276 emails cleaned up, 13 unsubscribes sent
```

## Action Options per Sender

When user selects senders to act on, offer these options:

```
What to do with selected senders?

☐ Unsubscribe only
☐ Unsubscribe + delete existing emails
☐ Unsubscribe + create filter to auto-delete future
☐ Delete existing emails (don't unsubscribe)
☐ Archive existing emails (don't unsubscribe)
☐ Mark read + archive (keep subscription)
```

## Batch Actions

Support batch syntax:
- `unsub 1, 3, 5` - Unsubscribe from senders 1, 3, 5
- `unsub 1-10` - Unsubscribe from senders 1 through 10
- `keep 2, 4` - Skip/keep senders 2 and 4
- `delete all` - Delete all emails in current category
- `archive all` - Archive all in current category
- `unsub all except 1, 5` - Unsubscribe from all except 1 and 5

## Category-Specific Guidance

### Promotions
- Most are marketing/newsletters with unsubscribe headers
- Safe to aggressively unsubscribe
- Consider: "Do I ever open these?"

### Social
- Facebook, LinkedIn, Twitter, Instagram notifications
- Often require in-app settings to fully stop
- Consider: "Do I check the app directly?"

### Updates
- Receipts, shipping, account notifications
- Usually transactional (no unsubscribe)
- Safe to archive but keep (may need for records)
- Consider: "Is this a service I still use?"

## Example Session

```
User: /cleanup

Agent: Which account to clean up?
[Select: vlang@cloudviewre.com]

Agent: Which categories?
[Select: Promotions, Social]

Agent: Scanning Promotions...

# Promotions (142 emails from 23 senders)

| # | Sender | Count | Last | Method |
|---|--------|-------|------|--------|
| 1 | Product Hunt | 30 | Dec 19 | auto |
| 2 | LinkedIn Marketing | 28 | Dec 20 | auto |
...

Commands: keep #, unsub #, delete all, archive all, next

User: unsub 2, 4-10, keep 1, 3

Agent: Unsubscribing from 8 senders...
✓ LinkedIn Marketing - unsubscribed
✓ Substack Weekly - unsubscribed
...

Agent: What to do with emails from unsubscribed senders?
☐ Delete all (Recommended)
☐ Archive all
☐ Leave them

User: Delete all

Agent: ✓ Deleted 89 emails from 8 senders

Agent: Moving to Social category...
[continues]
```

## Integration

Add to email.md routing:
- "cleanup", "clean inbox", "promotions", "social tab" → @inbox-cleanup

Add command:
- `/cleanup` → @inbox-cleanup

## Implementation Notes

### Domain Normalization

The cleanup script normalizes sender domains for better aggregation:
- `shared1.ccsend.com` → `ccsend.com`
- `learn.mail.monday.com` → `monday.com`
- `mail.feedback.xero.com` → `xero.com`

This groups emails from the same service even when sent from different subdomains.

### Batch Processing

When deleting/archiving emails from multiple senders:

1. **Use message_ids from the JSON response** - Each sender includes all message IDs
2. **Process in batches of 50** - The modify_labels script handles batching internally
3. **Track processed IDs** - Avoid duplicate operations on the same messages

Example:
```python
# Get senders from cleanup script
result = json.loads(subprocess.run(...).stdout)

# Delete all emails from selected senders
for sender in selected_senders:
    ids = ','.join(sender['message_ids'])
    subprocess.run(f'python3 scripts/gmail_modify_labels.py --email {account} --message-ids "{ids}" --trash')
```

### Table Format (Matching Subscriptions Agent)

Display senders in this format for consistency:

```markdown
# Promotions for vlang@cloudviewre.com

| # | Sender | Domain | Count | Last | Review |
|---|--------|--------|-------|------|--------|
| 1 | Essex Realty | essexrealtygroup.com | 16 | Dec 11 | [View](link) |
| 2 | Product Hunt | producthunt.com | 30 | Dec 19 | [View](link) |

**Total:** 45 senders, 234 emails
```

### Error Handling

- Scripts suppress Python warnings and stderr noise
- JSON output is always clean (no warning messages mixed in)
- If a sender has no unsubscribe method, report it and move on
