"""Exercise 1 Solution: First Async Function"""
import asyncio
import time

def fetch_user_data_sync(user_id: int) -> dict:
    """Synchronous version - simulates database query."""
    time.sleep(1)  # Simulate I/O delay
    return {"id": user_id, "name": f"User{user_id}", "email": f"user{user_id}@example.com"}

async def fetch_user_data_async(user_id: int) -> dict:
    """Asynchronous version - simulates database query."""
    await asyncio.sleep(1)  # Simulate async I/O delay
    return {"id": user_id, "name": f"User{user_id}", "email": f"user{user_id}@example.com"}

def main_sync():
    """Run synchronous version."""
    print("=== Synchronous Version ===")
    start = time.time()

    # Fetch 3 users sequentially
    users = []
    for user_id in [1, 2, 3]:
        user = fetch_user_data_sync(user_id)
        users.append(user)

    elapsed = time.time() - start
    print(f"Fetched {len(users)} users in {elapsed:.2f}s")
    print(f"Users: {users}")

async def main_async():
    """Run asynchronous version."""
    print("\n=== Asynchronous Version ===")
    start = time.time()

    # Create coroutines for all users
    coroutines = [fetch_user_data_async(i) for i in [1, 2, 3]]

    # Run all coroutines concurrently
    users = await asyncio.gather(*coroutines)

    elapsed = time.time() - start
    print(f"Fetched {len(users)} users in {elapsed:.2f}s")
    print(f"Users: {list(users)}")
    print(f"\nSpeedup: {3.0 / elapsed:.1f}x faster!")

if __name__ == "__main__":
    # Run synchronous version (takes ~3 seconds)
    main_sync()

    # Run asynchronous version (takes ~1 second)
    asyncio.run(main_async())
