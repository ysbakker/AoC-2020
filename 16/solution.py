# https://adventofcode.com/2020/day/16
import os, timeit


def between(val, b1, b2):
    return b1 <= val <= b2


def solve(inp, part):
    rules, mine, tickets = inp.split('\n\n')
    mine = [int(val) for val in mine.split('\n')[1].split(',')]
    tickets = [[int(val) for val in t.split(',')]
               for t in tickets.split('\n')[1:]]
    allRules = list()
    for r in rules.split('\n'):
        allRules.append([int(b) for b in r.split(' ')[-1].split('-')])
        allRules.append([int(b) for b in r.split(' ')[-3].split('-')])
    validCache = set()

    rate = 0
    for i, t in enumerate(tickets):
        for val in t:
            if val in validCache: continue
            valid = False
            for rule in allRules:
                if between(val, rule[0], rule[1]):
                    valid = True
                    validCache.add(val)
                    break
            if not valid:
                if part == 1: rate += val
                if part == 2: tickets.pop(i)
                break
    if part == 1: return rate
    if part == 2:
        candidates = {
            i: set(range(len(allRules) // 2))
            for i in range(len(mine))
        }
        for ticket in tickets:
            for i, val in enumerate(ticket):
                discarded = set()
                for rn in range(len(allRules) // 2):
                    if rn not in candidates[i]: continue
                    r1, r2 = (allRules[rn * 2], allRules[rn * 2 + 1])
                    if not (between(val, r1[0], r1[1])) and not (between(
                            val, r2[0], r2[1])):
                        candidates[i].discard(rn)
                        discarded.add(rn)
                if len(discarded) >= 20:
                    print(val, 'discarded')

        return candidates


with open(f'{os.getcwd()}/16/input') as inputFile:
    puzzleInput = inputFile.read()
    print(solve(puzzleInput, 1))
    print(solve(puzzleInput, 2))
    print(
        f'Part 1 avg: {timeit.timeit(lambda: solve(puzzleInput, 1), number=1) * 1000}ms'
    )
    print(
        f'Part 2 avg: {timeit.timeit(lambda: solve(puzzleInput, 2), number=1) * 1000}ms'
    )