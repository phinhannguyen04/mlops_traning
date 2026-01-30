"""Exercise 2 Solution: Field Constraints"""
from pydantic import BaseModel, Field

class Account(BaseModel):
    username: str = Field(min_length=3, max_length=20, pattern=r'^[a-zA-Z0-9_]+$')
    password: str = Field(min_length=8)
    age: int = Field(ge=18)

class Product(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0, le=1000000)
    quantity: int = Field(ge=0)
    sku: str = Field(pattern=r'^[A-Z]{3}-\d{3}$')

def main():
    account = Account(username="alice_123", password="SecurePass123", age=25)
    product = Product(name="Laptop", price=999.99, quantity=5, sku="LAP-001")
    print(f"Account: {account}")
    print(f"Product: {product}")

if __name__ == "__main__":
    main()
