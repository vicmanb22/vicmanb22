# GoogleAccounts

Centralized Google account management for Email and Calendar agents.

## Purpose

Single source of truth for Google OAuth authentication across all agents that interact with Google APIs (Gmail, Calendar, etc.).

## Architecture

```
GoogleAccounts/
├── CLAUDE.md                 # This file
├── CHANGELOG.md              # Version history
├── accounts.json             # Central account registry
├── scripts/
│   ├── auth.py               # Shared auth library (imported by other agents)
│   ├── add_account.py        # Initial OAuth flow for new accounts
│   ├── reauth.py             # Re-authenticate expired tokens
│   ├── list_accounts.py      # List all accounts with status
│   └── requirements.txt      # Python dependencies
└── .claude/
    ├── agents/
    │   └── google-accounts.md
    └── commands/
        └── google.md         # /google command
```

## Accounts Registry

**Location:** `accounts.json`

| Email | Type | Label |
|-------|------|-------|
| victor.lang22@gmail.com | personal | Personal Gmail |
| victor@verifiedmetrics.com | work | Verified Metrics |
| vlang@cloudviewre.com | work | Cloudview Real Estate |
| victor@argonautexpeditions.com | work | Argonaut Expeditions |
| victor.lang@modelun.net | work | Model UN |

**Total:** 5 accounts (1 personal + 4 work)

## Credentials Storage

OAuth tokens are stored at:
```
~/.google_workspace_mcp/credentials/{email}.json
```

This location is shared with the legacy Google Workspace MCP and allows the scripts to work with existing credentials.

## Commands

| Command | Description |
|---------|-------------|
| `/google` | Main command - shows menu of options |
| `/google list` | List all accounts with token status |
| `/google add {email}` | Add new account via OAuth flow |
| `/google reauth {email}` | Re-authenticate expired token |
| `/google status` | Check token validity for all accounts |

## Integration

### How Agents Use GoogleAccounts

Both Email and Calendar agents have thin wrapper `auth.py` files that delegate to GoogleAccounts:

```python
# Email/scripts/auth.py or Calendar/scripts/auth.py
import importlib.util
from pathlib import Path

GOOGLE_ACCOUNTS_AUTH = Path('/Users/vic-gini/ProjectsCode/Agents/GoogleAccounts/scripts/auth.py')
spec = importlib.util.spec_from_file_location("google_accounts_auth", GOOGLE_ACCOUNTS_AUTH)
_ga_auth = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_ga_auth)

# Re-export functions
get_gmail_service = _ga_auth.get_gmail_service
get_calendar_service = _ga_auth.get_calendar_service
load_accounts = _ga_auth.load_accounts
```

### Dynamic Account Support

When you add a new account to GoogleAccounts:
1. Run `/google add {email}` to add credentials
2. The account appears in `accounts.json`
3. **Email agent**: Automatically works with new account using `digest-default.md` template
4. **Calendar agent**: Automatically works with new account

### Connected Agents

| Agent | Integration | Notes |
|-------|-------------|-------|
| Email | `scripts/auth.py` → GoogleAccounts | Uses `digest-default.md` for new accounts |
| Calendar | `scripts/auth.py` → GoogleAccounts | Full functionality immediately |

## Forbidden Actions

- Never store credentials in plaintext outside the designated directory
- Never commit credentials to git
- Never share tokens between different Google Cloud projects

## Quality Control

### Required Checks
- Verify token validity before returning services
- Auto-refresh expired tokens when refresh_token exists
- Create backups before re-authentication

### Error Handling
- If credentials file missing → prompt to run add_account
- If refresh fails → prompt to run reauth
- If scopes insufficient → show required scopes and reauth

## Documentation Updates

**Update documentation immediately after changes — do not wait to be asked.**

| Change Type | Files to Update |
|-------------|-----------------|
| Any code/config change | CHANGELOG.md (immediately) |
| New account added | accounts.json |
| Structure change | CLAUDE.md |
| New capability | CLAUDE.md + CHANGELOG.md |
