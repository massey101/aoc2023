#!/usr/bin/python3

import sys
from day5lib import decode_almanac, get_location, get_seed, get_location_range

# This solution takes many hours to run.
def find_lowest_location_brute_force(almanac):
    num_seeds = sum(v for i, v in enumerate(almanac['seeds']) if i % 2 == 1)
    done_seeds = 0
    min_location = -1
    i = 0
    while i < len(almanac['seeds']):
        start = almanac['seeds'][i]
        length = almanac['seeds'][i+1]
        i += 2
        for seed in range(start, start + length):
            if done_seeds % 100000 == 0:
                sys.stderr.write("{} / {} ({:.2f}%)\n".format(done_seeds, num_seeds, 100.0 * done_seeds / num_seeds))
            location = get_location(seed, almanac['maps'])
            if min_location == -1 or location < min_location:
                min_location = location
            done_seeds += 1

def has_seed(seeds, seed):
    i = 0
    while i < len(seeds):
        start = seeds[i]
        length = seeds[i+1]
        if seed >= start and seed <= start + length:
            return True
        i += 2

    return False

# The reverse brute force is faster, only taking 47 seconds.
def find_lowest_location_reverse_brute_force(almanac):
    seeds, maps = almanac['seeds'], almanac['maps']

    i = 0
    while i < 2000000000:
        if i % 100000 == 0:
            sys.stderr.write("{}\n".format(i))
        seed = get_seed(i, maps)
        if has_seed(seeds, seed):
            return i
        i += 1

# The smartest solution that keeps the ranges together, breaking them down
# as they get separated by the mapping. 22ms
def find_lowest_location(almanac):
    seeds, maps = almanac['seeds'], almanac['maps']

    min_location = -1
    for start, length in zip(seeds[::2], seeds[1::2]):
        location_ranges = get_location_range(start, length, maps)
        new_min = min(s for s, l in location_ranges)
        if min_location == -1 or new_min < min_location:
            min_location = new_min

    return min_location

def main():
    if len(sys.argv) == 1:
        almanac = decode_almanac(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            almanac = decode_almanac(f)

    print(find_lowest_location(almanac))

if __name__ == '__main__':
    main()
