import typing


def fibonacci() -> typing.Generator[int, None, None]:
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, nxt + current
        yield current


def multiples_of(collection: typing.Iterable[int], number: int) -> typing.Generator[int, None, None]:
    for n in collection:
        if n % number == 0:
            yield n
