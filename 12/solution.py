# https://adventofcode.com/2020/day/12
import os, timeit


def moveShip(instruction, pos):
    ins, val = instruction
    new = pos[:]
    if ins == 'N': new[2] += val
    elif ins == 'S': new[2] -= val
    elif ins == 'E': new[1] += val
    elif ins == 'W': new[1] -= val
    elif ins == 'L': new[0] = (pos[0] - val + 360) % 360
    elif ins == 'R': new[0] = (pos[0] + val) % 360
    elif ins == 'F':
        new[pos[0] // 90 % 2 + 1] += val if pos[0] in (0, 270) else -val
    return new


def moveWaypoint(instruction, pos):
    ins, val = instruction
    new = pos[:]
    if ins == 'N': new[1] += val
    elif ins == 'S': new[1] -= val
    elif ins == 'E': new[0] += val
    elif ins == 'W': new[0] -= val
    elif ins == 'L':
        new[0] = pos[val // 90 % 2] * (-1 if val in (90, 180) else 1)
        new[1] = pos[(val // 90 + 1) % 2] * (-1 if val in (180, 270) else 1)
    elif ins == 'R':
        new[0] = pos[val // 90 % 2] * (-1 if val in (180, 270) else 1)
        new[1] = pos[(val // 90 + 1) % 2] * (-1 if val in (90, 180) else 1)
    return new


def solve(inp, part):
    instructions = [(line[:1], int(line[1:])) for line in inp.split('\n')]
    if part == 1:
        ship = [0, 0, 0]  # deg, x, y
        for instruction in instructions:
            ship = moveShip(instruction, ship)
        return abs(ship[1]) + abs(ship[2])
    if part == 2:
        waypoint = [10, 1]  # x, y
        ship = [0, 0]  # x, y
        for instruction in instructions:
            waypoint = moveWaypoint(instruction, waypoint)
            if (instruction[0] == 'F'):
                ship[0] = ship[0] + instruction[1] * waypoint[0]
                ship[1] = ship[1] + instruction[1] * waypoint[1]
        return abs(ship[0]) + abs(ship[1])


with open(f'{os.getcwd()}/12/input') as inputFile:
    puzzleInput = inputFile.read()
    print(solve(puzzleInput, 1))
    print(solve(puzzleInput, 2))
    print(
        f'Part 1 avg: {timeit.timeit(lambda: solve(puzzleInput, 1), number=1) * 1000 }ms'
    )
    print(
        f'Part 2 avg: {timeit.timeit(lambda: solve(puzzleInput, 2), number=1) * 1000 }ms'
    )
