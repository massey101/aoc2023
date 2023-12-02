#!/usr/bin/python3

import sys
from day2lib import decode_game

def game_filter(game):
    for draw in game['draws']:
        if (draw['red'] > 12 or draw['green'] > 13 or draw['blue'] > 14):
            return False

    return True


def main():
    games = [decode_game(line) for line in sys.stdin]
    filtered_games = [game for game in games if game_filter(game)]
    total = sum(g['id'] for g in filtered_games)
    print(total)

if __name__ == '__main__':
    main()
