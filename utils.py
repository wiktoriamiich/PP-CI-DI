"""Module with basic arithmetic functions."""

def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Return the difference of a and b."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b

def divide(a: int, b: int) -> float:
    """Return the result of dividing a by b."""
    return a / b

def word_count(text: str) -> int:
    """Return the number of words in the given text."""
    return len(text.split())


