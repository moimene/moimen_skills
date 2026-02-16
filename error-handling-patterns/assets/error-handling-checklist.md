# Error Handling Checklist

Use this checklist when reviewing error handling in your code.

## Input Validation

- [ ] All user inputs are validated before use
- [ ] Validation errors return specific field information
- [ ] Invalid inputs fail fast (early in the function)
- [ ] Validation messages are user-friendly

## Exception Handling

- [ ] Custom exceptions extend a base application exception
- [ ] Exceptions include error codes for programmatic handling
- [ ] Exceptions include contextual details (IDs, timestamps)
- [ ] Exception messages are descriptive and actionable
- [ ] No bare `except:` or `catch(Exception)` without re-throw

## Resource Management

- [ ] Files, connections, and handles are properly closed
- [ ] Using context managers / try-finally / defer
- [ ] Cleanup runs even when errors occur
- [ ] No resource leaks in error paths

## Logging

- [ ] Errors are logged with full stack traces
- [ ] Log includes correlation IDs for request tracing
- [ ] Sensitive data is redacted from logs
- [ ] Log levels are appropriate (error vs warning vs info)
- [ ] Expected failures don't spam error logs

## External Services

- [ ] Timeouts configured for all external calls
- [ ] Retry logic with exponential backoff where appropriate
- [ ] Circuit breaker for frequently failing services
- [ ] Fallback behavior when services are unavailable

## API Responses

- [ ] Error responses follow consistent format
- [ ] HTTP status codes are semantically correct
- [ ] Error messages don't leak internal details
- [ ] Stack traces not exposed in production

## Async/Concurrent Code

- [ ] All promises have error handlers
- [ ] Unhandled rejection handlers are configured
- [ ] Concurrent errors are collected, not lost
- [ ] Timeouts prevent indefinite hangs
- [ ] Graceful shutdown cancels pending operations

## Testing

- [ ] Unit tests cover error paths
- [ ] Integration tests verify error responses
- [ ] Edge cases and boundary conditions tested
- [ ] Retry/fallback logic is tested
- [ ] Error messages are verified

## Quick Reference

| Situation | Pattern |
|-----------|---------|
| Expected failure | Result type or specific exception |
| Unexpected failure | Log + generic error |
| Transient error | Retry with backoff |
| Dependency down | Circuit breaker + fallback |
| Partial failure | Collect errors, continue processing |
| Critical error | Fail fast, alert, compensate |
