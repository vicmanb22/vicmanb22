"""
Code Assistant - Self-Improving Agent (SDK Version)

A demo self-improving agent that helps with code-related tasks.
This agent automatically tracks its reliability via SDK hooks.

Run: python agent.py
"""

import asyncio
import sys
from pathlib import Path
from typing import Any

# Claude Agent SDK imports
try:
    from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, HookMatcher
    from claude_agent_sdk import AssistantMessage, TextBlock, ToolUseBlock, ResultMessage
except ImportError:
    print("Error: claude-agent-sdk not installed")
    print("Run: pip install claude-agent-sdk")
    sys.exit(1)

# Import reliability hooks
from reliability_hooks import create_hooks


# ============================================================================
# CONFIGURATION
# ============================================================================

AGENT_NAME = "Code Assistant"
AGENT_DESCRIPTION = "A self-improving agent that helps with code-related tasks."

SYSTEM_PROMPT = """You are Code Assistant, a helpful agent that assists with code-related tasks.

## Capabilities
- Read and analyze code files
- Search for patterns in codebases
- Explain code and suggest improvements
- Help with debugging

## Guidelines
- Always read files before making suggestions about them
- Use Grep to search for patterns efficiently
- Provide clear, actionable feedback
- Be concise but thorough

## Self-Improvement Protocol

You are a Phase 1 (LLM-Driven) self-improving agent. Your reliability is
being tracked automatically via SDK hooks.

**How it works:**
1. Every tool you use is logged automatically (no manual feedback needed)
2. Session outcomes are recorded when you finish
3. Pattern detection analyzes your logs for improvements
4. When 3+ similar failures detected → directive improvements proposed
5. When 3+ similar successes detected → codification to scripts proposed

**Your current phase:** Phase 1 (LLM-Driven)
**Target reliability:** 75-90%
"""

ALLOWED_TOOLS = ["Read", "Glob", "Grep", "Write", "Edit"]
PERMISSION_MODE = "acceptEdits"

AGENT_DIR = Path(__file__).parent
RELIABILITY_LOG = AGENT_DIR / "reliability-log.md"


# ============================================================================
# MESSAGE DISPLAY
# ============================================================================

def print_message(message: Any) -> None:
    """Pretty-print a message from the agent."""
    if isinstance(message, AssistantMessage):
        for block in message.content:
            if isinstance(block, TextBlock):
                print(f"\n{AGENT_NAME}: {block.text}")
            elif isinstance(block, ToolUseBlock):
                print(f"\n[Using tool: {block.name}]")
    elif isinstance(message, ResultMessage):
        if message.is_error:
            print(f"\n[Session ended with error]")
        else:
            cost_str = f", ${message.total_cost_usd:.4f}" if message.total_cost_usd else ""
            print(f"\n[Session completed - {message.num_turns} turns, {message.duration_ms}ms{cost_str}]")


# ============================================================================
# MAIN AGENT LOOP
# ============================================================================

async def run_agent():
    """Run the self-improving agent with automatic reliability logging."""
    print(f"\n{'='*60}")
    print(f"{AGENT_NAME}")
    print(f"{AGENT_DESCRIPTION}")
    print(f"{'='*60}")
    print(f"\nPhase 1 (LLM-Driven) - Auto-logging enabled")
    print(f"Reliability log: {RELIABILITY_LOG}")
    print(f"\nType 'exit' or 'quit' to end the session")
    print(f"{'='*60}\n")

    # Create options with reliability hooks
    hooks = create_hooks(str(RELIABILITY_LOG))

    options = ClaudeAgentOptions(
        system_prompt=SYSTEM_PROMPT,
        allowed_tools=ALLOWED_TOOLS,
        permission_mode=PERMISSION_MODE,
        hooks=hooks,
        cwd=str(AGENT_DIR)
    )

    async with ClaudeSDKClient(options=options) as client:
        while True:
            try:
                user_input = input("\nYou: ").strip()

                if not user_input:
                    continue

                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("\nEnding session...")
                    break

                # Send message to agent
                await client.query(user_input)

                # Process and display response
                async for message in client.receive_response():
                    print_message(message)

            except KeyboardInterrupt:
                print("\n\nInterrupted. Ending session...")
                break
            except Exception as e:
                print(f"\nError: {e}")
                continue

    print(f"\n{'='*60}")
    print(f"Session ended. Check {RELIABILITY_LOG.name} for performance data.")
    print(f"{'='*60}\n")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    asyncio.run(run_agent())
