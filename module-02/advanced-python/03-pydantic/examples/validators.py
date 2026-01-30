"""Custom Validator Examples

This module demonstrates field and model validators.
"""

from pydantic import BaseModel, field_validator, model_validator, ValidationError


class Password(BaseModel):
    """Password with strength validation."""

    value: str

    @field_validator('value')
    @classmethod
    def validate_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain uppercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain digit')
        return v


class DateRange(BaseModel):
    """Date range with validation."""

    start_date: str
    end_date: str

    @model_validator(mode='after')
    def validate_date_order(self) -> 'DateRange':
        if self.start_date >= self.end_date:
            raise ValueError('end_date must be after start_date')
        return self


class User(BaseModel):
    """User with email normalization."""

    username: str
    email: str

    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v

    @field_validator('email')
    @classmethod
    def normalize_email(cls, v: str) -> str:
        return v.lower().strip()


def main() -> None:
    """Demonstrate validators."""
    print("=== Field Validators ===")

    # Valid password
    pwd = Password(value="SecurePass123")
    print(f"Password accepted: {pwd.value}")

    # Invalid password
    try:
        Password(value="weak")
    except ValidationError as e:
        print(f"Password rejected: {e.errors()[0]['msg']}")

    print("\n=== Model Validators ===")

    # Valid date range
    dates = DateRange(start_date="2024-01-01", end_date="2024-12-31")
    print(f"Valid range: {dates.start_date} to {dates.end_date}")

    # Invalid range
    try:
        DateRange(start_date="2024-12-31", end_date="2024-01-01")
    except ValidationError as e:
        print(f"Invalid range: {e.errors()[0]['msg']}")

    print("\n=== Value Transformation ===")

    # Email normalized to lowercase
    user = User(username="alice123", email="Alice@EXAMPLE.COM  ")
    print(f"Email normalized: {user.email}")


if __name__ == "__main__":
    main()
