"""Bug Fix Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_reproduce_bug():
    """Test Generate a minimal reproduction case from bug description."""
    tools = AgentTools()
    result = await tools.reproduce_bug(bug_description="test", stack_trace="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_root_cause():
    """Test Trace the root cause from error logs and stack traces."""
    tools = AgentTools()
    result = await tools.analyze_root_cause(error="test", stack_trace="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_fix():
    """Test Generate a targeted fix for the identified root cause."""
    tools = AgentTools()
    result = await tools.generate_fix(root_cause="test", affected_code="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_regression_test():
    """Test Generate a test that catches this specific bug."""
    tools = AgentTools()
    result = await tools.generate_regression_test(bug_description="test", fix_code="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.bug_fix_agent_agent import BugFixAgentAgent
    agent = BugFixAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
