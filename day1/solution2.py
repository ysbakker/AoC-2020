# Trying to reduce the complexity by using python set

import os
import time


# O(n)
def step1(sumValue, arr):
    memory = set()
    for i, val in enumerate(arr):
        remainder = sumValue - val
        if remainder < 0: continue

        if remainder in memory:
            return val * remainder
        memory.add(val)


# O(n^2)
def step2(sumValue, arr):
    for i, val in enumerate(arr):
        remainder = sumValue - val
        if remainder < 0: continue

        result = step1(remainder, arr)
        if result is not None:
            return val * result


with open(f'{os.getcwd()}/day1/input') as inputFile:
    puzzleInput = [int(num) for num in inputFile.read().split('\n')]

    startTime = time.time()
    print(step1(2020, puzzleInput))
    print(f'Step 1 execution time: {(time.time() - startTime) * 1000}ms')

    startTime = time.time()
    print(step2(2020, puzzleInput))
    print(f'Step 2 execution time: {(time.time() - startTime) * 1000}ms')