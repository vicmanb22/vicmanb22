# Register Agent

Manually add an existing agent to the central directory or create a new agent.

## Instructions

Use the `@agent-directory` agent to register an agent in the central registry.

**Usage:** `/register-agent`

The agent will guide you through the process:

## Option 1: Register Existing Agent

1. **Provide agent path**
   - User supplies the path to an existing agent file
   - Example: `/Users/vic-gini/ProjectsCode/MyProject/.claude/agents/my-agent.md`

2. **Extract metadata**
   - Agent reads the file
   - Extracts name, description, tools from frontmatter
   - Reads project CLAUDE.md for context

3. **Categorize**
   - Agent suggests domain based on project context
   - Agent suggests function based on description and tools
   - User confirms or adjusts categorization

4. **Add to registry**
   - Update `/Users/vic-gini/ProjectsCode/AgentDirectory/agent-registry.json`
   - Confirm successful registration
   - Show where agent appears in directory

## Option 2: Create New Agent

1. **Gather requirements**
   - What should the agent do?
   - Which domain does it belong to?
   - What function does it serve?

2. **Execute `/new-agent` command**
   - Use the SlashCommand tool to run `/new-agent`
   - Follow the agent creation workflow

3. **Auto-register**
   - After agent is created, automatically scan and register it
   - Confirm registration and show directory location

## Output

Confirm successful registration with:
- Agent name
- Domain and function categorization
- File path (clickable link)
- Launch syntax
- Position in directory

Example:
```
✅ Agent registered successfully!

**Name:** email-writer
**Description:** Creates engaging email campaigns for marketing
**Domain:** Verified Metrics (Work)
**Function:** Creation
**Path:** [email-writer.md](/Users/vic-gini/ProjectsCode/EmailWriter/.claude/agents/email-writer.md)
**Launch:** `@email-writer`

You can now find this agent in:
Directory > Work Domains > Verified Metrics > Creation
```
