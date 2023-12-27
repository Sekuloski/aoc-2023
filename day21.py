from aocd import get_data
from aocd.post import submit


def main():
    data = get_data(day=21).split('\n')
    # data = open('test').read().split('\n')

    answer = 0

    start = (0, 0)
    for y in range(len(data)):
        if 'S' in data[y]:
            start = (data[y].index('S'), y)

    visited = []
    to_check = [start]
    for i in range(64):
        current = []
        temp = []
        for position in to_check:
            for direction in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                new_position = (position[0] + direction[0], position[1] + direction[1])
                if 0 > new_position[0] or new_position[0] >= len(data[0]) or 0 > new_position[1] or new_position[1] >= len(data):
                    continue

                if data[new_position[1]][new_position[0]] == '#':
                    continue

                current.append(new_position)
                if new_position not in visited:
                    visited.append(new_position)
                    temp.append(new_position)

                    if i % 2 == 1:
                        answer += 1

        to_check = temp.copy()

    print(answer)
    submit(answer, day=21)


if __name__ == '__main__':
    main()
