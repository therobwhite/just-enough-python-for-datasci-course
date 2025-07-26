def fibonacci(n: int) -> list[int]:
    numbers = []

    current, nxt = 0, 1
    for _ in range(n):
        current, nxt = nxt, nxt + current
        numbers.append(current)

    return numbers


print(fibonacci(5))


def fibonacci_gen():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, nxt + current
        yield current


def even_numbers(some_numbers):
    for n in some_numbers:
        if n % 2 == 0:
            yield n


even_fibs = even_numbers(fibonacci_gen())
for z in even_fibs:
    print(z)
    if z > 1500:
        break

print('Thirds')
thirds_fibs = (f for f in fibonacci_gen() if f % 3 == 0)
for z in even_fibs:
    print(z)
    if z > 15000:
        break

print('Done!')
