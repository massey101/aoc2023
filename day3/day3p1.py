#!/usr/bin/python3

import sys
from day3lib import get_engine_parts

def main():
    if len(sys.argv) == 1:
        lines = [line.strip() for line in sys.stdin]
    else:
        lines = []
        with open(sys.argv[1]) as f:
            for line in f:
                lines.append(line.strip())

    parts = get_engine_parts(lines)
    print(sum(p['serial_number'] for p in parts))

if __name__ == '__main__':
    main()
