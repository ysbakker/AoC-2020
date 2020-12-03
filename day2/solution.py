import os
import re
import time


def hasValidCharacterCount(char, min, max, text):
    return min <= text.count(char) <= max


def hasValidCharacterPosition(char, pos1, pos2, text):
    pos1 -= 1
    pos2 -= 1
    return (0 <= pos1 < len(text) and 0 <= pos2 < len(text)
            ) and (text[pos1] == char) != (text[pos2] == char)


def parse(passwords):
    pattern = re.compile(r'^(\d+)-(\d+)\s([a-z]):\s(.+)$')
    result = list()
    for password in passwords:
        match = pattern.match(password)
        if match is not None:
            result.append({
                'val1': int(match.group(1)),
                'val2': int(match.group(2)),
                'char': match.group(3),
                'text': match.group(4)
            })
    return result


# O(n)
def step1(puzzleInput):
    passwords = parse(puzzleInput)
    count = 0
    for password in passwords:
        if hasValidCharacterCount(password['char'], password['val1'],
                                  password['val2'], password['text']):
            count += 1
    return count


# O(n)
def step2(puzzleInput):
    passwords = parse(puzzleInput)
    count = 0
    for password in passwords:
        if hasValidCharacterPosition(password['char'], password['val1'],
                                     password['val2'], password['text']):
            count += 1
    return count


with open(f'{os.getcwd()}/day2/input') as inputFile:
    puzzleInput = inputFile.read().split('\n')
    startTime = time.time()
    print(step1(puzzleInput))
    print(f'Step 1 execution time: {(time.time() - startTime) * 1000}ms')

    startTime = time.time()
    print(step2(puzzleInput))
    print(f'Step 2 execution time: {(time.time() - startTime) * 1000}ms')