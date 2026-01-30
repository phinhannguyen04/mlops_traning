"""Basic Pydantic Model Examples

This module demonstrates fundamental Pydantic patterns.
"""

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class User(BaseModel):
    """Basic user model with type hints."""

    id: int
    username: str
    email: str
    is_active: bool = True  # Default value
    created_at: datetime = Field(default_factory=datetime.now)


class Product(BaseModel):
    """Product model with optional fields."""

    name: str
    price: float = Field(gt=0)  # Must be greater than 0
    description: str | None = None  # Optional field
    in_stock: bool = True
    tags: list[str] = Field(default_factory=list)


def demonstrate_basic_models() -> None:
    """Show basic model creation and validation."""
    print("=== Basic Model Creation ===")

    # Create valid user
    user = User(id=1, username="alice", email="alice@example.com")
    print(f"User created: {user}")
    print(f"  ID: {user.id}")
    print(f"  Username: {user.username}")
    print(f"  Active: {user.is_active}")

    print("\n=== Model Serialization ===")

    # Convert to dictionary
    user_dict = user.model_dump()
    print(f"As dict: {user_dict}")

    # Convert to JSON
    user_json = user.model_dump_json()
    print(f"As JSON: {user_json}")

    print("\n=== Default Values ===")

    # Create product with defaults
    product = Product(name="Laptop", price=999.99)
    print(f"Product: {product}")
    print(f"  Description: {product.description}")  # None (default)
    print(f"  In stock: {product.in_stock}")  # True (default)
    print(f"  Tags: {product.tags}")  # [] (default)


def demonstrate_validation() -> None:
    """Show validation errors."""
    print("\n=== Validation Errors ===")

    # Invalid user (wrong type)
    try:
        user = User(id="not-a-number", username="bob", email="bob@example.com")
    except ValidationError as e:
        print("Error: Invalid ID type")
        print(f"  {e.errors()[0]['msg']}")

    # Invalid product (negative price)
    try:
        product = Product(name="Broken", price=-10)
    except ValidationError as e:
        print("Error: Negative price")
        print(f"  {e.errors()[0]['msg']}")

    # Missing required field
    try:
        user = User(id=1, username="charlie")  # Missing email
    except ValidationError as e:
        print("Error: Missing required field")
        print(f"  {e.errors()[0]['loc']}: {e.errors()[0]['msg']}")


def demonstrate_parsing() -> None:
    """Show automatic type parsing."""
    print("\n=== Automatic Type Parsing ===")

    # String numbers are converted
    user = User(id="123", username="dave", email="dave@example.com")
    print(f"ID type: {type(user.id)}")  # int, not str
    print(f"ID value: {user.id}")

    # Price from string
    product = Product(name="Mouse", price="29.99")
    print(f"Price type: {type(product.price)}")  # float
    print(f"Price value: {product.price}")


def demonstrate_model_methods() -> None:
    """Show useful model methods."""
    print("\n=== Model Methods ===")

    user = User(id=1, username="eve", email="eve@example.com")

    # Get field names
    print(f"Fields: {list(user.model_fields.keys())}")

    # Copy with changes
    user2 = user.model_copy(update={"username": "eve_updated"})
    print(f"Original: {user.username}")
    print(f"Copy: {user2.username}")

    # Export with exclusions
    user_public = user.model_dump(exclude={'id', 'created_at'})
    print(f"Public data: {user_public}")


def main() -> None:
    """Run all demonstrations."""
    demonstrate_basic_models()
    demonstrate_validation()
    demonstrate_parsing()
    demonstrate_model_methods()


if __name__ == "__main__":
    main()
