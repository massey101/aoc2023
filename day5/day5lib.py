import sys

class Map():

    def __init__(self):
        self.registers = []

    def decode_line(self, line):
        destination, source, length = [int(v) for v in line.split()]

        self.registers.append({
            'destination': destination,
            'source': source,
            'length': length,
        })

    #   IN:                |----------------------------|
    #  MAP: |-----------|
    #  OUT:                |----------------------------|
    #                                   end
    #
    #   IN:        |------------------------------------|
    #  MAP: |--------------|
    #  OUT:        |-------|----------------------------|
    #                mid                end
    #
    #   IN: |----------------------------------|
    #  MAP:                       |-----------------|
    #  OUT: |---------------------|------------|
    #                start           mid
    #
    #   IN:        |----------------------------|
    #  MAP:                 |-----------|
    #  OUT:        |--------|-----------|-------|
    #                 start     mid        end
    #
    #   IN:        |----------------------------|
    #  MAP: |------------------------------------------|
    #  OUT:        |----------------------------|
    #                           mid
    def apply_mapping_range(self, start, length, mapping):
        start_range = None
        mid_range = None
        end_range = None
        end = start + length
        mstart = mapping['source']
        mend = mapping ['source'] + mapping['length']

        result = []
        if end <= mstart:
            return (start, length), None, None

        if start >= mend:
            return None, None, (start, length)

        if start < mstart:
            start_range = (start, mstart - start)
            length = length - (mstart - start)
            start = mstart

        if end > mend:
            end_range = (mend, end - mend)
            length = length - (end - mend)

        mid_range = (start - mstart + mapping['destination'], length)

        return start_range, mid_range, end_range

    def source_to_destination_range(self, start, length):
        return_ranges = [(start, length)]
        done_ranges = []
        end = start + length

        for mapping in self.registers:
            new_ranges = []
            for return_range in return_ranges:
                start, mid, end = self.apply_mapping_range(return_range[0], return_range[1], mapping)
                if start is not None:
                    new_ranges.append(start)
                if mid is not None:
                    done_ranges.append(mid)
                if end is not None:
                    new_ranges.append(end)

            return_ranges = new_ranges

        return_ranges.extend(done_ranges)
        return return_ranges

    def source_to_destination(self, source):
        for register in self.registers:
            if source >= register['source'] and source < register['source'] + register['length']:
                return source - register['source'] + register['destination']
        return source

    def destination_to_source(self, destination):
        for register in self.registers:
            if destination >= register['destination'] and destination < register['destination'] + register['length']:
                return destination - register['destination'] + register['source']
        return destination


def decode_almanac(lines):
    seeds = []
    mode = 'seeds'
    maps = {}
    for line in lines:
        line = line.strip()
        if mode == 'seeds':
            seeds = [int(v) for v in line.split(':')[1].split()]
            mode = 'unknown'
            continue

        if mode == 'unknown':
            if line == '':
                continue
            if line.endswith(' map:'):
                mode = line.split()[0]
                maps[mode] = Map()
                continue
            raise ValueError()

        if line == "":
            mode = 'unknown'
            continue

        maps[mode].decode_line(line)
    return {
        'seeds': seeds,
        'maps': maps,
    }

def get_location(seed, maps):
    map_order = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location',
    ]
    mapped_value = seed
    for map_to_apply in map_order:
        mapped_value = maps[map_to_apply].source_to_destination(mapped_value)

    return mapped_value

_map_order = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location',
]

def get_location_range(start, length, maps, map_order=None):
    if map_order == None:
        map_order = _map_order

    if len(map_order) == 0:
        return [(start, length)]

    map_to_apply = map_order[0]

    new_ranges = maps[map_to_apply].source_to_destination_range(start, length)
    return_ranges = []
    for new_range in new_ranges:
        return_ranges.extend(get_location_range(new_range[0], new_range[1], maps, map_order[1:]))

    return return_ranges


def get_seed(location, maps):
    map_order = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location',
    ]
    mapped_value = location
    for map_to_apply in reversed(map_order):
        mapped_value = maps[map_to_apply].destination_to_source(mapped_value)

    return mapped_value
