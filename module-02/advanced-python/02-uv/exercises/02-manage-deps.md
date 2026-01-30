# Exercise 2: Dependency Management

**Master adding, removing, and updating Python packages with uv**

## Objective

By the end of this exercise, you'll understand how to:
- Add runtime dependencies with `uv add`
- Understand the `uv.lock` lock file
- Remove packages with `uv remove`
- Install dependencies with `uv sync`
- Update packages with `uv lock --upgrade`
- Understand reproducible dependency resolution

## Background

Managing dependencies is crucial for Python projects. Traditional `pip install` doesn't track exact versions, leading to "works on my machine" problems. `uv` solves this with automatic lock files that capture exact versions of all dependencies (including transitive ones), ensuring reproducible builds across teams and environments.

## Step 1: Create a New Project

Start with a fresh project for this exercise:

```bash
cd module-02/advanced-python/02-uv
uv init dependency-demo
cd dependency-demo
```

## Step 2: Add Your First Dependency

Let's add the `requests` library for HTTP requests:

```bash
uv add requests
```

**Expected Output:**

```
Resolved 5 packages in 234ms
Downloaded 4 packages in 1.2s
Installed 5 packages in 45ms
 + certifi==2024.2.2
 + charset-normalizer==3.3.2
 + idna==3.6
 + requests==2.31.0
 + urllib3==2.2.0
```

### What Happened?

1. **Resolved**: uv figured out all required packages (requests + its dependencies)
2. **Downloaded**: Fetched packages from PyPI
3. **Installed**: Installed packages into `.venv`
4. **Transitive dependencies**: Notice requests brought in 4 additional packages

## Step 3: Inspect pyproject.toml

Check how dependencies are recorded:

```bash
cat pyproject.toml
```

**New Content:**

```toml
[project]
name = "dependency-demo"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.31.0",
]
```

Notice `requests>=2.31.0` is now in the `dependencies` array.

## Step 4: Understand the Lock File

The magic of reproducibility comes from `uv.lock`:

```bash
cat uv.lock
```

**Sample Output (truncated):**

```toml
version = 1
requires-python = ">=3.11"

[[package]]
name = "certifi"
version = "2024.2.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "...", hash = "sha256:..." }

[[package]]
name = "requests"
version = "2.31.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "charset-normalizer" },
    { name = "idna" },
    { name = "urllib3" },
]
sdist = { url = "...", hash = "sha256:..." }
```

### Key Points

- **Exact versions**: Every package has a precise version number
- **Hashes**: SHA256 hashes prevent tampering
- **Transitive dependencies**: All dependencies of dependencies are listed
- **Reproducible**: Anyone with this lock file gets identical package versions

## Step 5: Add Multiple Packages

Add several packages at once:

```bash
uv add pandas numpy
```

**Expected Output:**

```
Resolved 8 packages in 456ms
Downloaded 3 packages in 2.1s
Installed 3 packages in 98ms
 + numpy==1.26.3
 + pandas==2.2.0
 + python-dateutil==2.8.2
 + pytz==2024.1
 + tzdata==2024.1
```

Check `pyproject.toml` again:

```bash
cat pyproject.toml
```

**Updated Dependencies:**

```toml
dependencies = [
    "requests>=2.31.0",
    "numpy>=1.26.3",
    "pandas>=2.2.0",
]
```

## Step 6: Add Package with Version Constraint

Sometimes you need specific version ranges:

```bash
uv add "fastapi>=0.100.0,<1.0.0"
```

This installs FastAPI version 0.100.0 or higher, but less than 1.0.0.

Check `pyproject.toml`:

```toml
dependencies = [
    "requests>=2.31.0",
    "numpy>=1.26.3",
    "pandas>=2.2.0",
    "fastapi>=0.100.0,<1.0.0",
]
```

## Step 7: Use Installed Packages

Create a Python script that uses your dependencies:

```bash
cat > fetch_data.py << 'EOF'
"""Fetch data from an API using requests."""
import requests
import pandas as pd

def fetch_users():
    """Fetch user data from JSONPlaceholder API."""
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()

    # Convert to pandas DataFrame
    df = pd.DataFrame(users)
    print(f"Fetched {len(df)} users")
    print("\nFirst 3 users:")
    print(df[['name', 'email', 'company']].head(3))

if __name__ == "__main__":
    fetch_users()
EOF
```

Run it:

```bash
uv run python fetch_data.py
```

**Expected Output:**

```
Fetched 10 users

First 3 users:
                name                    email              company
0  Leanne Graham  Sincere@april.biz  {'name': 'Romaguera-Crona'...
1    Ervin Howell    Shanna@melissa.tv  {'name': 'Deckow-Crist'...
2  Clementine Bauch  Nathan@yesenia.net  {'name': 'Romaguera-Jacobson'...
```

## Step 8: Remove a Package

Let's remove FastAPI since we're not using it:

```bash
uv remove fastapi
```

**Expected Output:**

```
Removed fastapi>=0.100.0,<1.0.0
Updated 1 package in 123ms
```

Check `pyproject.toml`:

```bash
grep fastapi pyproject.toml
```

No output - it's gone!

## Step 9: Sync Dependencies

The `uv sync` command installs all dependencies from `pyproject.toml`:

```bash
# First, remove .venv to simulate a fresh install
rm -rf .venv  # Windows: rmdir /s .venv

# Now sync
uv sync
```

**Expected Output:**

```
Resolved 12 packages in 145ms
Downloaded 12 packages in 1.5s
Installed 12 packages in 89ms
 + certifi==2024.2.2
 + charset-normalizer==3.3.2
 + idna==3.6
 + numpy==1.26.3
 + pandas==2.2.0
 + python-dateutil==2.8.2
 + pytz==2024.1
 + requests==2.31.0
 + six==1.16.0
 + tzdata==2024.1
 + urllib3==2.2.0
```

### When to Use uv sync

- **After cloning a repository**: Install all dependencies
- **After pulling changes**: Update dependencies
- **After modifying pyproject.toml manually**: Sync environment with config
- **CI/CD pipelines**: Reproducible builds

## Step 10: Update Dependencies

Check for outdated packages:

```bash
uv pip list --outdated
```

**Sample Output:**

```
Package    Version  Latest
---------- -------- --------
numpy      1.26.3   1.26.4
pandas     2.2.0    2.2.1
```

Update all packages to latest compatible versions:

```bash
uv lock --upgrade
```

**Expected Output:**

```
Resolved 12 packages in 567ms
Updated uv.lock
```

Now install the updated versions:

```bash
uv sync
```

Check versions:

```bash
uv pip list
```

## Step 11: Update Specific Package

To update just one package:

```bash
uv lock --upgrade-package numpy
uv sync
```

This updates only `numpy` to the latest compatible version.

## Step 12: Simulate Team Collaboration

This demonstrates why lock files matter:

### Scenario: You Share Your Project

```bash
# Your teammate clones the repo and runs:
git clone <your-repo>
cd <your-repo>
uv sync
```

They get **exactly** the same package versions as you because of `uv.lock`.

### Without Lock Files (old pip way)

```bash
# Person A installs
pip install pandas  # Gets pandas 2.2.0

# Later, Person B installs
pip install pandas  # Gets pandas 2.2.1 (newer version released)

# Different versions = potential bugs!
```

### With uv Lock Files

```bash
# Person A
uv add pandas  # Creates lock with pandas 2.2.0
git commit uv.lock

# Person B
git pull
uv sync  # Gets exact same pandas 2.2.0

# Same versions = reproducible!
```

## Step 13: Working with requirements.txt (Legacy)

If you need to export to requirements.txt:

```bash
uv pip compile pyproject.toml -o requirements.txt
```

Or install from requirements.txt:

```bash
uv pip install -r requirements.txt
```

But prefer using `pyproject.toml` directly!

## Exploration Tasks

### Task A: Add a Data Science Stack

```bash
uv add scipy scikit-learn matplotlib seaborn
```

Check how many total packages were installed (including transitive dependencies).

### Task B: Create a Data Analysis Script

Create `analyze.py`:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randn(10)
})

print(data)
```

Run it:

```bash
uv run python analyze.py
```

### Task C: Version Pinning Experiment

Edit `pyproject.toml` and change:

```toml
dependencies = [
    "requests>=2.31.0",  # Flexible
]
```

To:

```toml
dependencies = [
    "requests==2.31.0",  # Pinned
]
```

Then run:

```bash
uv lock
```

What's the difference in behavior?

## Key Learnings

After completing this exercise, you should understand:

✅ **`uv add`** adds dependencies to `pyproject.toml` and `uv.lock`
✅ **`uv.lock`** captures exact versions for reproducibility
✅ **`uv remove`** removes dependencies cleanly
✅ **`uv sync`** installs all dependencies from lock file
✅ **`uv lock --upgrade`** updates dependencies to latest compatible versions
✅ **Transitive dependencies** are automatically managed
✅ **Lock files** should be committed to git

## Common Mistakes

### Mistake 1: Not Committing Lock Files

❌ **Don't do this:**

```bash
echo "uv.lock" >> .gitignore  # BAD!
```

✅ **Do this instead:**

```bash
git add pyproject.toml uv.lock
git commit -m "Add requests dependency"
```

### Mistake 2: Using pip in uv Projects

❌ **Don't do this:**

```bash
pip install requests  # Bypasses uv management
```

✅ **Do this instead:**

```bash
uv add requests  # Proper uv command
```

### Mistake 3: Ignoring Lock File Conflicts

When merging branches with different dependencies:

❌ **Don't do this:**

```bash
# Just accept one side of the conflict
git checkout --theirs uv.lock
```

✅ **Do this instead:**

```bash
# Merge both branches' dependencies
git merge <branch>
# Fix pyproject.toml conflicts manually
uv lock  # Regenerate lock file
uv sync
```

## Verification Checklist

Before moving to Exercise 3, ensure you can:

- [ ] Add packages with `uv add`
- [ ] Add multiple packages at once
- [ ] Specify version constraints
- [ ] Understand `uv.lock` contents
- [ ] Remove packages with `uv remove`
- [ ] Sync environment with `uv sync`
- [ ] Update dependencies with `uv lock --upgrade`
- [ ] Use installed packages in Python scripts

## Next Steps

Now that you understand dependency management, move to [Exercise 3: Development Dependencies](./03-dev-setup.md) to learn how to separate development tools from runtime requirements.

## Questions for Reflection

1. Why is `uv.lock` more important than `pyproject.toml` for reproducibility?
2. What are transitive dependencies and why does uv manage them?
3. When should you use `==` vs `>=` in version constraints?
4. How does uv lock file prevent "works on my machine" problems?

## Additional Resources

- [Theory: Understanding uv.lock](../../../../docs/module-02/02-project-management-uv.md)
- [Semantic Versioning Explained](https://semver.org/)
- [Python Packaging Guide](https://packaging.python.org/)
