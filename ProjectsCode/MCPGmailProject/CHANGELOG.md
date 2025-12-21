# Changelog

All notable changes to the MCP Google Workspace Server setup.

## [Unreleased]

### Added
- Initial project structure
- CLAUDE.md with project overview
- Plan.md with setup checklist
- This changelog
- MCP server `gmail-workspace` added to Claude Code

### Changed
- Switched from mcp-gsuite to google_workspace_mcp (better Python compatibility, broader Workspace support)

### Added
- (2025-12-11 11:05) Successfully sent first ShoppingListEmail to belinda@argonautexpeditions.com (Message ID: 19b0b5ad964e286c)

### Completed
- [x] Google Cloud Project setup
- [x] Enabled APIs: Gmail, Calendar, Drive, Docs
- [x] Configured OAuth consent screen with required scopes
- [x] OAuth credentials stored in `~/.config/mcp-servers/.gauth.json`
- [x] Added MCP server to Claude Code with `--tool-tier core`
- [x] Verified server connection with `claude mcp list`
- [x] Completed OAuth authentication flow for `victor.lang22@gmail.com`
- [x] Successfully tested Gmail read operations
- [x] Successfully tested Gmail search operations
- [x] Successfully tested Gmail send operations
