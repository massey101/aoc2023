#!/usr/bin/python3

import sys
import functools

DEBUG = False

def decode_hands(lines):
    lines = lines.read().strip().split('\n')

    return [(line.split()[0], int(line.split()[1])) for line in lines]

def get_hand_type(hand):
    # Five of a kind
    num = 0
    for card in hand:
        if card == hand[0]:
            num += 1
    if num == 5:
        return 0

    # Four of a kind
    for card in hand:
        num = 0
        for c in hand:
            if card == c:
                num += 1
        if num == 4:
            return 1

    # Full house
    # Three of a kind
    for card in hand:
        num = 0
        for c in hand:
            if card == c:
                num += 1
        if num == 3:
            other_cards = [c for c in hand if c != card]
            if other_cards[0] == other_cards[1]:
                return 2
            return 3

    # Two pair
    pairs = 0
    for card in hand:
        num = 0
        for c in hand:
            if card == c:
                num += 1
        if num == 2:
            pairs += 1

    pairs = pairs / 2
    if pairs == 2:
        return 4

    # One pair
    if pairs == 1:
        return 5

    # High card
    return 6

cards = 'AKQJT98765432'

def compare_hands(h1, h2):
    t1 = get_hand_type(h1[0])
    t2 = get_hand_type(h2[0])
    if t1 != t2:
        return t2 - t1
    for c1, c2 in zip(h1[0], h2[0]):
        if c1 != c2:
            return cards.index(c2) - cards.index(c1)

    return 0


def get_hand_type_part2(hand):
    # Five of a kind
    for card in hand:
        num = 0
        for c in hand:
            if card == c or c == 'J':
                num += 1
        if num == 5:
            return 0

    # Four of a kind
    for card in hand:
        num = 0
        for c in hand:
            if card == c or c == 'J':
                num += 1
        if num == 4:
            return 1

    # Full house
    # Three of a kind
    for card in hand:
        num = 0
        for c in hand:
            if card == c or c == 'J':
                num += 1
        if num == 3:
            other_cards = [c for c in hand if c != card and c != 'J']
            if other_cards[0] == other_cards[1]:
                return 2
            return 3

    # Two pair
    pairs = 0
    for card in hand:
        num = 0
        for c in hand:
            if card == c or c == 'J':
                num += 1
        if num == 2:
            pairs += 1

    num_js = len([c for c in hand if c == 'J'])
    if num_js > 0:
        pairs = pairs / (2 * num_js)
    pairs = pairs / 2

    if pairs == 2:
        return 4

    # One pair
    if pairs == 1:
        return 5

    # High card
    return 6

cardsp2 = 'AKQT98765432J'

def compare_hands_part2(h1, h2):
    t1 = get_hand_type_part2(h1[0])
    t2 = get_hand_type_part2(h2[0])
    if t1 != t2:
        return t2 - t1
    for c1, c2 in zip(h1[0], h2[0]):
        if c1 != c2:
            return cardsp2.index(c2) - cardsp2.index(c1)

    return 0

def human_readable_type(hand_type):
    return [
        "Five of a kind",
        "Four of a kind",
        "Full house",
        "Three of a kind",
        "Two pair",
        "One pair",
        "High card",
    ][hand_type]



def part2(hands):
    hands = [h for h in hands]
    hands = sorted(hands, key=functools.cmp_to_key(compare_hands_part2))
    if DEBUG:
        for h in hands:
            sys.stderr.write("{} {}\n".format(h[0], human_readable_type(get_hand_type_part2(h[0]))))
    return sum((i+1) * h[1] for i, h in enumerate(hands))


def part1(hands):
    hands = [h for h in hands]
    hands = sorted(hands, key=functools.cmp_to_key(compare_hands))
    if DEBUG:
        for h in hands:
            sys.stderr.write("{} {}\n".format(h[0], human_readable_type(get_hand_type_part2(h[0]))))
    return sum((i+1) * h[1] for i, h in enumerate(hands))

def main():
    if len(sys.argv) == 1:
        hands = decode_hands(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            hands = decode_hands(f)

    print(part1(hands))
    print(part2(hands))

if __name__ == '__main__':
    main()
