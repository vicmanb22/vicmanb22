# Changelog

All notable changes to GoogleAccounts.

## [1.1.0] - 2025-12-20

### Added
- vlang@cloudviewre.com (Cloudview Real Estate)
- victor@argonautexpeditions.com (Argonaut Expeditions)
- victor.lang@modelun.net (Model UN)

### Changed
- Registry now contains 5 accounts (1 personal + 4 work)

## [1.0.0] - 2025-12-20

### Added
- Initial release of GoogleAccounts agent
- Centralized OAuth authentication for Email and Calendar agents
- **auth.py** - Shared library providing `get_gmail_service()`, `get_calendar_service()`, `load_accounts()`
- **accounts.json** - Central registry with 2 accounts (personal + work)
- **add_account.py** - OAuth flow for adding new accounts
- **reauth.py** - Browser-based re-authentication for expired tokens
- **list_accounts.py** - List all accounts with token validation status
- `/google` command with subcommands: list, add, reauth, status

### Integration
- Email agent refactored to use GoogleAccounts auth (thin wrapper pattern)
- Calendar agent refactored to use GoogleAccounts auth (thin wrapper pattern)
- Both agents use `importlib.util.spec_from_file_location()` to avoid circular imports
- Dynamic account support: new accounts added here automatically work with Email/Calendar

---

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

Categories: Added, Changed, Deprecated, Removed, Fixed, Security

Entry format: `- (YYYY-MM-DD HH:MM) Description of change`
