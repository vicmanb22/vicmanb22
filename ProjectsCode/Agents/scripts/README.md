# Shared Scripts Library

Reusable Python scripts created by self-improving agents. These scripts represent **Phase 2 (Code-Driven)** workflows that have been proven reliable through repeated successful execution.

## Purpose

When an agent performs a task successfully multiple times using LLM reasoning, it can propose "codifying" that workflow into a deterministic Python script. Once approved, the script lives here for reuse across agents.

**Why scripts?**
- Scripts don't hallucinate - they either work or error cleanly
- Faster execution than LLM reasoning
- Consistent, repeatable results
- Target 99%+ reliability vs ~75-90% for LLM reasoning

## Directory Structure

```
scripts/
├── README.md                 # This file
├── validation/               # Data validation scripts
├── parsing/                  # File/text parsing scripts
├── formatting/               # Output formatting scripts
└── [category]/               # Other categories as needed
```

## Using Scripts

### From an Agent

Agents can run scripts using the Bash tool:

```bash
python /Users/vic-gini/ProjectsCode/Agents/scripts/[category]/[script].py [args]
```

### Permission Model

By default, agents must ask permission before running scripts. This can be configured per-agent in their `settings.json`:

```json
{
  "auto_run_scripts": false
}
```

Set to `true` to allow automatic script execution without asking.

## Contributing Scripts

### When to Create a Script

A task is ready for codification when:
- It has succeeded 3+ times with the same approach
- It is repeatable (not a one-off task)
- It has clear inputs and outputs
- A script would be faster/more reliable than reasoning

### Script Requirements

1. **Clear inputs/outputs** - Document what the script expects and returns
2. **Error handling** - Fail cleanly with meaningful error messages
3. **No side effects** - Scripts should be predictable and safe
4. **Standalone** - Minimize dependencies (prefer stdlib)

### Script Template

```python
#!/usr/bin/env python3
"""
[Script Name]

Purpose: [What this script does]
Created by: [Agent name]
Created from: [reliability-log entry reference]

Usage:
    python script.py [args]

Inputs:
    - [input 1]: [description]
    - [input 2]: [description]

Outputs:
    - [output description]

Exit codes:
    0 - Success
    1 - [Error type 1]
    2 - [Error type 2]
"""

import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='[Description]')
    # Add arguments
    args = parser.parse_args()

    try:
        # Script logic here
        result = do_work(args)
        print(result)
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def do_work(args):
    """Main script logic."""
    pass

if __name__ == "__main__":
    main()
```

## Script Failure Handling

If a script fails during execution:

1. **Agent flags for human review** - No automatic fallback to LLM reasoning
2. **User decides:** Fix the script, revert to Phase 1 (LLM reasoning), or take other action
3. **Log the failure** - Record in the agent's `reliability-log.md`

This ensures scripts remain trustworthy - if a script fails, it needs human attention.

## Existing Scripts

*No scripts yet. Scripts will be added here as agents graduate tasks from Phase 1 to Phase 2.*
