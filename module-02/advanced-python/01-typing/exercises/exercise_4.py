"""Exercise 4: Creating Type Aliases

Build reusable type definitions for complex types.

OBJECTIVE:
- Create type aliases for complex, repeated types
- Use NewType for distinct ID types
- Apply aliases in function signatures

INSTRUCTIONS:
1. Define type aliases using TypeAlias annotation
2. Create NewType definitions for distinct IDs
3. Use the aliases in function signatures
4. Run the code to verify behavior
5. Check with mypy: mypy exercises/exercise_4.py
"""

from typing import TypeAlias, NewType


# TODO: Create a type alias for user data dictionary
# UserData should be: dict[str, str | int | list[str]]


# TODO: Create a type alias for a matrix (list of list of ints)
# Matrix should be: list[list[int]]


# TODO: Create NewType for UserID (based on int)
# UserID = NewType('UserID', int)


# TODO: Create NewType for OrderID (based on int)
# OrderID = NewType('OrderID', int)


# TODO: Add type hints using UserData alias
def create_user(name, age, email, tags):
    """Create a user data structure.

    Args:
        name: User's name
        age: User's age
        email: User's email
        tags: List of user tags

    Returns:
        User data dictionary
    """
    return {
        "name": name,
        "age": age,
        "email": email,
        "tags": tags
    }


# TODO: Add type hints using UserData alias
def process_user(user_data):
    """Process user data.

    Args:
        user_data: User information dictionary

    Returns:
        None (prints user info)
    """
    print(f"Processing user: {user_data['name']}")


# TODO: Add type hints using UserID and OrderID NewTypes
def create_order(user_id, order_id):
    """Create an order for a user.

    Args:
        user_id: The user's unique ID
        order_id: The order's unique ID

    Returns:
        Status message
    """
    return f"Order #{order_id} for user #{user_id}"


# TODO: Add type hints using Matrix alias
def sum_matrix(matrix):
    """Calculate the sum of all elements in a matrix.

    Args:
        matrix: A 2D list of integers

    Returns:
        Sum of all matrix elements
    """
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total


# TODO: Add type hints using Matrix alias
def create_identity_matrix(size):
    """Create an identity matrix of given size.

    Args:
        size: The size of the square matrix

    Returns:
        Identity matrix (1s on diagonal, 0s elsewhere)
    """
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(1 if i == j else 0)
        matrix.append(row)
    return matrix


def main():
    """Run exercise demonstrations."""
    # Test user data with type alias
    user1 = create_user("Alice", 30, "alice@example.com", ["python", "docker"])
    user2 = create_user("Bob", 25, "bob@example.com", ["kubernetes"])

    process_user(user1)
    process_user(user2)

    # Test NewType for IDs
    user_id = UserID(5001)
    order_id = OrderID(1001)
    print(create_order(user_id, order_id))

    # This should work with properly typed IDs
    another_user = UserID(5002)
    another_order = OrderID(1002)
    print(create_order(another_user, another_order))

    # Test matrix type alias
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(f"Matrix sum: {sum_matrix(matrix)}")

    # Create identity matrix
    identity = create_identity_matrix(3)
    print("Identity matrix:")
    for row in identity:
        print(row)


if __name__ == "__main__":
    main()
