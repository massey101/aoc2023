#!/usr/bin/python3

import sys

def decode_puzzle(lines):
    return lines.read().strip().split('\n')

space = '.'
galaxy = '#'
expansion = '+'

def rotate_puzzle(puzzle):
    return [[puzzle[i][j] for i in range(len(puzzle))] for j in range(len(puzzle[0]))]

def expand_puzzle_rows(puzzle):
    new_puzzle = []
    for i in range(len(puzzle)):
        if galaxy not in puzzle[i]:
            new_puzzle.append([expansion] * len(puzzle[i]))
        else:
            new_puzzle.append(puzzle[i])
    return new_puzzle

def expand_puzzle(puzzle):
    new_puzzle = expand_puzzle_rows(puzzle)
    new_puzzle = rotate_puzzle(new_puzzle)
    new_puzzle = expand_puzzle_rows(new_puzzle)
    return rotate_puzzle(new_puzzle)

def get_galaxies(puzzle):
    galaxies = []
    for i, line in enumerate(puzzle):
        for j, c in enumerate(line):
            if c == galaxy:
                galaxies.append((i, j))
    return galaxies

def get_galaxy_pairs(galaxies):
    galaxy_pairs = {}
    for g1, _ in enumerate(galaxies):
        for g2, _ in enumerate(galaxies):
            i, j = g1, g2
            if i == j:
                continue
            if i > j:
                i, j = j, i
            if (i, j) not in galaxy_pairs:
                galaxy_pairs[(i, j)] = None

    return galaxy_pairs

def get_galaxy_distance(puzzle, g1, g2, expansion_factor):
    # In Manhattan distance we don't need to take diagonals.
    sy, ey = min(g1[0], g2[0]), max(g1[0], g2[0])
    sx, ex = min(g1[1], g2[1]), max(g1[1], g2[1])
    x = puzzle[sy][sx+1:ex+1]
    x = [expansion_factor if c == expansion else 1 for c in x]
    y = [puzzle[i][sx] for i in range(sy+1, ey+1)]
    y = [expansion_factor if c == expansion else 1 for c in y]
    return sum(x) + sum(y)


def part1(puzzle, expansion_factor=2):
    puzzle = expand_puzzle(puzzle)
    galaxies = get_galaxies(puzzle)
    galaxy_pairs = get_galaxy_pairs(galaxies)
    for pair in galaxy_pairs:
        g1, g2 = pair
        galaxy_pairs[pair] = get_galaxy_distance(puzzle, galaxies[g1], galaxies[g2], expansion_factor)

    return sum(galaxy_pairs.values())

def part2(puzzle):
    return part1(puzzle, expansion_factor=1000000)

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
