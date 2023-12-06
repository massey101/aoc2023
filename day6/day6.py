#!/usr/bin/python3

import sys

def decode_races(lines):
    data = lines.read().strip().split('\n')

    times = [int(t) for t in data[0].split(':')[1].strip().split()]
    distances = [int(d) for d in data[1].split(':')[1].strip().split()]

    return list(zip(times, distances))

def combine_races(races):
    time = int(''.join([str(r[0]) for r in races]))
    distance = int(''.join([str(r[1]) for r in races]))

    return [(time, distance)]

def calculate_win_methods(race):
    time = race[0]
    distance = race[1]
    return [t for t in range(time) if t * (time - t) > distance]

def part2(races):
    races = combine_races(races)
    return part1(races)

def part1(races):
    combinations = 1
    for race in races:
        combinations *= len(calculate_win_methods(race))

    return combinations

def main():
    if len(sys.argv) == 1:
        races = decode_races(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            races = decode_races(f)

    print(part1(races))
    print(part2(races))

if __name__ == '__main__':
    main()
