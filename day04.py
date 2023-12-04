from collections import defaultdict

from aocd import get_data
from aocd.post import submit
import numpy as np


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    answer = 0
    cards = defaultdict(int)
    original = []
    to_process = np.empty(0)

    for line in data:
        count = 0
        # points = 0
        winning, numbers = line.split('|')

        card = int([x for x in winning.strip().split(' ') if x != ''][1].split(':')[0])
        print(card)
        winning = [x for x in winning.strip().split(' ') if x != ''][2:]
        numbers = [x for x in numbers.strip().split(' ') if x != '']
        original.append({'card': card, 'winnings': winning, 'numbers': numbers})
        cards[card] += 1

        for number in numbers:
            if number != '' and number in winning:
                count += 1
                # if points == 0:
                #     points = 1
                # else:
                #     points *= 2

        # answer += points

        for i in range(count):
            to_process = np.append(to_process, card + i + 1)

        card_count = np.count_nonzero(to_process == card)
        cards[card] += card_count

        to_append = [card + i + 1 for i in range(count)]
        to_process = np.append(to_process, to_append * card_count)
        to_process = to_process[to_process != card]

    answer = sum(cards.values())
    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
