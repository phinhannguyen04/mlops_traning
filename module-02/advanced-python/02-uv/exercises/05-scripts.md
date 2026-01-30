# Exercise 5: Scripts and Task Running

**Define reusable project scripts and commands**

## Objective

Learn to define custom scripts in `pyproject.toml` for common development tasks.

## Background

Instead of documenting commands in README files, define them as project scripts. This makes tasks discoverable and consistent across teams.

## Step 1: Create Script Project

```bash
cd module-02/advanced-python/02-uv
uv init script-demo
cd script-demo
```

## Step 2: Add Dependencies

```bash
uv add requests
uv add --dev pytest black
```

## Step 3: Create Application Code

Create `app.py`:

```python
def main():
    print("Application is running!")
    print("This would start your ML model server...")

if __name__ == "__main__":
    main()
```

## Step 4: Define Scripts in pyproject.toml

Edit `pyproject.toml` and add:

```toml
[project.scripts]
start = "app:main"
greet = "app:greet_user"
```

Also add to `app.py`:

```python
def greet_user():
    print("Hello from uv scripts!")

def main():
    print("Application is running!")
```

## Step 5: Run Scripts

```bash
uv run start
uv run greet
```

**Expected Output:**

```
Application is running!
This would start your ML model server...

Hello from uv scripts!
```

## Step 6: Define Development Task Scripts

Common pattern for development tasks:

```toml
[project.scripts]
# Application
start = "app:main"

# Development tasks
test = "pytest:main"
format = "black:main"
lint = "ruff:main"
```

But this requires packages to have proper entry points. Better approach:

## Step 7: Use Shell Scripts for Complex Tasks

Create `scripts/` directory:

```bash
mkdir scripts
```

Create `scripts/test.py`:

```python
#!/usr/bin/env python
import subprocess
import sys

def main():
    result = subprocess.run(["pytest", "-v"], check=False)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
```

Reference in `pyproject.toml`:

```toml
[project.scripts]
test = "scripts.test:main"
```

## Step 8: Alternative: Use Makefile

Create `Makefile`:

```makefile
.PHONY: test lint format run

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run mypy .

format:
	uv run black .

run:
	uv run python app.py

all: format lint test
```

Run tasks:

```bash
make test
make lint
make format
make all
```

## Step 9: Document Available Commands

Add to `README.md`:

```markdown
## Available Commands

### Application
```bash
uv run start        # Start application
```

### Development
```bash
make test          # Run tests
make lint          # Check code quality
make format        # Format code
make all           # Format, lint, and test
```
```

## Step 10: Real-World Example

Complete setup for ML project:

**pyproject.toml:**

```toml
[project]
name = "ml-classifier"
dependencies = [
    "scikit-learn>=1.3.0",
    "pandas>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "black>=23.7.0",
    "mypy>=1.5.0",
]

[project.scripts]
train = "ml_classifier.train:main"
predict = "ml_classifier.predict:main"
evaluate = "ml_classifier.evaluate:main"
```

**Makefile:**

```makefile
.PHONY: install test train predict

install:
	uv sync --dev

test:
	uv run pytest tests/

train:
	uv run train --data data/train.csv

predict:
	uv run predict --model models/best.pkl --input data/test.csv

clean:
	rm -rf .venv __pycache__ .pytest_cache
```

## Key Learnings

✅ `[project.scripts]` defines CLI entry points
✅ Scripts reference Python functions: `"module:function"`
✅ Combine with Makefiles for complex tasks
✅ Document commands in README
✅ Makes projects self-documenting

## Verification Checklist

You should now be able to:

- [ ] Define scripts in `pyproject.toml`
- [ ] Run scripts with `uv run <script-name>`
- [ ] Create Makefiles for development tasks
- [ ] Organize commands for team consistency
- [ ] Document available commands

## Summary of All Exercises

You've learned the complete uv workflow:

1. **Initialize projects** with `uv init`
2. **Manage dependencies** with `uv add/remove/sync`
3. **Separate dev dependencies** with `--dev`
4. **Handle Python versions** with `uv python`
5. **Define project scripts** for common tasks

## Next Steps

Continue to [Data Validation with Pydantic](../03-pydantic/README.md) to learn about type-safe data handling.
