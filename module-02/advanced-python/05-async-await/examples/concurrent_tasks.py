"""Concurrent Task Management Examples"""
import asyncio
import time

async def task_with_delay(name: str, delay: float) -> str:
    """Task that takes specified time."""
    print(f"{name} starting...")
    await asyncio.sleep(delay)
    print(f"{name} completed!")
    return f"{name} result"

async def main():
    """Demonstrate concurrent task patterns."""
    print("=== Pattern 1: asyncio.gather() ===")
    start = time.time()
    results = await asyncio.gather(
        task_with_delay("Task A", 1.0),
        task_with_delay("Task B", 2.0),
        task_with_delay("Task C", 1.5)
    )
    print(f"All completed in {time.time() - start:.2f}s")
    print(f"Results: {results}")

    print("\n=== Pattern 2: asyncio.create_task() ===")
    task1 = asyncio.create_task(task_with_delay("Background 1", 1.0))
    task2 = asyncio.create_task(task_with_delay("Background 2", 1.0))
    
    print("Tasks running in background...")
    await asyncio.sleep(0.5)
    print("Doing other work...")
    
    await task1
    await task2
    print("Background tasks complete")

if __name__ == "__main__":
    asyncio.run(main())
