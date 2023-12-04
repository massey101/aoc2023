#!/usr/bin/python3

numbers = '0123456789'

def get_number_length(line):
    length = 0
    for char in line:
        if char not in numbers:
            break
        length += 1

    return length

def get_adjacent_symbols(lines, num_i, num_j, number_length):
    end_i = min(num_i + 1, len(lines) - 1)
    i = max(num_i - 1, 0)

    symbols = []

    while i <= end_i:
        line = lines[i]
        end_j = min(num_j + number_length, len(line) - 1)
        j = max(num_j - 1, 0)
        while j <= end_j:
            if line[j] not in numbers and line[j] != '.':
                symbols.append({
                    'symbol': line[j],
                    'location': (i, j),
                })
            j += 1


        i += 1

    return symbols

def get_engine_parts(lines):
    parts = []

    for i in range(len(lines)):
        line = lines[i]
        j = 0
        while j < len(line):
            number_length = get_number_length(line[j:])
            if number_length == 0:
                j += 1
                continue

            symbols = get_adjacent_symbols(lines, i, j, number_length)
            if len(symbols) > 0:
                parts.append({
                    'serial_number': int(line[j:j+number_length]),
                    'symbols': symbols,
                })

            j += number_length

    return parts
