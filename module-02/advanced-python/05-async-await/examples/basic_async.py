"""Basic Async/Await Examples"""
import asyncio
import time

async def greet_async(name: str) -> str:
    """Async greeting function."""
    await asyncio.sleep(1)  # Simulate I/O
    return f"Hello, {name}!"

async def fetch_data(url: str) -> str:
    """Simulate fetching data from URL."""
    print(f"Fetching {url}...")
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    """Demonstrate basic async patterns."""
    print("=== Basic Async Function ===")
    greeting = await greet_async("Alice")
    print(greeting)

    print("\n=== Sequential vs Concurrent ===")
    
    # Sequential (slow)
    start = time.time()
    data1 = await fetch_data("url1")
    data2 = await fetch_data("url2")
    data3 = await fetch_data("url3")
    print(f"Sequential: {time.time() - start:.2f}s")

    # Concurrent (fast)
    start = time.time()
    results = await asyncio.gather(
        fetch_data("url1"),
        fetch_data("url2"),
        fetch_data("url3")
    )
    print(f"Concurrent: {time.time() - start:.2f}s")
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())
