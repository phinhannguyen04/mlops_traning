"""Async File I/O Examples (requires aiofiles)"""
import asyncio
import aiofiles
import tempfile
import os

async def write_file(filename: str, content: str):
    """Write file asynchronously."""
    async with aiofiles.open(filename, 'w') as f:
        await f.write(content)
    print(f"Wrote {filename}")

async def read_file(filename: str) -> str:
    """Read file asynchronously."""
    async with aiofiles.open(filename, 'r') as f:
        content = await f.read()
    print(f"Read {filename}")
    return content

async def main():
    """Demonstrate async file I/O."""
    tmpdir = tempfile.gettempdir()
    
    print("=== Writing files concurrently ===")
    await asyncio.gather(
        write_file(os.path.join(tmpdir, 'async1.txt'), 'File 1 content'),
        write_file(os.path.join(tmpdir, 'async2.txt'), 'File 2 content'),
        write_file(os.path.join(tmpdir, 'async3.txt'), 'File 3 content')
    )

    print("\n=== Reading files concurrently ===")
    contents = await asyncio.gather(
        read_file(os.path.join(tmpdir, 'async1.txt')),
        read_file(os.path.join(tmpdir, 'async2.txt')),
        read_file(os.path.join(tmpdir, 'async3.txt'))
    )
    
    for i, content in enumerate(contents):
        print(f"File {i+1}: {content}")

if __name__ == "__main__":
    asyncio.run(main())
