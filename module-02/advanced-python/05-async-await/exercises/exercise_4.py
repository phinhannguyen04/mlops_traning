"""Exercise 4: Async Context Manager

Objective: Build a reusable async context manager for database connections.

Instructions:
1. Complete the AsyncDatabaseConnection class
2. Implement __aenter__ to establish connection
3. Implement __aexit__ to close connection and handle errors
4. Complete the query() method to simulate database queries
5. Use the context manager in the main() function

Expected: Connection should auto-close even if errors occur.
"""
import asyncio
import time
from typing import List, Optional

# TODO: Complete this async context manager
class AsyncDatabaseConnection:
    """Simulated async database connection."""

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connected = False

    # TODO: Implement __aenter__ method
    async def __aenter__(self):
        """Establish database connection.

        Returns:
            self (the connection instance)
        """
        print(f"Connecting to {self.db_name}...")
        # TODO: Simulate connection delay with await asyncio.sleep(0.5)
        # TODO: Set self.connected = True
        # TODO: Print "Connected to {self.db_name}"
        # TODO: Return self
        pass

    # TODO: Implement __aexit__ method
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Close database connection.

        Args:
            exc_type: Exception type if error occurred
            exc_val: Exception value if error occurred
            exc_tb: Exception traceback if error occurred
        """
        print(f"Closing connection to {self.db_name}...")
        # TODO: Simulate cleanup delay with await asyncio.sleep(0.2)
        # TODO: Set self.connected = False
        # TODO: Print "Connection closed"

        # TODO: If exc_type is not None, print the error
        # Hint: if exc_type is not None:
        #           print(f"Error occurred: {exc_val}")

        # Return False to propagate exceptions (default behavior)
        return False

    # TODO: Complete the query method
    async def query(self, sql: str) -> List[dict]:
        """Execute a database query.

        Args:
            sql: SQL query string

        Returns:
            List of result rows (simulated)
        """
        # TODO: Check if connected, raise error if not
        # Hint: if not self.connected:
        #           raise RuntimeError("Not connected to database")

        print(f"Executing query: {sql}")
        # TODO: Simulate query execution with await asyncio.sleep(0.5)

        # TODO: Return simulated results based on query type
        # If "SELECT" in sql: return [{"id": 1, "data": "row1"}, {"id": 2, "data": "row2"}]
        # Otherwise: return [{"affected_rows": 1}]
        pass

# TODO: Complete this function using the context manager
async def fetch_users():
    """Fetch users from database using context manager."""
    # TODO: Use 'async with' to create database connection
    # Hint: async with AsyncDatabaseConnection("users_db") as conn:

    # TODO: Execute a SELECT query
    # Hint: results = await conn.query("SELECT * FROM users")

    # TODO: Print results
    # Print: f"Found {len(results)} users: {results}"
    pass

# TODO: Complete this function to test error handling
async def fetch_with_error():
    """Demonstrate error handling in context manager."""
    print("\n=== Testing Error Handling ===")

    # TODO: Use try/except with async context manager
    try:
        # TODO: Create connection with 'async with'
        # Inside the context, raise an exception to test cleanup
        # Hint: async with AsyncDatabaseConnection("test_db") as conn:
        #           await conn.query("SELECT * FROM users")
        #           raise ValueError("Simulated error!")
        pass
    except ValueError as e:
        print(f"Caught error: {e}")

    # Note: Connection should still be closed even though error occurred

# TODO: Complete this function with concurrent connections
async def concurrent_queries():
    """Run multiple database queries concurrently."""
    print("\n=== Concurrent Queries ===")

    # TODO: Define an async function to query a database
    async def query_db(db_name: str, query: str):
        async with AsyncDatabaseConnection(db_name) as conn:
            return await conn.query(query)

    # TODO: Use asyncio.gather to run 3 concurrent queries
    # Query "users_db", "products_db", and "orders_db"
    # Hint: results = await asyncio.gather(
    #     query_db("users_db", "SELECT * FROM users"),
    #     query_db("products_db", "SELECT * FROM products"),
    #     query_db("orders_db", "SELECT * FROM orders")
    # )

    # TODO: Print results from all databases
    pass

async def main():
    """Run all examples."""
    print("=== Basic Context Manager Usage ===")
    # TODO: Call fetch_users()

    # TODO: Call fetch_with_error()

    # TODO: Call concurrent_queries()
    pass

if __name__ == "__main__":
    # TODO: Run the main function using asyncio.run()
    pass
