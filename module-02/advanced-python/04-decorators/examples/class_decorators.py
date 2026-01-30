"""Class Decorators"""
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
class Database:
    def __init__(self):
        print("Database initialized")

if __name__ == "__main__":
    db1 = Database()
    db2 = Database()
    print(db1 is db2)  # True
