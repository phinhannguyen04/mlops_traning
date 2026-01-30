"""Basic Type Annotations Examples

This module demonstrates fundamental type hinting patterns in Python.
"""


def greet_user(name: str) -> str:
    """Return a greeting message for the given name.

    Args:
        name: The user's name

    Returns:
        A personalized greeting message
    """
    return f"Hello, {name}!"


def calculate_total(price: float, quantity: int, tax_rate: float = 0.1) -> float:
    """Calculate the total price including tax.

    Args:
        price: Price per item
        quantity: Number of items
        tax_rate: Tax rate as a decimal (default: 0.1 for 10%)

    Returns:
        Total price including tax
    """
    subtotal = price * quantity
    return subtotal * (1 + tax_rate)


def is_adult(age: int) -> bool:
    """Check if a person is an adult (18 or older).

    Args:
        age: Person's age in years

    Returns:
        True if adult, False otherwise
    """
    return age >= 18


def log_message(message: str, level: str = "INFO") -> None:
    """Log a message with a specified level.

    Args:
        message: The message to log
        level: Log level (default: "INFO")

    Returns:
        None (this function doesn't return a value)
    """
    print(f"[{level}] {message}")


def main() -> None:
    """Demonstrate basic type annotations."""
    # String operations
    greeting: str = greet_user("Alice")
    print(greeting)

    # Numeric operations
    total: float = calculate_total(29.99, 2, 0.08)
    print(f"Total: ${total:.2f}")

    # Boolean operations
    age: int = 25
    adult_status: bool = is_adult(age)
    print(f"Is adult: {adult_status}")

    # No return value
    log_message("Application started")
    log_message("Something went wrong", level="ERROR")


if __name__ == "__main__":
    main()
