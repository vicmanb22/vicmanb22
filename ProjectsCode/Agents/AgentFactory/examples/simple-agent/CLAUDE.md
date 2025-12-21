# Simple Greeting Agent

A minimal example agent that demonstrates the basic structure of a Claude Code agent.

## Overview

This is a simple, read-only agent that greets users and answers basic questions. It has no file access and no special tools - just conversation.

## Purpose

Demonstrates the minimum viable agent structure:
- CLAUDE.md (this file)
- .claude/settings.json (minimal permissions)
- .claude/agents/greeter.md (agent definition)

## When to Use This Pattern

Use this pattern when your agent:
- Only needs to have conversations
- Doesn't need to read or write files
- Doesn't need to run commands
- Doesn't need web access
