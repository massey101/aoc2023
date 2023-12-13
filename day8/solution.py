#!/usr/bin/python3

import sys
import functools
from math import gcd

DEBUG = False

def decode_map(lines):
    directions, nodes = lines.read().strip().split('\n\n')

    decoded_nodes = {}
    for node in nodes.split('\n'):
        node_name, node_directions = [v.strip() for v in node.split('=')]
        node_directions = [v.strip().strip(')').strip('(') for v in node_directions.split(',')]
        decoded_nodes[node_name] = (node_directions[0], node_directions[1])

    return directions, decoded_nodes

def lcm(numbers):
    lcm = 1
    for i in numbers:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

def get_distance_to_z(directions, nodes, node):
    steps = 0
    should_not_break = True
    while True:
        for direction in directions:
            if direction == 'L':
                node = nodes[node][0]
            if direction == 'R':
                node = nodes[node][1]
            steps += 1

            if node.endswith('Z'):
                return steps

def part2(directions, nodes):
    start_nodes = [n for n in nodes.keys() if n.endswith('A')]
    distances = []
    for start_node in start_nodes:
        distances.append(get_distance_to_z(directions, nodes, start_node))

    return lcm(distances)

def part1(directions, nodes):
    node = 'AAA'
    end = 'ZZZ'
    steps = 0
    while node != end:
        if steps > 10000000:
            raise ValueError('ZZZ Not found')
        for direction in directions:
            if direction == 'L':
                node = nodes[node][0]
            if direction == 'R':
                node = nodes[node][1]
            steps += 1

    return steps

def main():
    if len(sys.argv) == 1:
        directions, nodes = decode_map(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            directions, nodes = decode_map(f)

    print(part1(directions, nodes))
    print(part2(directions, nodes))

if __name__ == '__main__':
    main()
