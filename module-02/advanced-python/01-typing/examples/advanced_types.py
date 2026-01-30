"""Advanced Type Annotations Examples

This module demonstrates generic types, protocols, and advanced typing patterns.
"""

from typing import TypeVar, Generic, Protocol


# Generic Types with TypeVar
T = TypeVar('T')


def get_first_element(items: list[T]) -> T:
    """Get the first element from a list.

    This is a generic function that works with any type.

    Args:
        items: A non-empty list of any type

    Returns:
        The first element (same type as input list elements)
    """
    return items[0]


def get_last_element(items: list[T]) -> T:
    """Get the last element from a list.

    Args:
        items: A non-empty list of any type

    Returns:
        The last element (same type as input list elements)
    """
    return items[-1]


# Generic Class
class Stack(Generic[T]):
    """A generic stack data structure.

    Can store elements of any single type.
    """

    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """Push an item onto the stack.

        Args:
            item: The item to add
        """
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top item from the stack.

        Returns:
            The top item from the stack

        Raises:
            IndexError: If the stack is empty
        """
        return self._items.pop()

    def peek(self) -> T | None:
        """View the top item without removing it.

        Returns:
            The top item, or None if stack is empty
        """
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            True if empty, False otherwise
        """
        return len(self._items) == 0

    def size(self) -> int:
        """Get the number of items in the stack.

        Returns:
            Number of items
        """
        return len(self._items)


# Protocol for Structural Subtyping
class Drawable(Protocol):
    """Protocol for objects that can be drawn."""

    def draw(self) -> str:
        """Draw the object and return a string representation."""
        ...


class Circle:
    """A circle shape."""

    def __init__(self, radius: float) -> None:
        """Initialize a circle.

        Args:
            radius: The circle's radius
        """
        self.radius = radius

    def draw(self) -> str:
        """Draw the circle.

        Returns:
            String representation of the circle
        """
        return f"Circle(radius={self.radius})"


class Square:
    """A square shape."""

    def __init__(self, side: float) -> None:
        """Initialize a square.

        Args:
            side: The length of the square's side
        """
        self.side = side

    def draw(self) -> str:
        """Draw the square.

        Returns:
            String representation of the square
        """
        return f"Square(side={self.side})"


def render_shape(shape: Drawable) -> None:
    """Render any drawable shape.

    This function accepts any object that has a draw() method,
    without requiring inheritance from a base class.

    Args:
        shape: Any object implementing the Drawable protocol
    """
    print(shape.draw())


# Constrained TypeVar
NumberType = TypeVar('NumberType', int, float)


def add_numbers(a: NumberType, b: NumberType) -> NumberType:
    """Add two numbers of the same type.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Sum of the two numbers (same type as inputs)
    """
    return a + b  # type: ignore


def main() -> None:
    """Demonstrate advanced type annotations."""
    print("=== Generic Functions ===")
    numbers: list[int] = [1, 2, 3, 4, 5]
    print(f"First number: {get_first_element(numbers)}")
    print(f"Last number: {get_last_element(numbers)}")

    names: list[str] = ["Alice", "Bob", "Charlie"]
    print(f"First name: {get_first_element(names)}")
    print(f"Last name: {get_last_element(names)}")

    print("\n=== Generic Stack ===")
    # Create a stack of strings
    str_stack: Stack[str] = Stack()
    str_stack.push("hello")
    str_stack.push("world")
    print(f"Stack size: {str_stack.size()}")
    print(f"Popped: {str_stack.pop()}")
    print(f"Peek: {str_stack.peek()}")

    # Create a stack of integers
    int_stack: Stack[int] = Stack()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    print(f"Int stack size: {int_stack.size()}")

    print("\n=== Protocols ===")
    circle = Circle(5.0)
    square = Square(10.0)

    # Both work because they implement the Drawable protocol
    render_shape(circle)
    render_shape(square)

    print("\n=== Constrained TypeVar ===")
    int_sum = add_numbers(5, 10)
    print(f"Int sum: {int_sum}")

    float_sum = add_numbers(3.14, 2.86)
    print(f"Float sum: {float_sum:.2f}")


if __name__ == "__main__":
    main()
