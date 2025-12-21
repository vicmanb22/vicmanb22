# MCPFirefliesProject

Integration project for setting up and configuring the Fireflies.ai MCP server with Claude.

## Purpose

This project enables Claude to access meeting transcripts, summaries, and action items directly from your Fireflies.ai account through the Model Context Protocol (MCP).

## What This Project Does

- Configures the Fireflies MCP server for Claude
- Provides direct access to meeting data without manual transcript copying
- Enables AI-powered analysis of meeting content, action items, and insights

## MCP Server Details

- **Server**: Fireflies.ai MCP Server by Props Labs
- **Package**: `@props-labs/mcp/fireflies`
- **Documentation**: https://github.com/props-labs/fireflies-mcp

## Available Capabilities

Once configured, you can:
- Retrieve meeting transcripts
- Search across meeting content
- Access meeting summaries
- Extract action items and key insights
- Analyze meeting patterns and trends

## Security

The MCP server uses your Fireflies API key and follows the same security standards as the Fireflies platform. Data handling follows Claude's terms of service when accessed through the MCP integration.
