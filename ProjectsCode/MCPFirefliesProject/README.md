# Fireflies MCP Server Setup

This project integrates the Fireflies.ai MCP (Model Context Protocol) server with Claude, enabling direct access to meeting transcripts, summaries, and action items.

## Installation Status

✅ Fireflies MCP server cloned and built locally
✅ Dependencies installed
✅ API key configured
⏳ Pending: Connection verification

## Server Location

The Fireflies MCP server is installed at:
```
/Users/vic-gini/ProjectsCode/MCPFirefliesProject/fireflies-mcp/
```

## Configuration

The server is configured in `/Users/vic-gini/.claude.json` under the ProjectsCode project with:

```json
{
  "fireflies": {
    "type": "stdio",
    "command": "node",
    "args": [
      "/Users/vic-gini/ProjectsCode/MCPFirefliesProject/fireflies-mcp/dist/index.js"
    ],
    "env": {
      "FIREFLIES_API_KEY": "6c966d12-1865-47e7-88e1-7a05a812bf20"
    }
  }
}
```

## Next Steps

1. **Restart Claude Code** - The MCP server configuration requires a restart to take effect
2. **Verify Connection** - Run `claude mcp list` to confirm the server is connected
3. **Test Functionality** - Try querying your Fireflies meeting data

## Available Features

Once connected, you'll be able to:
- Retrieve meeting transcripts
- Search across meeting content
- Access meeting summaries
- Extract action items and key insights
- Query meeting metadata and speaker information

## Troubleshooting

If the server fails to connect:

1. Verify the API key is valid at https://app.fireflies.ai/settings/api
2. Ensure you have meetings with processed transcripts
3. Check the server path is correct
4. Review logs for authentication or connection errors

## References

- [Props Labs Fireflies MCP Repository](https://github.com/props-labs/fireflies-mcp)
- [Fireflies API Documentation](https://docs.fireflies.ai)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
