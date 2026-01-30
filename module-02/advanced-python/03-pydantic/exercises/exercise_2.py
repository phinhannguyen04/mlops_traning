"""Exercise 2: Field Constraints

Apply validation rules using Field constraints.

OBJECTIVE:
- Use Field() for validation constraints
- Apply numeric constraints (gt, ge, lt, le)
- Apply string constraints (min_length, max_length, pattern)
"""

from pydantic import BaseModel, Field, ValidationError

# TODO: Complete Account model with Field constraints
class Account(BaseModel):
    """Account with constrained fields.
    
    - username: 3-20 characters, alphanumeric pattern
    - password: minimum 8 characters
    - age: must be >= 18
    """
    pass  # TODO

# TODO: Complete Product model with constraints
class Product(BaseModel):
    """Product with price and quantity constraints.
    
    - name: 1-100 characters
    - price: > 0, <= 1000000
    - quantity: >= 0
    - sku: pattern like "ABC-123"
    """
    pass  # TODO


def main() -> None:
    # TODO: Test valid and invalid data
    print("Complete the TODO sections")


if __name__ == "__main__":
    main()
