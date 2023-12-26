#!/usr/bin/python3

import sys
sys.setrecursionlimit(100000)

def decode_puzzle(lines):
    return [[c for c in line] for line in lines.read().strip().split('\n')]

directions = ['N', 'S', 'E', 'W']
options = {
    'N': {
        '.': ['N'],
        '|': ['N'],
        '-': ['E', 'W'],
        '/': ['E'],
        '\\': ['W'],
    },

    'S': {
        '.': ['S'],
        '|': ['S'],
        '-': ['E', 'W'],
        '/': ['W'],
        '\\': ['E'],
    },

    'E': {
        '.': ['E'],
        '|': ['N', 'S'],
        '-': ['E'],
        '/': ['N'],
        '\\': ['S'],
    },

    'W': {
        '.': ['W'],
        '|': ['N', 'S'],
        '-': ['E', 'W'],
        '/': ['S'],
        '\\': ['N'],
    },
}

def move(beam):
    i, j, d = beam

    if d == 'N':
        return i-1, j, d
    if d == 'S':
        return i+1, j, d
    if d == 'E':
        return i, j+1, d
    if d == 'W':
        return i, j-1, d

def valid_location(puzzle, i, j):
    if i >= len(puzzle) or i < 0 or j >= len(puzzle) or j < 0:
        return False
    return True

def run_beam(puzzle, beams, beam):
    i, j, d = beam
    if beams[i][j][directions.index(d)]:
        return

    beams[i][j][directions.index(d)] = 1

    new_ds = options[d][puzzle[i][j]]
    for new_d in new_ds:
        new_beam = move((i, j, new_d))
        if not valid_location(puzzle, new_beam[0], new_beam[1]):
            continue

        run_beam(puzzle, beams, new_beam)

def print_beams(puzzle, beams):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != '.':
                sys.stdout.write(puzzle[i][j])
                continue

            if sum(beams[i][j]) == 0:
                sys.stdout.write('.')
                continue

            if sum(beams[i][j]) == 2:
                sys.stdout.write('2')
                continue
            if sum(beams[i][j]) == 3:
                sys.stdout.write('3')
                continue
            if sum(beams[i][j]) == 4:
                sys.stdout.write('4')
                continue

            if beams[i][j][0] == 1:
                sys.stdout.write('^')
            if beams[i][j][1] == 1:
                sys.stdout.write('V')
            if beams[i][j][2] == 1:
                sys.stdout.write('>')
            if beams[i][j][3] == 1:
                sys.stdout.write('<')

        sys.stdout.write('\n')

def total_energized(beams):
    return sum(
        1 if sum(beams[i][j]) > 0 else 0
        for j in range(len(beams[0]))
        for i in range(len(beams))
    )

def part1(puzzle):
    beams = [[[0, 0, 0, 0] for c in l] for l in puzzle]
    run_beam(puzzle, beams, (0, 0, 'E'))
    print_beams(puzzle, beams)
    return total_energized(beams)

def part2(puzzle):
    maximum = 0
    for beam in get_combinations(puzzle):
        beams = [[[0, 0, 0, 0] for c in l] for l in puzzle]
        run_beam(puzzle, beams, beam)
        energized = sum(
            1 if sum(beams[i][j]) > 0 else 0
            for j in range(len(puzzle[0]))
            for i in range(len(puzzle))
        )
        if energized > maximum:
            maximum = energized

    return maximum

def get_combinations(puzzle):
    combinations = []
    for i in range(len(puzzle)):
        combinations.append((i, 0, 'E'))
    for i in range(len(puzzle)):
        combinations.append((i, len(puzzle[0])-1, 'W'))
    for j in range(len(puzzle[0])):
        combinations.append((0, j, 'S'))
    for i in range(len(puzzle)):
        combinations.append((len(puzzle) - 1, j, 'N'))
    return combinations

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
