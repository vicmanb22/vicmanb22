# Email

Multi-account email management agent for Gmail.

## Purpose

Unified email agent supporting multiple Gmail accounts with:
- **Digest** - Organized email summaries by category
- **Subscriptions** - View and manage email subscriptions, unsubscribe
- **Cleanup** - Bulk clean Promotions, Social, Updates categories
- **Compose** - Draft and send emails (planned)
- **Manage** - Label/archive operations (planned)

## Architecture

```
Email/
├── CLAUDE.md                 # This file
├── CHANGELOG.md              # Version history
├── scripts/                  # Python scripts for Gmail API
├── templates/                # Account-specific digest templates
└── .claude/
    ├── agents/
    │   ├── email.md          # Main orchestrator
    │   ├── digest.md         # Digest subagent
    │   ├── subscriptions.md  # Subscription manager subagent
    │   └── inbox-cleanup.md  # Promotions/Social/Updates cleanup
    ├── commands/
    │   ├── email.md          # /email command
    │   ├── digest.md         # /digest command
    │   ├── subscriptions.md  # /subscriptions command
    │   └── cleanup.md        # /cleanup command
    └── settings.json         # Bash permissions
```

## Accounts

Accounts are managed by the **GoogleAccounts** agent.

**Registry:** `/Users/vic-gini/ProjectsCode/Agents/GoogleAccounts/accounts.json`

| Template | Accounts |
|----------|----------|
| digest-personal.md | victor.lang22@gmail.com |
| digest-work.md | victor@verifiedmetrics.com |
| digest-default.md | All other accounts |

### Adding a New Account

1. Add account to GoogleAccounts: `/google add`
2. Email agent automatically works with the new account using `digest-default.md`
3. Optionally create custom template later: `templates/digest-{name}.md`

### Credentials

OAuth tokens stored at:
```
~/.google_workspace_mcp/credentials/{email}.json
```

### Re-authentication

If tokens expire:
```bash
# From Email agent:
python3 scripts/reauth.py --email {email}

# Or use GoogleAccounts agent:
/google reauth {email}
```

## Commands

| Command | Description |
|---------|-------------|
| `/email` | Open orchestrator (routing menu) |
| `/digest` | Generate digest (multi-select: all, one, or multiple accounts) |
| `/digest {email}` | Generate digest for specific account |
| `/subscriptions` | Manage email subscriptions (view, unsubscribe, filter) |
| `/subscriptions {email}` | Manage subscriptions for specific account |
| `/cleanup` | Clean up Promotions, Social, Updates categories |
| `/cleanup {email}` | Cleanup for specific account |

## Account Selection

When running `/digest` without specifying an account, you'll see a multi-select menu:
- **All accounts** - Run digests for all known accounts sequentially
- **victor.lang22@gmail.com (Personal)** - Personal Gmail only
- **victor@verifiedmetrics.com (Work)** - Work Gmail only

You can select multiple individual accounts to run digests for each.

## Scripts

| Script | Purpose |
|--------|---------|
| `auth.py` | OAuth token loading/refresh |
| `reauth.py` | Browser-based re-authentication |
| `gmail_search.py` | Search messages |
| `gmail_get_message.py` | Get single message |
| `gmail_get_messages_batch.py` | Batch fetch (max 100) |
| `gmail_get_thread.py` | Get thread content |
| `gmail_list_labels.py` | List labels |
| `gmail_get_known_contacts.py` | Extract sent recipients |
| `gmail_modify_labels.py` | Mark read/unread, star, archive, trash |
| `gmail_send_message.py` | Send emails |
| `gmail_create_draft.py` | Create/manage drafts |
| `gmail_list_subscriptions.py` | Scan and aggregate subscriptions by sender |
| `gmail_unsubscribe.py` | Unsubscribe via RFC 8058, mailto, or body link |
| `gmail_create_filter.py` | Create Gmail filters for senders |
| `gmail_cleanup_category.py` | Scan Promotions/Social/Updates and aggregate by sender |
| `utils.py` | Shared utilities |

## Digest Formats

Two table formats available for digests:

### Complete Format (Default)
10 columns with LLM-enriched data:
```
| # | Date | Time Ago | From | Company | To | Subject | Domain | Summary | Status |
|---|------|----------|------|---------|-----|---------|--------|---------|--------|
| 1 | Dec 20 | 2h ago | John Smith | CBIZ | victor@ | Q4 Report | Work | Sales report with action items. | [Unread] |
```

### Light Format
6 columns for quick scanning:
```
| # | Date | Time Ago | From | Subject | Status |
|---|------|----------|------|---------|--------|
| 1 | Dec 20 | 2h ago | John Smith | Q4 Report | [Unread] |
```

**Sequential Numbering:**
- `#` column contains sequential number for each email
- Numbers are sequential across entire digest (not per-category)
- Used for action references (e.g., "done 3", "view 5")

**Time Ago Format:**
- `< 1 hour` → `Xm ago` (e.g., "15m ago", "45m ago")
- `≥ 1 hour` → `Xh ago` (e.g., "2h ago", "5h ago")
- `≥ 1 day` → `Xd ago` (e.g., "1d ago", "3d ago")

**Complete format additional columns:**
- **Company**: Extracted from email domain or signature
- **To**: Recipient address
- **Domain**: Life domain classification (from Planning module):
  - Work: Verified Metrics, Argonaut Expeditions, IDEA/CIMUN, Cloudview Real Estate
  - Personal: Family, Life and Fun
  - Foundation: Recovery, Personal Finance, Organization
- **Summary**: LLM-generated 2-sentence summary (max 120 chars)

## Actions

After each digest, available actions are displayed:

### Basic Actions
| Action | Description |
|--------|-------------|
| **view #** | Show full email content |
| **done #** | Mark as read and archive |
| **spam #** | Mark as spam and archive |
| **star #** | Add star to email |
| **reply #** | Draft a reply |
| **subscriptions** | Manage email subscriptions |
| **light format** | Switch to compact 6-column table |

### Full Actions (type "more actions")
archive, mark read, mark unread, unstar, forward, label, delete

### Bulk Actions
- Commas: `done 1, 3, 5`
- Ranges: `mark read 1-5`
- Categories: `spam all unsolicited`

## Subscription Manager

The `/subscriptions` command helps you manage email subscriptions:

### Features
- **View subscriptions** sorted by frequency (most emails first)
- **One-click unsubscribe** via RFC 8058 when available
- **Fallback methods**: mailto, body link parsing, manual
- **Post-unsubscribe options**: archive existing, create filter

### Unsubscribe Methods (in priority order)
1. **RFC 8058 POST** - HTTP POST to List-Unsubscribe header URL
2. **Mailto** - Send email to List-Unsubscribe mailto address
3. **Body link** - GET request to unsubscribe link in email HTML
4. **Manual** - Provide link for user to click

### Usage
```bash
# List all subscriptions
python3 scripts/gmail_list_subscriptions.py --email {account} --days 90

# Unsubscribe (dry-run first)
python3 scripts/gmail_unsubscribe.py --email {account} --message-id {id} --dry-run

# Create filter to auto-delete future emails
python3 scripts/gmail_create_filter.py --email {account} create --from {sender} --action delete
```

### Display Format
```
| # | Sender | Domain | 30d | Total | Last | Method | Review |
|---|--------|--------|-----|-------|------|--------|--------|
| 1 | Product Hunt | producthunt.com | 30 | 90 | Dec 19 | auto | [View](link) |
```

- **30d**: Emails in last 30 days
- **Total**: Total emails in scan period
- **Method**: `auto` (RFC 8058/mailto), `link`, or `manual`
- **Review**: Link to most recent email in Gmail

## Inbox Cleanup

The `/cleanup` command helps you clean up Gmail's auto-categorized tabs:

### Categories
- **Promotions** - Marketing emails, deals, newsletters
- **Social** - Facebook, LinkedIn, Twitter notifications
- **Updates** - Receipts, confirmations, statements

### Features
- **Sender aggregation** by normalized domain
- **Bulk actions**: archive all, delete all, unsubscribe + delete
- **Domain normalization**: Groups `shared1.ccsend.com` → `ccsend.com`
- **Review links**: Click to see latest email from each sender

### Usage
```bash
# Scan Promotions category
python3 scripts/gmail_cleanup_category.py --email {account} --category promotions

# Scan Social category
python3 scripts/gmail_cleanup_category.py --email {account} --category social

# Scan Updates category
python3 scripts/gmail_cleanup_category.py --email {account} --category updates
```

### Display Format
```
| # | Sender | Domain | Count | Last | Review |
|---|--------|--------|-------|------|--------|
| 1 | Product Hunt | producthunt.com | 30 | Dec 19 | [View](link) |
```

### Actions
- `keep #` - Skip these senders
- `unsub #` - Unsubscribe from these senders
- `delete all` - Delete all emails in category
- `archive all` - Archive all emails in category

## Cross-Agent Integration

### Context File

After generating a digest, a context file is written for cross-agent communication:

**Location:** `/tmp/email-digest-context.json`

**Format:**
```json
{
  "account": "victor.lang22@gmail.com",
  "generated": "2025-12-20T10:30:00+08:00",
  "emails": {
    "1": {"id": "19b29806d80e3a92", "subject": "...", "from": "...", "date_iso": "..."},
    "2": {"id": "19b2611d31d58e1f", "subject": "...", "from": "...", "date_iso": "..."}
  }
}
```

**Usage:** Enables Calendar agent to reference emails by digest number and create events.

### Calendar Integration

Use `calendar #` action to create a calendar event from an email:
- "calendar 22" → Creates event from email #22 (extracts date, time, attendees)
- Calendar agent reads context file, fetches email, extracts details, shows preview

## Templates

Templates define category structures for digests:

### Personal (victor.lang22@gmail.com)
1. Attention Required
2. Payments & Receipts
3. Daughter (Nara) Updates
4. Healthcare & Appointments
5. Orders & Shipping

### Work (victor@verifiedmetrics.com)
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

### Default (new accounts)
1. Attention Required
2. Important
3. Transactions
4. Notifications
5. Other

## Integration

Part of MainOrchestrator routing:
- "email", "digest", "inbox" → @email

## Migration Notes

This agent consolidates:
- EmailDigest (personal) - deprecated 2025-12-20
- EmailDigestVM (work) - deprecated 2025-12-20

Both now use Python scripts instead of MCP server.

## MCP Deprecation (2025-12-20)

The Gmail MCP server (`gmail-workspace`) has been fully removed:
- Removed from `~/.claude.json` (ProjectsCode mcpServers)
- Removed from `~/.claude/settings.json` (global permissions)

All Gmail operations now use the Python scripts in `scripts/` which directly call the Gmail API.
