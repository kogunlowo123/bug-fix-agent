"""Bug Fix Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class BugReport(BaseModel):
    """BugReport for Bug Fix Agent."""
    title: str
    description: str
    stack_trace: str | None = None
    steps_to_reproduce: list[str] | None = None
    severity: str = 'medium'


class RootCauseAnalysis(BaseModel):
    """RootCauseAnalysis for Bug Fix Agent."""
    root_cause: str
    affected_files: list[str]
    confidence: float
    evidence: list[str]


class BugFix(BaseModel):
    """BugFix for Bug Fix Agent."""
    fix_description: str
    changed_files: dict[str, str]
    regression_test: str
    risk_assessment: str

