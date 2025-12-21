# MCP Notion Server Project

Integration project for setting up and configuring the official Notion MCP server with Claude Code.

## Purpose

This project enables Claude to access Notion workspaces directly through the Model Context Protocol (MCP), allowing reading and writing of pages, databases, and content without manual copying.

## What This Project Does

- Configures the official Notion MCP server for Claude Code
- Provides direct access to Notion pages, databases, and content
- Enables AI-powered content creation, analysis, and organization in Notion
- Follows a phased security approach: read-only access first, then selective write access

## MCP Server Details

- **Server**: Official Notion MCP Server by Notion
- **Package**: `@notionhq/notion-mcp-server`
- **GitHub**: https://github.com/makenotion/notion-mcp-server (3.6k+ stars)
- **Documentation**: https://developers.notion.com/docs/mcp

## Available Capabilities

### Current Phase: Read-Only Access
- Search pages and databases by title
- Read page content (text, blocks, properties)
- Retrieve database schemas and entries
- Access block-level content
- Read comments on pages

### Future Phase: Selective Write Access
Once enabled for specific pages:
- Create new pages in databases or as subpages
- Add blocks (text, headings, lists, etc.)
- Update page properties
- Modify database entries
- Add comments to pages

## Security Approach

### Token Security
- Integration token (`ntn_****`) stored in Claude's MCP config only
- Never committed to version control
- Regularly reviewed and rotated if needed

### Access Control
- **Phase 1**: Read-only capabilities enabled
- **Phase 2**: Write access granted only to specific designated pages
- Page-level connection control for granular permissions
- Regular access reviews and revocations

### Data Privacy
- Notion content is exposed to Claude's AI when accessed
- Start with non-sensitive test pages
- Expand access deliberately and document connected pages
- Consider creating a dedicated "Claude Workspace" in Notion

## Current Configuration Status

- **Access Level**: Read-only (Phase 1)
- **Connected Pages**: [To be documented after setup]
- **Write-Enabled Pages**: None (Phase 2 not yet implemented)

## Integration Setup Requirements

1. **Notion Integration**: Created at https://www.notion.so/profile/integrations
2. **Integration Token**: Securely stored in Claude MCP config
3. **Page Connections**: Integration granted access to specific pages via Notion's connection menu

## Quality Control

### Required Checks
- Verify integration token is valid and not exposed
- Confirm only intended pages have integration access
- Test read operations before enabling write access
- Document all connected pages in README.md

### Forbidden Actions
- Never commit integration token to git
- Do not enable write access without documenting target pages
- Avoid connecting sensitive personal/business pages initially
- Never bypass Notion's access control mechanisms

## File Structure

```
MCPNotionProject/
├── CLAUDE.md           # This file - project context
├── PLAN.md             # Detailed implementation plan
├── CHANGELOG.md        # Setup progress and changes
├── README.md           # Quick reference guide
└── .gitignore          # Protect sensitive files
```

## Common Use Cases

### Read Operations
- "Search my Notion for pages about [topic]"
- "Read the content of the [page name] page"
- "Show me all entries in the [database name] database"
- "Summarize the [page name] meeting notes"

### Write Operations (Phase 2)
- "Create a new page in [database] with [properties]"
- "Add a bullet list to [page] with [items]"
- "Update the status of [page] to [value]"
- "Comment on [page] with [feedback]"

## Context Management

For long-running sessions:
- Use `/rewind` to go back to good context points (not `/compact`)
- Use double-escape to fork conversations when you have good context
- Use `/resume` to continue from previous sessions with full context

## Maintaining Changelog & Plan

This project uses `CHANGELOG.md` and `PLAN.md` for tracking.

### When working on this project:
1. Check PLAN.md at the start to see current priorities
2. Update CHANGELOG.md after completing changes (under `## [Unreleased]`)
3. Move completed items from Current Focus to Completed in PLAN.md

### Changelog categories:
Added, Changed, Deprecated, Removed, Fixed, Security

## References

- [Official Notion MCP Server](https://github.com/makenotion/notion-mcp-server)
- [Notion MCP Documentation](https://developers.notion.com/docs/mcp)
- [Notion MCP Getting Started](https://developers.notion.com/docs/get-started-with-mcp)
- [Create Notion Integration](https://www.notion.so/profile/integrations)
- [NPM Package](https://www.npmjs.com/package/@notionhq/notion-mcp-server)
