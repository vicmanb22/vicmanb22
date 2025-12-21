---
description: Manage Google account authentication
---

# /google Command

Manage Google OAuth accounts used by Email and Calendar agents.

## Usage

- `/google` - Show all accounts and their status
- `/google list` - List all registered accounts
- `/google status` - Check token validity for all accounts
- `/google reauth {email}` - Re-authenticate an account
- `/google add` - Add a new account (guided flow)

## Process

### Default (no arguments or "list"):

1. Read accounts from `/Users/vic-gini/ProjectsCode/Agents/GoogleAccounts/accounts.json`
2. For each account, check credentials status
3. Display table:

```
## Google Accounts

| Email | Type | Label | Status |
|-------|------|-------|--------|
| victor.lang22@gmail.com | personal | Personal Gmail | Valid |
| victor@verifiedmetrics.com | work | Verified Metrics | Valid |

Total: 2 accounts
```

### Status check:

Run for each account:
```bash
python3 /Users/vic-gini/ProjectsCode/Agents/GoogleAccounts/scripts/auth.py --email {email}
```

### Reauth:

```bash
python3 /Users/vic-gini/ProjectsCode/Agents/GoogleAccounts/scripts/reauth.py --email {email}
```

### Add new account:

Guide user through:
1. Get email address
2. Get account type (personal/work)
3. Get label
4. Confirm they have client_secret.json
5. Run add_account.py

## Quick Reference

| Status | Meaning | Action |
|--------|---------|--------|
| Valid | Token works | None needed |
| Expired (can refresh) | Token expired but can auto-refresh | Will auto-fix on next use |
| Expired (needs reauth) | Refresh token invalid | Run `/google reauth {email}` |
| Not found | No credentials file | Run `/google add` |
