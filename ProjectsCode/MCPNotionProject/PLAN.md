# Notion MCP Server Setup Plan

## Project Location
`/Users/vic-gini/ProjectsCode/MCPNotionProject`

## Overview
Set up the official Notion MCP server to enable Claude Code to interact with Notion workspaces. Phased approach: start with read-only access, then selectively enable write access to specific pages.

## Prerequisites

### 1. Create Notion Integration
- [ ] Navigate to https://www.notion.so/profile/integrations
- [ ] Click "Create new integration"
- [ ] Name it: "Claude Code Integration" (or your preference)
- [ ] Configure **Read-Only Capabilities** (Phase 1):
  - [x] Read content
  - [x] Read comments
  - [ ] Insert content (disabled initially)
  - [ ] Update content (disabled initially)
- [ ] Save integration
- [ ] Note the integration ID for reference

### 2. Get Integration Token
- [ ] In integration settings, go to "Configuration" tab
- [ ] Copy the "Internal Integration Secret"
  - Format: `ntn_****`
  - **IMPORTANT**: Keep this secure, never commit to git
- [ ] Store securely for next step

### 3. Grant Access to Test Pages
- [ ] Choose 2-3 non-sensitive test pages in Notion
- [ ] For each page:
  - [ ] Open the page in Notion
  - [ ] Click "•••" (more menu) → "Connections"
  - [ ] Select your "Claude Code Integration"
  - [ ] Confirm access granted
- [ ] Document connected pages in README.md

## Installation Steps

### Step 1: Add MCP Server to Claude Code
```bash
claude mcp add notion-api npx -y @notionhq/notion-mcp-server
```

- [ ] Run the command above
- [ ] Verify it completes successfully

### Step 2: Configure Integration Token

**Manual configuration required:**

- [ ] Open Claude's MCP config file:
  - Location: `~/Library/Application Support/Claude/claude_desktop_config.json`
  - Use: `open ~/Library/Application\ Support/Claude/claude_desktop_config.json`

- [ ] Find the `notion-api` entry and add your token:

```json
{
  "mcpServers": {
    "notion-api": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_TOKEN": "ntn_YOUR_ACTUAL_TOKEN_HERE"
      }
    }
  }
}
```

- [ ] Save the file
- [ ] **Security Check**: Ensure token is NOT in any project files

### Step 3: Verify Installation

- [ ] Run: `claude mcp list`
- [ ] Confirm output shows:
  ```
  notion-api: npx -y @notionhq/notion-mcp-server - ✓ Connected
  ```
- [ ] If not connected, check token and restart Claude

## Testing Plan

### Phase 1: Read-Only Access Testing

#### Test 1: Basic Connectivity
- [ ] Test: "List my Notion pages"
- [ ] Expected: Should show only pages with integration access
- [ ] Result: _______________

#### Test 2: Page Search
- [ ] Test: "Search my Notion for pages containing '[keyword]'"
- [ ] Expected: Returns relevant pages
- [ ] Result: _______________

#### Test 3: Read Page Content
- [ ] Test: "Read the content of the '[page name]' page"
- [ ] Expected: Returns full page content with blocks
- [ ] Result: _______________

#### Test 4: Database Query (if applicable)
- [ ] Test: "Show me entries in the '[database name]' database"
- [ ] Expected: Returns database entries with properties
- [ ] Result: _______________

#### Test 5: Access Control Verification
- [ ] Test: "List all Notion pages"
- [ ] Expected: Only shows pages with integration access
- [ ] Verify: Pages without access are NOT visible
- [ ] Result: _______________

### Phase 2: Write Access (Future Implementation)

**Complete only when ready to enable write operations**

#### Preparation Steps
- [ ] Go to Notion integration settings
- [ ] Update capabilities:
  - [x] Insert content
  - [x] Update content (if needed)
- [ ] Identify specific pages/databases for write access:
  - Page 1: _______________
  - Page 2: _______________
  - Page 3: _______________
- [ ] Document write-enabled pages in README.md

#### Write Operation Tests
- [ ] Test: "Create a test page titled 'MCP Test' under '[parent page]'"
- [ ] Result: _______________

- [ ] Test: "Add a bullet list to '[page name]' with items: [A, B, C]"
- [ ] Result: _______________

- [ ] Test: "Update the '[property]' property of '[page name]' to '[value]'"
- [ ] Result: _______________

- [ ] Test: "Add a comment to '[page name]': 'Testing MCP integration'"
- [ ] Result: _______________

## Security Checklist

### Token Security
- [ ] Integration token is stored ONLY in Claude's MCP config
- [ ] Token is NOT in any project files (.env, config files, etc.)
- [ ] Token is NOT committed to git
- [ ] `.gitignore` includes any token-related files

### Access Control
- [ ] Only intended pages have integration access
- [ ] Read-only mode confirmed in Phase 1
- [ ] Write access limited to designated pages (Phase 2)
- [ ] Access list documented in README.md

### Data Privacy
- [ ] No sensitive personal data in connected pages
- [ ] No confidential business data in connected pages
- [ ] Testing performed on non-critical content
- [ ] Team members informed of integration (if shared workspace)

## Troubleshooting

### Issue: Server Won't Connect

**Symptoms:** `claude mcp list` shows error or not connected

**Solutions:**
1. [ ] Verify `NOTION_TOKEN` format is correct (`ntn_****`)
2. [ ] Check JSON syntax in config file (commas, brackets)
3. [ ] Restart Claude Desktop/Code
4. [ ] Check token hasn't been revoked in Notion
5. [ ] Try removing and re-adding: `claude mcp remove notion-api` then re-add

### Issue: "Page Not Found" Errors

**Symptoms:** Can't access specific pages

**Solutions:**
1. [ ] Verify integration has access to the page:
   - Open page in Notion
   - Check "•••" → "Connections" shows your integration
2. [ ] Grant access if missing
3. [ ] Wait a few seconds for sync
4. [ ] Try searching by exact page title

### Issue: Permission Errors

**Symptoms:** "Forbidden" or permission denied errors

**Solutions:**
1. [ ] Check integration capabilities in Notion settings
2. [ ] For write operations: Verify "Insert content" is enabled
3. [ ] Confirm workspace admin hasn't restricted integrations
4. [ ] Check page-level permissions (page may be locked)

### Issue: Token Exposed or Compromised

**Action Plan:**
1. [ ] Immediately revoke token in Notion integration settings
2. [ ] Generate new integration token
3. [ ] Update Claude's MCP config with new token
4. [ ] Review git history to ensure token wasn't committed
5. [ ] Document incident in CHANGELOG.md

## Configuration Options

### Read-Only Mode (Current - Phase 1)
```
Capabilities:
✓ Read content
✓ Read comments
✗ Insert content
✗ Update content
```

### Full Access Mode (Phase 2)
```
Capabilities:
✓ Read content
✓ Read comments
✓ Insert content
✓ Update content
```

## Success Criteria

- [ ] MCPNotionProject folder created with all documentation
- [ ] MCP server shows "✓ Connected" in `claude mcp list`
- [ ] Can successfully read from test Notion pages
- [ ] Integration token is secure (not in git)
- [ ] CHANGELOG.md tracks all setup steps
- [ ] README.md documents connected pages
- [ ] All Phase 1 tests pass
- [ ] Clear documentation for Phase 2 transition

## Rollback Plan

If issues occur or integration needs to be removed:

1. [ ] Remove MCP server:
   ```bash
   claude mcp remove notion-api
   ```

2. [ ] Revoke Notion integration access:
   - [ ] Go to each connected page
   - [ ] Remove integration from "Connections"
   - [ ] OR delete integration entirely in Notion settings

3. [ ] Clean up tokens:
   - [ ] Delete integration token in Notion
   - [ ] Remove token from Claude's config (if server removed)
   - [ ] Generate new token if reinstalling

4. [ ] Document:
   - [ ] Record reason for rollback in CHANGELOG.md
   - [ ] Note any issues encountered
   - [ ] Update README.md status

## Maintenance

### Regular Reviews (Monthly)
- [ ] Review list of connected pages
- [ ] Remove access from unused pages
- [ ] Verify token is still valid
- [ ] Check for Notion MCP server updates
- [ ] Update documentation if usage patterns change

### Updates
- [ ] Monitor official Notion MCP server releases
- [ ] Check for breaking changes before updating
- [ ] Test after updates to verify functionality

## References

- [Official Notion MCP Server](https://github.com/makenotion/notion-mcp-server)
- [Notion MCP Documentation](https://developers.notion.com/docs/mcp)
- [Notion MCP Getting Started](https://developers.notion.com/docs/get-started-with-mcp)
- [Create Notion Integration](https://www.notion.so/profile/integrations)
- [NPM Package](https://www.npmjs.com/package/@notionhq/notion-mcp-server)
- [Notion API Documentation](https://developers.notion.com)

## Project Pattern References

Following structure and patterns from:
- `/Users/vic-gini/ProjectsCode/MCPGmailProject/` - OAuth setup, documentation style
- `/Users/vic-gini/ProjectsCode/MCPFirefliesProject/` - MCP installation pattern
