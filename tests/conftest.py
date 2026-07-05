"""Test configuration for Bug Fix Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "bug-fix-agent", "category": "Software Engineering"}
