"""Practical Decorators: Cache, Retry, Rate Limit"""
from functools import wraps, lru_cache
import time

def cache(func):
    cached = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cached:
            cached[args] = func(*args)
        return cached[args]
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@lru_cache(maxsize=128)
def fibonacci_fast(n):
    if n < 2:
        return n
    return fibonacci_fast(n-1) + fibonacci_fast(n-2)

if __name__ == "__main__":
    print(fibonacci(35))
    print(fibonacci_fast(100))
