import multiprocessing
import time
from itertools import combinations, repeat
from numba import jit, cuda
import threading
from typing import Any

import numpy
from aocd import get_data
from aocd.post import submit


def count_combinations(conditions: str, status: str) -> int:
    result_needed = list(map(int, status.split(',')))
    total_broken = sum(result_needed)
    known_broken = conditions.count('#')
    unknown = conditions.count('?')
    need_to_put_periods = unknown - (total_broken - known_broken)
    need_to_put_broken = total_broken - known_broken

    replacement_one = '#'
    replacement_two = '.'
    need_to_put = need_to_put_broken

    if 0 < need_to_put_periods < need_to_put_broken:
        replacement_one = '.'
        replacement_two = '#'
        need_to_put = need_to_put_periods

    indices = [index for index in list(range(len(conditions))) if conditions[index] == '?']
    index_combinations: combinations = combinations(indices, need_to_put)

    count = 0
    for combo in index_combinations:
        temp_string = numpy.array(list(conditions))

        for index in combo:
            temp_string[index] = replacement_one

        result = [broken.count('#') for broken in ''.join(temp_string).replace('?', replacement_two).split('.') if broken]

        if result_needed == result:
            count += 1

    return count


def process_line(line: str) -> float:
    conditions, status = line.split(' ')
    result_one: int = count_combinations(conditions, status)

    if conditions[-1] == '#' or conditions[-1] == '?':
        conditions: str = '?'.join(repeat(conditions, 2))
        status: str = ','.join(repeat(status, 2))
        result_two: int = count_combinations(conditions, status)
        print('Done')
        return ((result_two / result_one) ** 4) * result_one

    else:
        conditions: str = '?' + conditions
        end_result: int = count_combinations(conditions, status)
        print('Done')
        return (end_result ** 4) * result_one


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    start_time = time.time()

    answer = 0

    with multiprocessing.Pool() as p:
        for result in p.map(process_line, reversed(data)):
            answer += result

    print(int(answer))
    print("--- %s seconds ---" % (time.time() - start_time))
    # submit(int(answer))


if __name__ == '__main__':
    main()
