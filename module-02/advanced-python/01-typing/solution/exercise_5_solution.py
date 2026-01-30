"""Exercise 5 Solution: Generic Functions

This solution demonstrates TypeVar and Generic for writing type-safe
generic functions and classes.
"""

from typing import TypeVar, Generic


# Declare a generic type variable
T = TypeVar('T')


def get_first(items: list[T]) -> T:
    """Get the first element from a list.

    Args:
        items: A non-empty list of any type

    Returns:
        The first element (same type as list elements)
    """
    return items[0]


def get_last(items: list[T]) -> T:
    """Get the last element from a list.

    Args:
        items: A non-empty list of any type

    Returns:
        The last element (same type as list elements)
    """
    return items[-1]


def chunk_list(items: list[T], chunk_size: int) -> list[list[T]]:
    """Split a list into chunks of specified size.

    Args:
        items: List to chunk
        chunk_size: Size of each chunk

    Returns:
        List of chunks (list of lists)
    """
    chunks: list[list[T]] = []
    for i in range(0, len(items), chunk_size):
        chunks.append(items[i:i + chunk_size])
    return chunks


class Stack(Generic[T]):
    """A generic stack data structure.

    Type parameter T specifies the type of elements stored.
    """

    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """Push an item onto the stack.

        Args:
            item: Item to push (type T)
        """
        self._items.append(item)

    def pop(self) -> T:
        """Pop an item from the stack.

        Returns:
            The top item from the stack (type T)

        Raises:
            IndexError: If stack is empty
        """
        return self._items.pop()

    def peek(self) -> T | None:
        """Peek at the top item without removing it.

        Returns:
            Top item (type T) or None if empty
        """
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        """Check if stack is empty.

        Returns:
            True if empty
        """
        return len(self._items) == 0

    def size(self) -> int:
        """Get the number of items in stack.

        Returns:
            Number of items
        """
        return len(self._items)


def main() -> None:
    """Run exercise demonstrations."""
    print("=== Generic Functions ===")

    # Test with integers - type inference works!
    numbers: list[int] = [1, 2, 3, 4, 5]
    first_num: int = get_first(numbers)  # Type checker infers return type is int
    print(f"First number: {first_num}")
    print(f"Last number: {get_last(numbers)}")

    # Test with strings - same function, different type
    names: list[str] = ["Alice", "Bob", "Charlie"]
    first_name: str = get_first(names)  # Type checker infers return type is str
    print(f"First name: {first_name}")
    print(f"Last name: {get_last(names)}")

    # Test with scores
    scores: list[int] = [95, 88, 92, 87]
    print(f"Last score: {get_last(scores)}")

    # Test with tags
    tags: list[str] = ["python", "typing", "generics"]
    print(f"Last tag: {get_last(tags)}")

    # Test chunking
    items: list[int] = [1, 2, 3, 4, 5, 6]
    chunks: list[list[int]] = chunk_list(items, 2)
    print(f"Chunks: {chunks}")

    print("\n=== Generic Stack ===")

    # Create a string stack - type parameter specified
    str_stack: Stack[str] = Stack()
    str_stack.push("hello")
    str_stack.push("world")
    # str_stack.push(123)  # Type checker error: Expected str, got int
    print(f"Stack size: {str_stack.size()}")
    popped: str = str_stack.pop()  # Type checker knows this is str
    print(f"Popped: {popped}")
    print(f"Stack size: {str_stack.size()}")

    # Create an integer stack - different type parameter
    int_stack: Stack[int] = Stack()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    # int_stack.push("hello")  # Type checker error: Expected int, got str
    print(f"Int stack size: {int_stack.size()}")
    top: int | None = int_stack.peek()  # Type checker knows this is int | None
    print(f"Peek: {top}")


if __name__ == "__main__":
    main()
