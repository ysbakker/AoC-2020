# https://adventofcode.com/2020/day/10

import os, timeit


def step1(puzzleInput):
    joltages = sorted([int(joltage)
                       for joltage in puzzleInput.split('\n')] + [0])
    diff = [0, 0, 0, 1]

    for i, joltage in enumerate(joltages):
        diff[joltage - joltages[max(0, i - 1)]] += 1

    return diff[1] * diff[3]


def calculatePaths(joltages, joltage):
    reachable = set()
    paths = 0
    for i in range(3):
        if joltage - i - 1 in joltages:
            reachable.add(joltage - i - 1)
            paths += 1
    for nxtJoltage in reachable:
        paths += calculatePaths(joltages, nxtJoltage)
    return paths


def step2(puzzleInput):
    joltages = [int(joltage) for joltage in puzzleInput.split('\n')]
    joltages = sorted(joltages + [0, max(joltages) + 3])

    paths = dict()
    paths[0] = 1

    for joltage in joltages[1:]:
        paths[joltage] = sum([paths.get(joltage - c - 1, 0) for c in range(3)])

    return paths[max(joltages)]


with open(f'{os.getcwd()}/10/input') as inputFile:
    puzzleInput = inputFile.read()
    print(step1(puzzleInput))
    print(step2(puzzleInput))
    print(
        f'Step 1 avg: {timeit.timeit(lambda: step1(puzzleInput), number=1000)}ms'
    )
    print(
        f'Step 2 avg: {timeit.timeit(lambda: step2(puzzleInput), number=1000)}ms'
    )
