# Deep Explore

Force Claude to spend tokens building comprehensive context before any work begins.

## Usage

```
/deep-explore [area or topic]
```

Example: `/deep-explore the authentication system`

## Purpose

This command makes Claude invest significant effort understanding a codebase or topic BEFORE attempting any work. The goal is to build high-quality context that leads to better output.

## Instructions

When the user provides an area to explore, you must:

1. **Do NOT write any code or make any changes**
2. **Spend significant tokens exploring** - Don't rush to conclusions
3. **Read widely before synthesizing** - Look at multiple files, not just one
4. **Verify your understanding** - Check assumptions against actual code

## Exploration Process

### Phase 1: Discovery
- Search for all relevant files using Glob and Grep
- Identify the core files vs. peripheral files
- Note the file structure and naming conventions

### Phase 2: Deep Reading
- Read the main files thoroughly
- Understand the data flow and dependencies
- Identify patterns and conventions used

### Phase 3: Understanding
- Map out how components interact
- Identify entry points and key functions
- Note any unusual patterns or potential issues

### Phase 4: Summary
Present your understanding in this format:

```
## [Area] Overview

### Structure
- [Key files and their purposes]
- [Directory organization]

### Key Components
1. **[Component 1]** - [what it does, where it lives]
2. **[Component 2]** - [what it does, where it lives]

### Data Flow
[How data moves through the system]

### Patterns Used
- [Pattern 1] - [where and why]
- [Pattern 2] - [where and why]

### Dependencies
- Internal: [other parts of codebase this depends on]
- External: [libraries, services, APIs]

### Potential Concerns
- [Thing that seems fragile or confusing]
- [Technical debt or inconsistency noticed]

### Ready to Work On
I now have sufficient context to work on:
- [Specific thing 1]
- [Specific thing 2]

I would need more exploration to work on:
- [Area that's still unclear]
```

## Key Behaviors

### DO:
- Read more files than you think necessary
- Take time to understand patterns before summarizing
- Acknowledge when something is unclear
- Note inconsistencies or surprises

### DO NOT:
- Rush to provide an answer
- Assume based on file names alone
- Skip reading files to save time
- Write any code during exploration

## Verifying Understanding

After presenting your summary, ask the user:

> "Does this match your understanding? Any areas I should explore more deeply before we proceed?"

This catches misunderstandings before they propagate into work.
