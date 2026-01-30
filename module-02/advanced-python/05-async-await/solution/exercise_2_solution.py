"""Exercise 2 Solution: Concurrent Tasks"""
import asyncio
import time
from typing import List

async def process_data(item_id: int, delay: float) -> dict:
    """Process a data item asynchronously."""
    print(f"  Processing item {item_id}...")
    await asyncio.sleep(delay)
    return {"id": item_id, "result": f"Processed {item_id}"}

async def pattern_gather():
    """Pattern 1: Run all tasks concurrently with gather()."""
    print("=== Pattern 1: asyncio.gather() ===")
    start = time.time()

    # All tasks start simultaneously and we wait for all to complete
    results = await asyncio.gather(
        process_data(1, 1.0),
        process_data(2, 0.5),
        process_data(3, 1.5)
    )

    elapsed = time.time() - start
    print(f"Completed in {elapsed:.2f}s")
    print(f"Results: {results}\n")

async def pattern_create_task():
    """Pattern 2: Create background tasks."""
    print("=== Pattern 2: asyncio.create_task() ===")
    start = time.time()

    # Create tasks (they start running immediately in background)
    task1 = asyncio.create_task(process_data(1, 1.0))
    task2 = asyncio.create_task(process_data(2, 0.5))
    task3 = asyncio.create_task(process_data(3, 1.5))

    # Tasks are running in background while we do other work
    print("  Tasks running in background...")
    await asyncio.sleep(0.2)
    print("  Doing other work...")

    # Wait for all tasks to complete
    results = await asyncio.gather(task1, task2, task3)

    elapsed = time.time() - start
    print(f"Completed in {elapsed:.2f}s")
    print(f"Results: {results}\n")

async def pattern_as_completed():
    """Pattern 3: Process results as they complete."""
    print("=== Pattern 3: asyncio.as_completed() ===")
    start = time.time()

    # Create list of coroutines
    tasks = [
        process_data(1, 1.0),
        process_data(2, 0.5),  # This will finish first
        process_data(3, 1.5)
    ]

    # Process results in completion order (not creation order)
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"  Got result: {result}")

    elapsed = time.time() - start
    print(f"Total time: {elapsed:.2f}s\n")

async def main():
    """Run all patterns."""
    await pattern_gather()
    await pattern_create_task()
    await pattern_as_completed()

if __name__ == "__main__":
    asyncio.run(main())
