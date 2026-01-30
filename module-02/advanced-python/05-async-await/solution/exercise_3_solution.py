"""Exercise 3 Solution: Async HTTP Requests"""
import asyncio
import time
import aiohttp

async def fetch_url(session: aiohttp.ClientSession, url: str) -> dict:
    """Fetch a single URL and return response info."""
    print(f"  Fetching {url}...")

    try:
        async with session.get(url) as response:
            status = response.status
            content = await response.text()
            return {
                "url": url,
                "status": status,
                "length": len(content)
            }
    except aiohttp.ClientError as e:
        return {
            "url": url,
            "error": str(e)
        }

async def fetch_all_urls(urls: list[str]) -> list[dict]:
    """Fetch multiple URLs concurrently."""
    async with aiohttp.ClientSession() as session:
        # Create tasks for all URLs
        tasks = [fetch_url(session, url) for url in urls]

        # Run all tasks concurrently
        results = await asyncio.gather(*tasks)

        return results

async def main():
    """Demonstrate concurrent HTTP requests."""
    # Test URLs (these endpoints add artificial delays)
    urls = [
        "https://httpbin.org/delay/1",  # 1 second delay
        "https://httpbin.org/delay/2",  # 2 second delay
        "https://httpbin.org/delay/1",  # 1 second delay
    ]

    print(f"=== Fetching {len(urls)} URLs concurrently ===")
    start = time.time()

    results = await fetch_all_urls(urls)

    elapsed = time.time() - start

    print(f"\nCompleted in {elapsed:.2f}s")
    print("\nResults:")
    for result in results:
        if "error" in result:
            print(f"  {result['url']}: ERROR - {result['error']}")
        else:
            print(f"  {result['url']}: {result['status']} ({result['length']} bytes)")

    # Calculate speedup
    sequential_time = 4.0  # 1 + 2 + 1 = 4 seconds
    speedup = sequential_time / elapsed
    print(f"\nSpeedup: {speedup:.1f}x faster than sequential")
    print(f"(Sequential would take ~{sequential_time:.0f}s)")

if __name__ == "__main__":
    asyncio.run(main())
