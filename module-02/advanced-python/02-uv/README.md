# Project Management with uv - Hands-On Lab

**Master modern Python project management through practical CLI exercises**

## Overview

This lab provides hands-on practice with `uv`, the fast Python package and project manager. You'll learn to create projects, manage dependencies, handle virtual environments, work with multiple Python versions, and define project scripts.

## Prerequisites

- Basic command-line knowledge
- Understanding of Python packages and dependencies
- Terminal or command prompt access

## Setup

### 1. Install uv

**Windows (PowerShell):**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Verify installation:**

```bash
uv --version
```

### 2. Navigate to Lab Directory

```bash
cd module-02/advanced-python/02-uv
```

## Lab Structure

```
02-uv/
├── README.md              # This file
└── exercises/             # Exercise guides
    ├── 01-init-project.md
    ├── 02-manage-deps.md
    ├── 03-dev-setup.md
    ├── 04-python-versions.md
    └── 05-scripts.md
```

## How to Work Through Exercises

1. **Read the exercise description** below
2. **Open the detailed guide** in `exercises/`
3. **Follow step-by-step commands** in your terminal
4. **Verify the expected output** matches what you see
5. **Understand what each command does** before moving on
6. **Complete all exploration tasks** to deepen understanding

## Exercises

### Exercise 1: Project Initialization

**Objective:** Learn to create new Python projects with uv

**What You'll Learn:**
- Creating projects with `uv init`
- Understanding project structure
- Reading `pyproject.toml` configuration
- Understanding `.python-version` files

**Instructions:**

Open `exercises/01-init-project.md` and follow the step-by-step guide.

**Key Commands:**

```bash
uv init my-first-project
cd my-first-project
cat pyproject.toml
uv run python hello.py
```

**Expected Outcomes:**
- New project directory created
- `pyproject.toml` and `.python-version` files present
- Sample Python file runs successfully
- Understanding of project structure

**Time Investment:** Practice the concepts thoroughly

### Exercise 2: Dependency Management

**Objective:** Master adding, removing, and updating packages

**What You'll Learn:**
- Adding runtime dependencies with `uv add`
- Understanding `uv.lock` file
- Removing packages with `uv remove`
- Installing dependencies with `uv sync`
- Updating packages with `uv lock --upgrade`

**Instructions:**

Open `exercises/02-manage-deps.md` and follow the step-by-step guide.

**Key Commands:**

```bash
uv add requests pandas
cat pyproject.toml
cat uv.lock
uv remove pandas
uv sync
uv lock --upgrade
```

**Expected Outcomes:**
- Dependencies added to `pyproject.toml`
- Lock file created with exact versions
- Understanding of reproducible dependency resolution
- Ability to manage package versions

**Time Investment:** Practice the concepts thoroughly

### Exercise 3: Development Dependencies

**Objective:** Set up development tools separately from runtime dependencies

**What You'll Learn:**
- Adding dev dependencies with `--dev` flag
- Organizing dependencies by purpose
- Installing dev vs production dependencies
- Working with testing and linting tools

**Instructions:**

Open `exercises/03-dev-setup.md` and follow the step-by-step guide.

**Key Commands:**

```bash
uv add --dev pytest black mypy ruff
uv sync --dev
uv run pytest
uv run black --check .
```

**Expected Outcomes:**
- Dev dependencies in `[project.optional-dependencies.dev]`
- Testing framework set up and working
- Linting and formatting tools configured
- Understanding of dependency separation

**Time Investment:** Practice the concepts thoroughly

### Exercise 4: Python Version Management

**Objective:** Work with multiple Python versions

**What You'll Learn:**
- Installing Python versions with uv
- Switching between Python versions
- Using `.python-version` file
- Running commands with specific Python versions

**Instructions:**

Open `exercises/04-python-versions.md` and follow the step-by-step guide.

**Key Commands:**

```bash
uv python list
uv python install 3.11
uv python install 3.12
echo "3.12" > .python-version
uv run python --version
```

**Expected Outcomes:**
- Multiple Python versions installed
- Ability to switch between versions
- Understanding of version specification
- Project-specific Python version configuration

**Time Investment:** Practice the concepts thoroughly

### Exercise 5: Scripts and Task Running

**Objective:** Define and run project scripts efficiently

**What You'll Learn:**
- Defining scripts in `pyproject.toml`
- Running scripts with `uv run`
- Creating command-line entry points
- Organizing development tasks

**Instructions:**

Open `exercises/05-scripts.md` and follow the step-by-step guide.

**Key Commands:**

```bash
# Edit pyproject.toml to add scripts
uv run my-script
uv run -m pytest
uv run python -m my_module
```

**Expected Outcomes:**
- Custom scripts defined in configuration
- Understanding of entry points
- Efficient task execution workflow
- Reusable development commands

**Time Investment:** Practice the concepts thoroughly

## Common Commands Reference

### Project Management

```bash
uv init <project-name>      # Create new project
uv sync                     # Install all dependencies
uv sync --dev               # Install including dev dependencies
uv run <command>            # Run command in project environment
```

### Package Management

```bash
uv add <package>            # Add runtime dependency
uv add --dev <package>      # Add dev dependency
uv remove <package>         # Remove dependency
uv lock                     # Update lock file
uv lock --upgrade           # Upgrade all packages
uv pip list                 # List installed packages
```

### Python Version Management

```bash
uv python list              # List available Python versions
uv python install <version> # Install Python version
uv run --python 3.11 <cmd>  # Run with specific Python version
```

### Virtual Environments

```bash
uv venv                     # Create virtual environment
uv venv --python 3.11       # Create with specific Python
```

## What You Learned

After completing this lab, you should be able to:

- Create new Python projects with proper structure
- Manage dependencies efficiently with lock files
- Separate development and runtime dependencies
- Work with multiple Python versions
- Define and run project scripts
- Understand `pyproject.toml` configuration
- Use `uv.lock` for reproducible builds
- Integrate uv into development workflows

## Troubleshooting

### uv Command Not Found

**Issue:** `uv: command not found` after installation

**Solution:**

```bash
# macOS/Linux - Add to PATH
export PATH="$HOME/.cargo/bin:$PATH"

# Windows PowerShell - Add to PATH
$env:PATH += ";$HOME\.cargo\bin"

# Restart terminal and verify
uv --version
```

### Lock File Out of Sync

**Issue:** `uv.lock is out of sync with pyproject.toml`

**Solution:**

```bash
uv lock
uv sync
```

### Permission Denied

**Issue:** Permission errors when installing

**Solution (macOS/Linux):**

```bash
# Don't use sudo with uv
# It installs to user directory by default
```

**Solution (Windows):**

Run PowerShell as Administrator for initial install only.

### Python Version Not Found

**Issue:** `Python 3.x not found`

**Solution:**

```bash
uv python install 3.11
uv python install 3.12
```

## Real-World Scenarios

### Scenario 1: Starting a New ML Project

```bash
# Create project
uv init ml-classifier
cd ml-classifier

# Add ML dependencies
uv add numpy pandas scikit-learn matplotlib

# Add dev tools
uv add --dev jupyter pytest

# Run Jupyter
uv run jupyter notebook
```

### Scenario 2: Cloning and Running a Project

```bash
# Clone repository
git clone https://github.com/team/project
cd project

# Install all dependencies (including dev)
uv sync --dev

# Run tests
uv run pytest

# Start application
uv run python -m app.main
```

### Scenario 3: Updating Dependencies

```bash
# Check for outdated packages
uv pip list --outdated

# Update all to latest compatible versions
uv lock --upgrade

# Install updated versions
uv sync

# Run tests to verify compatibility
uv run pytest
```

## Best Practices from This Lab

### 1. Always Commit Lock Files

```bash
git add pyproject.toml uv.lock
git commit -m "Update dependencies"
```

The lock file ensures everyone on your team uses identical dependency versions.

### 2. Separate Dev Dependencies

Keep development tools separate from runtime requirements:

```toml
[project]
dependencies = ["requests", "pandas"]  # Production

[project.optional-dependencies]
dev = ["pytest", "black", "mypy"]      # Development only
```

### 3. Specify Python Version

Always include `.python-version` file in your project:

```bash
echo "3.11" > .python-version
git add .python-version
```

### 4. Use Scripts for Common Tasks

Define frequently used commands:

```toml
[project.scripts]
test = "pytest:main"
lint = "ruff:main"
serve = "uvicorn app.main:app"
```

### 5. Keep Dependencies Updated

Regularly update dependencies:

```bash
# Weekly or bi-weekly
uv lock --upgrade
uv sync
uv run pytest
```

## Next Steps

After mastering uv, continue to:

- [Theory: Data Validation with Pydantic](../../../docs/module-02/03-data-validation-pydantic.md)
- [Hands-On: Pydantic Lab](../03-pydantic/README.md)

## Additional Practice Ideas

1. **Migrate an Existing Project**
   - Take an old pip-based project
   - Convert to uv
   - Create `pyproject.toml` and lock file

2. **Create a CLI Tool**
   - Use `uv init` to start
   - Add `[project.scripts]` entry points
   - Package and distribute

3. **Set Up CI/CD**
   - Create GitHub Actions workflow using uv
   - Run tests and linting
   - Build and publish package

4. **Monorepo Workspace**
   - Create multiple related packages
   - Set up uv workspace
   - Share dependencies across packages

## Additional Resources

- [Theory: Project Management with uv](../../../docs/module-02/02-project-management-uv.md)
- [Official uv documentation](https://github.com/astral-sh/uv)
- [PEP 621 - pyproject.toml specification](https://peps.python.org/pep-0621/)
- [Python Packaging Guide](https://packaging.python.org/)
