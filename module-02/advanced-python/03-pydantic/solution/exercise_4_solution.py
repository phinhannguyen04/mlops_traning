"""Exercise 4 Solution: Custom Validators"""
from pydantic import BaseModel, field_validator, model_validator

class Password(BaseModel):
    value: str

    @field_validator('value')
    @classmethod
    def validate_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Too short')
        if not any(c.isupper() for c in v):
            raise ValueError('Need uppercase')
        return v

class DateRange(BaseModel):
    start: str
    end: str

    @model_validator(mode='after')
    def check_order(self) -> 'DateRange':
        if self.start >= self.end:
            raise ValueError('end must be after start')
        return self

def main():
    pwd = Password(value="SecurePass123")
    dates = DateRange(start="2024-01-01", end="2024-12-31")
    print(f"Password: {pwd.value}")
    print(f"Dates: {dates}")

if __name__ == "__main__":
    main()
