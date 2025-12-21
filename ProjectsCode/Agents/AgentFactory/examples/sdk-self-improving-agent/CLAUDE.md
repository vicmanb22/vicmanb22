# SDK Self-Improving Agent Example

A complete working example of a self-improving agent using the Claude Agent SDK with automated reliability logging.

## What This Example Demonstrates

1. **SDK-based agent** - Uses `ClaudeSDKClient` for multi-turn conversations
2. **Automated logging** - Hooks auto-populate `reliability-log.md`
3. **Phase 1 tracking** - Every tool use and session is recorded
4. **Zero friction** - No manual feedback required

## Files

```
sdk-self-improving-agent/
├── CLAUDE.md                 # This file
├── agent.py                  # Main agent script
├── reliability_hooks.py      # Hook implementations
├── reliability-log.md        # Auto-populated log
└── README.md                 # Usage instructions
```

## How to Run

```bash
# Install dependencies
pip install claude-agent-sdk

# Run the agent
python agent.py
```

## How Auto-Logging Works

1. **PreToolUse hook** fires before every tool → logs tool name and inputs
2. **PostToolUse hook** fires after every tool → logs success/failure
3. **Stop hook** fires when session ends → logs session summary

All logging is automatic. The `reliability-log.md` file grows with each session.

## Two-Phase Maturity Model

### Phase 1: LLM-Driven (Current)
- Agent uses LLM reasoning for all tasks
- Hooks auto-log every action
- Target reliability: 75-90%

### Phase 2: Code-Driven (Future)
- When patterns detected → scripts proposed
- Human approves → scripts created
- Agent runs scripts instead of re-reasoning
- Target reliability: 99%+

## Customizing

To create your own SDK self-improving agent:

1. Copy this example directory
2. Edit `agent.py`:
   - Change `AGENT_NAME` and `AGENT_DESCRIPTION`
   - Customize `SYSTEM_PROMPT`
   - Adjust `ALLOWED_TOOLS`
3. Run and watch `reliability-log.md` populate
