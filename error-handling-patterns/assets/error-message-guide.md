# Error Message Guide

Write error messages that help users and developers solve problems.

## Principles

1. **Say what happened** - Clear description of the problem
2. **Say why it happened** - Context about the cause
3. **Say how to fix it** - Actionable next steps

## Structure

```
[What happened]: [Why it happened]. [How to fix it].
```

## Examples

### ❌ Bad Messages

```
Error
Something went wrong
Invalid input
Failed to process
null
undefined
Exception occurred
```

### ✅ Good Messages

**For Users:**
```
Unable to save your document: The file is too large (15MB). 
Please reduce the file size to under 10MB and try again.
```

```
Payment failed: Your card was declined. 
Please check your card details or try a different payment method.
```

```
Session expired for security reasons.
Please sign in again to continue.
```

**For Developers:**
```
Database connection failed: Connection refused to postgres://db:5432.
Verify the database is running and the connection string is correct.
Details: ECONNREFUSED, attempts: 3, timeout: 5000ms
```

```
API request failed: GET /api/users/123 returned 404.
The user may have been deleted or the ID is incorrect.
Request ID: req-abc123, Duration: 245ms
```

## By Error Type

### Validation Errors

```
// Single field
Email address is invalid: "not-an-email" is not a valid email format.

// Multiple fields
Unable to create account:
- Email: already registered
- Password: must be at least 8 characters
- Username: contains invalid characters (use letters and numbers only)
```

### Authentication Errors

```
// Wrong credentials
Sign in failed: The email or password you entered is incorrect.

// Account locked
Account temporarily locked after 5 failed attempts.
Try again in 15 minutes or reset your password.

// Token expired
Your session has expired. Please sign in again.
```

### Authorization Errors

```
// No permission
You don't have permission to delete this project.
Contact the project owner to request access.

// Role required
This action requires administrator privileges.
```

### Resource Errors

```
// Not found
User not found: No user exists with ID "abc123".
The user may have been deleted or the ID is incorrect.

// Conflict
Unable to create user: An account with this email already exists.
Try signing in instead, or use a different email address.
```

### External Service Errors

```
// Service unavailable
Payment processing is temporarily unavailable.
Your payment was not charged. Please try again in a few minutes.

// Timeout
Request timed out: The server took too long to respond.
This might be a temporary issue. Please try again.
```

## Technical Details

Include in logs, not in user-facing messages:

```json
{
  "error": "DATABASE_CONNECTION_FAILED",
  "message": "Unable to connect to database",
  "details": {
    "host": "db.example.com",
    "port": 5432,
    "database": "myapp",
    "error_code": "ECONNREFUSED",
    "attempts": 3,
    "last_attempt": "2024-01-15T10:30:00Z"
  },
  "request_id": "req-abc123",
  "stack": "Error: Connection refused\n    at ..."
}
```

## Localization Tips

1. Keep messages in resource files, not in code
2. Use placeholders for dynamic values: `"User {userId} not found"`
3. Avoid concatenating translated strings
4. Include context for translators
