#!/usr/bin/python3

import sys
from day5lib import decode_almanac, get_location

def main():
    if len(sys.argv) == 1:
        almanac = decode_almanac(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            almanac = decode_almanac(f)

    locations = []
    for seed in almanac['seeds']:
        locations.append(get_location(seed, almanac['maps']))

    print(min(locations))

if __name__ == '__main__':
    main()
