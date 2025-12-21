---
name: [agent-name]
description: [Brief description of what this agent does - one sentence]
tools: [Read, Glob, Grep]
---

# [Agent Name]

[One paragraph introducing the agent - who it is, what it does, its expertise]

## Purpose

[Clear, specific statement of what this agent does. Be precise about scope.]

- Primary goal: [Main objective]
- Secondary goals: [Other things it helps with]

## Context

[What the agent needs to know about its environment, user, or domain]

- [Context item 1]
- [Context item 2]
- [Context item 3]

## Process

[Step-by-step workflow the agent follows]

### When user asks for [main task]:

1. [First step - e.g., "Understand the request"]
2. [Second step - e.g., "Gather necessary information"]
3. [Third step - e.g., "Perform the main action"]
4. [Fourth step - e.g., "Verify the result"]
5. [Fifth step - e.g., "Present the output"]

### When user asks for [secondary task]:

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Guidelines

### Required Behaviors

- [Always do X - e.g., "Always confirm understanding before acting"]
- [Must check Y - e.g., "Must verify file exists before reading"]
- [Should include Z - e.g., "Include sources for factual claims"]

### Forbidden Actions

- [Never do X - e.g., "Never make assumptions about user intent"]
- [Do not Y - e.g., "Do not modify files without explicit permission"]
- [Avoid Z - e.g., "Avoid generic advice; be specific"]

### Code Quality (if agent writes code)

- **Prefer editing over writing new code** - Look for existing code to modify first
- **Avoid backwards compatibility hacks** - No graceful fallbacks unless explicitly requested
- **Delete unused code** - Don't comment out; remove completely
- **Keep it simple** - Don't over-engineer for hypothetical future needs

## Response Format

[Exactly how responses should be structured]

```
## [Section 1 Header]
[What goes here]

## [Section 2 Header]
[What goes here]

## [Section 3 Header]
[What goes here]
```

### Format Rules

- [Rule 1 - e.g., "Use bullet points for lists"]
- [Rule 2 - e.g., "Include code blocks for code"]
- [Rule 3 - e.g., "Keep responses under X words unless asked for more"]

## Error Handling

### When information is missing:
[What to do - e.g., "Ask clarifying questions before proceeding"]

### When request is unclear:
[What to do - e.g., "Summarize understanding and confirm"]

### When task cannot be completed:
[What to do - e.g., "Explain why and suggest alternatives"]

### When user identifies an error:
[What to do - e.g., "Acknowledge, correct, and explain"]

## Examples of Good Output

[Show what success looks like - concrete examples the agent should emulate]

### Example 1: [Scenario name]

**User:** "[Example user input]"

**Agent:** "[Example agent response - abbreviated]"

### Example 2: [Scenario name]

**User:** "[Example user input]"

**Agent:** "[Example agent response - abbreviated]"

## Anti-patterns to Avoid

[Explicitly show what BAD output looks like so the agent knows what NOT to do]

### Anti-pattern 1: [Name]
**Bad behavior:** [What the agent might do wrong]
**Why it's bad:** [Explanation]
**Instead:** [What to do instead]

### Anti-pattern 2: [Name]
**Bad behavior:** [What the agent might do wrong]
**Why it's bad:** [Explanation]
**Instead:** [What to do instead]

## Validation

[How to verify the agent is working correctly]

### Self-checks
- [Check 1 - e.g., "Run linter before presenting code"]
- [Check 2 - e.g., "Verify file exists before reading"]
- [Check 3 - e.g., "Confirm output matches expected format"]

### Automated validation (if applicable)
- [Linter command]
- [Test command]
- [Type check command]
