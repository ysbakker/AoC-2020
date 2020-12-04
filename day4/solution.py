# https://adventofcode.com/2020/day/4

import os, time, re


def parse(data):
    passports = list()
    for passport in data:
        fields = dict()
        for field in passport.split():
            key, value = field.split(':')
            fields[key] = value
        passports.append(fields)
    return passports


def validate(key, value):
    if value is None: return False
    if key == 'byr': return 1920 <= int(value) <= 2002
    elif key == 'iyr': return 2010 <= int(value) <= 2020
    elif key == 'eyr': return 2020 <= int(value) <= 2030
    elif key == 'hgt':
        match = re.compile(r'^(\d{2,3})(in|cm)$').match(value)
        if match is not None:
            hgt, unit = [match.group(1), match.group(2)]
            return (unit == 'cm'
                    and 150 <= int(hgt) <= 193) or (unit == 'in'
                                                    and 59 <= int(hgt) <= 76)
        return False
    elif key == 'hcl':
        return re.compile(r'^#[\da-f]{6}$').match(value) is not None
    elif key == 'ecl':
        return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    elif key == 'pid':
        return re.compile(r'^\d{9}$').match(value) is not None


def step1(puzzleInput):
    valid = 0
    required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    passports = parse(puzzleInput)
    for passport in passports:
        if all([passport.get(field) is not None for field in required]):
            valid += 1
    return valid


def step2(puzzleInput):
    valid = 0
    required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    passports = parse(puzzleInput)
    for passport in passports:
        if all([validate(field, passport.get(field)) for field in required]):
            valid += 1
    return valid


with open(f'{os.getcwd()}/day4/input') as inputFile:
    puzzleInput = inputFile.read().split('\n\n')
    startTime = time.time()
    print(step1(puzzleInput))
    print(f'Step 1 execution time: {(time.time() - startTime) * 1000}ms')
    # ~ 2-4ms

    startTime = time.time()
    print(step2(puzzleInput))
    print(f'Step 2 execution time: {(time.time() - startTime) * 1000}ms')
    # ~ 7-9ms