# Python Typing - Hands-On Lab

**Practice type hints and static type checking with progressive exercises**

## Overview

This lab provides hands-on practice with Python type hints, from basic annotations to advanced generic types. You'll learn to write type-safe code that catches errors early and improves code maintainability.

## Prerequisites

- Python 3.10 or higher
- Basic Python knowledge (functions, classes, collections)
- Text editor or IDE with Python support

## Setup

### 1. Navigate to Lab Directory

```bash
cd module-02/advanced-python/01-typing
```

### 2. Install Type Checker (Optional but Recommended)

```bash
pip install mypy
# or
pip install pyright
```

### 3. Verify Installation

```bash
mypy --version
# or
pyright --version
```

## Lab Structure

```
01-typing/
├── README.md           # This file
├── examples/           # Reference examples
│   ├── basic_types.py
│   ├── advanced_types.py
│   └── type_checking.py
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
2. **Open the exercise file** in `exercises/`
3. **Complete the TODO sections** following the instructions
4. **Run the code** to verify it works
5. **Check with type checker**: `mypy exercises/exercise_N.py`
6. **Compare with solution** in `solution/` if needed
7. **Understand the concepts** before moving to the next exercise

## Exercises

### Exercise 1: Basic Type Annotations

**Objective:** Add type hints to function signatures and variables

**Background:**

Type hints make your code self-documenting and help catch type errors early. In this exercise, you'll add basic type annotations to existing functions.

**Instructions:**

1. Open `exercises/exercise_1.py`
2. Add type hints to all function parameters and return types
3. Add type annotations to variables where helpful
4. Run the code to ensure it still works
5. Check with mypy: `mypy exercises/exercise_1.py`
6. Fix any type errors mypy reports

**Expected Output:**

```
User: Alice (age 30)
Total price: $110.00
Greeting: Hello, Bob!
Average: 87.67
```

**Type Checker Output:**

```
Success: no issues found in 1 source file
```

**Key Learnings:**

- How to annotate function parameters with simple types (int, str, float, bool)
- How to specify return types including `None`
- How to annotate variables explicitly
- How type checkers verify your annotations

**Common Mistakes:**

- Forgetting return type annotation (always include `-> ReturnType`)
- Using `None` without `-> None` for functions that don't return anything
- Mixing up int and float types

### Exercise 2: Working with Collections

**Objective:** Type complex data structures (lists, dicts, sets, tuples)

**Background:**

Real applications work with collections of data. You need to specify not just that something is a list, but what type of elements it contains. This helps catch errors when you accidentally mix different types.

**Instructions:**

1. Open `exercises/exercise_2.py`
2. Add type hints for all collection parameters and returns
3. Pay attention to nested collections (list of dicts, dict of lists, etc.)
4. Run the code to verify behavior
5. Check with type checker: `mypy exercises/exercise_2.py`

**Expected Output:**

```
ALICE
BOB
CHARLIE
User alice has scores: [95, 87, 92]
User bob has scores: [88, 91]
Unique tags: python, typing, tutorial, advanced
```

**Type Checker Output:**

```
Success: no issues found in 1 source file
```

**Key Learnings:**

- How to type lists: `list[str]`, `list[int]`
- How to type dictionaries: `dict[str, int]`, `dict[str, list[int]]`
- How to type sets: `set[str]`
- How to type tuples: `tuple[str, int]` (fixed) vs `tuple[int, ...]` (variable)
- Nesting collection types for complex structures

**Common Mistakes:**

- Using `list` without specifying element type (should be `list[str]`)
- Using `dict` without specifying key and value types
- Confusing tuple types: `tuple[int, int]` (2 elements) vs `tuple[int, ...]` (any number)

### Exercise 3: Optional and Union Types

**Objective:** Handle nullable values and multiple possible types

**Background:**

Functions often return `None` in certain cases or accept multiple types of input. Type hints let you express these possibilities clearly. `Optional[T]` is shorthand for `T | None`, and Union types allow multiple possibilities.

**Instructions:**

1. Open `exercises/exercise_3.py`
2. Add type hints that allow `None` where appropriate
3. Add Union types for functions that accept multiple types
4. Handle all None cases properly in your logic
5. Run the code to verify behavior
6. Check with type checker: `mypy exercises/exercise_3.py`

**Expected Output:**

```
Found user: Alice
User not found
ID as string: 12345
ID as string: USER-789
Value: 10.5
Value: 0.0 (default)
```

**Type Checker Output:**

```
Success: no issues found in 1 source file
```

**Key Learnings:**

- How to use `Optional[T]` for values that might be None
- Modern syntax: `T | None` (Python 3.10+)
- How to use Union types: `int | str | float`
- Why None checking is important with Optional types
- Type narrowing with `if value is not None:`

**Common Mistakes:**

- Not checking for None before using Optional values
- Using `Optional[T]` when None isn't actually possible
- Forgetting that `Optional[int]` can't be used directly in arithmetic

### Exercise 4: Creating Type Aliases

**Objective:** Build reusable type definitions for complex types

**Background:**

Complex types like `dict[str, list[dict[str, int | str]]]` are hard to read and error-prone. Type aliases give names to complex types, making code more readable and maintainable. When you change the type definition, you only need to update it in one place.

**Instructions:**

1. Open `exercises/exercise_4.py`
2. Create type aliases for complex types
3. Use the aliases in function signatures
4. Create a NewType for distinct ID types
5. Run the code to verify behavior
6. Check with type checker: `mypy exercises/exercise_4.py`

**Expected Output:**

```
Processing user: Alice
Processing user: Bob
Order #1001 for user #5001
Order #1002 for user #5002
Matrix sum: 21
```

**Type Checker Output:**

```
Success: no issues found in 1 source file
```

**Key Learnings:**

- How to create type aliases: `TypeAlias = ComplexType`
- When to use type aliases (complex, repeated types)
- How `NewType` creates distinct types that prevent mixing
- Benefits of named types for code clarity
- How type aliases improve refactoring

**Common Mistakes:**

- Not using `TypeAlias` annotation for clarity
- Creating too many trivial aliases (over-engineering)
- Forgetting that NewType requires explicit construction

### Exercise 5: Generic Functions

**Objective:** Write type-safe generic utilities using TypeVar

**Background:**

Generic functions work with any type while maintaining type safety. When you pass a `list[int]` to a generic function, it returns values of type `int`, not just `Any`. This is powerful for building reusable utilities.

**Instructions:**

1. Open `exercises/exercise_5.py`
2. Add TypeVar declarations for generic parameters
3. Use TypeVar in function signatures
4. Create a generic class using `Generic[T]`
5. Run the code to verify behavior
6. Check with type checker: `mypy exercises/exercise_5.py`

**Expected Output:**

```
First number: 1
First name: Alice
Last score: 92
Last tag: python
Chunks: [[1, 2], [3, 4], [5, 6]]
Stack size: 2
Popped: world
Stack size: 1
```

**Type Checker Output:**

```
Success: no issues found in 1 source file
```

**Key Learnings:**

- How to declare TypeVar: `T = TypeVar('T')`
- How to use TypeVar in function signatures
- How Generic[T] works for classes
- Type inference with generic functions
- When generics are better than Any

**Common Mistakes:**

- Forgetting to import TypeVar from typing
- Using `T` without declaring it as TypeVar
- Mixing TypeVar types in the same function incorrectly

## Running Examples

Before starting exercises, review the example files to see type hints in action:

```bash
# View basic type examples
python examples/basic_types.py

# View advanced generic and protocol examples
python examples/advanced_types.py

# View type checking integration
python examples/type_checking.py
```

## Type Checking Your Solutions

### Using mypy

```bash
# Check a single file
mypy exercises/exercise_1.py

# Check all exercises
mypy exercises/

# Strict mode (recommended for learning)
mypy --strict exercises/exercise_1.py
```

### Using pyright

```bash
# Check a single file
pyright exercises/exercise_1.py

# Check all exercises
pyright exercises/
```

## What You Learned

After completing this lab, you should be able to:

- Add type hints to function parameters and return values
- Type collections (lists, dicts, sets, tuples)
- Handle optional and union types
- Create and use type aliases
- Write generic functions with TypeVar
- Use static type checkers to catch errors early
- Understand when and how to use type hints effectively

## Troubleshooting

### Type Checker Not Finding Issues

If mypy or pyright doesn't report expected errors, make sure you're using the correct Python version:

```bash
mypy --python-version 3.10 exercises/exercise_1.py
```

### Import Errors

If you see `ImportError` for typing module features, ensure you're using Python 3.10+:

```bash
python --version
```

### IDE Not Showing Type Hints

Configure your IDE to use a type checker:

- **VS Code**: Install Pylance extension
- **PyCharm**: Type checking is built-in
- **Vim/Neovim**: Use ALE or coc-pyright

## Next Steps

After mastering Python typing, continue to:

- [Project Management with uv](../02-uv/README.md)
- [Theory: Data Validation with Pydantic](../../../docs/module-02/03-data-validation-pydantic.md)

## Additional Practice

Want more practice? Try:

1. Add type hints to your existing Python projects
2. Run mypy in strict mode on your codebase
3. Refactor complex types into type aliases
4. Write generic utilities for common patterns
5. Create Protocol types for duck-typed interfaces

## Additional Resources

- [Theory: Python Typing](../../../docs/module-02/01-python-typing.md)
- [mypy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Python typing documentation](https://docs.python.org/3/library/typing.html)
- [Real Python: Type Checking](https://realpython.com/python-type-checking/)
