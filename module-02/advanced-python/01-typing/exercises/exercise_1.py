"""Exercise 1: Basic Type Annotations

Add type hints to all functions and variables in this module.

OBJECTIVE:
- Add type hints to function parameters
- Add return type annotations
- Add variable type annotations where helpful

INSTRUCTIONS:
1. Add type hints to every function parameter
2. Add return type annotations (including -> None where appropriate)
3. Run the code to ensure it still works correctly
4. Check with mypy: mypy exercises/exercise_1.py
5. Fix any type errors until mypy reports success
"""


# TODO: Add type hints to all parameters and return type
def create_user_profile(name, age, email):
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


# TODO: Add type hints to all parameters and return type
def calculate_tax(amount, tax_rate):
    """Calculate tax amount.

    Args:
        amount: The base amount
        tax_rate: Tax rate as a decimal (e.g., 0.15 for 15%)

    Returns:
        The tax amount
    """
    return amount * tax_rate


# TODO: Add type hints to all parameters and return type
def format_currency(amount):
    """Format a number as currency.

    Args:
        amount: The amount to format

    Returns:
        Formatted currency string
    """
    return f"${amount:.2f}"


# TODO: Add type hints to all parameters and return type
def send_notification(message, recipient, urgent=False):
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


# TODO: Add type hints to all parameters and return type
def calculate_average(numbers):
    """Calculate the average of a list of numbers.

    Args:
        numbers: List of numbers to average

    Returns:
        The arithmetic mean
    """
    return sum(numbers) / len(numbers)


def main():
    """Run exercise demonstrations."""
    # TODO: Add type annotation to this variable
    name = "Alice"

    # TODO: Add type annotation to this variable
    age = 30

    # Create user profile
    user = create_user_profile(name, age, "alice@example.com")
    print(f"User: {user['name']} (age {user['age']})")

    # Calculate tax
    price = 100.0
    tax = calculate_tax(price, 0.10)
    total = price + tax
    print(f"Total price: {format_currency(total)}")

    # Send notification
    send_notification("Hello, Bob!", "bob@example.com")

    # Calculate average
    scores = [95, 82, 88]
    avg = calculate_average(scores)
    print(f"Average: {avg:.2f}")


if __name__ == "__main__":
    main()
