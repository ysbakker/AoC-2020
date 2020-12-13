# https://adventofcode.com/2020/day/13
import os, timeit, time


def solve(inp, part):
    mins = int(inp.split('\n')[0])
    buses = inp.split('\n')[1].split(',')
    if part == 1:
        buses = [int(bus) for bus in buses if bus != 'x']
        wait = {(mins // bus + 1) * bus - mins: bus for bus in buses}
        return wait.get(min(wait), 0) * min(wait)
    if part == 2:
        dt = [i for i, b in enumerate(buses) if b != 'x']
        buses = [int(bus) for bus in buses if bus != 'x']
        i = 1
        done = False
        val = 0
        while not done:
            done = True
            val = max(buses) * i - dt[buses.index(max(buses))]
            for n, bus in enumerate(buses):
                if (val + dt[n]) % bus != 0:
                    done = False
            i += 1
        return val


with open(f'{os.getcwd()}/13/input') as inputFile:
    puzzleInput = inputFile.read()
    print(solve(puzzleInput, 1))
    print(solve(puzzleInput, 2))
    print(
        f'Part 1 avg: {timeit.timeit(lambda: solve(puzzleInput, 1), number=1000)}ms'
    )
    # print(
    #     f'Part 2 avg: {timeit.timeit(lambda: solve(puzzleInput, 2), number=1000)}ms'
    # )
