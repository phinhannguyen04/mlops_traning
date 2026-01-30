"""Exercise 3 Solution: Nested Models"""
from pydantic import BaseModel, Field

class Address(BaseModel):
    street: str
    city: str
    country: str

class Person(BaseModel):
    name: str
    age: int
    address: Address

class Item(BaseModel):
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(ge=1)

class Order(BaseModel):
    order_id: int
    items: list[Item]

def main():
    person = Person(name="Alice", age=30, address={"street": "123 Main", "city": "NYC", "country": "USA"})
    order = Order(order_id=1, items=[{"name": "Laptop", "price": 999, "quantity": 1}])
    print(f"Person: {person.name} in {person.address.city}")
    print(f"Order: {order}")

if __name__ == "__main__":
    main()
