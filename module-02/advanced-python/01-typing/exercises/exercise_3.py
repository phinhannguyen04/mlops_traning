"""Exercise 3: Optional and Union Types

Handle nullable values and multiple possible types.

OBJECTIVE:
- Use Optional[T] or T | None for values that might be None
- Use Union types or | for multiple possible types
- Handle None cases properly in logic

INSTRUCTIONS:
1. Add Optional/Union type hints where values can be None or multiple types
2. Ensure proper None checking before using Optional values
3. Run the code to verify behavior
4. Check with mypy: mypy exercises/exercise_3.py
"""


# TODO: Add type hints with Optional return (user might not be found)
def find_user_by_id(user_id: int) -> str | None:
    """Find a user by their ID.

    Args:
        user_id: The user's ID number

    Returns:
        Username if found, None otherwise
    """
    users = {
        1: "Alice",
        2: "Bob",
        3: "Charlie"
    }
    return users.get(user_id)


# TODO: Add type hints with Union type (accepts int or str)

def convert_id_to_string(user_id: int | str) -> str | None:
    """Convert a user ID to string format.

    Args:
        user_id: User ID as either int or str

    Returns:
        String representation of the ID
    """
    return str(user_id)

from typing import Any

# TODO: Add type hints with Optional parameter and return
def calculate_with_default(value: Any | None, default: Any | None =None):
    """Calculate a value, using default if value is None.

    Args:
        value: The value to use (or None)
        default: Default value if value is None (or None)

    Returns:
        The value, default, or 0.0 if both are None
    """
    if value is not None:
        return value
    if default is not None:
        return default
    return 0.0


# TODO: Add type hints (config can be dict or None)
def initialize_system(config: dict | None):
    """Initialize system with optional configuration.

    Args:
        config: Optional configuration dictionary

    Returns:
        Status message
    """
    if config is None:
        return "System initialized with default settings"
    return f"System initialized with {len(config)} custom settings"


# TODO: Add type hints (accepts int, float, or str; returns float)
def parse_number(value: int | float | str) -> float:
    """Parse a number from various input types.

    Args:
        value: Number as int, float, or string

    Returns:
        The value as a float
    """
    return float(value)


# TODO: Add type hints (returns list or None)
def get_user_tags(user_id: int) -> list[str] | None:
    """Get tags for a user.

    Args:
        user_id: The user's ID

    Returns:
        List of tags if user exists, None otherwise
    """
    user_tags = {
        1: ["python", "mlops"],
        2: ["kubernetes", "docker"],
    }
    return user_tags.get(user_id)


def main():
    """Run exercise demonstrations."""
    # Test finding users
    user = find_user_by_id(1)
    if user is not None:
        print(f"Found user: {user}")

    user = find_user_by_id(999)
    if user is None:
        print("User not found")

    # Test ID conversion with different types
    print(f"ID as string: {convert_id_to_string(12345)}")
    print(f"ID as string: {convert_id_to_string('USER-789')}")

    # Test default values
    result1 = calculate_with_default(10.5)
    print(f"Value: {result1}")

    result2 = calculate_with_default(None, 5.0)
    print(f"Value: {result2}")

    result3 = calculate_with_default(None, None)
    print(f"Value: {result3} (default)")

    # Test optional config
    print(initialize_system(None))
    print(initialize_system({"theme": "dark", "debug": True}))

    # Test number parsing
    print(f"Parsed: {parse_number(42)}")
    print(f"Parsed: {parse_number(3.14)}")
    print(f"Parsed: {parse_number('2.718')}")

    # Test optional tags
    tags = get_user_tags(1)
    if tags is not None:
        print(f"User 1 tags: {', '.join(tags)}")

    tags = get_user_tags(999)
    if tags is None:
        print("User 999 has no tags")


if __name__ == "__main__":
    main()
