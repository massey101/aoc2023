#!/usr/bin/python3

import sys

digits = '0123456789'

calibration_values = []

with open(sys.argv[1]) as f:
    for line in f:
        foundDigits = []

        for char in line:
            for num, digit in enumerate(digits):
                if char == digit:
                    foundDigits.append(num)

        if len(foundDigits) == 0:
            raise ValueError("Digits not found")

        calibration_values.append(foundDigits[0] * 10 + foundDigits[-1])

print(sum(calibration_values))
