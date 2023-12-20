#!/usr/bin/python3

import sys

DEBUG = False

def decode_carts(lines):
    return lines.read().strip().split('\n')


def part1(carts):
    carts = [line for line in carts]
    start = find_start(carts)
    carts[start[0]] = carts[start[0]][:start[1]] + convert_start(carts, start) + carts[start[0]][start[1]+1:]
    distances = dfs(carts, start)
    print_distances(distances) if DEBUG else None
    return max(max(l) for l in distances)

def find_start(carts):
    for i, line in enumerate(carts):
        for j, c in enumerate(line):
            if c == 'S':
                return i, j

    return ValueError('Start Not Found')

pipe_directions = {
    '|': 'NS',
    '-': 'EW',
    'L': 'NE',
    'J': 'NW',
    '7': 'SW',
    'F': 'SE',
    '.': '',
    ' ': '',
}

directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
}

opposite = {'N': 'S', 'E': 'W', 'W': 'E', 'S': 'N'}

def out_of_bounds(carts, l):
    i, j = l
    if i >= len(carts) or i < 0 or j >= len(carts[0]) or j < 0:
        return True
    return False

def move(carts, l, direction):
    d = directions[direction]
    new_l = l[0] + d[0], l[1] + d[1]
    if out_of_bounds(carts, new_l):
        return None
    return new_l

def dfs(carts, start):
    distances = [[-1] * len(carts[0]) for _ in range(len(carts))]

    distance = 0
    points = [start]
    while points:
        new_points = []
        for point in points:
            if point is None:
                continue

            i, j = point
            if distances[i][j] != -1:
                continue

            distances[i][j] = distance
            for direction in pipe_directions[carts[i][j]]:
                new_points.append(move(carts, (i, j), direction))
        points = new_points
        distance += 1
    return distances

def print_distances(distances):
    size = 1
    for line in distances:
        for c in line:
            if c > 10:
                size = 2
            if c > 100:
                size = 3

    for line in distances:
        for c in line:
            if c == -1:
                sys.stderr.write('.'.rjust(size))
                continue
            sys.stderr.write('{}'.format(c).rjust(size))
        sys.stderr.write('\n')

def convert_start(carts, l):
    start_directions = ''
    for direction in directions:
        new_l = move(carts, l, direction)
        if new_l is None:
            continue
        i, j = new_l
        if opposite[direction] in pipe_directions[carts[i][j]]:
            start_directions += direction

    for pipe, d in pipe_directions.items():
        if d == start_directions:
            return pipe


def part2(carts):
    carts = [line for line in carts]
    start = find_start(carts)
    carts[start[0]] = carts[start[0]][:start[1]] + convert_start(carts, start) + carts[start[0]][start[1]+1:]
    distances = dfs(carts, start)
    print_distances(distances) if DEBUG else None

    inside = get_inside(carts, distances)
    print_distances(inside) if DEBUG else None

    return sum(sum(l) for l in inside)

def get_inside(carts, distances):
    inside = [[0] * len(carts[0]) for _ in range(len(carts))]
    for i in range(len(carts)):
        for j in range(len(carts[0])):
            if distances[i][j] != -1:
                continue
            intersections = cast_ray(carts, distances, (i, j))
            if intersections % 2 == 1:
                inside[i][j] = 1

    return inside

def cast_ray(carts, distances, l):
    i, j = l
    selection = carts[i][:j]
    filtered = [c for c, d in zip(selection, distances[i][:j]) if d != -1 and c != '-']
    intersections = 0
    i = len(filtered) - 1
    while i >= 0:
        if filtered[i] == '|':
            intersections += 1
        if filtered[i] == '7':
            i -= 1
            if filtered[i] == 'L':
                intersections += 1
        if filtered[i] == 'J':
            i -= 1
            if filtered[i] == 'F':
                intersections += 1

        i -= 1

    return intersections

def main():
    if len(sys.argv) == 1:
        carts = decode_carts(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            carts= decode_carts(f)

    print(part1(carts))
    print(part2(carts))

if __name__ == '__main__':
    main()
