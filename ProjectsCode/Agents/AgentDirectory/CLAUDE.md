# Agent Directory

A centralized directory and launcher for all AI agents across the system, organized by domain and function.

## Purpose

This project provides a "Start Menu" for all agents, making it easy to discover, search, launch, and manage specialized AI agents across different projects and domains.

## What This Project Does

1. **Central Registry** - Maintains `agent-registry.json` with all discovered agents
2. **Automatic Discovery** - Scans directories for agent files and registers them
3. **Organization** - Categorizes agents by domain (Work/Personal/System) and function
4. **Search & Launch** - Helps users find and launch the right agent for their task

## Project Structure

```
AgentDirectory/
├── CLAUDE.md                          # This file
├── agent-registry.json                # Central registry of all agents
└── .claude/
    ├── settings.json                  # Permissions configuration
    └── agents/
        └── agent-directory.md         # Directory agent system prompt
```

## Registry Location

**Central registry:** `/Users/vic-gini/ProjectsCode/Agents/AgentDirectory/agent-registry.json`

This JSON file stores:
- List of all discovered agents
- Agent metadata (name, description, tools, path)
- Domain categorization (Work/Personal/System)
- Function categorization (Analysis/Creation/Planning/Research/Review/Setup)
- Last scan timestamp
- Project discovery information

## Scan Directories

The agent automatically scans these directories for agent files:
- `/Users/vic-gini/ProjectsCode/Agents/` - All agents
- `/Users/vic-gini/ProjectsCode/Projects/` - All projects
- `/Users/vic-gini/Documents/Victor L Obsidian Vault/` - Obsidian planning vault

## Domain Taxonomy

**Work Domains:**
- Verified Metrics
- Argonaut Expeditions
- IDEA/CIMUN
- Cloudview Real Estate

**Personal Domains:**
- Family
- Personal Finance
- Recovery
- Life and Fun
- Organization/Routines/Maintenance

**System Domains:**
- Agent Factory (meta-agents that create/manage other agents)
- Agent Directory (this project - organizing and launching agents)
- General (cross-cutting utility agents)

## Function Taxonomy

Agents are categorized by their primary function:
- **Analysis** - Analyze code, content, competitors, data
- **Creation** - Create copy, code, content, designs
- **Planning** - Plan projects, tasks, goals, schedules
- **Research** - Research keywords, competitors, markets, topics
- **Review** - Review and audit code, copy, agents, quality
- **Setup** - Setup projects, configure systems, bootstrap environments

## How to Use

### View the Agent Directory
1. Chat with `@agent-directory`
2. See all agents organized by domain and function
3. Browse available agents with descriptions and paths

### Search for Agents
1. Ask `@agent-directory` to search by name, domain, function, or keywords
2. View matching agents with details
3. Get launch syntax for the agent you want

### Scan for New Agents
1. Request a scan to discover new agents
2. Agent-directory will scan configured directories
3. Registry is updated with newly discovered agents
4. New projects are automatically catalogued

### Launch an Agent
1. Find the agent you need in the directory
2. Use the provided launch syntax (e.g., `@agent-name`)
3. Start working with the specialized agent

## Key Features

- **Automatic Discovery** - Finds agents by scanning for `CLAUDE.md` and `.claude/agents/*.md` files
- **Smart Categorization** - Infers domain and function from paths and descriptions
- **Search Capabilities** - Find agents by name, domain, function, tools, or keywords
- **Launch Integration** - Provides proper syntax for launching any agent
- **Project Tracking** - Discovers and tracks projects containing agents
- **Statistics** - Maintains counts of agents by domain and function

## Registry Schema

The `agent-registry.json` contains:
- `version` - Registry format version
- `last_updated` - Last modification timestamp
- `last_scan` - Last scan timestamp
- `scan_directories` - Directories to scan
- `agents[]` - Array of agent objects with metadata
- `discovered_projects[]` - Projects containing agents
- `domains{}` - Agents organized by domain hierarchy
- `functions{}` - Agents organized by function
- `stats{}` - Aggregate statistics

## Guidelines

- Registry is the single source of truth for all agents
- Agents are never deleted without confirmation
- Manual categorizations are preserved
- Timestamps are updated on every modification
- File paths are always clickable markdown links

## Maintaining Changelog & Plan

This project uses `CHANGELOG.md` and `PLAN.md` for tracking.

**⚠️ IMPORTANT: Always update CHANGELOG.md immediately and automatically after making ANY changes to project files — including templates, prompts, configuration files, system files, or any other project assets. Do NOT wait for the user to ask. This must happen automatically after every change.**

### When working on this project:
1. Check PLAN.md at the start to see current priorities
2. **Update CHANGELOG.md immediately after completing any changes** (under `## [Unreleased]`)
3. Move completed items from Current Focus to Completed in PLAN.md

### Changelog categories:
Added, Changed, Deprecated, Removed, Fixed, Security

### Entry format:
`- (YYYY-MM-DD HH:MM) Description of change`

### Plan sections:
- **Current Focus** - Active work (1-3 items max)
- **Backlog** - Future ideas
- **Completed** - Done items
