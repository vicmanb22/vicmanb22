# SDK Self-Improving Agent Example

A complete working example of a self-improving agent using the Claude Agent SDK with **automated reliability logging**.

## Quick Start

```bash
# 1. Install the Claude Agent SDK
pip install claude-agent-sdk

# 2. Set your API key
export ANTHROPIC_API_KEY=your-api-key

# 3. Run the agent
python agent.py
```

## What This Example Demonstrates

### 1. SDK-Based Multi-Turn Conversations

Uses `ClaudeSDKClient` for persistent, multi-turn conversations:

```python
async with ClaudeSDKClient(options=options) as client:
    await client.query("Read the README file")
    async for message in client.receive_response():
        print_message(message)
```

### 2. Automated Reliability Logging

SDK hooks auto-populate `reliability-log.md` - no manual feedback needed:

- **PreToolUse hook**: Logs every tool invocation
- **PostToolUse hook**: Logs success/failure of each tool
- **Stop hook**: Logs complete session summary

### 3. Two-Phase Maturity Model

This agent is in **Phase 1 (LLM-Driven)**:
- Uses LLM reasoning for all tasks
- Target reliability: 75-90%
- All actions logged for pattern analysis

**Phase 2 (Code-Driven)** comes later:
- When 3+ similar successes → propose script codification
- When 3+ similar failures → propose directive improvements
- Human approves changes
- Agent runs scripts instead of re-reasoning

## Files

| File | Purpose |
|------|---------|
| `agent.py` | Main agent script with hooks |
| `reliability_hooks.py` | Hook implementations |
| `reliability-log.md` | Auto-populated log (grows with use) |
| `CLAUDE.md` | Project context |
| `README.md` | This file |

## Customizing

To create your own self-improving agent:

1. **Copy this directory** to your project

2. **Edit `agent.py`**:
   ```python
   AGENT_NAME = "Your Agent Name"
   AGENT_DESCRIPTION = "What your agent does"
   SYSTEM_PROMPT = """Your custom instructions..."""
   ALLOWED_TOOLS = ["Read", "Write", ...]  # Tools your agent needs
   ```

3. **Run and watch logs populate**:
   ```bash
   python agent.py
   # Use the agent for a few tasks
   # Check reliability-log.md - it grows automatically!
   ```

## How Logging Works

Every interaction follows this flow:

```
User Input
    ↓
PreToolUse Hook → Logs tool name + inputs
    ↓
Tool Execution
    ↓
PostToolUse Hook → Logs success/failure
    ↓
Agent Response
    ↓
(repeat for each tool)
    ↓
Session End
    ↓
Stop Hook → Logs session summary
```

The `reliability-log.md` accumulates data:
- Session timestamps and durations
- Tool usage patterns
- Success/failure rates
- Cost tracking (if available)

## Example Log Entry

After using the agent, you'll see entries like:

```markdown
### 2025-12-19 10:30:45

**Session ID:** `abc12345...`
**Duration:** 5234ms | **Turns:** 3 | **Outcome:** SUCCESS
**Cost:** $0.0123

**Tool Sequence:**
1. Read → ✓ success (agent.py)
2. Grep → ✓ success (def.*main)
3. Read → ✓ success (reliability_hooks.py)

---
```

## Troubleshooting

### "claude-agent-sdk not installed"
```bash
pip install claude-agent-sdk
```

### "reliability_logger not found"
The agent looks for `reliability_logger.py` in `AgentFactory/scripts/`. Make sure you're running from within the AgentFactory structure, or copy the logger to your project.

### Logs not populating
Check that:
1. The agent is running (not just starting up)
2. You're actually using tools (ask it to read a file)
3. You exit cleanly (`exit` or `quit`) to trigger the Stop hook
