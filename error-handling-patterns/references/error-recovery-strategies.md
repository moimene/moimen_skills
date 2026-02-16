# Error Recovery Strategies

Patterns for recovering from errors gracefully.

## Strategy Matrix

| Error Type | Strategy | Example |
|------------|----------|---------|
| Transient | Retry with backoff | Network timeout |
| Rate limit | Wait and retry | API 429 response |
| Stale data | Refresh and retry | Cache miss |
| Partial failure | Compensate | Rollback transaction |
| Dependency down | Circuit break | Service unavailable |
| Invalid input | Reject fast | Validation error |

## Retry Strategies

### Exponential Backoff

```python
import time
import random

def retry_with_backoff(
    func,
    max_retries=3,
    base_delay=1.0,
    max_delay=60.0,
    jitter=True
):
    for attempt in range(max_retries):
        try:
            return func()
        except RetryableError as e:
            if attempt == max_retries - 1:
                raise
            
            delay = min(base_delay * (2 ** attempt), max_delay)
            if jitter:
                delay *= (0.5 + random.random())
            
            time.sleep(delay)
```

### Retry Budget

```python
class RetryBudget:
    """Limit retries across all operations."""
    
    def __init__(self, max_retries_per_minute=100):
        self.max_retries = max_retries_per_minute
        self.retries = []
    
    def can_retry(self) -> bool:
        now = time.time()
        self.retries = [t for t in self.retries if now - t < 60]
        return len(self.retries) < self.max_retries
    
    def record_retry(self):
        self.retries.append(time.time())
```

## Fallback Strategies

### Primary/Secondary

```python
def get_data(key: str) -> Data:
    try:
        return primary_cache.get(key)
    except CacheError:
        return secondary_cache.get(key)
```

### Degraded Mode

```python
def get_recommendations(user_id: str) -> List[Item]:
    try:
        return personalization_service.get(user_id)
    except ServiceError:
        # Fall back to popular items
        return get_popular_items()
```

### Default Values

```python
def get_config(key: str, default: Any = None) -> Any:
    try:
        return config_service.get(key)
    except ConfigError:
        logger.warning(f"Using default for {key}")
        return default
```

## Compensation Patterns

### Saga Pattern

```python
class OrderSaga:
    def __init__(self):
        self.steps_completed = []
    
    def execute(self, order: Order):
        try:
            self.reserve_inventory(order)
            self.steps_completed.append("inventory")
            
            self.charge_payment(order)
            self.steps_completed.append("payment")
            
            self.send_confirmation(order)
            self.steps_completed.append("confirmation")
            
        except Exception as e:
            self.compensate()
            raise
    
    def compensate(self):
        for step in reversed(self.steps_completed):
            if step == "payment":
                self.refund_payment()
            elif step == "inventory":
                self.release_inventory()
```

## Decision Tree

```
Error occurs
    │
    ├─ Is it retryable?
    │   ├─ Yes → Has retry budget?
    │   │         ├─ Yes → Retry with backoff
    │   │         └─ No → Use fallback
    │   └─ No → Is there a fallback?
    │           ├─ Yes → Use fallback
    │           └─ No → Fail gracefully
    │
    └─ Should we compensate?
        ├─ Yes → Run compensation logic
        └─ No → Log and propagate
```
