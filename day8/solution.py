# https://adventofcode.com/2020/day/8

import os, timeit


def runBootCode(instructions, mem=[0, 0, set()]):
    mem[2].add(mem[0])
    op, val = instructions[mem[0]]

    if op == 'jmp': mem[0] += val - 1
    elif op == 'acc': mem[1] += val

    mem[0] += 1


def step1(puzzleInput):
    instructions = [(i.split(' ')[0], int(i.split(' ')[1]))
                    for i in puzzleInput.split('\n')]
    mem = [0, 0, set()]  # [cursor, accumulator, seen]
    while mem[0] not in mem[2] and mem[0] < len(instructions):
        runBootCode(instructions, mem)
    return mem[1]


def step2(puzzleInput):
    instructions = [[i.split(' ')[0], int(i.split(' ')[1])]
                    for i in puzzleInput.split('\n')]

    for cursor, instruction in enumerate(instructions):
        op, val = instruction
        if op == 'acc': continue
        instruction[0] = 'jmp' if op == 'nop' else 'nop'

        mem = [0, 0, set()]  # [cursor, accumulator, seen]
        while mem[0] not in mem[2] and mem[0] != len(instructions):
            runBootCode(instructions, mem)

        if mem[0] == len(instructions): return mem[1]
        instruction[0] = 'jmp' if instruction[0] == 'nop' else 'nop'


with open(f'{os.getcwd()}/day8/input') as inputFile:
    puzzleInput = inputFile.read()
    print(step1(puzzleInput))
    print(step2(puzzleInput))
    print(
        f'Step 1 avg: {timeit.timeit(lambda: step1(puzzleInput), number=1000)}ms'
    )  # <1ms
    print(
        f'Step 2 avg: {timeit.timeit(lambda: step2(puzzleInput), number=1000)}ms'
    )  # ~10ms
