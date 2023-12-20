#!/usr/bin/python3

import sys

def decode_puzzle(lines):
    lines = lines.read().strip().split('\n')
    return [(l.split(' ')[0], [int(g) for g in l.split(' ')[1].split(',')]) for l in lines]


def apply_combination_num(data, combination):
    new_data = []
    i = 0
    for s in data:
        if s == '?':
            new_data.append('.' if combination & (1 << i) else '#')
            i += 1
            continue
        new_data.append(s)

    return ''.join(new_data)

def combination_is_valid(data, groups):
    data_groups = [len(broken) for broken in data.split('.') if len(broken) > 0]
    return data_groups == groups

def get_possible_arrangements(row):
    data, groups = row

    num_unknowns = sum(1 if s == '?' else 0 for s in data)
    combinations = []
    for combination in range(2**num_unknowns):
        new_combination = apply_combination_num(data, combination)
        if combination_is_valid(new_combination, groups):
            combinations.append(new_combination)
    print(data, len(combinations))
    return len(combinations)


def part1(puzzle):
    total = 0
    for i, row in enumerate(puzzle):
        print(i, '/', len(puzzle))
        total += get_possible_arrangements(row)
    return total

def part2(puzzle):
    new_puzzle = []
    for data, groups in puzzle:
        new_puzzle.append(('?'.join([data]*5), groups * 5))
    for data, groups in new_puzzle:
        num_unknowns = sum(1 if s == '?' else 0 for s in data)
        print(num_unknowns)
    return part1(new_puzzle)

def main():
    if len(sys.argv) == 1:
        puzzle = decode_puzzle(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            puzzle = decode_puzzle(f)

    print(part1(puzzle))
    print(part2(puzzle))

if __name__ == '__main__':
    main()
