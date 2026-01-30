# Exercise 1: Project Initialization

**Learn to create and understand Python project structure with uv**

## Objective

By the end of this exercise, you'll understand how to:
- Create new Python projects with `uv init`
- Understand project file structure
- Read and interpret `pyproject.toml`
- Work with `.python-version` files
- Run Python code in a uv project

## Background

Traditional Python projects require manual setup: creating directories, writing `setup.py`, managing virtual environments. `uv init` automates this, creating a modern project structure following Python packaging standards (PEP 517/621).

## Step 1: Create Your First Project

Run the following command to create a new project:

```bash
uv init my-first-project
```

**Expected Output:**

```
Initialized project `my-first-project` at `/path/to/my-first-project`
```

## Step 2: Explore the Project Structure

Navigate into the project and list its contents:

```bash
cd my-first-project
ls -la
```

**Expected Output (Windows: dir, macOS/Linux: ls):**

```
.python-version
README.md
hello.py
pyproject.toml
```

### What Each File Does

**`.python-version`** - Specifies the Python version for this project:

```bash
cat .python-version
```

Output:

```
3.11
```

This tells uv which Python version to use. If this version isn't installed, uv will install it automatically.

**`pyproject.toml`** - Project configuration and metadata:

```bash
cat pyproject.toml
```

Output:

```toml
[project]
name = "my-first-project"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

**`hello.py`** - Sample Python file:

```bash
cat hello.py
```

Output:

```python
def main():
    print("Hello from my-first-project!")


if __name__ == "__main__":
    main()
```

## Step 3: Run the Sample Code

Execute the sample Python file using `uv run`:

```bash
uv run python hello.py
```

**Expected Output:**

```
Hello from my-first-project!
```

### What Happened?

When you ran `uv run python hello.py`, uv:
1. Checked if a virtual environment exists (`.venv`)
2. Created one if needed
3. Installed the required Python version (if necessary)
4. Activated the environment
5. Ran your Python code

All automatically!

## Step 4: Inspect the Virtual Environment

After running, check for the virtual environment:

```bash
ls -la
```

**New Directory:**

```
.venv/     # Virtual environment (created automatically)
```

Look inside:

```bash
# Windows
dir .venv\Scripts

# macOS/Linux
ls .venv/bin
```

You'll see Python executables and tools installed in this isolated environment.

## Step 5: Understand pyproject.toml Sections

Let's break down each section of `pyproject.toml`:

### [project] Section

```toml
[project]
name = "my-first-project"           # Package name (for distribution)
version = "0.1.0"                   # Semantic version
description = "Add your description here"  # Short description
readme = "README.md"                # Path to README file
requires-python = ">=3.11"          # Minimum Python version
dependencies = []                   # Runtime dependencies (empty for now)
```

### [build-system] Section

```toml
[build-system]
requires = ["hatchling"]            # Build tool
build-backend = "hatchling.build"   # Build backend
```

This tells Python how to build your package for distribution.

## Step 6: Modify Project Metadata

Let's personalize the project. Edit `pyproject.toml`:

```bash
# Use your favorite editor
# Windows: notepad pyproject.toml
# macOS/Linux: nano pyproject.toml or vi pyproject.toml
```

Update these fields:

```toml
[project]
name = "my-first-project"
version = "0.1.0"
description = "My first uv project for MLOps training"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []
authors = [
    {name = "Your Name", email = "you@example.com"}
]
```

Save the file.

## Step 7: Create a New Python Module

Let's add more functionality. Create a new file called `greet.py`:

```bash
# Windows
echo def greet(name): print(f"Hello, {name}!") > greet.py

# macOS/Linux
cat > greet.py << 'EOF'
def greet(name: str) -> None:
    """Greet someone by name."""
    print(f"Hello, {name}!")

def main() -> None:
    """Main entry point."""
    greet("MLOps Engineer")

if __name__ == "__main__":
    main()
EOF
```

Run it:

```bash
uv run python greet.py
```

**Expected Output:**

```
Hello, MLOps Engineer!
```

## Step 8: Understanding uv run

The `uv run` command is powerful. Try these variations:

**Run Python directly:**

```bash
uv run python -c "print('Hello from Python!')"
```

**Run with imports (even before installing packages):**

```bash
uv run python -c "import sys; print(sys.version)"
```

**Run Python module:**

```bash
uv run python -m http.server 8000
```

Press `Ctrl+C` to stop the server.

## Step 9: Exploration Tasks

Complete these tasks to reinforce learning:

### Task A: Create Another Project

```bash
cd ..
uv init calculator-project
cd calculator-project
```

What files were created? Are they the same as your first project?

### Task B: Change Python Version

Edit `.python-version`:

```bash
echo "3.12" > .python-version
```

Run your code:

```bash
uv run python hello.py
```

What happens? (uv may install Python 3.12 if not present)

### Task C: Check Python Version

Verify which Python version is being used:

```bash
uv run python --version
```

Does it match `.python-version`?

## Key Learnings

After completing this exercise, you should understand:

✅ **`uv init`** creates a standard project structure
✅ **`pyproject.toml`** is the central configuration file
✅ **`.python-version`** specifies the Python version
✅ **`uv run`** automatically handles virtual environments
✅ **Virtual environments** are created automatically in `.venv`
✅ **No manual activation** needed with `uv run`

## Common Mistakes

### Mistake 1: Manual Virtual Environment Activation

❌ **Don't do this:**

```bash
source .venv/bin/activate  # Manual activation
python hello.py
```

✅ **Do this instead:**

```bash
uv run python hello.py  # uv handles activation
```

### Mistake 2: Using pip Instead of uv

❌ **Don't do this:**

```bash
pip install requests  # Wrong tool
```

✅ **Do this instead:**

```bash
uv add requests  # Proper uv command (covered in Exercise 2)
```

### Mistake 3: Editing .python-version Manually with Wrong Format

❌ **Don't do this:**

```
python-3.11.5  # Too specific
```

✅ **Do this instead:**

```
3.11  # Major.minor is sufficient
```

## Verification Checklist

Before moving to Exercise 2, ensure you can:

- [ ] Create a new project with `uv init`
- [ ] Identify and explain each file in the project
- [ ] Read and understand `pyproject.toml`
- [ ] Run Python code with `uv run`
- [ ] See the `.venv` directory created automatically
- [ ] Modify project metadata in `pyproject.toml`
- [ ] Change Python version in `.python-version`

## Next Steps

Now that you understand project initialization, move to [Exercise 2: Dependency Management](./02-manage-deps.md) to learn how to add and manage packages.

## Questions for Reflection

1. Why is `uv run` better than manually activating virtual environments?
2. What's the purpose of the lock file (you'll learn more in Exercise 2)?
3. When would you change the `requires-python` field?
4. How does uv know which Python version to install?

## Additional Resources

- [Theory: Project Management with uv](../../../../docs/module-02/02-project-management-uv.md)
- [PEP 621 - pyproject.toml standard](https://peps.python.org/pep-0621/)
