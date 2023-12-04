#!/usr/bin/python3

import sys
from day3lib import get_engine_parts

def locate_gears(parts):
    gears = {

    }
    for part in parts:
        for symbol in part['symbols']:
            if symbol['symbol'] != "*":
                continue

            location = symbol['location']
            if location in gears:
                gears[location].append(part['serial_number'])
            else:
                gears[location] = [part['serial_number']]

    return gears

def multiply_list(l):
    total = 1
    for v in l:
        total *= v

    return total

def main():
    if len(sys.argv) == 1:
        lines = [line.strip() for line in sys.stdin]
    else:
        lines = []
        with open(sys.argv[1]) as f:
            for line in f:
                lines.append(line.strip())

    parts = get_engine_parts(lines)
    gears = locate_gears(parts)
    print(sum(multiply_list(g) for g in gears.values() if len(g) > 1))

if __name__ == '__main__':
    main()
