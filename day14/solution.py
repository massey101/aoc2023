#!/usr/bin/python3

import sys

def decode_puzzle(lines):
    return [[c for c in l] for l in lines.read().strip().split('\n')]

def take_slice(puzzle, l):
    i, j = l
    s = []
    for x in range(i-1, -1, -1):
        s.append(puzzle[x][j])

    return s

def find_collision(puzzle_slice):
    for i, c in enumerate(puzzle_slice):
        if c in ['O', '#']:
            return i

    return len(puzzle_slice)


def tilt(puzzle):
    puzzle = [[c for c in l] for l in puzzle]
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] != 'O':
                continue
            s = take_slice(puzzle, (i, j))
            x = find_collision(s)
            if x > 0:
                puzzle[i-x][j] = 'O'
                puzzle[i][j] = '.'

    return puzzle


def calculate_load(puzzle):
    total = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == 'O':
                total += len(puzzle) - i
    return total

def part1(puzzle):
    puzzle = tilt(puzzle)
    return calculate_load(puzzle)

def rotate_puzzle(m):
    return [[m[len(m)-i-1][j] for i in range(len(m))] for j in range(len(m[0]))]

def spin(puzzle):
    for i in range(4):
        puzzle = tilt(puzzle)
        puzzle = rotate_puzzle(puzzle)

    return puzzle

def fast_spin(puzzle, spins):
    puzzle_history = []
    puzzle_history.append(puzzle)
    i = 0
    while i < spins:
        puzzle = spin(puzzle)
        if puzzle in puzzle_history:
            index = puzzle_history.index(puzzle) - 1 # -1 to account for initial input
            distance = i - index
            while i < spins - 2 * distance:
                i += distance
        puzzle_history.append(puzzle)
        i += 1
    return puzzle

def part2(puzzle):
    spins = 1000000000
    puzzle = fast_spin(puzzle, spins)

    return calculate_load(puzzle)

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
