"""Async HTTP Examples (requires aiohttp)"""
import asyncio
import aiohttp

async def fetch_url(session: aiohttp.ClientSession, url: str) -> dict:
    """Fetch URL and return response info."""
    async with session.get(url) as response:
        content = await response.text()
        return {
            'url': url,
            'status': response.status,
            'length': len(content)
        }

async def main():
    """Demonstrate async HTTP requests."""
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/1'
    ]

    print(f"=== Fetching {len(urls)} URLs concurrently ===")
    
    async with aiohttp.ClientSession() as session:
        import time
        start = time.time()
        
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        elapsed = time.time() - start
        print(f"Fetched {len(results)} URLs in {elapsed:.2f}s")
        
        for result in results:
            print(f"  {result['url']}: {result['status']} ({result['length']} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
