# Decorators - Hands-On Lab

**Master Python decorators through progressive exercises**

## Overview

Practice creating decorators from simple function wrappers to advanced patterns like caching, retry logic, and authentication.

## Prerequisites

- Python 3.10+
- Understanding of functions and closures
- Basic knowledge of `*args` and `**kwargs`

## Setup

```bash
cd module-02/advanced-python/04-decorators
```

## Lab Structure

```
04-decorators/
├── README.md
├── examples/
│   ├── basic_decorator.py
│   ├── decorator_arguments.py
│   ├── class_decorators.py
│   └── practical_decorators.py
├── exercises/
│   ├── exercise_1.py  # Simple timing decorator
│   ├── exercise_2.py  # Retry decorator with arguments
│   ├── exercise_3.py  # Class decorator (singleton)
│   ├── exercise_4.py  # Stacking decorators
│   └── exercise_5.py  # Caching decorator with TTL
└── solution/
    └── exercise_[1-5]_solution.py
```

## Exercises

### Exercise 1: Simple Function Decorator
Create a timing decorator that measures execution time.

### Exercise 2: Decorator with Arguments
Build a retry decorator with configurable attempts.

### Exercise 3: Class Decorator
Create a singleton pattern decorator.

### Exercise 4: Stacking Decorators
Combine auth + logging decorators.

### Exercise 5: Practical Application
Build a caching decorator with TTL.

## What You'll Learn

- Function decorator basics
- Using `@wraps` correctly
- Decorators with arguments
- Class decorators
- Stacking multiple decorators
- Real-world decorator patterns

## Next Steps

Continue to [Async/Await](../05-async-await/README.md).
