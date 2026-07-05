# Bug Fix Agent Architecture

Automated bug diagnosis and repair agent that reproduces bugs from issue descriptions, performs root cause analysis via stack traces and logs, generates targeted fixes with regression tests, and validates fixes don't introduce new issues.

## Domain Tools

- **reproduce_bug**: Generate a minimal reproduction case from bug description
- **analyze_root_cause**: Trace the root cause from error logs and stack traces
- **generate_fix**: Generate a targeted fix for the identified root cause
- **generate_regression_test**: Generate a test that catches this specific bug
- **validate_fix**: Run full test suite to verify fix doesn't break anything
- **search_similar_bugs**: Find similar past bugs and their fixes