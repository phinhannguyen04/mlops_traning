"""Exercise 3: Async HTTP Requests

Objective: Fetch multiple URLs concurrently using aiohttp.

Instructions:
1. Install aiohttp: uv add aiohttp
2. Complete the fetch_url() function to fetch a single URL
3. Complete the fetch_all_urls() function to fetch multiple URLs concurrently
4. Add error handling for failed requests
5. Compare timing with sequential fetching

Expected: Concurrent fetching should be significantly faster than sequential.

Note: This exercise requires aiohttp library.
"""
import asyncio
import time
# TODO: Import aiohttp
# Hint: import aiohttp

# TODO: Complete this async function
async def fetch_url(session, url: str) -> dict:
    """Fetch a single URL and return response info.

    Args:
        session: aiohttp.ClientSession instance
        url: URL to fetch

    Returns:
        Dict with url, status, and content length
    """
    print(f"  Fetching {url}...")

    # TODO: Use session.get(url) with async context manager
    # Hint: async with session.get(url) as response:
    #           status = response.status
    #           content = await response.text()
    #           return {"url": url, "status": status, "length": len(content)}

    # TODO: Add try/except to handle errors
    # Hint: except aiohttp.ClientError as e:
    #           return {"url": url, "error": str(e)}
    pass

# TODO: Complete this async function
async def fetch_all_urls(urls: list[str]) -> list[dict]:
    """Fetch multiple URLs concurrently.

    Args:
        urls: List of URLs to fetch

    Returns:
        List of response info dicts
    """
    # TODO: Create aiohttp.ClientSession with async context manager
    # Hint: async with aiohttp.ClientSession() as session:

    # TODO: Create tasks for all URLs
    # Hint: tasks = [fetch_url(session, url) for url in urls]

    # TODO: Use asyncio.gather() to run all tasks concurrently
    # Hint: results = await asyncio.gather(*tasks)

    # TODO: Return results
    pass

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

    # TODO: Call fetch_all_urls() and await the results
    # Hint: results = await fetch_all_urls(urls)

    # TODO: Calculate elapsed time
    # TODO: Print results
    # Print: f"Completed in {elapsed:.2f}s"
    # For each result:
    #   if "error" in result:
    #       print(f"  {result['url']}: ERROR - {result['error']}")
    #   else:
    #       print(f"  {result['url']}: {result['status']} ({result['length']} bytes)")

    # TODO: Calculate and print speedup
    # Sequential would take: 1 + 2 + 1 = 4 seconds
    # Print: f"\nSpeedup: {4.0 / elapsed:.1f}x faster than sequential"
    pass

if __name__ == "__main__":
    # TODO: Run the main function using asyncio.run()
    # Hint: asyncio.run(main())
    pass
