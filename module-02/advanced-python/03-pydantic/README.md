# Data Validation with Pydantic - Hands-On Lab

**Practice building type-safe data models with automatic validation**

## Overview

This lab provides hands-on practice with Pydantic, from basic models to advanced validation patterns. You'll learn to validate data, handle complex nested structures, create custom validators, and integrate with real-world APIs.

## Prerequisites

- Python 3.10 or higher
- Understanding of Python type hints (see [Python Typing](../01-typing/README.md))
- Basic knowledge of classes and objects

## Setup

### 1. Navigate to Lab Directory

```bash
cd module-02/advanced-python/03-pydantic
```

### 2. Install Pydantic

```bash
# With uv
uv add pydantic

# With email validation
uv add "pydantic[email]"

# Or with pip
pip install "pydantic[email]"
```

### 3. Verify Installation

```bash
python -c "import pydantic; print(pydantic.__version__)"
```

## Lab Structure

```
03-pydantic/
├── README.md           # This file
├── examples/           # Reference examples
│   ├── basic_model.py
│   ├── validators.py
│   ├── nested_models.py
│   └── api_example.py
├── exercises/          # Your practice files
│   ├── exercise_1.py
│   ├── exercise_2.py
│   ├── exercise_3.py
│   ├── exercise_4.py
│   └── exercise_5.py
└── solution/           # Solution files
    ├── exercise_1_solution.py
    ├── exercise_2_solution.py
    ├── exercise_3_solution.py
    ├── exercise_4_solution.py
    └── exercise_5_solution.py
```

## How to Work Through Exercises

1. **Read the exercise description** in this README
2. **Review example files** in `examples/` for reference
3. **Open the exercise file** in `exercises/`
4. **Complete the TODO sections** following instructions
5. **Run the code** to verify it works
6. **Test with invalid data** to see validation in action
7. **Compare with solution** in `solution/` if needed

## Exercises

### Exercise 1: Basic Models

**Objective:** Create simple Pydantic models with type annotations and default values

**Background:**

Pydantic models use type hints to automatically validate data. When you create an instance with invalid data, Pydantic raises a `ValidationError` with clear error messages.

**Instructions:**

1. Open `exercises/exercise_1.py`
2. Create BaseModel classes with specified fields
3. Add type hints to all fields
4. Set default values where specified
5. Test creating instances with valid and invalid data
6. Run the code to see validation in action

**Expected Output:**

```
User created: name='Alice' age=30 email='alice@example.com' is_active=True
Product created: name='Laptop' price=999.99 stock=10 description=None
ValidationError: age must be positive
ValidationError: price must be positive
```

**Key Learnings:**

- How to create Pydantic BaseModel classes
- How type hints enable automatic validation
- How to set default values
- How ValidationError works
- How to access model fields

**Common Mistakes:**

- Forgetting to inherit from BaseModel
- Using `=` instead of `:` for type hints
- Not handling ValidationError when testing invalid data

### Exercise 2: Field Constraints

**Objective:** Apply validation rules using Field constraints

**Background:**

Field constraints let you specify rules beyond type checking: minimum/maximum values, string lengths, regex patterns, and more. This catches business logic errors early.

**Instructions:**

1. Open `exercises/exercise_2.py`
2. Add Field constraints to model fields
3. Implement min/max values for numeric fields
4. Add string length constraints
5. Use regex patterns for formatted strings
6. Test with both valid and invalid data

**Expected Output:**

```
Account created: username='alice_123' password='SecurePass123' age=25
Product validated: name='Laptop' price=999.99 quantity=5 sku='LAP-001'
ValidationError: username must be 3-20 characters
ValidationError: password must be at least 8 characters
ValidationError: price must be greater than 0
ValidationError: SKU format invalid
```

**Key Learnings:**

- How to use Field() for constraints
- Numeric constraints: gt, ge, lt, le
- String constraints: min_length, max_length, pattern
- How to combine multiple constraints
- When to use different constraint types

**Common Mistakes:**

- Confusing gt (greater than) with ge (greater or equal)
- Forgetting to import Field from pydantic
- Regex patterns without r'' prefix

### Exercise 3: Nested Models

**Objective:** Build complex hierarchical data structures

**Background:**

Real applications deal with nested data: users with addresses, orders with items, posts with comments. Pydantic makes nested validation straightforward - each level is validated independently.

**Instructions:**

1. Open `exercises/exercise_3.py`
2. Create models for nested data structures
3. Use models as field types in other models
4. Handle lists of nested models
5. Access and manipulate nested data
6. Test validation at all nesting levels

**Expected Output:**

```
User with address: name='Alice' city='New York'
Order total: $1059.97
Post with 2 tags and 1 comment
ValidationError: Invalid nested address
ValidationError: Invalid item in order
```

**Key Learnings:**

- How to use models as field types
- Lists of models: `list[ModelName]`
- Accessing nested fields with dot notation
- Validation cascades through nesting levels
- Creating instances from nested dictionaries

**Common Mistakes:**

- Not creating separate classes for nested data
- Forgetting to type list elements: `list[Item]` not `list`
- Accessing nested fields incorrectly

### Exercise 4: Custom Validators

**Objective:** Write custom validation logic

**Background:**

Field constraints handle common cases, but business logic often requires custom validation: checking passwords, validating date ranges, enforcing cross-field rules. Custom validators give you full control.

**Instructions:**

1. Open `exercises/exercise_4.py`
2. Create `@field_validator` methods
3. Write validation logic for individual fields
4. Create `@model_validator` for cross-field validation
5. Return transformed values when appropriate
6. Raise ValueError with clear messages for invalid data

**Expected Output:**

```
Password validated: Strong password accepted
Date range valid: 2024-01-01 to 2024-12-31
User validated: email normalized to lowercase
ValidationError: Password too weak
ValidationError: end_date must be after start_date
ValidationError: Username must be alphanumeric
```

**Key Learnings:**

- How to use `@field_validator`
- How to use `@model_validator` for cross-field validation
- When to use `mode='before'` vs `mode='after'`
- How to transform values in validators
- Writing clear error messages

**Common Mistakes:**

- Forgetting `@classmethod` decorator
- Not returning the value from validator
- Using instance methods instead of class methods
- Validators that are too complex (split into multiple)

### Exercise 5: API Integration

**Objective:** Use Pydantic for request/response validation in a realistic API scenario

**Background:**

Pydantic shines in API development. You define models for requests and responses, and validation happens automatically. This exercise simulates an ML model serving API.

**Instructions:**

1. Open `exercises/exercise_5.py`
2. Create models for API requests
3. Create models for API responses
4. Implement validation for ML input data
5. Handle nested prediction results
6. Serialize responses to JSON

**Expected Output:**

```
Prediction request validated:
  Features: [5.1, 3.5, 1.4, 0.2]
  Model: iris_classifier
Prediction response:
  {"prediction": "setosa", "confidence": 0.95, "model_version": "1.0"}
ValidationError: Invalid feature count
ValidationError: Unsupported model
```

**Key Learnings:**

- Separating request and response models
- Using Literal for enumerated values
- JSON serialization with `model_dump_json()`
- Excluding sensitive fields from responses
- Real-world API patterns with Pydantic

**Common Mistakes:**

- Using same model for request and response
- Not excluding internal fields from responses
- Overly permissive validation in APIs

## Running Examples

Before starting exercises, review example files:

```bash
# View basic model examples
python examples/basic_model.py

# View custom validation patterns
python examples/validators.py

# View nested model examples
python examples/nested_models.py

# View API integration example
python examples/api_example.py
```

## Validation Error Handling

All exercises should handle ValidationError:

```python
from pydantic import ValidationError

try:
    user = User(name="Alice", age="invalid")
except ValidationError as e:
    print("Validation failed:")
    print(e)
    # Access errors programmatically
    for error in e.errors():
        print(f"Field: {error['loc']}, Error: {error['msg']}")
```

## What You Learned

After completing this lab, you should be able to:

- Create Pydantic BaseModel classes
- Apply Field constraints for validation
- Build nested model hierarchies
- Write custom field and model validators
- Serialize models to JSON
- Handle ValidationError exceptions
- Use Pydantic for API request/response validation
- Understand when to use different validation approaches

## Troubleshooting

### Import Errors

If you see `ImportError: cannot import name 'BaseModel'`:

```bash
# Reinstall pydantic
pip uninstall pydantic
pip install "pydantic>=2.0"
```

### ValidationError Not Caught

Make sure to import and catch ValidationError:

```python
from pydantic import ValidationError

try:
    model = MyModel(**data)
except ValidationError as e:
    print(e)
```

### Email Validation Not Working

Install email validation extras:

```bash
pip install "pydantic[email]"
```

### Type Checker Complaints

Some type checkers need help with Pydantic:

```bash
# Install pydantic mypy plugin
pip install pydantic[mypy]
```

Add to `mypy.ini`:

```ini
[mypy]
plugins = pydantic.mypy
```

## Real-World Scenarios

### Scenario 1: API Request Validation

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class TrainRequest(BaseModel):
    dataset: str
    model_type: str = Field(pattern=r'^(rf|svm|nn)$')
    hyperparameters: dict[str, float]

@app.post("/train")
def train_model(request: TrainRequest):
    # request is automatically validated
    return {"status": "training", "dataset": request.dataset}
```

### Scenario 2: Configuration Management

```python
from pydantic import BaseModel, Field
import os

class DatabaseConfig(BaseModel):
    host: str = Field(default="localhost")
    port: int = Field(ge=1, le=65535)
    database: str
    username: str
    password: str

class AppConfig(BaseModel):
    debug: bool = False
    database: DatabaseConfig
    api_key: str = Field(min_length=32)

# Load from environment or file
config = AppConfig(**os.environ)
```

### Scenario 3: Data ETL Pipeline

```python
from pydantic import BaseModel, field_validator
import pandas as pd

class UserRecord(BaseModel):
    id: int
    email: str
    age: int = Field(ge=0, le=150)
    country: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v.lower()

# Validate DataFrame rows
def validate_users(df: pd.DataFrame) -> list[UserRecord]:
    validated = []
    errors = []
    for idx, row in df.iterrows():
        try:
            validated.append(UserRecord(**row.to_dict()))
        except ValidationError as e:
            errors.append((idx, e))
    return validated, errors
```

## Best Practices from This Lab

### 1. Always Use Type Hints

```python
# Good
class User(BaseModel):
    name: str
    age: int

# Bad
class User(BaseModel):
    name = ""  # No type hint
    age = 0
```

### 2. Separate Input and Output Models

```python
# Input (accept password)
class UserCreate(BaseModel):
    username: str
    password: str

# Output (never expose password)
class User(BaseModel):
    id: int
    username: str
```

### 3. Use Field Descriptions

```python
class Product(BaseModel):
    name: str = Field(description="Product name")
    price: float = Field(gt=0, description="Price in USD")
```

### 4. Handle Validation Errors Gracefully

```python
try:
    user = User(**user_data)
except ValidationError as e:
    # Log error details
    logger.error(f"Validation failed: {e}")
    # Return user-friendly message
    return {"error": "Invalid user data"}
```

### 5. Use Computed Fields for Derived Data

```python
from pydantic import computed_field

class Order(BaseModel):
    items: list[Item]

    @computed_field
    @property
    def total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
```

## Next Steps

After mastering Pydantic, continue to:

- [Theory: Decorators](../../../docs/module-02/04-decorators.md)
- [Hands-On: Decorators Lab](../04-decorators/README.md)

## Additional Practice Ideas

1. **Build a REST API**
   - Use FastAPI with Pydantic models
   - Create CRUD endpoints
   - Handle validation errors

2. **Create a Configuration System**
   - Load config from YAML/JSON
   - Validate with Pydantic
   - Support environment variable overrides

3. **Data Pipeline Validation**
   - Validate CSV/JSON data files
   - Track validation errors
   - Generate data quality reports

4. **Build an ORM-like System**
   - Create models for database tables
   - Implement CRUD operations
   - Use Pydantic for validation

## Additional Resources

- [Theory: Data Validation with Pydantic](../../../docs/module-02/03-data-validation-pydantic.md)
- [Official Pydantic Docs](https://docs.pydantic.dev/)
- [Pydantic with FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic Performance Tips](https://docs.pydantic.dev/latest/concepts/performance/)
