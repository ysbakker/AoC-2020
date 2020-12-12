# https://adventofcode.com/2020/day/12
import os, timeit


def moveShip(instruction, pos):
    ins, val = instruction
    deg = pos[0]
    if ins == 'N': pos[2] += val
    elif ins == 'S': pos[2] -= val
    elif ins == 'E': pos[1] += val
    elif ins == 'W': pos[1] -= val
    elif ins == 'L': pos[0] = (deg - val + 360) % 360
    elif ins == 'R': pos[0] = (deg + val) % 360
    elif ins == 'F': pos[deg // 90 % 2 + 1] += val if deg in (0, 270) else -val


def moveWaypoint(instruction, pos):
    ins, val = instruction
    if ins == 'N': pos[1] += val
    elif ins == 'S': pos[1] -= val
    elif ins == 'E': pos[0] += val
    elif ins == 'W': pos[0] -= val
    elif ins == 'L':
        new = (pos[val // 90 % 2] * (-1 if val in (90, 180) else 1),
               pos[(val // 90 + 1) % 2] * (-1 if val in (180, 270) else 1))
        pos[0] = new[0]
        pos[1] = new[1]
    elif ins == 'R':
        new = (pos[val // 90 % 2] * (-1 if val in (180, 270) else 1),
               pos[(val // 90 + 1) % 2] * (-1 if val in (90, 180) else 1))
        pos[0] = new[0]
        pos[1] = new[1]


def solve(inp, part):
    instructions = [(line[:1], int(line[1:])) for line in inp.split('\n')]
    if part == 1:
        ship = [0, 0, 0]  # deg, x, y
        for instruction in instructions:
            moveShip(instruction, ship)
        return abs(ship[1]) + abs(ship[2])
    if part == 2:
        waypoint = [10, 1]  # x, y
        ship = [0, 0]  # x, y
        for instruction in instructions:
            if (instruction[0] == 'F'):
                ship = [
                    ship[0] + instruction[1] * waypoint[0],
                    ship[1] + instruction[1] * waypoint[1]
                ]
            else:
                moveWaypoint(instruction, waypoint)
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
