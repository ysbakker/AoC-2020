# https://adventofcode.com/2020/day/9

import os, timeit


def findWeakness(transmission, pa):
    if pa >= len(transmission): return
    for i in range(len(transmission) - pa):
        current = transmission[i + pa]
        values = transmission[i:i + pa]
        valid = False
        for value in values:
            remainder = current - value
            if remainder in values and remainder != value:
                valid = True
                break
        if not valid: return current


def findSum(transmission, weakness):
    for i, value in enumerate(transmission):
        current = i + 1
        total = value
        while total < weakness:
            total += transmission[current]
            current += 1
        if total == weakness:
            values = transmission[i:current]
            return min(values) + max(values)


def step1(puzzleInput):
    transmission = [int(val) for val in puzzleInput.split('\n')]
    return findWeakness(transmission, 25)


def step2(puzzleInput):
    transmission = [int(val) for val in puzzleInput.split('\n')]
    return findSum(transmission, step1(puzzleInput))


with open(f'{os.getcwd()}/09/input') as inputFile:
    puzzleInput = inputFile.read()
    print(step1(puzzleInput))
    print(step2(puzzleInput))
    print(
        f'Step 1 avg: {timeit.timeit(lambda: step1(puzzleInput), number=1000)}ms'
    )  # <1ms
    print(
        f'Step 2 avg: {timeit.timeit(lambda: step2(puzzleInput), number=1000)}ms'
    )  # ~10ms
