"""
Reliability Hooks Template - SDK hooks for automated Phase 1 tracking

These hooks integrate with the Claude Agent SDK to automatically log
all tool usage and session outcomes. Copy this file to your agent
directory and customize as needed.

Usage in your SDK agent:
    from reliability_hooks import create_reliability_hooks

    options = ClaudeAgentOptions(
        hooks=create_reliability_hooks("./reliability-log.md")
    )
"""

import sys
from pathlib import Path
from typing import Any, Optional

# Add the AgentFactory scripts to path for reliability_logger
AGENT_FACTORY_SCRIPTS = Path(__file__).parent.parent / "scripts"
if str(AGENT_FACTORY_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(AGENT_FACTORY_SCRIPTS))

from reliability_logger import ReliabilityLogger, get_logger


def create_reliability_hooks(log_path: str = "./reliability-log.md") -> dict:
    """
    Create a complete hooks configuration for reliability logging.

    Args:
        log_path: Path to the reliability-log.md file

    Returns:
        A hooks dict ready to pass to ClaudeAgentOptions
    """
    logger = get_logger(log_path)

    async def pre_tool_hook(
        input_data: dict[str, Any],
        tool_use_id: Optional[str],
        context: Any
    ) -> dict[str, Any]:
        """
        PreToolUse hook - logs tool invocation before execution.

        This captures:
        - Which tool is being called
        - What inputs are being passed
        - Timestamp of the call
        """
        tool_name = input_data.get("tool_name", "unknown")
        tool_input = input_data.get("tool_input", {})

        if tool_use_id:
            logger.log_tool_use(tool_name, tool_input, tool_use_id)

        # Don't modify the tool call - just observe
        return {}

    async def post_tool_hook(
        input_data: dict[str, Any],
        tool_use_id: Optional[str],
        context: Any
    ) -> dict[str, Any]:
        """
        PostToolUse hook - logs tool result after execution.

        This captures:
        - Success or failure
        - Error messages (if any)
        - Links result to the original tool_use_id
        """
        tool_result = input_data.get("tool_result", {})

        # Determine if this was an error
        is_error = False
        error_message = None

        if isinstance(tool_result, dict):
            is_error = tool_result.get("is_error", False)
            if is_error:
                content = tool_result.get("content", "")
                if isinstance(content, str):
                    error_message = content
                elif isinstance(content, list) and content:
                    # Extract text from content blocks
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

        This captures:
        - Total session duration
        - Number of conversation turns
        - Overall success/failure
        - Cost (if available)
        """
        session_id = input_data.get("session_id", "unknown")
        duration_ms = input_data.get("duration_ms", 0)
        num_turns = input_data.get("num_turns", 0)
        total_cost_usd = input_data.get("total_cost_usd")
        is_error = input_data.get("is_error", False)
        result = input_data.get("result", "")

        # Summarize the result
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

    # Return the hooks configuration
    # Note: HookMatcher is imported from claude_agent_sdk in the actual implementation
    return {
        "PreToolUse": [
            {"hooks": [pre_tool_hook]}
        ],
        "PostToolUse": [
            {"hooks": [post_tool_hook]}
        ],
        "Stop": [
            {"hooks": [stop_hook]}
        ]
    }


# Pre-built hook functions for direct use
# These can be passed to HookMatcher directly

async def log_pre_tool(input_data: dict, tool_use_id: str | None, context: Any) -> dict:
    """Standalone PreToolUse logging hook."""
    logger = get_logger()
    tool_name = input_data.get("tool_name", "unknown")
    tool_input = input_data.get("tool_input", {})
    if tool_use_id:
        logger.log_tool_use(tool_name, tool_input, tool_use_id)
    return {}


async def log_post_tool(input_data: dict, tool_use_id: str | None, context: Any) -> dict:
    """Standalone PostToolUse logging hook."""
    logger = get_logger()
    tool_result = input_data.get("tool_result", {})
    is_error = tool_result.get("is_error", False) if isinstance(tool_result, dict) else False
    error_msg = None
    if is_error and isinstance(tool_result, dict):
        content = tool_result.get("content", "")
        error_msg = content if isinstance(content, str) else str(content)[:100]
    if tool_use_id:
        logger.log_tool_result(tool_use_id, success=not is_error, error_message=error_msg)
    return {}


async def log_session_stop(input_data: dict, tool_use_id: str | None, context: Any) -> dict:
    """Standalone Stop logging hook."""
    logger = get_logger()
    logger.log_session_end(
        session_id=input_data.get("session_id", "unknown"),
        duration_ms=input_data.get("duration_ms", 0),
        num_turns=input_data.get("num_turns", 0),
        total_cost_usd=input_data.get("total_cost_usd"),
        is_error=input_data.get("is_error", False),
        result_summary=str(input_data.get("result", ""))[:200] if input_data.get("result") else None
    )
    return {}
