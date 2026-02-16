# Async Error Handling

Patterns for handling errors in asynchronous and concurrent code.

## Promise/Async-Await Patterns

### Always Handle Rejections

```typescript
// ❌ Unhandled rejection
async function fetchData() {
  const data = await api.get('/data'); // Can throw!
  return data;
}

// ✅ Proper handling
async function fetchData() {
  try {
    const data = await api.get('/data');
    return data;
  } catch (error) {
    logger.error('Fetch failed:', error);
    throw new DataFetchError('Failed to fetch data', { cause: error });
  }
}
```

### Promise.all Error Handling

```typescript
// ❌ First error stops everything, others are lost
const results = await Promise.all([fetch1(), fetch2(), fetch3()]);

// ✅ Collect all results/errors
const results = await Promise.allSettled([fetch1(), fetch2(), fetch3()]);

const successful = results
  .filter((r): r is PromiseFulfilledResult<Data> => r.status === 'fulfilled')
  .map(r => r.value);

const failed = results
  .filter((r): r is PromiseRejectedResult => r.status === 'rejected')
  .map(r => r.reason);

if (failed.length > 0) {
  logger.warn(`${failed.length} requests failed:`, failed);
}
```

### Timeout Handling

```typescript
function withTimeout<T>(promise: Promise<T>, ms: number): Promise<T> {
  const timeout = new Promise<never>((_, reject) => {
    setTimeout(() => reject(new TimeoutError(`Timeout after ${ms}ms`)), ms);
  });
  return Promise.race([promise, timeout]);
}

// Usage
try {
  const data = await withTimeout(fetchData(), 5000);
} catch (error) {
  if (error instanceof TimeoutError) {
    // Handle timeout specifically
  }
}
```

## Python Async Patterns

### TaskGroup Error Handling (Python 3.11+)

```python
async def fetch_all(urls: list[str]) -> list[Data]:
    results = []
    errors = []
    
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(fetch(url)) for url in urls]
    
    # If any task fails, TaskGroup raises ExceptionGroup
    for task in tasks:
        if task.exception():
            errors.append(task.exception())
        else:
            results.append(task.result())
    
    return results
```

### Graceful Shutdown

```python
async def main():
    tasks = set()
    
    try:
        # Create background tasks
        for i in range(10):
            task = asyncio.create_task(worker(i))
            tasks.add(task)
            task.add_done_callback(tasks.discard)
        
        await asyncio.gather(*tasks)
        
    except asyncio.CancelledError:
        # Graceful shutdown
        for task in tasks:
            task.cancel()
        
        await asyncio.gather(*tasks, return_exceptions=True)
        raise
```

## Concurrent Error Collection

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_batch(items: list[Item]) -> tuple[list[Result], list[Exception]]:
    results = []
    errors = []
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_item = {
            executor.submit(process_item, item): item 
            for item in items
        }
        
        for future in as_completed(future_to_item):
            item = future_to_item[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                errors.append((item, e))
    
    return results, errors
```

## Error Propagation in Streams

```typescript
// Node.js streams
import { pipeline } from 'stream/promises';

async function processFile(input: string, output: string) {
  try {
    await pipeline(
      fs.createReadStream(input),
      transformStream,
      fs.createWriteStream(output)
    );
  } catch (error) {
    // Pipeline handles cleanup automatically
    logger.error('Pipeline failed:', error);
    throw error;
  }
}
```

## Key Principles

1. **Never ignore unhandled rejections** - Set up global handlers
2. **Use structured concurrency** - TaskGroups, Promise.allSettled
3. **Implement timeouts** - Async ops can hang forever
4. **Clean up resources** - Cancel pending operations on shutdown
5. **Collect errors, don't lose them** - AllSettled over All when appropriate
