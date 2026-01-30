"""Type Checking Integration Examples

This module demonstrates how to integrate with static type checkers
and check types at runtime.
"""

from typing import get_type_hints, Any


def calculate_discount(price: float, discount_rate: float) -> float:
    """Calculate discounted price.

    Args:
        price: Original price
        discount_rate: Discount as a decimal (0.1 = 10% off)

    Returns:
        Discounted price
    """
    return price * (1 - discount_rate)


def process_user_data(
    name: str,
    age: int,
    email: str,
    tags: list[str] | None = None
) -> dict[str, Any]:
    """Process user data into a structured format.

    Args:
        name: User's name
        age: User's age
        email: User's email address
        tags: Optional list of user tags

    Returns:
        Dictionary containing processed user data
    """
    return {
        "name": name.strip().title(),
        "age": age,
        "email": email.lower(),
        "tags": tags or [],
        "is_adult": age >= 18
    }


def main() -> None:
    """Demonstrate runtime type checking and introspection."""
    print("=== Type Hints Introspection ===")

    # Get type hints from a function
    hints = get_type_hints(calculate_discount)
    print(f"calculate_discount type hints: {hints}")

    hints = get_type_hints(process_user_data)
    print(f"\nprocess_user_data type hints:")
    for param, type_hint in hints.items():
        print(f"  {param}: {type_hint}")

    print("\n=== Function Usage ===")

    # Correct usage
    discounted_price = calculate_discount(100.0, 0.2)
    print(f"Discounted price: ${discounted_price:.2f}")

    # Process user data
    user = process_user_data(
        name="  alice smith  ",
        age=25,
        email="Alice@Example.COM",
        tags=["python", "mlops"]
    )
    print(f"\nProcessed user: {user}")

    # Type checker would catch these errors at static analysis time:
    # calculate_discount("100", 0.2)  # Error: Expected float, got str
    # process_user_data(123, 25, "email")  # Error: Expected str, got int

    print("\n=== Type Checking with mypy ===")
    print("Run this file through mypy to verify type correctness:")
    print("  mypy examples/type_checking.py")
    print("\nOr use pyright:")
    print("  pyright examples/type_checking.py")


if __name__ == "__main__":
    main()
