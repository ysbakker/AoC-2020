# https://adventofcode.com/2020/day/15
import os, timeit


def solve(inp, part):
    startingN = inp.split(',')
    memory = {int(n): i + 1 for i, n in enumerate(startingN[:-1])}
    current = int(startingN[-1])
    if part == 1:
        for i in range(len(startingN), 2020):
            prevIndex = memory.get(current, 0)
            memory[current] = i
            current = i - prevIndex if prevIndex != 0 else 0
    if part == 2:
        for i in range(len(startingN), 30000000):
            prevIndex = memory.get(current, 0)
            memory[current] = i
            current = i - prevIndex if prevIndex != 0 else 0

    return current


with open(f'{os.getcwd()}/15/input') as inputFile:
    puzzleInput = inputFile.read()
    print(solve(puzzleInput, 1))
    print(solve(puzzleInput, 2))
    print(
        f'Part 1 avg: {timeit.timeit(lambda: solve(puzzleInput, 1), number=1000)}ms'
    )
    print(
        f'Part 2 avg: {timeit.timeit(lambda: solve(puzzleInput, 2), number=1) * 1000}ms'
    )