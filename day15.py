from collections import defaultdict

from aocd import get_data
from aocd.post import submit


def main():
    data = get_data().split(',')
    # data = open('test').read().split(',')

    answer = 0
    boxes = defaultdict(dict)
    for word in data:
        box = 0

        if '-' in word:
            label = word.split('-')[0]
        else:
            label = word.split('=')[0]

        for c in label:
            box += ord(c)
            box *= 17
            box %= 256

        if '-' in word:
            if label in boxes[box]:
                del boxes[box][label]
        else:
            boxes[box][label] = word[-1]

    for box, values in boxes.items():
        position = 1
        for label, value in values.items():
            answer += (box + 1) * position * int(value)
            position += 1

    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
