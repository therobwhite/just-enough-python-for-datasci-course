def three_fib(n: int) -> list[int]:
    if n == 0:
        fib_three = [0]
    elif n == 1:
        fib_three = [0, 1]
    elif n == 2:
        fib_three = [0, 1, 1]
    else:
        fib_three = [0, 1, 1]
        for i in range(3, n):
            fib_three.append(fib_three[i - 1] + fib_three[i - 2] + fib_three[i - 3])
    return fib_three


def fibonacci(n: int) -> list[int]:
    if n == 0:
        fib_sequence = [0]
    elif n == 1:
        fib_sequence = [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence
    

print(fibonacci(5))
print(three_fib(5))
