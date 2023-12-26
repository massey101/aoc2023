#!/usr/bin/python3

import sys

def decode_step(step):
    put = step.split('=')
    if len(put) == 2:
        return '=', put[0], int(put[1])
    return '-', step.split('-')[0], 0

def decode_puzzle(lines):
    line = lines.read().strip().split('\n')[0]
    steps = line.split(',')
    decoded_steps = [decode_step(s) for s in steps]
    return steps, decoded_steps

def HASH(data: str) -> int:
    data = data.encode('utf8')
    result = 0
    for c in data:
        result += c
        result = (result * 17) % 256

    return result


def part1(puzzle):
    steps, _ = puzzle
    return sum(HASH(step) for step in steps)

def insert_lens(boxes, label, focal_length):
    box = boxes[HASH(label)]
    try:
        index = [l[0] for l in box].index(label)
        box[index] = (label, focal_length)
    except ValueError:
        box.append((label, focal_length))

def remove_lens(boxes, label):
    box = boxes[HASH(label)]
    try:
        index = [l[0] for l in box].index(label)
        box.pop(index)
    except ValueError:
        pass

def get_focusing_power(boxes):
    return sum(
        (box+1) * (i+1) * lense[1]
        for box, lenses in boxes.items()
        for i, lense in enumerate(lenses)
    )

def part2(puzzle):
    _, steps = puzzle
    boxes = {i: list() for i in range(256)}
    for step in steps:
        operation, label, focal_length = step

        if operation == '=':
            insert_lens(boxes, label, focal_length)
        else:
            remove_lens(boxes, label)

    return get_focusing_power(boxes)

def main():
    if len(sys.argv) == 1:
        puzzle = decode_puzzle(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            puzzle = decode_puzzle(f)

    print(part1(puzzle))
    print(part2(puzzle))

if __name__ == '__main__':
    main()
