---
description: Get full 6-expert panel response on a GTM question
---

# /panel Command

Invoke the full advisory panel to respond to a GTM question or challenge.

## Process

1. **Get timestamp**: Run `node -e "console.log(new Date().toLocaleString() + ' (Local Time)')"`

2. **Analyze the question**: Identify the core GTM challenge or topic

3. **Select 6 experts**:
   - 2 most relevant to the specific inquiry
   - 2 with contrarian or opposing viewpoints
   - 2 randomly selected from different specializations than the first four

4. **Generate responses**: Each expert provides 500+ words including:
   - Timestamp
   - Situation analysis
   - Key framework concepts
   - Specific recommendations with metrics
   - Questions for further exploration

5. **Provide interactive options**: After all responses, offer:
   - Request specific experts
   - Request a debate
   - Deep-dive consultation
   - Case study analysis
   - Quantitative modeling
   - Extract action items

## Usage

```
/panel What's the best GTM strategy for a $25K ACV treasury management platform?
```

```
/panel How should we approach pricing for our private credit monitoring solution?
```

## Context Loading

If the user has saved context files in `.claude/contexts/`, reference them:
```
/panel [Load verified-metrics context] How should we handle the data sharing objection?
```

## Output Format

Follow the response format defined in CLAUDE.md:
- Horizontal rules between experts
- Expert name and specialty as H2
- Timestamp in bold
- Key Recommendations as H3 with numbered list
- Questions for Further Exploration as H3 with bullet list
- Interactive Options section at the end
