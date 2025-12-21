# Notion MCP Server - Quick Reference

Official Notion MCP server integration for Claude Code, enabling direct access to Notion workspaces.

## Current Status

- **MCP Server**: `@notionhq/notion-mcp-server` (Official by Notion)
- **Access Level**: 🔒 Read-Only (Phase 1)
- **Installation**: Not yet installed
- **Connected Pages**: None (awaiting setup)

## Quick Start

### 1. Create Notion Integration
Visit: https://www.notion.so/profile/integrations

### 2. Install MCP Server
```bash
claude mcp add notion-api npx -y @notionhq/notion-mcp-server
```

### 3. Configure Token
Edit: `~/Library/Application Support/Claude/claude_desktop_config.json`

Add your token to the `notion-api` env section:
```json
"NOTION_TOKEN": "ntn_YOUR_TOKEN_HERE"
```

### 4. Verify
```bash
claude mcp list
# Should show: notion-api - ✓ Connected
```

## Connected Notion Pages

**Phase 1 (Read-Only):**
- [ ] Page 1: [Name] - [URL]
- [ ] Page 2: [Name] - [URL]
- [ ] Page 3: [Name] - [URL]

**Phase 2 (Write-Enabled):**
- None yet (Phase 2 not implemented)

## Common Commands

### Search & Discovery
```
"Search my Notion for pages about [topic]"
"List all my Notion pages"
"Find pages containing '[keyword]'"
```

### Read Operations
```
"Read the content of the '[page name]' page"
"Show me the '[database name]' database structure"
"Get all entries from '[database name]'"
"Summarize the '[page name]' meeting notes"
```

### Write Operations (Phase 2 Only)
```
"Create a new page titled '[title]' in '[parent page]'"
"Add a bullet list to '[page]' with items: [A, B, C]"
"Update the '[property]' of '[page]' to '[value]'"
"Add a comment to '[page]': '[comment text]'"
```

## Use Cases

### Knowledge Management
- Search across Notion workspace for information
- Summarize meeting notes and docs
- Extract insights from databases
- Cross-reference pages and content

### Content Creation (Phase 2)
- Create structured pages from conversations
- Generate meeting notes from discussions
- Populate databases with collected data
- Add comments and feedback to pages

### Analysis & Reporting
- Query databases for metrics and trends
- Aggregate information across pages
- Generate summaries and reports
- Track project statuses

## Security Notes

### Token Protection
- ✅ Token stored in Claude's MCP config only
- ❌ Never commit token to git
- ❌ Never share token publicly
- 🔄 Rotate token if compromised

### Access Control
- **Current**: Read-only access to selected test pages
- **Future**: Write access limited to designated pages only
- **Review**: Monthly audit of connected pages

## Troubleshooting

### Server Not Connected
1. Check token format: `ntn_****`
2. Verify JSON syntax in config file
3. Restart Claude
4. Run `claude mcp list` to check status

### Can't Access Page
1. Verify integration has page access
2. Check page → "•••" → "Connections"
3. Grant access if missing

### Permission Errors
1. Check integration capabilities (read/write)
2. Verify workspace settings allow integrations
3. Confirm page isn't locked

## Files

- [CLAUDE.md](CLAUDE.md) - Full project context and guidelines
- [PLAN.md](PLAN.md) - Detailed setup and testing plan
- [CHANGELOG.md](CHANGELOG.md) - Project history and changes
- `.gitignore` - Protect sensitive files

## Resources

- [Official MCP Server](https://github.com/makenotion/notion-mcp-server)
- [Notion MCP Docs](https://developers.notion.com/docs/mcp)
- [Create Integration](https://www.notion.so/profile/integrations)
- [API Documentation](https://developers.notion.com)

## Next Steps

- [ ] Create Notion integration
- [ ] Get integration token
- [ ] Grant access to test pages
- [ ] Install MCP server
- [ ] Configure token
- [ ] Test read operations
- [ ] Document connected pages
- [ ] Plan Phase 2 (write access)

---

**Need Help?** See [PLAN.md](PLAN.md) for detailed instructions or [CLAUDE.md](CLAUDE.md) for full context.
