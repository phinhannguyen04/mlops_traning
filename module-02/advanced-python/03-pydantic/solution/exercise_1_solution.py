"""Exercise 1 Solution: Basic Models"""

from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    """User model with type hints and defaults."""
    id: int
    name: str
    age: int = Field(gt=0)
    email: str
    is_active: bool = True


class Product(BaseModel):
    """Product model with constraints."""
    name: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    description: str | None = None


def main() -> None:
    # Valid user
    user = User(id=1, name="Alice", age=30, email="alice@example.com")
    print(f"User: {user}")

    # Valid product
    product = Product(name="Laptop", price=999.99, stock=10)
    print(f"Product: {product}")

    # Serialization
    print(f"User dict: {user.model_dump()}")
    print(f"User JSON: {user.model_dump_json()}")


if __name__ == "__main__":
    main()
