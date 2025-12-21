# MCP Google Workspace Server Project

Set up an MCP (Model Context Protocol) server to provide Claude with access to Google Workspace services.

## Goal

Configure and run an MCP server that enables Claude to:
- Read and send emails (Gmail)
- Manage calendar events (Google Calendar)
- Access and create documents (Google Drive, Docs)
- Search across services

## Technical Approach

Using `google_workspace_mcp` (by Taylor Wilsdon) which provides comprehensive Google Workspace integration via MCP.

## Current Configuration

- **MCP Server**: `gmail-workspace` (added to Claude Code)
- **Tool Tier**: `core` (essential read/create/search operations)
- **OAuth Credentials**: `~/.config/mcp-servers/.gauth.json`

## Upgrade Options

To enable more features, change the tool tier:
- `core` - Essential read/create/search (current)
- `extended` - Adds labels, folders, batch operations
- `complete` - Full admin access including deletion

## Files

- `CLAUDE.md` - This file, project instructions
- `CHANGELOG.md` - Record of setup progress and changes
- `Plan.md` - Detailed setup plan and checklist

## Resources

- [google_workspace_mcp GitHub](https://github.com/taylorwilsdon/google_workspace_mcp)
- [Google Cloud Console](https://console.cloud.google.com/)
- [Claude MCP Documentation](https://docs.anthropic.com/en/docs/claude-code/mcp)
