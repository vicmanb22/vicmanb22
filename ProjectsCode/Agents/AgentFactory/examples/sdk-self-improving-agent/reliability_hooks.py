"""
Reliability Hooks - SDK hooks for automated Phase 1 tracking

These hooks integrate with the Claude Agent SDK to automatically log
all tool usage and session outcomes.
"""

import sys
from pathlib import Path
from typing import Any, Optional

# Add the AgentFactory scripts to path for reliability_logger
AGENTFACTORY_SCRIPTS = Path(__file__).parent.parent.parent / "scripts"
if str(AGENTFACTORY_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(AGENTFACTORY_SCRIPTS))

try:
    from reliability_logger import ReliabilityLogger, get_logger
    LOGGER_AVAILABLE = True
except ImportError:
    print("Warning: reliability_logger not found. Auto-logging disabled.")
    LOGGER_AVAILABLE = False

# Import HookMatcher from the SDK
try:
    from claude_agent_sdk import HookMatcher
except ImportError:
    # Fallback for when SDK is not installed (e.g., during testing)
    class HookMatcher:
        def __init__(self, hooks=None, matcher=None, timeout=None):
            self.hooks = hooks or []
            self.matcher = matcher
            self.timeout = timeout


def create_hooks(log_path: str = "./reliability-log.md") -> dict:
    """
    Create a complete hooks configuration for reliability logging.

    Args:
        log_path: Path to the reliability-log.md file

    Returns:
        A hooks dict ready to pass to ClaudeAgentOptions
    """
    if not LOGGER_AVAILABLE:
        return {}

    logger = get_logger(log_path)

    async def pre_tool_hook(
        input_data: dict[str, Any],
        tool_use_id: Optional[str],
        context: Any
    ) -> dict[str, Any]:
        """
        PreToolUse hook - logs tool invocation before execution.
        """
        tool_name = input_data.get("tool_name", "unknown")
        tool_input = input_data.get("tool_input", {})

        if tool_use_id:
            logger.log_tool_use(tool_name, tool_input, tool_use_id)

        return {}

    async def post_tool_hook(
        input_data: dict[str, Any],
        tool_use_id: Optional[str],
        context: Any
    ) -> dict[str, Any]:
        """
        PostToolUse hook - logs tool result after execution.
        """
        tool_result = input_data.get("tool_result", {})

        is_error = False
        error_message = None

        if isinstance(tool_result, dict):
            is_error = tool_result.get("is_error", False)
            if is_error:
                content = tool_result.get("content", "")
                if isinstance(content, str):
                    error_message = content
                elif isinstance(content, list) and content:
                    for block in content:
                        if isinstance(block, dict) and block.get("type") == "text":
                            error_message = block.get("text", "")
                            break

        if tool_use_id:
            logger.log_tool_result(tool_use_id, success=not is_error, error_message=error_message)

        return {}

    async def stop_hook(
        input_data: dict[str, Any],
        tool_use_id: Optional[str],
        context: Any
    ) -> dict[str, Any]:
        """
        Stop hook - logs complete session summary when agent finishes.
        """
        session_id = input_data.get("session_id", "unknown")
        duration_ms = input_data.get("duration_ms", 0)
        num_turns = input_data.get("num_turns", 0)
        total_cost_usd = input_data.get("total_cost_usd")
        is_error = input_data.get("is_error", False)
        result = input_data.get("result", "")

        result_summary = None
        if result:
            result_summary = str(result)[:200]

        logger.log_session_end(
            session_id=session_id,
            duration_ms=duration_ms,
            num_turns=num_turns,
            total_cost_usd=total_cost_usd,
            is_error=is_error,
            result_summary=result_summary
        )

        return {}

    return {
        "PreToolUse": [HookMatcher(hooks=[pre_tool_hook])],
        "PostToolUse": [HookMatcher(hooks=[post_tool_hook])],
        "Stop": [HookMatcher(hooks=[stop_hook])]
    }
