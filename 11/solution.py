# https://adventofcode.com/2020/day/10

import os, timeit


def step1(puzzleInput):
    arrangement = puzzleInput.split('\n')
    occupied = 0
    done = False
    while not done:
        newArrangement = []
        done = True
        for r, row in enumerate(arrangement):
            newRow = ''
            for s, seat in enumerate(row):
                adjacent = 0
                for y in (-1, 0, 1):
                    for x in (-1, 0, 1):
                        if x == y == 0: continue
                        if 0 <= r + y < len(arrangement) and 0 <= s + x < len(
                                arrangement[0]):
                            if arrangement[r + y][s + x] == '#': adjacent += 1
                if adjacent == 0 and seat == 'L':
                    done = False
                    newRow += '#'
                    occupied += 1
                elif adjacent >= 4 and seat == '#':
                    done = False
                    newRow += 'L'
                    occupied -= 1
                else:
                    newRow += seat
            newArrangement.append(newRow)
        arrangement = newArrangement
    return occupied


def step2(puzzleInput):
    arrangement = puzzleInput.split('\n')
    occupied = 0
    done = False
    while not done:
        newArrangement = []
        done = True
        for r, row in enumerate(arrangement):
            newRow = ''
            for s, seat in enumerate(row):
                adjacent = 0
                for y in (-1, 0, 1):
                    for x in (-1, 0, 1):
                        if x == y == 0: continue
                        i = 1
                        while 0 <= r + i * y < len(
                                arrangement) and 0 <= s + i * x < len(
                                    arrangement[0]):
                            if arrangement[r + i * y][s + i * x] == '#':
                                adjacent += 1
                            if arrangement[r + i * y][s + i * x] != '.': break
                            i += 1
                if adjacent == 0 and seat == 'L':
                    done = False
                    newRow += '#'
                    occupied += 1
                elif adjacent >= 5 and seat == '#':
                    done = False
                    newRow += 'L'
                    occupied -= 1
                else:
                    newRow += seat
            newArrangement.append(newRow)
        arrangement = newArrangement
    return occupied


with open(f'{os.getcwd()}/11/input') as inputFile:
    puzzleInput = inputFile.read()
    print(step1(puzzleInput))
    print(step2(puzzleInput))
    print(
        f'Step 1 avg: {timeit.timeit(lambda: step1(puzzleInput), number=1) * 1000 }ms'
    )
    print(
        f'Step 2 avg: {timeit.timeit(lambda: step2(puzzleInput), number=1) * 1000 }ms'
    )
