import sys

def process_cards(lines):
    cards = []
    for line in lines:
        line = line.strip()
        line_split = line.split(':')
        card_number = int(line_split[0].split()[1])
        numbers = line_split[1].strip()
        winning_numbers = [int(n) for n in numbers.split('|')[0].strip().split()]
        my_numbers = [int(n) for n in numbers.split('|')[1].strip().split()]
        cards.append({
            'number': card_number,
            'my_numbers': my_numbers,
            'winning_numbers': winning_numbers,
            'duplicates': 0,
        })

    return cards

def calculate_matches(card):
    matches = 0

    for number in card['my_numbers']:
        if number in card['winning_numbers']:
            matches += 1

    return matches
