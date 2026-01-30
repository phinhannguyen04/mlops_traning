"""Exercise 1: Basic Models

Create simple Pydantic models with type annotations and default values.

OBJECTIVE:
- Create BaseModel classes
- Add type hints to fields
- Set default values
- Test validation with valid and invalid data

INSTRUCTIONS:
1. Complete the User and Product models with specified fields
2. Add appropriate type hints
3. Set default values where indicated
4. Test creating instances
5. Handle ValidationError for invalid data
"""

from pydantic import BaseModel, ValidationError

# TODO: Complete the User model
class User(BaseModel):
    """User model.

    Fields:
    - id: int (required)
    - name: str (required)
    - age: int (required)
    - email: str (required)
    - is_active: bool (default: True)
    """
    pass  # TODO: Add fields here


# TODO: Complete the Product model
class Product(BaseModel):
    """Product model.

    Fields:
    - name: str (required)
    - price: float (required, must be positive)
    - stock: int (required, must be >= 0)
    - description: str or None (optional, default: None)
    """
    pass  # TODO: Add fields here


def test_models() -> None:
    """Test model creation and validation."""
    print("=== Testing User Model ===")

    # TODO: Create a valid user
    # user = User(id=1, name="Alice", age=30, email="alice@example.com")
    # print(f"User created: {user}")

    # TODO: Create a user with default is_active
    # user2 = User(id=2, name="Bob", age=25, email="bob@example.com")
    # print(f"Is active (default): {user2.is_active}")

    print("\n=== Testing Product Model ===")

    # TODO: Create a valid product
    # product = Product(name="Laptop", price=999.99, stock=10)
    # print(f"Product created: {product}")

    print("\n=== Testing Validation ===")

    # TODO: Test invalid user (negative age)
    # try:
    #     invalid_user = User(id=3, name="Charlie", age=-5, email="charlie@example.com")
    # except ValidationError as e:
    #     print(f"ValidationError caught: age must be positive")

    # TODO: Test invalid product (negative price)
    # try:
    #     invalid_product = Product(name="Broken", price=-10, stock=5)
    # except ValidationError as e:
    #     print(f"ValidationError caught: price must be positive")


def test_serialization() -> None:
    """Test model serialization."""
    print("\n=== Testing Serialization ===")

    # TODO: Create a user and convert to dict
    # user = User(id=1, name="Alice", age=30, email="alice@example.com")
    # user_dict = user.model_dump()
    # print(f"As dict: {user_dict}")

    # TODO: Convert user to JSON
    # user_json = user.model_dump_json()
    # print(f"As JSON: {user_json}")


def main() -> None:
    """Run all tests."""
    test_models()
    test_serialization()


if __name__ == "__main__":
    main()
