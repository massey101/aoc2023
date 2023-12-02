#!/usr/bin/python3

import sys
from day2lib import decode_game

def convert_to_power(game):
    min_cubes = {'red': 0, 'blue': 0, 'green': 0}

    for draw in game['draws']:
        for colour in min_cubes:
            min_cubes[colour] = max(min_cubes[colour], draw[colour])

    return min_cubes['red'] * min_cubes['blue'] * min_cubes['green']

def main():
    games = [decode_game(line) for line in sys.stdin]
    powers = [convert_to_power(game) for game in games]
    total = sum(powers)
    print(total)

if __name__ == '__main__':
    main()
