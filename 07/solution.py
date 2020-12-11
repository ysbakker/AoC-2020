# https://adventofcode.com/2020/day/7

import os, timeit


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


def countBags(rules, color):
    count = 0
    for child in rules[color]:
        count += child[0] + child[0] * countBags(rules, child[1])
    return count


def step1(puzzleInput):
    rules = parse(puzzleInput)
    bagsWithGold = {'shiny gold'}
    seen = set()
    done = False
    while not done:
        done = True
        for bag in rules:
            for content in rules[bag]:
                if content[1] in bagsWithGold and bag not in seen:
                    done = False
                    bagsWithGold.add(bag)
                    seen.add(bag)

    return len(seen)


def step2(puzzleInput):
    rules = parse(puzzleInput)
    return countBags(rules, 'shiny gold')


with open(f'{os.getcwd()}/07/input') as inputFile:
    puzzleInput = inputFile.read().split('.\n')
    print(step1(puzzleInput))
    print(step2(puzzleInput))
    print(
        f'Step 1 avg: {timeit.timeit(lambda: step1(puzzleInput), number=1000)}ms'
    )  # 4-6ms
    print(
        f'Step 2 avg: {timeit.timeit(lambda: step2(puzzleInput), number=1000)}ms'
    )  # 3-5ms
