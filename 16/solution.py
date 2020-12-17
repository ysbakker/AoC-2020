# https://adventofcode.com/2020/day/16
import os, timeit, math


def solve(inp, part):
    rules, mine, tickets = inp.split('\n\n')
    mine = [int(val) for val in mine.split('\n')[1].split(',')]
    tickets = [[int(val) for val in t.split(',')]
               for t in tickets.split('\n')[1:]]
    rules = [
        r.split(' ')[-1].split('-') + r.split(' ')[-3].split('-')
        for r in rules.split('\n')
    ]
    candidates = {pos: set(range(len(rules))) for pos in range(len(mine))}
    validTickets = tickets[:]

    rate = 0
    for t in tickets:
        for pos, val in enumerate(t):
            valid = False
            for rn in range(len(rules)):
                r1, r2, r3, r4 = [int(r) for r in rules[rn]]
                if r1 <= val <= r2 or r3 <= val <= r4:
                    valid = True
                    break
            if not valid:
                rate += val
                validTickets.remove(t)
                break

    if part == 1: return rate
    if part == 2:
        for t in validTickets:
            for pos, val in enumerate(t):
                for rn in range(len(rules)):
                    if rn not in candidates[pos]: continue
                    r1, r2, r3, r4 = [int(r) for r in rules[rn]]
                    if not r1 <= val <= r2 and not r3 <= val <= r4:
                        candidates[pos].discard(rn)
        positions = {i: None for i in range(len(rules))}
        while any([positions[p] is None for p in positions]):
            for p in positions:
                if len(candidates[p]) == 1:
                    rule = next(iter(candidates[p]))
                    positions[rule] = p
                    for c in candidates:
                        candidates[c].discard(rule)
        return math.prod([
            mine[pos]
            for pos in [positions[pos] for pos in positions if pos < 6]
        ])


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