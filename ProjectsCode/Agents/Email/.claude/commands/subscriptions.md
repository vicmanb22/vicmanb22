# Subscription Manager Command

Manage email subscriptions - view, unsubscribe, and filter.

**Usage:**
- `/subscriptions` - Prompts for account selection
- `/subscriptions {email}` - Manage subscriptions for specific account
- `/subscriptions all` - Scan all accounts

Use @subscriptions subagent with the selected account(s).

**Accounts:** Read from `/Users/vic-gini/ProjectsCode/Agents/GoogleAccounts/accounts.json`

**Features:**
- View subscriptions sorted by frequency (most emails first)
- One-click unsubscribe via RFC 8058 when available
- Fallback to mailto or body link parsing
- Optional: archive existing emails from sender
- Optional: create filter to auto-delete future emails

**Options:**
- `--days N` - Scan period (default: 90)
- `--min-count N` - Only show senders with N+ emails (default: 2)
