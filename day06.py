import threading
from collections import defaultdict

from aocd import get_data
from aocd.post import submit


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    answer = 0
    time = int(''.join(list(map(str, data[0].strip().split()[1:]))))
    distance = int(''.join(list(map(str, data[1].strip().split()[1:]))))

    for i in range(1, time + 1):
        total_distance = i * (time - i)
        if total_distance > distance:
            answer += 1

    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
