"""Nested Model Examples

This module demonstrates nested Pydantic models.
"""

from pydantic import BaseModel, Field


class Address(BaseModel):
    """Address model."""
    street: str
    city: str
    country: str
    postal_code: str


class Person(BaseModel):
    """Person with nested address."""
    name: str
    age: int
    address: Address


class Item(BaseModel):
    """Order item."""
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(ge=1)


class Order(BaseModel):
    """Order with multiple items."""
    order_id: int
    customer: str
    items: list[Item]

    def total(self) -> float:
        """Calculate order total."""
        return sum(item.price * item.quantity for item in self.items)


def main() -> None:
    """Demonstrate nested models."""
    print("=== Nested Models ===")

    person = Person(
        name="Alice",
        age=30,
        address={
            "street": "123 Main St",
            "city": "New York",
            "country": "USA",
            "postal_code": "10001"
        }
    )
    print(f"Person: {person.name}, City: {person.address.city}")

    print("\n=== Lists of Nested Models ===")

    order = Order(
        order_id=1001,
        customer="Bob",
        items=[
            {"name": "Laptop", "price": 999.99, "quantity": 1},
            {"name": "Mouse", "price": 29.99, "quantity": 2},
        ]
    )
    print(f"Order #{order.order_id} for {order.customer}")
    print(f"Total: ${order.total():.2f}")

    for item in order.items:
        print(f"  {item.name}: ${item.price} x {item.quantity}")


if __name__ == "__main__":
    main()
