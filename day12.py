import multiprocessing
import time
from itertools import combinations, repeat
from numba import jit, cuda
import threading
from typing import Any

import numpy
from aocd import get_data
from aocd.post import submit

states = {}


def process(sequence, blocks, position=0, block=0, damaged=0) -> int:
    if (position, block, damaged) in states:
        return states[position, block, damaged]

    # On end of sequence
    if position == len(sequence):
        # No more blocks -> ###.
        if block == len(blocks) and damaged == 0:
            return 1
        # On last block -> ###
        if block == len(blocks) - 1 and damaged == blocks[block]:
            return 1

        return 0

    result = 0
    # On '#'
    if sequence[position] == '#':
        result = process(sequence, blocks, position + 1, block, damaged + 1)

    # On '.'
    elif sequence[position] == '.':
        # ##. [(2), 3]
        if damaged > 0:
            if block < len(blocks) and damaged == blocks[block]:
                result = process(sequence, blocks, position + 1, block + 1, 0)
        # ..
        else:
            result = process(sequence, blocks, position + 1, block, 0)

    # On '?'
    else:
        # -> ##? [(2), 3]
        if damaged > 0:
            if block < len(blocks) and damaged == blocks[block]:
                result = process(sequence, blocks, position + 1, block + 1, 0)
            else:
                result = process(sequence, blocks, position + 1, block, damaged + 1)

        # -> .?
        else:
            if block == len(blocks):
                result = process(sequence, blocks, position + 1, block, 0)
            else:
                result = process(sequence, blocks, position + 1, block, damaged + 1) + process(sequence, blocks, position + 1, block, 0)

    states[(position, block, damaged)] = result
    return result


def main():
    data = get_data(day=12).split('\n')
    # data = open('test').read().split('\n')

    answer = 0

    for line in data:
        states.clear()
        sequence, blocks = line.split(' ')
        blocks = list(map(int, blocks.split(',')))
        result = process(sequence, blocks, damaged=0)
        answer += result
        print(sequence, blocks, result)

    print(int(answer))
    submit(int(answer))


if __name__ == '__main__':
    main()
