"""Exercise 2: Concurrent Tasks

Objective: Learn different patterns for running concurrent tasks.

Instructions:
1. Complete the process_data() async function
2. Implement Pattern 1: Using asyncio.gather() to run tasks concurrently
3. Implement Pattern 2: Using asyncio.create_task() for background tasks
4. Implement Pattern 3: Using asyncio.as_completed() to process results as they arrive
5. Observe how each pattern handles task execution differently

Expected: All patterns should run tasks concurrently, but with different behaviors.
"""
import asyncio
import time
from typing import List

# TODO: Complete this async function
async def process_data(item_id: int, delay: float) -> dict:
    """Process a data item asynchronously."""
    print(f"  Processing item {item_id}...")
    # TODO: Use await asyncio.sleep(delay) to simulate processing
    # TODO: Return a dict with "id": item_id and "result": f"Processed {item_id}"
    pass

# TODO: Implement Pattern 1 - asyncio.gather()
async def pattern_gather():
    """Pattern 1: Run all tasks concurrently with gather()."""
    print("=== Pattern 1: asyncio.gather() ===")
    start = time.time()

    # TODO: Use asyncio.gather() to run 3 tasks concurrently
    # Process items 1, 2, 3 with delays 1.0, 0.5, 1.5 seconds
    # Hint: results = await asyncio.gather(
    #     process_data(1, 1.0),
    #     process_data(2, 0.5),
    #     process_data(3, 1.5)
    # )

    # TODO: Print elapsed time and results
    # Print: f"Completed in {elapsed:.2f}s"
    # Print: f"Results: {results}"
    pass

# TODO: Implement Pattern 2 - asyncio.create_task()
async def pattern_create_task():
    """Pattern 2: Create background tasks."""
    print("\n=== Pattern 2: asyncio.create_task() ===")
    start = time.time()

    # TODO: Create 3 tasks using asyncio.create_task()
    # Hint: task1 = asyncio.create_task(process_data(1, 1.0))
    #       task2 = asyncio.create_task(process_data(2, 0.5))
    #       task3 = asyncio.create_task(process_data(3, 1.5))

    # TODO: Do some other work while tasks run
    print("  Tasks running in background...")
    await asyncio.sleep(0.2)
    print("  Doing other work...")

    # TODO: Wait for all tasks to complete
    # Hint: results = await asyncio.gather(task1, task2, task3)

    # TODO: Print elapsed time and results
    pass

# TODO: Implement Pattern 3 - asyncio.as_completed()
async def pattern_as_completed():
    """Pattern 3: Process results as they complete."""
    print("\n=== Pattern 3: asyncio.as_completed() ===")
    start = time.time()

    # TODO: Create a list of coroutines
    # tasks = [
    #     process_data(1, 1.0),
    #     process_data(2, 0.5),
    #     process_data(3, 1.5)
    # ]

    # TODO: Use asyncio.as_completed() to process results as they finish
    # Hint: for coro in asyncio.as_completed(tasks):
    #           result = await coro
    #           print(f"  Got result: {result}")

    # TODO: Print total elapsed time
    pass

async def main():
    """Run all patterns."""
    # TODO: Call all three pattern functions
    # await pattern_gather()
    # await pattern_create_task()
    # await pattern_as_completed()
    pass

if __name__ == "__main__":
    # TODO: Run the main function using asyncio.run()
    pass
