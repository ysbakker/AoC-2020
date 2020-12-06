# https://adventofcode.com/2020/day/6

import os, time


def uniqueAnswers(groupAnswers):
    return sum([len(set(answer.replace('\n', ''))) for answer in groupAnswers])


def unanimousAnswers(groupAnswers):
    unanimous = 0
    for group in groupAnswers:
        memberAnswers = group.split('\n')
        currentlyUnanimous = set(memberAnswers[0])
        for i, answers in enumerate(memberAnswers):
            if i == 0: continue
            currentlyUnanimous = currentlyUnanimous & set(answers)
        unanimous += len(currentlyUnanimous)
    return unanimous


def step1(puzzleInput):
    return uniqueAnswers(puzzleInput)


def step2(puzzleInput):
    return unanimousAnswers(puzzleInput)


with open(f'{os.getcwd()}/day6/input') as inputFile:
    puzzleInput = inputFile.read().split('\n\n')
    startTime = time.time()
    print(step1(puzzleInput))
    print(f'Step 1 execution time: {(time.time() - startTime) * 1000}ms')
    # ~ 1 ms

    startTime = time.time()
    print(step2(puzzleInput))
    print(f'Step 2 execution time: {(time.time() - startTime) * 1000}ms')
    # ~ 2-3 ms
