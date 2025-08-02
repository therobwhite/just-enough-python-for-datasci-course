from collections.abc import Generator, Iterable


def fibonacci() -> Generator[int, None, None]:
    """Generate an infinite sequence of Fibonacci numbers.

    Yields:
        int: The next Fibonacci number in the sequence (1, 1, 2, 3, 5, 8, ...)

    Example:
        >>> fib = fibonacci()
        >>> [next(fib) for _ in range(5)]
        [1, 1, 2, 3, 5]
    """
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, nxt + current
        yield current


def multiples_of(collection: Iterable[int], number: int) -> Generator[int, None, None]:
    """Filter a collection to yield only multiples of a given number.

    Args:
        collection: An iterable of integers to filter
        number: The number to find multiples of (must be positive)

    Yields:
        int: Numbers from the collection that are multiples of the given number

    Raises:
        ValueError: If number is not positive

    Example:
        >>> list(multiples_of([1, 2, 3, 4, 5, 6], 2))
        [2, 4, 6]
    """
    if number <= 0:
        raise ValueError('Number must be positive')

    for n in collection:
        if n % number == 0:
            yield n
