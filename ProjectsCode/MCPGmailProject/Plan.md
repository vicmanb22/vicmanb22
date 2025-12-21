# MCP Google Workspace Server Setup Plan

## Phase 1: Google Cloud Setup

- [x] Create or select a Google Cloud Project
- [x] Enable APIs: Gmail, Calendar, Drive, Docs
- [x] Configure OAuth consent screen
  - [x] Set to "External" user type
  - [x] Add required scopes (gmail.modify, calendar, drive, documents, openid, userinfo.email)
- [x] Create OAuth 2.0 credentials
  - [x] Application type: Desktop app
  - [x] Download credentials JSON file to `~/.config/mcp-servers/.gauth.json`

## Phase 2: Install google_workspace_mcp

- [x] Verify `uv` is installed (v0.9.16)
- [x] Python 3.13.11 available via uv

## Phase 3: Configure Claude Code

- [x] Add MCP server to Claude Code:
  ```bash
  claude mcp add gmail-workspace \
    --env GOOGLE_OAUTH_CLIENT_ID=<client_id> \
    --env GOOGLE_OAUTH_CLIENT_SECRET=<client_secret> \
    -- uvx workspace-mcp --tool-tier core
  ```
- [x] Verify server appears in `claude mcp list`
- [x] Complete OAuth authentication flow (victor.lang22@gmail.com)

## Phase 4: Test and Verify

- [x] Test reading emails
- [x] Test searching emails
- [x] Test sending emails
- [ ] Test calendar access (optional)

## Notes

- OAuth tokens will be stored locally after first authentication
- May need to re-authenticate periodically
- Can upgrade to `extended` or `complete` tier for more features
