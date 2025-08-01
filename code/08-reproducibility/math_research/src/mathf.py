import typing


def fibonacci(limit: int) -> list[int]:
    """
    Generate a list containing the first n Fibonacci numbers.
    
    The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13, ...
    
    Args:
        limit: The number of Fibonacci numbers to generate
        
    Returns:
        A list of the first 'limit' Fibonacci numbers
        
    Example:
        >>> fibonacci(7)
        [0, 1, 1, 2, 3, 5, 8]
    """
    numbers = []
    current, nxt = 0, 1
    for _ in range(limit):
        numbers.append(current)
        current, nxt = nxt, nxt + current

    return numbers


def fibonacci_gen() -> typing.Generator[int, None, None]:
    """
    Generate an infinite sequence of Fibonacci numbers.
    
    The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13, ...
    
    This is a generator function that yields one Fibonacci number at a time,
    allowing for efficient iteration without storing the entire sequence in memory.
    
    Yields:
        Each successive Fibonacci number in the sequence
        
    Example:
        >>> fib = fibonacci_gen()
        >>> [next(fib) for _ in range(7)]
        [0, 1, 1, 2, 3, 5, 8]
    """
    current, nxt = 0, 1
    while True:
        yield current
        current, nxt = nxt, nxt + current


def multiples_of(numbers: typing.Iterable[int], base_num: int) -> typing.Iterable[int]:
    for num in numbers:
        if num % base_num == 0:
            yield num
