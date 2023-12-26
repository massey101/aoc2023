#!/usr/bin/python3

import sys

def decode_puzzle(lines):
    maps = lines.read().strip().split('\n\n')
    return [[l for l in m.split('\n')] for m in maps]

def get_horizontal_mirror(m, compare_func):
    for i in range(1, len(m)):
        end = min(len(m), i+i)
        size = end - i
        left = m[i - size:i]
        right = m[i:end]
        right = list(reversed(right))
        if compare_func(left, right):
            return i
    return None

def rotate_map(m):
    return [''.join(m[i][j] for i in range(len(m))) for j in range(len(m[0]))]

def get_mirror(m, compare_func):
    horizontal_mirror = get_horizontal_mirror(m, compare_func)
    if horizontal_mirror is not None:
        return 100 * horizontal_mirror
    rotated_m = rotate_map(m)
    return get_horizontal_mirror(rotated_m, compare_func)

def compare_part1(left, right):
    return left == right

def part1(puzzle):
    mirrors = [get_mirror(m, compare_part1) for m in puzzle]
    return sum(mirrors)

def compare_part2(left, right):
    errors = 0
    for left_line, right_line in zip(left, right):
        for left_c, right_c in zip(left_line, right_line):
            if left_c == right_c:
                continue
            errors += 1

    return errors == 1

def part2(puzzle):
    mirrors = [get_mirror(m, compare_part2) for m in puzzle]
    return sum(mirrors)

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
