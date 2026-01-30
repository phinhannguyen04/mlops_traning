"""Exercise 2 Solution: Retry Decorator"""
from functools import wraps
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt+1} failed, retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_call():
    import random
    if random.random() < 0.7:
        raise Exception("Failed")
    return "Success"

if __name__ == "__main__":
    try:
        result = unstable_call()
        print(result)
    except:
        print("All attempts failed")
