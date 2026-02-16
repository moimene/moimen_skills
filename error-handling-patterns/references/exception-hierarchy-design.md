# Exception Hierarchy Design

Guide for designing custom exception hierarchies in your applications.

## Principles

1. **Single Base Exception**: All custom exceptions inherit from one base
2. **Semantic Naming**: Name describes the problem, not the location
3. **Minimal Depth**: 2-3 levels maximum
4. **Include Context**: Exceptions carry useful debugging data

## Recommended Structure

```
ApplicationError (base)
├── ValidationError
│   ├── RequiredFieldError
│   └── InvalidFormatError
├── NotFoundError
│   ├── UserNotFoundError
│   └── ResourceNotFoundError
├── AuthorizationError
│   ├── AuthenticationError
│   └── PermissionDeniedError
├── ExternalServiceError
│   ├── NetworkError
│   └── TimeoutError
└── ConflictError
    └── DuplicateEntryError
```

## Base Exception Template

### Python

```python
from datetime import datetime
from typing import Optional, Dict, Any

class ApplicationError(Exception):
    """Base exception with context tracking."""
    
    default_code = "APPLICATION_ERROR"
    default_status = 500
    
    def __init__(
        self,
        message: str,
        code: str = None,
        status: int = None,
        details: Dict[str, Any] = None,
        cause: Exception = None
    ):
        super().__init__(message)
        self.code = code or self.default_code
        self.status = status or self.default_status
        self.details = details or {}
        self.cause = cause
        self.timestamp = datetime.utcnow()
    
    def to_dict(self) -> Dict[str, Any]:
        """Serialize for API responses."""
        return {
            "error": self.code,
            "message": str(self),
            "details": self.details,
            "timestamp": self.timestamp.isoformat()
        }
```

### TypeScript

```typescript
interface ErrorContext {
  code: string;
  statusCode: number;
  details?: Record<string, any>;
  cause?: Error;
  timestamp: Date;
}

abstract class ApplicationError extends Error {
  readonly code: string;
  readonly statusCode: number;
  readonly details: Record<string, any>;
  readonly cause?: Error;
  readonly timestamp: Date;

  constructor(message: string, context: Partial<ErrorContext> = {}) {
    super(message);
    this.name = this.constructor.name;
    this.code = context.code || 'APPLICATION_ERROR';
    this.statusCode = context.statusCode || 500;
    this.details = context.details || {};
    this.cause = context.cause;
    this.timestamp = new Date();
    Error.captureStackTrace(this, this.constructor);
  }

  toJSON(): object {
    return {
      error: this.code,
      message: this.message,
      details: this.details,
      timestamp: this.timestamp.toISOString()
    };
  }
}
```

## Anti-Patterns

❌ **Too Generic**
```python
class MyException(Exception):
    pass
```

❌ **Too Deep**
```python
class UserValidationEmailFormatError(UserValidationError):  # 4+ levels
    pass
```

❌ **Location-Based Naming**
```python
class UserServiceException(Exception):  # Names the location, not the problem
    pass
```

✅ **Correct Approach**
```python
class ValidationError(ApplicationError):
    default_code = "VALIDATION_ERROR"
    default_status = 400
    
    def __init__(self, field: str, message: str, **kwargs):
        super().__init__(f"{field}: {message}", **kwargs)
        self.details["field"] = field
```
