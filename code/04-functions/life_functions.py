import os
import random
import time
import typing

# TODO: Note, this is only partially final, still needs functions, next chapter.

# ANSI color codes
ALIVE_CHAR: typing.Final[str] = '\033[92mO\033[0m'  # green O
DEAD_CHAR: typing.Final[str] = ' '  # blank for dead
HEADER_COL: typing.Final[str] = '\033[96m'  # cyan
RESET_COL: typing.Final[str] = '\033[0m'

SURVIVING_COUNTS: typing.Final[set[int]] = {2, 3}
IS_ALIVE: typing.Final[int] = 1
REVIVED_COUNT: typing.Final[int] = 3

# Game params
rows: typing.Final[int] = 20
cols: typing.Final[int] = 50
generations: typing.Final[int] = 100
delay: typing.Final[float] = 0.1

# initialize random grid
# noinspection DuplicatedCode
grid = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

for gen in range(1, generations + 1):
    # noinspection DuplicatedCode
    os.system('cls' if os.name == 'nt' else 'clear')
    alive_count = sum(sum(row) for row in grid)
    # header
    print(
        HEADER_COL
        + f' Game of Life | Generation {gen}/{generations} | Alive: {alive_count} '.center(cols, '=')
        + RESET_COL
    )
    # grid display
    for row in grid:
        print(''.join(ALIVE_CHAR if cell else DEAD_CHAR for cell in row))
    # update

    old_grid = grid
    grid: list[list[int]] = []

    for i in range(rows):
        new_row = []
        for j in range(cols):
            # Count live neighbors (including wraparound)
            neighbor_count = sum(
                old_grid[(i + di) % rows][(j + dj) % cols]
                for di in (-1, 0, 1)
                for dj in (-1, 0, 1)
                if not (di == 0 and dj == 0)
            )

            # Apply Conway's rules:
            # 1. Any live cell with 2-3 neighbors survives
            # 2. Any dead cell with exactly 3 neighbors becomes alive
            # 3. All other cells die or stay dead
            if old_grid[i][j] == IS_ALIVE:
                new_row.append(1 if neighbor_count in SURVIVING_COUNTS else 0)
            else:  # Currently dead
                new_row.append(1 if neighbor_count == REVIVED_COUNT else 0)

        grid.append(new_row)

    time.sleep(delay)
