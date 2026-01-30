"""Mixing Sync and Async Code Examples"""
import asyncio
import time

def blocking_operation():
    """Synchronous blocking function."""
    time.sleep(2)
    return "Blocking result"

async def async_operation():
    """Async operation."""
    await asyncio.sleep(1)
    return "Async result"

async def run_sync_in_async():
    """Run sync code from async context."""
    loop = asyncio.get_event_loop()
    
    # Run blocking code in thread pool
    result = await loop.run_in_executor(None, blocking_operation)
    return result

async def main():
    """Demonstrate mixing sync and async."""
    print("=== Running sync code in async ===")
    result = await run_sync_in_async()
    print(f"Result: {result}")

    print("\n=== Multiple sync operations concurrently ===")
    loop = asyncio.get_event_loop()
    results = await asyncio.gather(
        loop.run_in_executor(None, blocking_operation),
        loop.run_in_executor(None, blocking_operation)
    )
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())
