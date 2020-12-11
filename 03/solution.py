# https://adventofcode.com/2020/day/3

import os, time


# O(n) -> n = len(grid)
def calculateTreeColissions(grid, slopex, slopey):
    i = 0
    width = len(grid[0])
    colissions = 0
    while i * slopey < len(grid):
        if grid[i * slopey][(i * slopex) % (width)] == '#': colissions += 1
        i += 1

    return colissions


def step1(grid):
    return calculateTreeColissions(grid, 3, 1)


def step2(grid):
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    product = 1
    for slope in slopes:
        product *= calculateTreeColissions(grid, slope[0], slope[1])

    return product


with open(f'{os.getcwd()}/03/input') as inputFile:
    puzzleInput = inputFile.read().split('\n')
    startTime = time.time()
    print(step1(puzzleInput))
    print(f'Step 1 execution time: {(time.time() - startTime) * 1000}ms')

    startTime = time.time()
    print(step2(puzzleInput))
    print(f'Step 2 execution time: {(time.time() - startTime) * 1000}ms')