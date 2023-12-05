#!/usr/bin/python3

import sys
from day4lib import process_cards, calculate_matches

def get_points(matches):
    if matches == 0:
        return 0
    return 2 ** (matches - 1)

def main():
    if len(sys.argv) == 1:
        cards = process_cards(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            cards = process_cards(f)

    print(sum(get_points(calculate_matches(card)) for card in cards))

if __name__ == '__main__':
    main()
