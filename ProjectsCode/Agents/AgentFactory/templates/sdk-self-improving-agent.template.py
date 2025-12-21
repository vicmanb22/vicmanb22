"""
{{AGENT_NAME}} - Self-Improving Agent (SDK Version)

Phase 1: LLM-Driven with automated reliability logging
Phase 2: Graduates to code-driven when patterns detected

This template creates an SDK-based agent with automatic reliability
tracking via hooks. No manual feedback required - logs populate
automatically after every tool use and session.

SETUP:
1. Install the Claude Agent SDK: pip install claude-agent-sdk
2. Copy this template to your agent directory
3. Customize the system prompt and tools
4. Run: python agent.py

TEMPLATE VARIABLES (replace with actual values):
- {{AGENT_NAME}}: Your agent's name
- {{AGENT_DESCRIPTION}}: What your agent does
- {{SYSTEM_PROMPT}}: The agent's system prompt/instructions
- {{TOOLS}}: List of allowed tools, e.g., ["Read", "Write", "Edit"]
- {{PERMISSION_MODE}}: One of "default", "acceptEdits", "bypassPermissions"
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

# Import reliability logging hooks
# Adjust this path based on your project structure
AGENT_DIR = Path(__file__).parent
SCRIPTS_DIR = AGENT_DIR / "scripts"
AGENTFACTORY_SCRIPTS = Path(__file__).parent.parent / "scripts"

# Add paths for imports
for path in [SCRIPTS_DIR, AGENTFACTORY_SCRIPTS]:
    if path.exists() and str(path) not in sys.path:
        sys.path.insert(0, str(path))

try:
    from reliability_logger import get_logger
except ImportError:
    print("Warning: reliability_logger not found. Auto-logging disabled.")
    get_logger = None


# ============================================================================
# CONFIGURATION - Customize these for your agent
# ============================================================================

AGENT_NAME = "{{AGENT_NAME}}"
AGENT_DESCRIPTION = "{{AGENT_DESCRIPTION}}"

SYSTEM_PROMPT = """{{SYSTEM_PROMPT}}

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
**Graduation to Phase 2:** When workflows are codified to scripts

Check `reliability-log.md` to see your performance data.
"""

ALLOWED_TOOLS = {{TOOLS}}  # e.g., ["Read", "Write", "Edit", "Glob", "Grep", "Bash"]
PERMISSION_MODE = "{{PERMISSION_MODE}}"  # "default", "acceptEdits", or "bypassPermissions"
RELIABILITY_LOG = AGENT_DIR / "reliability-log.md"


# ============================================================================
# RELIABILITY HOOKS
# ============================================================================

def create_hooks(log_path: Path) -> dict:
    """Create reliability logging hooks for this agent."""
    if get_logger is None:
        return {}

    logger = get_logger(str(log_path))

    async def pre_tool_hook(
        input_data: dict[str, Any],
        tool_use_id: str | None,
        context: Any
    ) -> dict[str, Any]:
        """Log tool invocation before execution."""
        tool_name = input_data.get("tool_name", "unknown")
        tool_input = input_data.get("tool_input", {})
        if tool_use_id:
            logger.log_tool_use(tool_name, tool_input, tool_use_id)
        return {}

    async def post_tool_hook(
        input_data: dict[str, Any],
        tool_use_id: str | None,
        context: Any
    ) -> dict[str, Any]:
        """Log tool result after execution."""
        tool_result = input_data.get("tool_result", {})
        is_error = tool_result.get("is_error", False) if isinstance(tool_result, dict) else False
        error_msg = None
        if is_error and isinstance(tool_result, dict):
            content = tool_result.get("content", "")
            error_msg = content if isinstance(content, str) else str(content)[:100]
        if tool_use_id:
            logger.log_tool_result(tool_use_id, success=not is_error, error_message=error_msg)
        return {}

    async def stop_hook(
        input_data: dict[str, Any],
        tool_use_id: str | None,
        context: Any
    ) -> dict[str, Any]:
        """Log session summary when agent finishes."""
        logger.log_session_end(
            session_id=input_data.get("session_id", "unknown"),
            duration_ms=input_data.get("duration_ms", 0),
            num_turns=input_data.get("num_turns", 0),
            total_cost_usd=input_data.get("total_cost_usd"),
            is_error=input_data.get("is_error", False),
            result_summary=str(input_data.get("result", ""))[:200] if input_data.get("result") else None
        )
        return {}

    return {
        "PreToolUse": [HookMatcher(hooks=[pre_tool_hook])],
        "PostToolUse": [HookMatcher(hooks=[post_tool_hook])],
        "Stop": [HookMatcher(hooks=[stop_hook])]
    }


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
            print(f"\n[Session completed - {message.num_turns} turns, {message.duration_ms}ms]")


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
    print(f"Type 'exit' or 'quit' to end the session")
    print(f"{'='*60}\n")

    # Create options with reliability hooks
    hooks = create_hooks(RELIABILITY_LOG)

    options = ClaudeAgentOptions(
        system_prompt=SYSTEM_PROMPT,
        allowed_tools=ALLOWED_TOOLS,
        permission_mode=PERMISSION_MODE,
        hooks=hooks if hooks else None
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
