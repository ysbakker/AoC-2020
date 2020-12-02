import os
import time


# O(n^2)
def step1(sumValue, arr):
    for i, val in enumerate(arr):
        remainder = sumValue - val
        if remainder < 0: continue

        for j, selected in enumerate(arr):
            if selected == remainder and i != j:
                return val * selected
    return None


# O(n^3) ?
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
    print(f'Execution time: {(time.time() - startTime) * 1000}ms')