# Exercise 4: Python Version Management

**Work with multiple Python versions using uv**

## Objective

Learn to install, switch between, and manage multiple Python versions.

## Background

Different projects require different Python versions. `uv` handles Python installation and version switching automatically.

## Step 1: List Available Python Versions

```bash
uv python list
```

**Expected Output:**

```
cpython-3.8
cpython-3.9
cpython-3.10
cpython-3.11
cpython-3.12
cpython-3.13
```

## Step 2: Install Python Versions

```bash
uv python install 3.11
uv python install 3.12
```

**Expected Output:**

```
Downloading Python 3.11.8
Installed Python 3.11.8 to /path/to/python
```

## Step 3: Create Project with Specific Version

```bash
cd module-02/advanced-python/02-uv
uv init version-demo
cd version-demo
```

## Step 4: Set Python Version

Edit `.python-version`:

```bash
echo "3.12" > .python-version
```

##  Step 5: Verify Version

```bash
uv run python --version
```

**Expected Output:**

```
Python 3.12.2
```

## Step 6: Switch Versions

Change to Python 3.11:

```bash
echo "3.11" > .python-version
uv run python --version
```

**Expected Output:**

```
Python 3.11.8
```

## Step 7: Use Specific Version for Single Command

```bash
uv run --python 3.12 python --version
```

This runs with Python 3.12 regardless of `.python-version`.

## Step 8: Check Installed Pythons

```bash
uv python list --only-installed
```

Shows which Python versions uv has installed.

## Step 9: Test Version-Specific Features

Create `version_test.py`:

```python
import sys

print(f"Python version: {sys.version}")

# Python 3.10+ feature: match statement
def check_version():
    match sys.version_info.major, sys.version_info.minor:
        case 3, 11:
            print("Python 3.11")
        case 3, 12:
            print("Python 3.12")
        case _:
            print("Other Python version")

check_version()
```

Run with different versions:

```bash
uv run --python 3.11 python version_test.py
uv run --python 3.12 python version_test.py
```

## Key Learnings

✅ `uv python install <version>` installs Python versions
✅ `.python-version` sets project default
✅ `uv run --python <version>` overrides for single command
✅ No need for pyenv or manual Python installation
✅ Each project can use different Python versions

## Next Steps

Move to [Exercise 5: Scripts and Task Running](./05-scripts.md).
