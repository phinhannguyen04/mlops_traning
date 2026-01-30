"""Exercise 4 Solution: Creating Type Aliases

This solution demonstrates creating and using type aliases and NewType
for improved code readability and type safety.
"""

from typing import TypeAlias, NewType


# Type alias for complex user data structure
UserData: TypeAlias = dict[str, str | int | list[str]]

# Type alias for a matrix (2D list of integers)
Matrix: TypeAlias = list[list[int]]

# NewType creates distinct types that prevent accidental mixing
UserID = NewType('UserID', int)
OrderID = NewType('OrderID', int)


def create_user(name: str, age: int, email: str, tags: list[str]) -> UserData:
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


def process_user(user_data: UserData) -> None:
    """Process user data.

    Args:
        user_data: User information dictionary

    Returns:
        None (prints user info)
    """
    print(f"Processing user: {user_data['name']}")


def create_order(user_id: UserID, order_id: OrderID) -> str:
    """Create an order for a user.

    Args:
        user_id: The user's unique ID
        order_id: The order's unique ID

    Returns:
        Status message
    """
    return f"Order #{order_id} for user #{user_id}"


def sum_matrix(matrix: Matrix) -> int:
    """Calculate the sum of all elements in a matrix.

    Args:
        matrix: A 2D list of integers

    Returns:
        Sum of all matrix elements
    """
    total: int = 0
    for row in matrix:
        for value in row:
            total += value
    return total


def create_identity_matrix(size: int) -> Matrix:
    """Create an identity matrix of given size.

    Args:
        size: The size of the square matrix

    Returns:
        Identity matrix (1s on diagonal, 0s elsewhere)
    """
    matrix: Matrix = []
    for i in range(size):
        row: list[int] = []
        for j in range(size):
            row.append(1 if i == j else 0)
        matrix.append(row)
    return matrix


def main() -> None:
    """Run exercise demonstrations."""
    # Test user data with type alias
    user1: UserData = create_user("Alice", 30, "alice@example.com", ["python", "docker"])
    user2: UserData = create_user("Bob", 25, "bob@example.com", ["kubernetes"])

    process_user(user1)
    process_user(user2)

    # Test NewType for IDs
    # NewType requires explicit construction
    user_id: UserID = UserID(5001)
    order_id: OrderID = OrderID(1001)
    print(create_order(user_id, order_id))

    # This works with properly typed IDs
    another_user: UserID = UserID(5002)
    another_order: OrderID = OrderID(1002)
    print(create_order(another_user, another_order))

    # Type checker would catch these errors:
    # create_order(5001, 1001)  # Error: Expected UserID and OrderID, got int
    # create_order(order_id, user_id)  # Error: Swapped types

    # Test matrix type alias
    matrix: Matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(f"Matrix sum: {sum_matrix(matrix)}")

    # Create identity matrix
    identity: Matrix = create_identity_matrix(3)
    print("Identity matrix:")
    for row in identity:
        print(row)


if __name__ == "__main__":
    main()
