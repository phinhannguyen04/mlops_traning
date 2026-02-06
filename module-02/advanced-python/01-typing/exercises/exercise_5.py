"""Exercise 5: Generic Functions

Write type-safe generic utilities using TypeVar.

OBJECTIVE:
- Declare and use TypeVar for generic parameters
- Write generic functions that work with any type
- Create a generic class using Generic[T]

INSTRUCTIONS:
1. Define TypeVar for generic type parameters
2. Use TypeVar in function signatures
3. Create a generic Stack class
4. Run the code to verify behavior
5. Check with mypy: mypy exercises/exercise_5.py
"""

from typing import TypeVar, Generic


# TODO: Declare a TypeVar named 'T'
# T = TypeVar('T')
T = TypeVar('T')


# TODO: Add type hints using TypeVar T for generic first element function
def get_first(items: list[T]) -> T:
    """Get the first element from a list.

    Args:
        items: A non-empty list of any type

    Returns:
        The first element (same type as list elements)
    """
    return items[0]


# TODO: Add type hints using TypeVar T for generic last element function
def get_last(items: list[T]) -> T:
    """Get the last element from a list.

    Args:
        items: A non-empty list of any type

    Returns:
        The last element (same type as list elements)
    """
    return items[-1]


# TODO: Add type hints using TypeVar T for generic chunk function
def chunk_list(items: list[T], chunk_size: int) -> list[list[T]]:
    """Split a list into chunks of specified size.

    Args:
        items: List to chunk
        chunk_size: Size of each chunk

    Returns:
        List of chunks (list of lists)
    """
    chunks = []
    for i in range(0, len(items), chunk_size):
        chunks.append(items[i:i + chunk_size])
    return chunks


# TODO: Create a generic Stack class using Generic[T]
# The class should:
# - Store items of type T
# - Have push(item: T) -> None
# - Have pop() -> T
# - Have peek() -> T | None
# - Have is_empty() -> bool
# - Have size() -> int

class Stack(Generic[T]):
    """A generic stack data structure.

    TODO: Make this class generic using Generic[T]
    """

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item: T) -> None:
        """Push an item onto the stack.

        TODO: Add type hints (item should be type T)

        Args:
            item: Item to push
        """
        self._items.append(item)

    def pop(self) -> T:
        """Pop an item from the stack.

        TODO: Add type hints (returns type T)

        Returns:
            The top item from the stack

        Raises:
            IndexError: If stack is empty
        """
        return self._items.pop()

    def peek(self) -> T | None:
        """Peek at the top item without removing it.

        TODO: Add type hints (returns T | None)

        Returns:
            Top item or None if empty
        """
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        """Check if stack is empty.

        TODO: Add type hints

        Returns:
            True if empty
        """
        return len(self._items) == 0

    def size(self) -> int:
        """Get the number of items in stack.

        TODO: Add type hints

        Returns:
            Number of items
        """
        return len(self._items)


def main():
    """Run exercise demonstrations."""
    print("=== Generic Functions ===")

    # Test with integers
    numbers = [1, 2, 3, 4, 5]
    print(f"First number: {get_first(numbers)}")
    print(f"Last number: {get_last(numbers)}")

    # Test with strings
    names = ["Alice", "Bob", "Charlie"]
    print(f"First name: {get_first(names)}")
    print(f"Last name: {get_last(names)}")

    # Test with scores
    scores = [95, 88, 92, 87]
    print(f"Last score: {get_last(scores)}")

    # Test with tags
    tags = ["python", "typing", "generics"]
    print(f"Last tag: {get_last(tags)}")

    # Test chunking
    items = [1, 2, 3, 4, 5, 6]
    chunks = chunk_list(items, 2)
    print(f"Chunks: {chunks}")

    print("\n=== Generic Stack ===")

    # Create a string stack
    str_stack = Stack()  # TODO: After making generic, use Stack[str]()
    str_stack.push("hello")
    str_stack.push("world")
    print(f"Stack size: {str_stack.size()}")
    print(f"Popped: {str_stack.pop()}")
    print(f"Stack size: {str_stack.size()}")

    # Create an integer stack
    int_stack = Stack()  # TODO: After making generic, use Stack[int]()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    print(f"Int stack size: {int_stack.size()}")
    print(f"Peek: {int_stack.peek()}")


if __name__ == "__main__":
    main()
