#!/usr/bin/python3

import sys

digits = '0123456789'
digitsspelled = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def searchForDigits(line):
    foundDigits = []

    for i in range(len(line)):
        for num, digit in enumerate(digits):
            if line[i] == digit:
                foundDigits.append(num)

        for num, digit in enumerate(digitsspelled):
            if line[i:min(len(line), i+len(digit))] == digit:
                foundDigits.append(num)

    return foundDigits


calibration_values = []

with open(sys.argv[1]) as f:
    for line in f:
        foundDigits = searchForDigits(line.strip())
        if len(foundDigits) == 0:
            raise ValueError("Digits not found")

        calibration_values.append(foundDigits[0] * 10 + foundDigits[-1])

print(sum(calibration_values))
