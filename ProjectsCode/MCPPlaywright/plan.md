# Playwright MCP Setup Plan

## Overview
Configure Playwright MCP server for browser automation and visual design review in Claude Code.

## Current Status
- [x] Playwright MCP added to Claude Code (user scope)
- [ ] Restart Claude Code to activate
- [ ] Test basic functionality
- [ ] Configure security settings if needed

---

## Additional Considerations

### 1. Security & Access Control

**Domain Restrictions**
Playwright MCP can be configured with allowlists/blocklists:
- `--allowed-origins`: Only allow specific domains
- `--blocked-origins`: Block specific domains

Consider if you want to:
- Restrict to only your own websites (e.g., verifiedmetrics.com)
- Block sensitive sites (banking, email login pages)

**Example restricted setup:**
```bash
claude mcp add --transport stdio playwright --scope user -- npx -y @playwright/mcp@latest --allowed-origins "https://verifiedmetrics.com,https://staging.verifiedmetrics.com"
```

### 2. Browser Choice

Playwright supports multiple browsers:
- **Chromium** (default) - Best compatibility
- **Firefox** - Good for cross-browser testing
- **WebKit** - Safari rendering engine

For design review, Chromium is usually sufficient.

### 3. Headless vs Headed Mode

- **Headless** (default): No visible browser window, faster
- **Headed**: Shows browser window, useful for debugging

For design review, headless with screenshots is typically what you want.

### 4. Performance Considerations

- First run downloads browser binaries (~200-400MB)
- Each navigation creates a new browser context
- Screenshots are returned as base64 (can be large)

### 5. Network & Firewall

- Playwright needs internet access to fetch web pages
- Corporate firewalls may block automated browsers
- Some sites have bot detection that may block Playwright

### 6. Privacy & Data

- Playwright runs locally on your machine
- No data is sent to third parties (except the sites you visit)
- Browser sessions are isolated and don't persist cookies/data by default

---

## Testing Checklist

After setup, verify these work:
- [ ] Navigate to a URL
- [ ] Take a screenshot
- [ ] Click on elements
- [ ] Check different viewport sizes
- [ ] Scroll the page

## Common Use Cases

1. **Design Review**: Screenshot pages, compare layouts
2. **Responsive Testing**: Test at mobile/tablet/desktop widths
3. **Visual Regression**: Compare before/after changes
4. **Interactive Testing**: Fill forms, click buttons, verify flows

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MCP not showing tools | Restart Claude Code |
| Browser download fails | Check internet connection, try again |
| Site blocks access | Some sites block automated browsers |
| Timeout errors | Increase timeout or check site availability |

## Next Steps

1. Restart Claude Code to activate the MCP
2. Test with a simple navigation command
3. Use for VM Website design review
