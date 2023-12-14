import math
from collections import defaultdict
from itertools import repeat

from aocd import get_data
from aocd.post import submit

from day12 import count_combinations


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    answer = 0
    all_states = []
    current_grid = data[::]
    exit_flag = False
    offset = 0

    while True:
        if exit_flag:
            break
        for direction in ('north', 'west', 'south', 'east'):
            result = []
            match direction:
                case 'north':
                    current_grid = list(zip(*current_grid))
                case 'west':
                    current_grid = current_grid[::]
                case 'south':
                    current_grid = list(zip(*current_grid[::-1]))
                case 'east':
                    current_grid = [list(reversed(c)) for c in current_grid]

            for column in current_grid:
                empty = []
                new_column = []
                for i in range(len(column)):
                    new_column.append(column[i])
                    match column[i]:
                        case '.':
                            empty.insert(0, i)
                        case 'O':
                            if empty:
                                new_column[empty.pop()] = 'O'
                                new_column[i] = '.'
                                empty.insert(0, i)
                        case '#':
                            empty.clear()

                result.append(new_column)

            match direction:
                case 'north':
                    current_grid = list(zip(*result))
                case 'west':
                    current_grid = result[::]
                case 'south':
                    current_grid = list(zip(*result))[::-1]
                case 'east':
                    current_grid = [list(reversed(c)) for c in result]

        if current_grid in all_states:
            offset = all_states.index(current_grid)
            all_states = all_states[offset:]
            exit_flag = True

        else:
            all_states.append(current_grid)

    index = (1000000000 - offset - 1) % (len(all_states))
    grid = all_states[index]
    row = len(grid)
    for column in grid:
        column: str
        answer += row * column.count('O')
        row -= 1

    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
