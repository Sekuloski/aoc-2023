from collections import defaultdict

from aocd import get_data
from aocd.post import submit


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    answer = 0
    number = ''
    gears = defaultdict(list)

    for y, line in enumerate(data):
        number_x = -1
        number_y = -1
        for i, c in enumerate(line + '.'):
            if c.isdigit():
                if number_x == -1:
                    number_x = int(i)
                    number_y = int(y)

                number += c

            elif number != '':
                stop = False
                for y1 in range(max(0, number_y-1), min(len(data), number_y + 2)):
                    if stop:
                        break
                    for x1 in range(max(0, number_x-1), min(len(line), len(number) + number_x + 1)):
                        if data[y1][x1] not in '.0123456789':
                            # answer += int(number)

                            if data[y1][x1] == '*':
                                gears[f'{x1},{y1}'].append(number)

                            stop = True
                            break

                number = ''
                number_x = -1
                number_y = -1

    for gear, numbers in gears.items():
        if len(numbers) == 2:
            answer += int(numbers[0]) * int(numbers[1])
            print(numbers)

    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
