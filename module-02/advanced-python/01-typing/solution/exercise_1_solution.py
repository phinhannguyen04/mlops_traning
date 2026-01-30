"""Exercise 1 Solution: Basic Type Annotations

This solution demonstrates proper type hints for function parameters,
return values, and variables.
"""


def create_user_profile(name: str, age: int, email: str) -> dict[str, str | int | bool]:
    """Create a user profile dictionary.

    Args:
        name: User's full name
        age: User's age in years
        email: User's email address

    Returns:
        Dictionary containing user profile information
    """
    return {
        "name": name,
        "age": age,
        "email": email,
        "is_adult": age >= 18
    }


def calculate_tax(amount: float, tax_rate: float) -> float:
    """Calculate tax amount.

    Args:
        amount: The base amount
        tax_rate: Tax rate as a decimal (e.g., 0.15 for 15%)

    Returns:
        The tax amount
    """
    return amount * tax_rate


def format_currency(amount: float) -> str:
    """Format a number as currency.

    Args:
        amount: The amount to format

    Returns:
        Formatted currency string
    """
    return f"${amount:.2f}"


def send_notification(message: str, recipient: str, urgent: bool = False) -> None:
    """Send a notification message.

    Args:
        message: The notification message
        recipient: Email address of recipient
        urgent: Whether this is an urgent notification (default: False)

    Returns:
        None (prints notification details)
    """
    urgency = "URGENT" if urgent else "NORMAL"
    print(f"[{urgency}] To: {recipient}")
    print(f"Message: {message}")


def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers.

    Args:
        numbers: List of numbers to average

    Returns:
        The arithmetic mean
    """
    return sum(numbers) / len(numbers)


def main() -> None:
    """Run exercise demonstrations."""
    # Type annotations on variables make intent clear
    name: str = "Alice"
    age: int = 30

    # Create user profile
    user = create_user_profile(name, age, "alice@example.com")
    print(f"User: {user['name']} (age {user['age']})")

    # Calculate tax
    price: float = 100.0
    tax: float = calculate_tax(price, 0.10)
    total: float = price + tax
    print(f"Total price: {format_currency(total)}")

    # Send notification
    send_notification("Hello, Bob!", "bob@example.com")

    # Calculate average
    scores: list[float] = [95, 82, 88]
    avg: float = calculate_average(scores)
    print(f"Average: {avg:.2f}")


if __name__ == "__main__":
    main()
