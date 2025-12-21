# Find Agent

Search for agents in the directory by name, domain, function, tools, or keywords.

## Instructions

Use the `@agent-directory` agent to search for agents matching the user's criteria.

**Usage:** `/find-agent [search query]`

**Examples:**
- `/find-agent copywriter` - Search by name
- `/find-agent domain:VerifiedMetrics` - Search by domain
- `/find-agent function:Analysis` - Search by function
- `/find-agent tools:WebSearch` - Search by required tools
- `/find-agent competitor analysis` - Search by keywords

## Process

1. Load the agent registry
2. Parse the search query for:
   - Name matches (partial, case-insensitive)
   - Domain filters (domain:X)
   - Function filters (function:X)
   - Tool filters (tools:X)
   - Keyword matches in descriptions
3. Filter and rank results by relevance
4. Present results with:
   - Agent name and clickable file path
   - Full description
   - Domain and function categorization
   - Tools used
   - Launch syntax (`@agent-name` or path)
5. Offer to launch the agent or view more details

If no agents match, suggest similar options or offer to create a new agent.
