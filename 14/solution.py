# https://adventofcode.com/2020/day/14
import os, timeit


def getAddresses(address, mask):
    addresses = []
    bl = mask.count('X')
    address = format(address | int(mask.replace('X', '0'), 2),
                     f'0{len(mask)}b')
    combinations = [format(c, f'0{bl}b') for c in range(pow(2, bl))]
    for c in combinations:
        new = ''
        cursor = 0
        for i, ch in enumerate(mask):
            if ch == 'X':
                new += c[cursor]
                cursor += 1
            else:
                new += address[i]
        addresses.append(new)
    return addresses


def solve(inp, part):
    inst = inp.split('\n')
    memory = {}
    for cmd, val in [i.split(' = ') for i in inst]:
        mask = val if cmd == 'mask' else mask
        if 'mem' in cmd and part == 1:
            val = int(val) & int(mask.replace('X', '1'), 2)
            val = val | int(mask.replace('X', '0'), 2)
            memory[cmd[4:-1]] = val
        if 'mem' in cmd and part == 2:
            for a in getAddresses(int(cmd[4:-1]), mask):
                memory[a] = int(val)
    return sum([memory[pos] for pos in memory])


with open(f'{os.getcwd()}/14/input') as inputFile:
    puzzleInput = inputFile.read()
    print(solve(puzzleInput, 1))
    print(solve(puzzleInput, 2))
    print(
        f'Part 1 avg: {timeit.timeit(lambda: solve(puzzleInput, 1), number=1000)}ms'
    )
    print(
        f'Part 2 avg: {timeit.timeit(lambda: solve(puzzleInput, 2), number=1) * 1000}ms'
    )
