"""Exercise 1 Solution: Timing Decorator"""
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
def slow_task():
    time.sleep(0.5)
    return "done"

if __name__ == "__main__":
    result = slow_task()
