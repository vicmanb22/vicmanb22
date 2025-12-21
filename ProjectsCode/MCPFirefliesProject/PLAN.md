# Fireflies MCP Server Setup Plan

## Project Location
`/Users/vic-gini/ProjectsCode/MCPFirefliesProject`

## Overview
Set up the Fireflies.ai MCP server to enable Claude to access meeting transcripts, summaries, and action items from your Fireflies account.

## Prerequisites
1. Active Fireflies.ai account
2. Fireflies API key (obtain from https://app.fireflies.ai/settings/api)

## Implementation Steps

### 1. Get Fireflies API Key
- Navigate to https://app.fireflies.ai/settings/api
- Generate a new API key
- Save the key securely

### 2. Install Fireflies MCP Server
Using the Props Labs implementation (recommended):
```bash
claude mcp add fireflies npx -y @props-labs/mcp/fireflies
```

### 3. Configure API Key
The MCP server requires the `FIREFLIES_API_KEY` environment variable. This will be set in the Claude MCP configuration with:
```json
{
  "fireflies": {
    "command": "npx",
    "args": ["-y", "@props-labs/mcp/fireflies"],
    "env": {
      "FIREFLIES_API_KEY": "<YOUR_API_KEY>"
    }
  }
}
```

### 4. Verify Installation
- Run `claude mcp list` to confirm the server is configured
- Test connection by asking Claude to list recent meetings or search transcripts

## Available Capabilities
Once configured, the Fireflies MCP server will enable:
- Retrieving meeting transcripts
- Searching across meeting content
- Accessing meeting summaries
- Extracting action items and key insights

## References
- [Props Labs Fireflies MCP](https://github.com/props-labs/fireflies-mcp)
- [Fireflies MCP Documentation](https://docs.fireflies.ai/getting-started/mcp-configuration)
- [Fireflies API Docs](https://docs.fireflies.ai)
