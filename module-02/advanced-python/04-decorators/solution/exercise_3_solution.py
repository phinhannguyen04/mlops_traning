"""Exercise 3 Solution: Singleton Decorator"""
from functools import wraps

def singleton(cls):
    instances = {}
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Config:
    def __init__(self):
        self.settings = {}

if __name__ == "__main__":
    c1 = Config()
    c2 = Config()
    print(c1 is c2)  # True
