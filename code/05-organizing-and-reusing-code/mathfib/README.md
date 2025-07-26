# mathfib

A Python package providing Fibonacci sequence and mathematical filtering utilities.

## Installation

```bash
uv pip install mathfib
```

## Usage

### Fibonacci Sequence Generator

```python
from mathfib import fibonacci

# Get the first 10 Fibonacci numbers
fib_gen = fibonacci()
fib_numbers = [next(fib_gen) for _ in range(10)]
print(fib_numbers)  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### Filtering Multiples

```python
from mathfib import multiples_of

# Get all multiples of 3 from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiples_of_3 = list(multiples_of(numbers, 3))
print(multiples_of_3)  # [3, 6, 9]
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.