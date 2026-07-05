# Bug Fix Agent

[![CI](https://github.com/kogunlowo123/bug-fix-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/bug-fix-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Software Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Automated bug diagnosis and repair agent that reproduces bugs from issue descriptions, performs root cause analysis via stack traces and logs, generates targeted fixes with regression tests, and validates fixes don't introduce new issues.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `reproduce_bug` | Generate a minimal reproduction case from bug description |
| `analyze_root_cause` | Trace the root cause from error logs and stack traces |
| `generate_fix` | Generate a targeted fix for the identified root cause |
| `generate_regression_test` | Generate a test that catches this specific bug |
| `validate_fix` | Run full test suite to verify fix doesn't break anything |
| `search_similar_bugs` | Find similar past bugs and their fixes |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/bugs/reproduce` | Generate bug reproduction |
| `POST` | `/api/v1/bugs/diagnose` | Analyze root cause |
| `POST` | `/api/v1/bugs/fix` | Generate targeted fix |
| `POST` | `/api/v1/bugs/regression-test` | Generate regression test |
| `POST` | `/api/v1/bugs/validate` | Validate fix against test suite |
| `POST` | `/api/v1/bugs/similar` | Search for similar past bugs |

## Features

- Bug Reproduction
- Root Cause Analysis
- Fix Generation
- Regression Testing
- Fix Validation

## Integrations

- Github Connector
- Gitlab Connector
- Jira
- Sentry Connector
- Test Runner

## Architecture

```
bug-fix-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── bug_fix_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LLM + Debugger Integration + Test Runner**

---

Built as part of the Enterprise AI Agent Platform.
