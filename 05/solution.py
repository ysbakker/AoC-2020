# https://adventofcode.com/2020/day/5

import os, time


def parseBinary(inpt):
    inpt = inpt.replace('B', '1')
    inpt = inpt.replace('R', '1')
    inpt = inpt.replace('F', '0')
    inpt = inpt.replace('L', '0')
    return int(inpt, 2)


def getSeats(inpt):
    seats = set()
    for chair in inpt:
        row, col = (parseBinary(chair[:7]), parseBinary(chair[7:]))
        seats.add(row * 8 + col)
    return seats


def step1(puzzleInput):
    return max(getSeats(puzzleInput))


def step2(puzzleInput):
    seats = getSeats(puzzleInput)
    for i in range(127 * 8 + 7):
        if i not in seats:
            if i + 1 in seats and i - 1 in seats:
                return i


with open(f'{os.getcwd()}/day5/input') as inputFile:
    puzzleInput = inputFile.read().split('\n')
    startTime = time.time()
    print(step1(puzzleInput))
    print(f'Step 1 execution time: {(time.time() - startTime) * 1000}ms')
    # ~ 2-3 ms

    startTime = time.time()
    print(step2(puzzleInput))
    print(f'Step 2 execution time: {(time.time() - startTime) * 1000}ms')
    # ~ 2-3 ms
