# Scan for Agents

Scan the filesystem for all AI agents and update the central registry.

## Instructions

Use the `@agent-directory` agent to:

1. Scan these directories for CLAUDE.md files and .claude/agents/ directories:
   - `/Users/vic-gini/ProjectsCode/Agents/`
   - `/Users/vic-gini/ProjectsCode/Projects/`
   - `/Users/vic-gini/Documents/Victor L Obsidian Vault/`

2. For each discovered agent:
   - Read the agent file metadata (frontmatter: name, description, tools)
   - Extract the project context from CLAUDE.md
   - Infer domain from path or content
   - Infer function from description and tools used
   - Record the file path

3. Update `/Users/vic-gini/ProjectsCode/Agents/AgentDirectory/agent-registry.json` with:
   - New agents discovered
   - Updated metadata for existing agents
   - Archived status for agents no longer found
   - New timestamp

4. Report findings:
   - Number of new agents found
   - Number of existing agents updated
   - Number of projects discovered
   - List of new agents with their categorization

The scan ensures the agent directory stays current with all available agents across the system.
