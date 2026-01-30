"""Exercise 5 Solution: Cache with TTL"""
from functools import wraps
import time

def cache_with_ttl(ttl=60):
    def decorator(func):
        cache = {}
        @wraps(func)
        def wrapper(*args):
            now = time.time()
            if args in cache:
                result, timestamp = cache[args]
                if now - timestamp < ttl:
                    return result
            result = func(*args)
            cache[args] = (result, now)
            return result
        return wrapper
    return decorator

@cache_with_ttl(ttl=5)
def expensive_operation(n):
    time.sleep(1)
    return n ** 2

if __name__ == "__main__":
    print(expensive_operation(10))  # Slow
    print(expensive_operation(10))  # Fast (cached)
    time.sleep(6)
    print(expensive_operation(10))  # Slow (cache expired)
