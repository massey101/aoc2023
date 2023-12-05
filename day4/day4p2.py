#!/usr/bin/python3

import sys
from day4lib import process_cards, calculate_matches

def run_game(cards):
    for card in cards:
        matches = calculate_matches(card)
        for j in range(card['number'] + 1, card['number'] + matches + 1):
            newCard = next(c for c in cards if c['number'] == j)
            for duplicate in range(card['duplicates'] + 1):
                newCard['duplicates'] += 1


def main():
    if len(sys.argv) == 1:
        cards = process_cards(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            cards = process_cards(f)

    run_game(cards)
    print(sum(c['duplicates'] + 1 for c in cards))

if __name__ == '__main__':
    main()
