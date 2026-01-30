# Advanced Python - Hands-On Labs

**Practical exercises for mastering advanced Python concepts**

## Overview

This directory contains hands-on labs for all advanced Python topics. Each lab includes examples, exercises, and solutions to help you master the concepts through practice.

## Lab Structure

```
advanced-python/
├── 01-typing/          # Python type hints
├── 02-uv/              # Project management with uv
├── 03-pydantic/        # Data validation
├── 04-decorators/      # Decorator patterns
└── 05-async-await/     # Asynchronous programming
```

Each lab contains:

- **README.md**: Lab overview and instructions
- **examples/**: Working code examples
- **exercises/**: Practice files with TODO sections
- **solution/**: Complete solutions

## Prerequisites

- Python 3.10 or higher
- Code editor or IDE
- Terminal/command prompt
- Basic Python knowledge

## Setup

### 1. Navigate to Advanced Python Directory

```bash
cd module-02/advanced-python
```

### 2. Install uv (for package management)

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Install Development Tools

```bash
uv add --dev mypy pytest black ruff
```

## Labs

### Lab 1: Python Typing

**Directory:** `01-typing/`
**Theory:** [Python Typing](../../docs/module-02/01-python-typing.md)

Learn type hints through 5 progressive exercises:

1. Basic type annotations
2. Collection types
3. Optional and Union types
4. Type aliases
5. Generic functions

**Estimated completion:** Practice thoroughly until concepts are clear

[Start Lab →](./01-typing/README.md)

### Lab 2: Project Management with uv

**Directory:** `02-uv/`
**Theory:** [Project Management with uv](../../docs/module-02/02-project-management-uv.md)

Master uv through 5 CLI exercises:

1. Project initialization
2. Dependency management
3. Development dependencies
4. Python version management
5. Scripts and task running

**Estimated completion:** Practice thoroughly until concepts are clear

[Start Lab →](./02-uv/README.md)

### Lab 3: Data Validation with Pydantic

**Directory:** `03-pydantic/`
**Theory:** [Data Validation with Pydantic](../../docs/module-02/03-data-validation-pydantic.md)

Build robust data models through 5 exercises:

1. Basic models
2. Field constraints
3. Nested models
4. Custom validators
5. API integration

**Estimated completion:** Practice thoroughly until concepts are clear

[Start Lab →](./03-pydantic/README.md)

### Lab 4: Decorators

**Directory:** `04-decorators/`
**Theory:** [Decorators](../../docs/module-02/04-decorators.md)

Master decorator patterns through 5 exercises:

1. Simple function decorator (timing)
2. Decorator with arguments (retry)
3. Class decorator (singleton)
4. Stacking decorators
5. Practical application (caching with TTL)

**Estimated completion:** Practice thoroughly until concepts are clear

[Start Lab →](./04-decorators/README.md)

### Lab 5: Async/Await

**Directory:** `05-async-await/`
**Theory:** [Async/Await](../../docs/module-02/05-async-await.md)

Learn asynchronous programming through 5 exercises:

1. First async function
2. Concurrent tasks
3. Async HTTP requests
4. Async context manager
5. Data processing pipeline

**Estimated completion:** Practice thoroughly until concepts are clear

[Start Lab →](./05-async-await/README.md)

## How to Use These Labs

### For Each Lab:

1. **Read theory first**
   - Review conceptual documentation
   - Understand key concepts
   - Study code examples

2. **Study examples**
   - Run example files
   - Understand how patterns work
   - Experiment with variations

3. **Complete exercises**
   - Read exercise description
   - Complete TODO sections
   - Test your code
   - Verify output matches expected results

4. **Check solutions**
   - Only after attempting yourself
   - Understand alternative approaches
   - Learn best practices

5. **Practice more**
   - Create your own variations
   - Combine multiple concepts
   - Build small projects

## Development Environment

### Recommended IDE Setup

**VS Code:**
- Install Python extension
- Install Pylance for type checking
- Enable mypy linting
- Configure auto-formatting with Black

**PyCharm:**
- Built-in type checking
- Excellent code completion
- Integrated testing

### Type Checking

Run mypy on your exercises:

```bash
mypy exercises/exercise_1.py
```

Run mypy in strict mode:

```bash
mypy --strict exercises/
```

### Code Formatting

Format code with Black:

```bash
black exercises/
```

Lint code with Ruff:

```bash
ruff check exercises/
```

## Testing Your Code

Most exercises include expected output. Verify your implementation:

```bash
# Run exercise
python exercises/exercise_1.py

# Run tests (if provided)
pytest tests/
```

## Common Issues

### Import Errors

If you see import errors:

```bash
# Ensure you're in correct directory
pwd

# Install required packages
uv add pydantic aiohttp aiofiles
```

### Type Checker Errors

If mypy reports errors you don't understand:

```bash
# Check with less strict settings
mypy --ignore-missing-imports exercises/

# Gradually enable strict mode
mypy --disallow-untyped-defs exercises/
```

### Virtual Environment Issues

If packages aren't found:

```bash
# Let uv handle it
uv run python exercises/exercise_1.py

# Or activate manually (if needed)
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

## Learning Tips

### 1. Type as You Learn

Always run type checkers on your code:

```bash
mypy --strict your_file.py
```

### 2. Read Error Messages Carefully

Type errors and validation errors contain valuable information:

```python
# Read the full error message
# It tells you exactly what's wrong
```

### 3. Experiment Freely

Try breaking things to understand how they work:

```python
# What happens if I pass wrong type?
# What if I forget await?
# How does the decorator order change behavior?
```

### 4. Build Small Projects

After each lab, build something:

- **After Typing**: Create a typed data processing script
- **After uv**: Set up a new project from scratch
- **After Pydantic**: Build an API request/response validator
- **After Decorators**: Add logging to existing code
- **After Async**: Fetch multiple URLs concurrently

### 5. Combine Concepts

Later exercises should use earlier concepts:

```python
# Combine typing + Pydantic + decorators + async
from pydantic import BaseModel
from functools import wraps
import asyncio

class User(BaseModel):  # Pydantic
    id: int            # Typing
    name: str

@timing  # Decorator
async def fetch_user(user_id: int) -> User:  # Typing + Async
    # Implementation
    pass
```

## Progressive Difficulty

Labs increase in complexity:

1. **01-typing**: Foundation (easiest)
2. **02-uv**: Tools (easy)
3. **03-pydantic**: Data handling (moderate)
4. **04-decorators**: Patterns (moderate)
5. **05-async-await**: Concurrency (challenging)

Work through in order for best results.

## Completion Checklist

Track your progress:

- [ ] Python Typing Lab complete (5 exercises)
- [ ] uv Lab complete (5 exercises)
- [ ] Pydantic Lab complete (5 exercises)
- [ ] Decorators Lab complete (5 exercises)
- [ ] Async/Await Lab complete (5 exercises)
- [ ] Built at least one project combining concepts
- [ ] Can explain concepts to others

## Next Steps

After completing all labs:

1. **Build a complete project** combining all concepts
2. **Review module-03** for CI/CD and monitoring
3. **Contribute improvements** to these labs
4. **Help others learn** in the community

## Example Combined Project

Build a type-safe async API client:

```python
from pydantic import BaseModel
from functools import lru_cache
from typing import List
import asyncio
import aiohttp

class User(BaseModel):
    id: int
    name: str
    email: str

@lru_cache(maxsize=100)
async def fetch_user(user_id: int) -> User:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"/api/users/{user_id}") as resp:
            data = await resp.json()
            return User(**data)

async def fetch_all_users(user_ids: List[int]) -> List[User]:
    tasks = [fetch_user(uid) for uid in user_ids]
    return await asyncio.gather(*tasks)
```

This combines: typing, Pydantic, decorators, and async/await!

## Additional Resources

- [Theory Documentation](../../docs/module-02/README.md)
- [Python Official Docs](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Mypy Documentation](https://mypy.readthedocs.io/)

## Getting Help

- **Stuck on an exercise?** Review the theory docs and examples
- **Type errors confusing?** Check the mypy documentation
- **Need clarification?** Open an issue in the repository
- **Want to discuss?** Join the community discussions

---

**Ready to start?** Begin with [Python Typing Lab →](./01-typing/README.md)
