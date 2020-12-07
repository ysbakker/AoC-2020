# https://adventofcode.com/2020/day/7

import os, time


def parse(inp):
    rules = dict()
    for rule in inp:
        color, children = rule.split(' bags contain ')
        children = [child.split(' ') for child in children.split(', ')]
        if children[0][0] == 'no':
            rules[color] = []
            continue
        rules[color] = [(int(child[0]), f'{child[1]} {child[2]}')
                        for child in children]
    return rules


def findColor(rules, color):
    matches = set()
    for parent in rules:
        for child in rules[parent]:
            if (child[1] == color):
                matches.add(parent)
    return matches


def countBags(rules, color):
    count = 0
    for child in rules[color]:
        count += child[0] + child[0] * countBags(rules, child[1])
    return count


def step1(puzzleInput):
    rules = parse(puzzleInput)
    colors = findColor(rules, 'shiny gold')
    length = [0, len(colors)]
    while length[0] != length[1]:
        length[0] = length[1]
        newColors = set()
        for color in colors:
            newColors.update(findColor(rules, color))
        colors.update(newColors)
        length[1] = len(colors)

    return len(colors)


def step2(puzzleInput):
    rules = parse(puzzleInput)
    return countBags(rules, 'shiny gold')


with open(f'{os.getcwd()}/day7/input') as inputFile:
    puzzleInput = inputFile.read().split('.\n')
    startTime = time.time()
    print(step1(puzzleInput))
    print(f'Step 1 execution time: {(time.time() - startTime) * 1000}ms')
    # ~  ms

    startTime = time.time()
    print(step2(puzzleInput))
    print(f'Step 2 execution time: {(time.time() - startTime) * 1000}ms')
    # ~  ms
