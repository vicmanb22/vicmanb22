# Playwright MCP Project

This folder contains documentation and configuration for the Playwright MCP integration with Claude Code.

## What is Playwright MCP?

An MCP (Model Context Protocol) server that gives Claude Code the ability to control a real browser for:
- Visual design review (screenshots)
- Interactive testing (clicking, typing, scrolling)
- Responsive design testing (different viewport sizes)
- Web automation tasks

## Configuration Location

The Playwright MCP is configured at the **user scope**:
- Config file: `~/.claude.json`
- Available in: All Claude Code projects

## Available Playwright Tools

Once active, these tools become available:

| Tool | Purpose |
|------|---------|
| `browser_navigate` | Go to a URL |
| `browser_screenshot` | Capture the current page |
| `browser_click` | Click on an element |
| `browser_type` | Type text into inputs |
| `browser_scroll` | Scroll the page |
| `browser_resize` | Change viewport size |

## Usage Examples

**Take a screenshot of a website:**
> "Take a screenshot of https://verifiedmetrics.com"

**Test responsive design:**
> "Show me how the homepage looks at 375px width (mobile)"

**Interactive testing:**
> "Navigate to the contact page and fill out the form"

## Troubleshooting

If Playwright tools don't appear:
1. Restart Claude Code
2. Check MCP status with `/mcp` command
3. Verify config: `claude mcp list`

## Related Files

- `plan.md` - Setup plan and considerations
- `changelog.md` - Changes and updates
