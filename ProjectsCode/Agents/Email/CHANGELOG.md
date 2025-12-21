# Changelog

All notable changes to the Email agent.

## [1.1.0] - 2025-12-20

### Added
- **Subscription Manager** (`/subscriptions` command):
  - View all subscriptions sorted by frequency (most emails first)
  - One-click unsubscribe via RFC 8058 when available
  - Fallback methods: mailto, body link parsing, manual
  - Post-unsubscribe options: archive existing, create filter
  - New scripts: `gmail_list_subscriptions.py`, `gmail_unsubscribe.py`, `gmail_create_filter.py`

- **Inbox Cleanup** (`/cleanup` command):
  - Clean up Promotions, Social, Updates categories
  - Sender aggregation by normalized domain
  - Bulk actions: archive all, delete all, unsubscribe + delete
  - Domain normalization (e.g., `shared1.ccsend.com` → `ccsend.com`)
  - New script: `gmail_cleanup_category.py`

- **New subagents**:
  - `@subscriptions` - Subscription management workflow
  - `@inbox-cleanup` - Category cleanup workflow

### Changed
- **Warning suppression**: All Gmail scripts now suppress Python warnings that previously contaminated JSON output
  - `importlib.metadata` errors (Python 3.9 compatibility)
  - Google API discovery cache warnings
  - urllib3 SSL warnings
- **GoogleAccounts auth.py**: Fixed stdout contamination during googleapiclient import
- **Updated email.md routing**: Added routing for subscriptions and cleanup intents

---

## [1.0.9] - 2025-12-20

### Changed
- Now supports 5 accounts via GoogleAccounts integration (was 2)
- New accounts: vlang@cloudviewre.com, victor@argonautexpeditions.com, victor.lang@modelun.net
- All new accounts use `digest-default.md` template

## [1.0.8] - 2025-12-20

### Changed
- **Dynamic account support**: Email agent now reads accounts from GoogleAccounts registry
- New accounts added via `/google add` automatically work with Email agent
- Uses `digest-default.md` template for accounts without custom templates
- Updated documentation to reflect GoogleAccounts integration

---

## [1.0.7] - 2025-12-20

### Changed
- **Auth refactored to use GoogleAccounts**: `auth.py` and `reauth.py` now delegate to centralized `GoogleAccounts/scripts/auth.py`
- All authentication logic is now in one place for easier maintenance
- No changes to script interfaces - fully backward compatible

---

## [1.0.6] - 2025-12-20

### Added
- **Cross-agent context file**: Digest now writes `/tmp/email-digest-context.json` after generating
  - Contains email number-to-ID mapping for cross-agent communication
  - Enables Calendar agent to create events from emails by number reference
  - Fields: id, subject, from, date_iso (with sender's timezone)

### Changed
- Updated bash permissions to use correct `:*` suffix syntax for prefix matching
- Added `calendar #` action to create calendar events from emails

---

## [1.0.5] - 2025-12-20

### Changed
- Time Ago format now shows minutes for recent emails:
  - `< 1 hour` → `Xm ago` (e.g., "15m ago", "45m ago")
  - `≥ 1 hour` → `Xh ago` (e.g., "2h ago", "5h ago")
  - `≥ 1 day` → `Xd ago` (e.g., "1d ago", "3d ago")

---

## [1.0.4] - 2025-12-20

### Added
- Sequential numbering (`#` column) for all digest tables
  - Numbers are sequential across entire digest (not per-category)
  - Used for action references (e.g., "done 3", "view 5")
- Actions menu displayed after each digest with quick commands
- `done` action combining mark as read + archive
- Format toggle in actions menu (switch between Light/Complete)
- Full actions list available via "more actions" command

### Changed
- **Complete format is now the default** (was Light)
- Light format: 6 columns - #, Date, Time Ago, From, Subject, Status
- Complete format: 10 columns - #, Date, Time Ago, From, Company, To, Subject, Domain, Summary, Status
- Updated all templates (default, personal, work) with new format documentation

### Actions Available
Basic: view, done, spam, star, reply, format toggle
Full: + archive, mark read, mark unread, unstar, forward, label, delete
Bulk: commas (1, 3, 5), ranges (1-5), categories (all unsolicited)

---

## [1.0.3] - 2025-12-20

### Added
- Two standardized table formats for digests:
  - **Light**: 5 columns - Date, Time Ago, From, Subject, Status
  - **Complete**: 9 columns - adds Company, To, Domain, Summary
- `time_ago()` utility function for human-readable relative times (2h ago, 1d ago, 3w ago)
- `format_date_short()` utility for short date format (Dec 20)
- Life domain classification using Planning module's 9 domains
- LLM enrichment for Complete format (Company, Domain, Summary)

### Changed
- All templates updated with Light/Complete format documentation
- Digest subagent now accepts `--format` parameter (light or complete)

---

## [1.0.2] - 2025-12-20

### Changed
- Account selection now uses multi-select to allow choosing multiple accounts or all at once
- Added "All accounts" option to run digests for all known accounts sequentially

---

## [1.0.1] - 2025-12-20

### Removed
- Gmail MCP server configuration from `~/.claude.json`
- Gmail MCP permissions from `~/.claude/settings.json`
- All MCP dependencies now fully deprecated

---

## [1.0.0] - 2025-12-20

### Added
- Initial release of unified Email agent
- Multi-account support for any Gmail account
- Orchestrator pattern with subagents:
  - `@email` - Main orchestrator
  - `@digest` - Email digest generation
- Template system for account-specific digests:
  - `digest-default.md` - Generic 5-category template
  - `digest-personal.md` - Personal account (victor.lang22@gmail.com)
  - `digest-work.md` - Work account (victor@verifiedmetrics.com)
- Python scripts for Gmail API (copied from EmailDigest):
  - auth.py, reauth.py, utils.py
  - gmail_search.py, gmail_get_message.py, gmail_get_messages_batch.py
  - gmail_get_thread.py, gmail_list_labels.py, gmail_get_known_contacts.py
  - gmail_modify_labels.py, gmail_send_message.py, gmail_create_draft.py
- Commands: `/email`, `/digest`
- Integration with MainOrchestrator

### Migrated From
- **EmailDigest** (victor.lang22@gmail.com)
  - 5 personal categories
  - Python script architecture
- **EmailDigestVM** (victor@verifiedmetrics.com)
  - 10 work categories
  - Threading support
  - Company/To columns

### Deprecated
- EmailDigest agent (use Email with personal template)
- EmailDigestVM agent (use Email with work template)
- Gmail MCP server dependency

---

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
