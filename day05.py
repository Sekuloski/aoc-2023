from collections import defaultdict

import numpy
import numpy as np
from aocd import get_data
from aocd.post import submit


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    seeds_map = list(map(int, data[0].split(' ')[1:]))
    final_range = [(seeds_map[new_range], seeds_map[new_range] + seeds_map[new_range + 1]) for new_range in range(0, len(seeds_map), 2)]
    print(final_range)

    maps = {}
    current_map = ''
    current_ranges = []

    for line in data[2:]:
        if line == '':
            maps[current_map] = current_ranges
            current_ranges = []
            continue

        if line.endswith('map:'):
            current_map = line.split(' ')[0]
            continue

        current_ranges.append(list(map(int, line.split(' '))))

    maps[current_map] = current_ranges

    for original_location in range(4265193, 1000000000):
        new_location = original_location
        for range_object in maps['humidity-to-location']:
            # (60 56 93)
            if range_object[0] <= new_location <= range_object[0] + range_object[2]:
                new_location = new_location - (range_object[0] - range_object[1])
                # print(original_location, new_location)
                break

        for mapping in reversed(list(maps.keys())[:-1]):
            for secondary_range_object in maps[mapping]:
                destination_range = secondary_range_object[1]
                source_range = secondary_range_object[0]
                count = secondary_range_object[2]

                if source_range <= new_location <= source_range + count:
                    # print(original_location, new_location, source_range, source_range + count, destination_range, mapping)
                    new_location = new_location - (source_range - destination_range)

                    if 'seed' in mapping:
                        for new_range in final_range:
                            if new_range[0] <= new_location <= new_range[1]:
                                print(original_location, new_location, new_range[0], new_range[1])
                                exit()

                    break


if __name__ == '__main__':
    main()
