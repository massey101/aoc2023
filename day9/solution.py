#!/usr/bin/python3

import sys

def decode_oasis(lines):
    sensors = lines.read().strip().split('\n')

    return [[int(r) for r in s.split()] for s in sensors]

def all_zeros(sensor):
    for reading in sensor:
        if reading != 0:
            return False
    return True

def extrapolate(sensor, reverse=False):
    new_sensor = sensor.copy()
    if all_zeros(sensor):
        if reverse:
            new_sensor.insert(0, 0)
        else:
            new_sensor.append(0)
        return new_sensor

    reading_differences = [sensor[i+1] - sensor[i] for i in range(len(sensor) - 1)]
    reading_differences = extrapolate(reading_differences, reverse)
    if reverse:
        new_sensor.insert(0, new_sensor[0] - reading_differences[0])
    else:
        new_sensor.append(new_sensor[-1] + reading_differences[-1])
    return new_sensor

def part1(oasis):
    new_sensors = []
    for sensor in oasis:
        new_sensors.append(extrapolate(sensor))

    return sum(s[-1] for s in new_sensors)

def part2(oasis):
    new_sensors = []
    for sensor in oasis:
        new_sensors.append(extrapolate(sensor, reverse=True))

    return sum(s[0] for s in new_sensors)

    return 0

def main():
    if len(sys.argv) == 1:
        oasis = decode_oasis(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            oasis = decode_oasis(f)

    print(part1(oasis))
    print(part2(oasis))

if __name__ == '__main__':
    main()
