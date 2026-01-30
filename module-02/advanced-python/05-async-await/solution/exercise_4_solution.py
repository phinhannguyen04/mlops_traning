"""Exercise 4 Solution: Async Context Manager"""
import asyncio
from typing import List

class AsyncDatabaseConnection:
    """Simulated async database connection."""

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connected = False

    async def __aenter__(self):
        """Establish database connection."""
        print(f"Connecting to {self.db_name}...")
        await asyncio.sleep(0.5)  # Simulate connection delay
        self.connected = True
        print(f"Connected to {self.db_name}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Close database connection."""
        print(f"Closing connection to {self.db_name}...")
        await asyncio.sleep(0.2)  # Simulate cleanup delay
        self.connected = False
        print("Connection closed")

        if exc_type is not None:
            print(f"Error occurred: {exc_val}")

        # Return False to propagate exceptions
        return False

    async def query(self, sql: str) -> List[dict]:
        """Execute a database query."""
        if not self.connected:
            raise RuntimeError("Not connected to database")

        print(f"Executing query: {sql}")
        await asyncio.sleep(0.5)  # Simulate query execution

        # Return simulated results based on query type
        if "SELECT" in sql:
            return [
                {"id": 1, "data": "row1"},
                {"id": 2, "data": "row2"}
            ]
        else:
            return [{"affected_rows": 1}]

async def fetch_users():
    """Fetch users from database using context manager."""
    async with AsyncDatabaseConnection("users_db") as conn:
        results = await conn.query("SELECT * FROM users")
        print(f"Found {len(results)} users: {results}")

async def fetch_with_error():
    """Demonstrate error handling in context manager."""
    print("\n=== Testing Error Handling ===")

    try:
        async with AsyncDatabaseConnection("test_db") as conn:
            await conn.query("SELECT * FROM users")
            raise ValueError("Simulated error!")
    except ValueError as e:
        print(f"Caught error: {e}")

    print("Notice: Connection was still closed despite the error\n")

async def concurrent_queries():
    """Run multiple database queries concurrently."""
    print("=== Concurrent Queries ===")

    async def query_db(db_name: str, query: str):
        async with AsyncDatabaseConnection(db_name) as conn:
            return await conn.query(query)

    # Run 3 database queries concurrently
    results = await asyncio.gather(
        query_db("users_db", "SELECT * FROM users"),
        query_db("products_db", "SELECT * FROM products"),
        query_db("orders_db", "SELECT * FROM orders")
    )

    print("\nResults from all databases:")
    db_names = ["users_db", "products_db", "orders_db"]
    for db_name, result in zip(db_names, results):
        print(f"  {db_name}: {result}")

async def main():
    """Run all examples."""
    print("=== Basic Context Manager Usage ===")
    await fetch_users()

    await fetch_with_error()

    await concurrent_queries()

if __name__ == "__main__":
    asyncio.run(main())
