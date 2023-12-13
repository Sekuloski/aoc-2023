from collections import defaultdict

from aocd import get_data
from aocd.post import submit
import difflib


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')
    data.append('')
    answer = 0

    current = []

    for line in data:
        if line == '':
            transposed_list = list(map(list, zip(*current)))
            rotated_list = [''.join(row) for row in transposed_list]
            found = False
            for i in range(len(rotated_list) - 1):
                temp = 0
                try:
                    for j in range(i + 1):
                        temp += sum(1 for a, b in zip(rotated_list[i - j], rotated_list[j + i + 1]) if a != b)
                        if temp > 1:
                            break

                        found = True
                except:
                    pass

                if temp == 1 and found:
                    answer += i + 1
                    print(f'Vertical: {i + 1}')
                    break

                found = False

            for i in range(len(current) - 1):
                temp = 0
                found = False
                try:
                    for j in range(i + 1):
                        temp += sum(1 for a, b in zip(current[i - j], current[j + i + 1]) if a != b)
                        if temp > 1:
                            break
                        found = True

                except:
                    pass

                if temp == 1 and found:
                    horizontal_count = i + 1
                    answer += horizontal_count * 100
                    print(f'Horizontal: {i + 1}')

            print()
            current = []
        else:
            current.append(line)

    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
