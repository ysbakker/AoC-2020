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


startTime = time.time()

puzzleInput = open(f'{os.getcwd()}/day1/input.txt').read().split('\n')
puzzleInput = [int(num) for num in puzzleInput]

print(step1(2020, puzzleInput))

print(f'Execution time: {(time.time() - startTime) * 1000}ms')