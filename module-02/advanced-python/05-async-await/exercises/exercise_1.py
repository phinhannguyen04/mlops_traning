"""Exercise 1: First Async Function

Objective: Convert synchronous code to async and understand the timing differences.

Instructions:
1. Complete the fetch_user_data_async() function by making it async
2. Add await keyword to simulate I/O operations
3. Complete the main_async() function to run async functions
4. Compare the timing between sync and async versions
5. Run the code and observe the performance difference

Expected: Async version should complete faster when fetching multiple users.
"""
import asyncio
import time

def fetch_user_data_sync(user_id: int) -> dict:
    """Synchronous version - simulates database query."""
    time.sleep(1)  # Simulate I/O delay
    return {"id": user_id, "name": f"User{user_id}", "email": f"user{user_id}@example.com"}

# TODO: Convert this to an async function
# Hint: Use 'async def' and replace time.sleep with await asyncio.sleep
def fetch_user_data_async(user_id: int) -> dict:
    """Asynchronous version - simulates database query."""
    # TODO: Replace time.sleep(1) with await asyncio.sleep(1)
    # TODO: Return the same dict structure as the sync version
    pass

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

# TODO: Complete this async function
# Hint: Use 'async def' and await the async functions
async def main_async():
    """Run asynchronous version."""
    print("\n=== Asynchronous Version ===")
    # TODO: Record start time using time.time()

    # TODO: Create a list of coroutines for users 1, 2, 3
    # Hint: Use list comprehension [fetch_user_data_async(i) for i in [1, 2, 3]]

    # TODO: Use asyncio.gather() to run all coroutines concurrently
    # Hint: users = await asyncio.gather(*coroutines)

    # TODO: Calculate elapsed time and print results
    # Print: f"Fetched {len(users)} users in {elapsed:.2f}s"
    # Print: f"Users: {users}"
    pass

if __name__ == "__main__":
    # Run synchronous version
    main_sync()

    # TODO: Run asynchronous version using asyncio.run()
    # Hint: asyncio.run(main_async())
    pass
