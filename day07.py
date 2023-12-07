from collections import defaultdict

from aocd import get_data
from aocd.post import submit


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    all_hands = {
        'High': [],
        'One': [],
        'Two': [],
        'Three': [],
        'Full': [],
        'Four': [],
        'Five': []
    }
    replace_dict = {
        'A': 'E',
        'K': 'D',
        'Q': 'C',
        'J': 'B',
        'T': 'A',
    }
    bids = {}

    for line in data:
        hand, bid = line.split()
        hand_with_J = hand
        hand_without_J = hand

        for initial, new in replace_dict.items():
            if initial != 'J':
                hand_with_J = hand_with_J.replace(initial, new)
            hand_without_J = hand_without_J.replace(initial, new)

        hand = hex(int(hand_without_J.upper().replace('B', '1'), 16))[2:]
        all_hands[get_type(hand_with_J)].append(hand)
        bids[hand] = int(bid)

    for hand_type in all_hands.keys():
        all_hands[hand_type] = sorted(all_hands[hand_type])

    answer = 0

    rank = 1
    for hand_type, hands in all_hands.items():
        for hand in hands:
            answer += rank * bids[hand]
            rank += 1

    submit(answer)


def get_type(hand: str):
    if len(set(hand)) == 1:
        'AAAAA'
        'JJJJJ'
        return 'Five'

    if len(set(hand)) == 5:
        if hand.count('J') == 1:
            '2345J'
            return 'One'

        return 'High'

    if len(set(hand)) == 4:
        '23455'
        if hand.count('J') == 1:
            '23J55'
            return 'Three'

        if hand.count('J') == 2:
            '234JJ'
            return 'Three'

        return 'One'

    if len(set(hand)) == 3:
        '23444'
        '23344'
        '23JJJ'
        '233JJ'
        '2J444'
        '2JJ44'
        '2JJJ4'
        'J3444'
        'J3344'
        for number in sorted([hand.count(c) for c in set(hand)], reverse=True):
            if number >= 3:
                if hand.count('J') == 1:
                    'J3444'
                    return 'Four'

                if hand.count('J') == 3:
                    '43JJJ'
                    return 'Four'

                return 'Three'

            elif number >= 2:
                '23344'

                if hand.count('J') == 1:
                    'J3344'
                    return 'Full'

                if hand.count('J') == 2:
                    'JJ344'
                    return 'Four'

                return 'Two'

    if len(set(hand)) == 2:
        for number in sorted([hand.count(c) for c in set(hand)], reverse=True):
            if number >= 4:
                '34444'

                if hand.count('J') == 1:
                    'J4444'
                    return 'Five'

                if hand.count('J') == 4:
                    '4JJJJ'
                    return 'Five'

                return 'Four'

            elif number >= 3:
                '33444'

                if hand.count('J') == 2:
                    'JJ444'
                    return 'Five'

                if hand.count('J') == 3:
                    '33JJJ'
                    return 'Five'

                return 'Full'


if __name__ == '__main__':
    main()
