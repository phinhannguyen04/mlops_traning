"""Basic Decorator Examples"""
from functools import wraps
import time

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper

@timing
def slow_function():
    time.sleep(0.1)
    return "done"

if __name__ == "__main__":
    slow_function()
