"""
Reliability Logger - Core logging utility for automated Phase 1 tracking

This module provides functions to write structured reliability data to
reliability-log.md files. Used by SDK hooks to auto-populate logs without
requiring manual user feedback.

Usage:
    from reliability_logger import ReliabilityLogger

    logger = ReliabilityLogger(log_path="./reliability-log.md")
    logger.log_tool_use("Read", {"file_path": "/path/to/file"}, "tool_123")
    logger.log_tool_result("tool_123", success=True)
    logger.log_session_end(session_id="abc", duration_ms=5000, num_turns=3)
"""

from datetime import datetime
from pathlib import Path
import json
import re
from typing import Any, Optional, Union
from dataclasses import dataclass, field, asdict


@dataclass
class ToolUseEntry:
    """A single tool use event."""
    timestamp: str
    tool_name: str
    tool_use_id: str
    input_summary: str


@dataclass
class ToolResultEntry:
    """Result of a tool execution."""
    timestamp: str
    tool_use_id: str
    outcome: str  # "success" or "failure"
    error_message: Optional[str] = None


@dataclass
class SessionEntry:
    """Summary of a complete session."""
    timestamp: str
    session_id: str
    duration_ms: int
    num_turns: int
    total_cost_usd: Optional[float] = None
    is_error: bool = False
    tool_sequence: list = field(default_factory=list)
    outcome: str = "success"  # "success", "failure", "partial"
    result_summary: Optional[str] = None


class ReliabilityLogger:
    """
    Writes reliability data to a markdown log file.

    The log format supports both human readability and machine parsing
    for future pattern detection.
    """

    def __init__(self, log_path: Union[str, Path]):
        self.log_path = Path(log_path)
        self._current_session_tools: list[dict] = []
        self._ensure_log_exists()

    def _ensure_log_exists(self):
        """Create the log file with headers if it doesn't exist."""
        if not self.log_path.exists():
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
            self._write_initial_log()

    def _write_initial_log(self):
        """Write the initial log structure."""
        initial_content = """# Reliability Log

## Overview

This log is **automatically populated** by SDK hooks. No manual feedback required.

**Phase:** 1 (LLM-Driven)
**Auto-logging:** Enabled

---

## Summary Statistics

<!-- AUTO-UPDATED: Do not edit manually -->
| Metric | Value |
|--------|-------|
| Total Sessions | 0 |
| Success Rate | N/A |
| Total Tool Uses | 0 |
| Last Updated | Never |

---

## Session Logs

<!-- New sessions are appended below -->
"""
        self.log_path.write_text(initial_content)

    def log_tool_use(self, tool_name: str, tool_input: dict, tool_use_id: str):
        """
        Log a tool use event. Called by PreToolUse hook.

        Args:
            tool_name: Name of the tool (e.g., "Read", "Write", "Bash")
            tool_input: The input parameters passed to the tool
            tool_use_id: Unique identifier for this tool use
        """
        entry = ToolUseEntry(
            timestamp=datetime.now().isoformat(),
            tool_name=tool_name,
            tool_use_id=tool_use_id,
            input_summary=self._summarize_input(tool_name, tool_input)
        )

        # Store for session summary
        self._current_session_tools.append({
            "tool": tool_name,
            "input": entry.input_summary,
            "tool_use_id": tool_use_id,
            "outcome": None  # Will be filled by log_tool_result
        })

    def log_tool_result(self, tool_use_id: str, success: bool, error_message: Optional[str] = None):
        """
        Log a tool result. Called by PostToolUse hook.

        Args:
            tool_use_id: The tool use ID to update
            success: Whether the tool execution succeeded
            error_message: Error message if failed
        """
        # Update the stored tool entry
        for tool in self._current_session_tools:
            if tool.get("tool_use_id") == tool_use_id:
                tool["outcome"] = "success" if success else "failure"
                if error_message:
                    tool["error"] = error_message[:100]  # Truncate long errors
                break

    def log_session_end(
        self,
        session_id: str,
        duration_ms: int,
        num_turns: int,
        total_cost_usd: Optional[float] = None,
        is_error: bool = False,
        result_summary: Optional[str] = None
    ):
        """
        Log the end of a session with full summary. Called by Stop hook.

        This writes the complete session entry to the log file.
        """
        # Determine overall outcome
        failures = sum(1 for t in self._current_session_tools if t.get("outcome") == "failure")
        successes = sum(1 for t in self._current_session_tools if t.get("outcome") == "success")

        if is_error or failures > successes:
            outcome = "failure"
        elif failures > 0:
            outcome = "partial"
        else:
            outcome = "success"

        session = SessionEntry(
            timestamp=datetime.now().isoformat(),
            session_id=session_id,
            duration_ms=duration_ms,
            num_turns=num_turns,
            total_cost_usd=total_cost_usd,
            is_error=is_error,
            tool_sequence=self._current_session_tools.copy(),
            outcome=outcome,
            result_summary=result_summary
        )

        # Append to log file
        self._append_session(session)

        # Update summary statistics
        self._update_summary_stats()

        # Clear current session
        self._current_session_tools = []

    def _append_session(self, session: SessionEntry):
        """Append a session entry to the log file."""
        content = self.log_path.read_text()

        # Format the session entry
        session_md = self._format_session_markdown(session)

        # Append after "## Session Logs" section
        content += "\n" + session_md

        self.log_path.write_text(content)

    def _format_session_markdown(self, session: SessionEntry) -> str:
        """Format a session as markdown."""
        lines = [
            f"### {session.timestamp[:10]} {session.timestamp[11:19]}",
            "",
            f"**Session ID:** `{session.session_id[:8]}...`",
            f"**Duration:** {session.duration_ms}ms | **Turns:** {session.num_turns} | **Outcome:** {session.outcome.upper()}",
        ]

        if session.total_cost_usd is not None:
            lines.append(f"**Cost:** ${session.total_cost_usd:.4f}")

        lines.append("")
        lines.append("**Tool Sequence:**")

        for i, tool in enumerate(session.tool_sequence, 1):
            outcome_emoji = "✓" if tool.get("outcome") == "success" else "✗"
            tool_line = f"{i}. {tool['tool']} → {outcome_emoji} {tool.get('outcome', 'unknown')}"
            if tool.get("input"):
                tool_line += f" ({tool['input']})"
            if tool.get("error"):
                tool_line += f" - Error: {tool['error']}"
            lines.append(tool_line)

        if session.result_summary:
            lines.append("")
            lines.append(f"**Result:** {session.result_summary[:200]}")

        lines.append("")
        lines.append("---")
        lines.append("")

        return "\n".join(lines)

    def _update_summary_stats(self):
        """Update the summary statistics table in the log."""
        content = self.log_path.read_text()

        # Parse existing sessions to calculate stats
        sessions = self._parse_sessions(content)

        total_sessions = len(sessions)
        successes = sum(1 for s in sessions if s.get("outcome") == "success")
        success_rate = f"{(successes/total_sessions*100):.0f}%" if total_sessions > 0 else "N/A"

        # Count total tool uses
        total_tools = sum(len(s.get("tools", [])) for s in sessions)

        # Update the summary table
        new_stats = f"""## Summary Statistics

<!-- AUTO-UPDATED: Do not edit manually -->
| Metric | Value |
|--------|-------|
| Total Sessions | {total_sessions} |
| Success Rate | {success_rate} |
| Total Tool Uses | {total_tools} |
| Last Updated | {datetime.now().strftime('%Y-%m-%d %H:%M')} |"""

        # Replace the existing summary section
        pattern = r"## Summary Statistics.*?(?=\n---)"
        content = re.sub(pattern, new_stats, content, flags=re.DOTALL)

        self.log_path.write_text(content)

    def _parse_sessions(self, content: str) -> list[dict]:
        """Parse session entries from log content."""
        sessions = []

        # Find all session blocks
        session_pattern = r"### (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*?(?=### \d{4}|$)"
        matches = re.findall(session_pattern, content, re.DOTALL)

        for match in matches:
            session = {"timestamp": match}

            # Extract outcome
            if "SUCCESS" in content:
                session["outcome"] = "success"
            elif "FAILURE" in content:
                session["outcome"] = "failure"
            else:
                session["outcome"] = "partial"

            # Count tools (simplified)
            tool_matches = re.findall(r"\d+\. (\w+) →", content)
            session["tools"] = tool_matches

            sessions.append(session)

        return sessions

    def _summarize_input(self, tool_name: str, tool_input: dict) -> str:
        """Create a brief summary of tool input."""
        if tool_name == "Read":
            path = tool_input.get("file_path", "")
            return Path(path).name if path else ""
        elif tool_name == "Write":
            path = tool_input.get("file_path", "")
            return Path(path).name if path else ""
        elif tool_name == "Edit":
            path = tool_input.get("file_path", "")
            return Path(path).name if path else ""
        elif tool_name == "Bash":
            cmd = tool_input.get("command", "")
            return cmd[:30] + "..." if len(cmd) > 30 else cmd
        elif tool_name == "Glob":
            return tool_input.get("pattern", "")
        elif tool_name == "Grep":
            return tool_input.get("pattern", "")[:20]
        else:
            return json.dumps(tool_input)[:30]


# Singleton instance for easy import
_default_logger: Optional[ReliabilityLogger] = None

def get_logger(log_path: Union[str, Path] = "./reliability-log.md") -> ReliabilityLogger:
    """Get or create the default reliability logger."""
    global _default_logger
    if _default_logger is None or _default_logger.log_path != Path(log_path):
        _default_logger = ReliabilityLogger(log_path)
    return _default_logger
