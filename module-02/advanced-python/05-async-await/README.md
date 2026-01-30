# Async/Await - Hands-On Lab

**Master asynchronous programming through progressive exercises**

## Overview

This lab provides hands-on practice with async/await, from basic coroutines to real-world patterns. You'll learn to write concurrent code for I/O-bound operations like HTTP requests, file operations, and data processing.

## Prerequisites

- Python 3.10 or higher
- Understanding of functions and loops
- Basic knowledge of I/O operations
- Completed previous labs (typing, decorators)

## Setup

### 1. Navigate to Lab Directory

```bash
cd module-02/advanced-python/05-async-await
```

### 2. Install Async Libraries

```bash
# With uv
uv add aiohttp aiofiles

# Or with pip
pip install aiohttp aiofiles
```

### 3. Verify Installation

```bash
python -c "import asyncio, aiohttp, aiofiles; print('Ready!')"
```

## Lab Structure

```
05-async-await/
├── README.md           # This file
├── examples/           # Reference examples
│   ├── basic_async.py
│   ├── concurrent_tasks.py
│   ├── async_http.py
│   ├── async_file_io.py
│   └── mixed_sync_async.py
├── exercises/          # Your practice files
│   ├── exercise_1.py
│   ├── exercise_2.py
│   ├── exercise_3.py
│   ├── exercise_4.py
│   └── exercise_5.py
└── solution/           # Solution files
    ├── exercise_1_solution.py
    ├── exercise_2_solution.py
    ├── exercise_3_solution.py
    ├── exercise_4_solution.py
    └── exercise_5_solution.py
```

## How to Work Through Exercises

1. **Read the exercise description** in this README
2. **Review example files** for patterns
3. **Open the exercise file** in `exercises/`
4. **Complete the TODO sections**
5. **Run the code**: `python exercises/exercise_N.py`
6. **Verify timing improvements** (async should be faster)
7. **Compare with solution** if needed

## Exercises

### Exercise 1: First Async Function

**Objective:** Convert synchronous code to async

**Background:**

The first step in async programming is understanding how to convert sync functions to async. You'll see dramatic performance improvements when operations wait for I/O.

**Instructions:**

1. Open `exercises/exercise_1.py`
2. Convert sync functions to async
3. Use `await asyncio.sleep()` instead of `time.sleep()`
4. Use `asyncio.run()` to execute
5. Compare execution times

**Expected Output:**

```
=== Synchronous Version ===
Fetching data1...
Got data1
Fetching data2...
Got data2
Fetching data3...
Got data3
Total time: 3.01s

=== Asynchronous Version ===
Fetching data1...
Fetching data2...
Fetching data3...
Got data1
Got data2
Got data3
Total time: 1.01s
```

**Key Learnings:**

- How to convert sync to async functions
- Difference between `time.sleep()` and `await asyncio.sleep()`
- Using `asyncio.run()` as entry point
- Why async is faster for I/O-bound operations

**Common Mistakes:**

- Forgetting `await` keyword
- Using `time.sleep()` in async functions (blocks event loop)
- Not using `asyncio.run()` at top level

### Exercise 2: Concurrent Tasks with gather()

**Objective:** Run multiple tasks concurrently

**Background:**

`asyncio.gather()` is the primary way to run multiple tasks concurrently. All tasks start immediately and gather waits for all to complete.

**Instructions:**

1. Open `exercises/exercise_2.py`
2. Use `asyncio.gather()` to run tasks concurrently
3. Use `asyncio.create_task()` for background tasks
4. Compare sequential vs concurrent execution
5. Handle results from multiple tasks

**Expected Output:**

```
=== Sequential Execution ===
Fetching user 1...
Got user 1
Fetching user 2...
Got user 2
Fetching user 3...
Got user 3
Time: 3.00s

=== Concurrent Execution (gather) ===
Fetching user 1...
Fetching user 2...
Fetching user 3...
Got user 1
Got user 2
Got user 3
Time: 1.00s
Results: [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Charlie'}]
```

**Key Learnings:**

- Using `asyncio.gather()` for concurrent execution
- Difference between sequential awaits and gather
- How `asyncio.create_task()` works
- Results are returned in order from gather

**Common Mistakes:**

- Sequential awaits instead of gather (slow)
- Not unpacking gather results correctly
- Forgetting to await gather itself

### Exercise 3: Async HTTP Requests

**Objective:** Fetch multiple URLs concurrently with aiohttp

**Background:**

Real-world async programming often involves HTTP requests. `aiohttp` is the standard async HTTP library. This exercise demonstrates massive performance gains over synchronous requests.

**Instructions:**

1. Open `exercises/exercise_3.py`
2. Use `aiohttp.ClientSession` for HTTP requests
3. Fetch multiple URLs concurrently
4. Handle responses and errors
5. Compare with synchronous requests library

**Expected Output:**

```
=== Fetching 10 URLs Concurrently ===
Fetching https://jsonplaceholder.typicode.com/posts/1
Fetching https://jsonplaceholder.typicode.com/posts/2
Fetching https://jsonplaceholder.typicode.com/posts/3
...
Fetched 10 URLs in 1.2 seconds

Results:
  URL 1: Status 200, Length 292 bytes
  URL 2: Status 200, Length 289 bytes
  ...

Average response time: 0.12s per URL
```

**Key Learnings:**

- Using `aiohttp.ClientSession` for async HTTP
- `async with` context managers
- Fetching multiple URLs concurrently
- 10x+ speedup vs synchronous requests
- Error handling in async HTTP

**Common Mistakes:**

- Not using `async with` for session
- Creating new session for each request (slow)
- Not handling network errors

### Exercise 4: Async Context Manager

**Objective:** Build an async database connection manager

**Background:**

Async context managers (`async with`) ensure proper resource cleanup in async code. This exercise simulates a database connection that requires async operations to connect and disconnect.

**Instructions:**

1. Open `exercises/exercise_4.py`
2. Create a class with `__aenter__` and `__aexit__`
3. Implement async connection logic
4. Use the context manager with `async with`
5. Verify proper cleanup

**Expected Output:**

```
Connecting to database...
Connection established
Executing query: SELECT * FROM users
Query result: [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
Closing connection...
Connection closed

=== Multiple Concurrent Queries ===
Connecting to database...
Connection established
Query 1 executing...
Query 2 executing...
Query 3 executing...
Query 1 complete
Query 2 complete
Query 3 complete
Closing connection...
Connection closed
Total time: 1.5s (queries ran concurrently)
```

**Key Learnings:**

- Implementing `__aenter__` and `__aexit__`
- Using `async with` for resource management
- Automatic cleanup even with exceptions
- Concurrent operations within context manager

**Common Mistakes:**

- Using regular `__enter__`/`__exit__` instead of async versions
- Not awaiting in `__aenter__` and `__aexit__`
- Not re-raising exceptions in `__aexit__`

### Exercise 5: Real-world Data Pipeline

**Objective:** Create an async data processing pipeline

**Background:**

This exercise combines everything: async HTTP, file I/O, concurrent processing, and error handling. You'll build a pipeline that fetches data, processes it, and writes results - all concurrently.

**Instructions:**

1. Open `exercises/exercise_5.py`
2. Build a pipeline: fetch → process → save
3. Use `aiohttp` for fetching
4. Use `aiofiles` for file I/O
5. Process multiple items concurrently
6. Handle errors gracefully

**Expected Output:**

```
=== Starting Data Pipeline ===

Stage 1: Fetching data from 5 APIs...
  Fetching https://api.example.com/data/1
  Fetching https://api.example.com/data/2
  Fetching https://api.example.com/data/3
  Fetching https://api.example.com/data/4
  Fetching https://api.example.com/data/5
Fetched 5 items in 1.2s

Stage 2: Processing data...
  Processing item 1
  Processing item 2
  Processing item 3
  Processing item 4
  Processing item 5
Processed 5 items in 0.5s

Stage 3: Saving results...
  Writing output/result_1.json
  Writing output/result_2.json
  Writing output/result_3.json
  Writing output/result_4.json
  Writing output/result_5.json
Saved 5 files in 0.3s

=== Pipeline Complete ===
Total time: 2.0s
Successfully processed 5 items
```

**Key Learnings:**

- Building multi-stage async pipelines
- Combining aiohttp and aiofiles
- Error handling in complex workflows
- Rate limiting with Semaphore
- Real-world async patterns

**Common Mistakes:**

- Not limiting concurrent connections (overwhelming API)
- Sequential stages instead of concurrent
- Poor error handling (one failure stops all)

## Running Examples

Study the examples before exercises:

```bash
# Basic async patterns
python examples/basic_async.py

# Concurrent task management
python examples/concurrent_tasks.py

# HTTP requests with aiohttp
python examples/async_http.py

# File I/O with aiofiles
python examples/async_file_io.py

# Mixing sync and async code
python examples/mixed_sync_async.py
```

## Understanding Performance

### Timing Your Code

```python
import asyncio
import time

async def timed_operation():
    start = time.time()
    # Your async code here
    elapsed = time.time() - start
    print(f"Completed in {elapsed:.2f}s")
```

### Expected Speedups

For I/O-bound operations:

- **3 concurrent tasks**: ~3x faster
- **10 concurrent tasks**: ~10x faster
- **100 concurrent tasks**: ~100x faster (with proper rate limiting)

CPU-bound operations won't benefit from async/await.

## What You Learned

After completing this lab, you should be able to:

- Convert synchronous code to async
- Use `asyncio.gather()` for concurrent execution
- Work with `aiohttp` for async HTTP requests
- Use `aiofiles` for async file operations
- Create async context managers
- Build real-world async pipelines
- Handle errors in async code
- Understand when to use async vs sync

## Troubleshooting

### RuntimeWarning: coroutine was never awaited

```python
# ❌ Wrong
async def task():
    return 42

result = task()  # Warning!

# ✅ Correct
result = await task()
# or
result = asyncio.run(task())
```

### Event Loop is Already Running

```python
# ❌ Wrong (in Jupyter/IPython)
asyncio.run(main())  # Error if loop already exists

# ✅ Correct (in Jupyter/IPython)
await main()  # Use await directly
```

### Blocking the Event Loop

```python
# ❌ Wrong - blocks everything
async def bad():
    time.sleep(1)  # Don't use time.sleep!

# ✅ Correct
async def good():
    await asyncio.sleep(1)  # Use asyncio.sleep
```

### aiohttp Import Errors

```bash
# Install aiohttp
pip install aiohttp

# If SSL errors occur
pip install aiohttp[speedups]
```

## Best Practices from This Lab

### 1. Always Use async with for Resources

```python
# ✅ Good
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.json()

# ❌ Bad
session = aiohttp.ClientSession()
response = await session.get(url)
data = await response.json()
await session.close()  # Easy to forget!
```

### 2. Use gather() for Concurrent Tasks

```python
# ✅ Good - concurrent
results = await asyncio.gather(
    fetch_data(1),
    fetch_data(2),
    fetch_data(3)
)

# ❌ Bad - sequential
result1 = await fetch_data(1)
result2 = await fetch_data(2)
result3 = await fetch_data(3)
```

### 3. Limit Concurrent Operations

```python
# ✅ Good - respects API limits
from asyncio import Semaphore

sem = Semaphore(5)  # Max 5 concurrent

async def fetch_with_limit(url):
    async with sem:
        return await fetch(url)

# ❌ Bad - might overwhelm API
tasks = [fetch(url) for url in urls]  # All at once!
```

### 4. Handle Errors Gracefully

```python
# ✅ Good
results = await asyncio.gather(
    *tasks,
    return_exceptions=True
)
for result in results:
    if isinstance(result, Exception):
        logging.error(f"Task failed: {result}")

# ❌ Bad - one error stops everything
results = await asyncio.gather(*tasks)
```

### 5. Use Type Hints

```python
from typing import List, Dict
import aiohttp

async def fetch_users(
    session: aiohttp.ClientSession,
    user_ids: List[int]
) -> List[Dict[str, any]]:
    tasks = [fetch_user(session, uid) for uid in user_ids]
    return await asyncio.gather(*tasks)
```

## Common Async Patterns

### Pattern 1: Fan-Out, Fan-In

```python
async def process_batch(items):
    # Fan-out: Start all tasks
    tasks = [process_item(item) for item in items]

    # Fan-in: Wait for all results
    results = await asyncio.gather(*tasks)

    return results
```

### Pattern 2: Producer-Consumer

```python
from asyncio import Queue

async def producer(queue):
    for i in range(10):
        await queue.put(i)
    await queue.put(None)  # Sentinel

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        await process(item)
```

### Pattern 3: Retry with Exponential Backoff

```python
async def retry_with_backoff(coro, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return await coro
        except Exception as e:
            if attempt == max_attempts - 1:
                raise
            delay = 2 ** attempt  # 1s, 2s, 4s
            await asyncio.sleep(delay)
```

## Next Steps

After mastering async/await:

- Build an async web scraper
- Create an async API client
- Build a concurrent data processing pipeline
- Explore async frameworks (FastAPI, aiohttp server)

## Performance Benchmarks

Typical speedups for I/O-bound operations:

| Operation | Sync Time | Async Time | Speedup |
|-----------|-----------|------------|---------|
| 10 HTTP requests | 10s | 1s | 10x |
| 100 file reads | 50s | 5s | 10x |
| 50 DB queries | 25s | 2.5s | 10x |

**Remember:** Async doesn't help with CPU-bound operations!

## Additional Resources

- [Theory: Async/Await](../../../docs/module-02/05-async-await.md)
- [Official asyncio docs](https://docs.python.org/3/library/asyncio.html)
- [aiohttp documentation](https://docs.aiohttp.org/)
- [aiofiles documentation](https://github.com/Tinche/aiofiles)
- [Real Python: Async IO](https://realpython.com/async-io-python/)

## Summary

You've learned:

- ✅ Converting sync code to async
- ✅ Concurrent execution with gather()
- ✅ Async HTTP requests with aiohttp
- ✅ Async file I/O with aiofiles
- ✅ Async context managers
- ✅ Real-world async pipelines
- ✅ Error handling in async code
- ✅ Performance optimization patterns

Async/await is essential for modern Python applications, especially in MLOps where you're often waiting for APIs, databases, and file systems!
