from collections import defaultdict
from itertools import combinations, repeat

import numpy
from aocd import get_data
from aocd.post import submit


def main(repetitions):
    data = get_data().split('\n')
    # data = open('test').read().split('\n')
    distances = 0
    data = edit_data(data, repetitions)
    galaxies = set()

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                galaxies.add((x, y))

    pairs = list(combinations(galaxies, 2))

    for pair in pairs:
        distances += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

    return distances


def edit_data(data, repetitions):
    new_data = numpy.empty(0)
    for y in range(len(data)):
        if '#' not in data[y]:
            new_data = numpy.append(new_data, list(repeat(data[y], repetitions)))
        else:
            new_data = numpy.append(new_data, data[y])
    data = [''.join(column).rstrip() for column in zip(*new_data)]
    new_data = numpy.empty(0)
    for y in range(len(data)):
        if '#' not in data[y]:
            new_data = numpy.append(new_data, list(repeat(data[y], repetitions)))
        else:
            new_data = numpy.append(new_data, data[y])

    return [''.join(column).rstrip() for column in zip(*new_data)]


if __name__ == '__main__':
    one = main(1)
    two = main(2)
    difference = two - one
    multiplier = 1000000
    answer = one + (difference * (multiplier - 1))

    print(answer)
    submit(answer)
