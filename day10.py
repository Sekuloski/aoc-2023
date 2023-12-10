from collections import defaultdict

from aocd import get_data
from aocd.post import submit


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    possible_directions = {
        '7': ((-1, 0), (0, 1)),
        'F': ((1, 0), (0, 1)),
        'J': ((-1, 0), (0, -1)),
        'L': ((1, 0), (0, -1)),
        '-': ((1, 0), (-1, 0)),
        '|': ((0, 1), (0, -1)),
        'S': ((0, 1), (0, -1), (1, 0), (-1, 0))
    }
    possible_pipes = {
        # Looking up
        (0, -1): ('7', '|', 'F', 'S'),
        # Looking Down
        (0, 1): ('L', '|', 'J', 'S'),
        # Looking Right
        (1, 0): ('J', '-', '7', 'S'),
        # Looking Left
        (-1, 0): ('L', '-', 'F', 'S'),
    }
    opposites = {
        (0, -1): (0, 1),
        (0, 1): (0, -1),
        (1, 0): (-1, 0),
        (-1, 0): (1, 0),
    }

    count = 0
    start = (0, 0)
    for line in data:
        if 'S' in line:
            start = (line.index('S'), count)
        count += 1

    current_pipe = 'S'
    current_x = start[0]
    current_y = start[1]
    came_from = (0, 0)
    loop = set()

    while True:
        loop.add((current_x, current_y))
        if data[current_y][current_x] == 'S' and came_from != (0, 0):
            print(loop)
            print(len(loop))
            answer = len(loop) // 2
            break

        found = 0
        for direction in possible_directions[current_pipe]:
            try:
                if data[current_y + direction[1]][current_x + direction[0]] in possible_pipes[direction]:
                    if came_from != direction:
                        came_from = opposites[direction]
                        current_x = current_x + direction[0]
                        current_y = current_y + direction[1]
                        current_pipe = data[current_y][current_x]
                        found += 1

            except IndexError:
                continue

    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
