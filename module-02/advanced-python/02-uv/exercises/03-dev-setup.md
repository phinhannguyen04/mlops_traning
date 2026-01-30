# Exercise 3: Development Dependencies

**Separate development tools from runtime requirements**

## Objective

Learn to organize dependencies by purpose: runtime vs development-only packages.

## Background

Production applications shouldn't include testing frameworks, linters, or development tools. `uv` lets you separate these concerns using optional dependency groups.

## Step 1: Create Test Project

```bash
cd module-02/advanced-python/02-uv
uv init test-project
cd test-project
```

## Step 2: Add Runtime Dependencies

```bash
uv add requests pydantic
```

These are required for your application to run.

## Step 3: Add Development Dependencies

```bash
uv add --dev pytest black mypy ruff
```

**Expected Output:**

```
Installed 15 packages in 234ms
 + black==24.1.1
 + mypy==1.8.0
 + pytest==7.4.4
 + ruff==0.1.14
 + ...
```

## Step 4: Check pyproject.toml

```bash
cat pyproject.toml
```

**Notice the separation:**

```toml
[project]
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.5.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.4",
    "black>=24.1.1",
    "mypy>=1.8.0",
    "ruff>=0.1.14",
]
```

## Step 5: Install Only Runtime Dependencies

```bash
rm -rf .venv
uv sync  # Without --dev flag
```

Only `requests` and `pydantic` are installed. Perfect for production!

## Step 6: Install Development Dependencies

```bash
uv sync --dev
```

Now all dependencies (runtime + dev) are installed.

## Step 7: Write Tests

Create `test_app.py`:

```python
def add(a: int, b: int) -> int:
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

Run tests:

```bash
uv run pytest
```

## Step 8: Format Code

```bash
uv run black .
```

## Step 9: Lint Code

```bash
uv run ruff check .
```

## Step 10: Type Check

```bash
uv run mypy test_app.py
```

## Key Learnings

✅ Use `--dev` flag for development-only packages
✅ Runtime dependencies in `[project.dependencies]`
✅ Dev dependencies in `[project.optional-dependencies.dev]`
✅ Production builds use `uv sync` (no --dev)
✅ Development uses `uv sync --dev`

## Next Steps

Move to [Exercise 4: Python Version Management](./04-python-versions.md).
