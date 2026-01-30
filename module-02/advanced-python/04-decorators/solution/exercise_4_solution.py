"""Exercise 4 Solution: Stacking Decorators"""
from functools import wraps

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs.get('authenticated'):
            raise PermissionError("Not authenticated")
        return func(*args, **kwargs)
    return wrapper

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log
@require_auth
def protected_resource(authenticated=False):
    return "Secret data"

if __name__ == "__main__":
    result = protected_resource(authenticated=True)
