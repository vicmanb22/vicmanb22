# Scripts Folder

This folder is for codified workflows that have graduated from Phase 1 (LLM-Driven) to Phase 2 (Code-Driven).

## Current Status

**Phase:** 1 (LLM-Driven) - No scripts codified yet

This agent is still building reliability through LLM reasoning. Once task patterns achieve 3+ consistent successes, they can be proposed for codification.

## How Scripts Work

When a task type is codified:

1. A Python script is created in the **shared scripts library**:
   `/Users/vic-gini/ProjectsCode/Agents/scripts/`

2. The script is organized by category (e.g., `summarization/`, `validation/`)

3. The agent runs the script instead of using LLM reasoning for that task type

4. If the script fails, it flags for human review (no auto-fallback)

## Shared Scripts Library

All codified scripts are stored in a shared location for reuse across agents:

**Location:** `/Users/vic-gini/ProjectsCode/Agents/scripts/`

This allows:
- Multiple agents to use the same proven scripts
- Centralized maintenance and updates
- Consistent behavior across the agent ecosystem

## Codification Criteria

A task is ready for codification when:
- It has succeeded 3+ times with the same approach
- It is repeatable (not a one-off task)
- It has clear inputs and outputs
- A script would be faster/more reliable than reasoning

## Pending Codification Candidates

Check `reliability-log.md` for tasks approaching the 3-success threshold.

Currently monitoring:
- Meeting Notes Summarization (2/3 successes)
