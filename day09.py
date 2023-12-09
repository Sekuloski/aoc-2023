from collections import defaultdict

from aocd import get_data
from aocd.post import submit


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    answer = 0

    for line in data:
        inputs = list(map(int, line.split()))
        last_values = [inputs[-1]]
        first_values = [inputs[0]]
        sequence = inputs.copy()
        new_seq = []
        flag = True
        while flag:
            flag = False
            for i in range(len(sequence) - 1):
                difference = sequence[i + 1] - sequence[i]
                new_seq.append(difference)

                if difference != 0:
                    flag = True

            # last_values.append(new_seq[-1])
            first_values.append(new_seq[0])
            sequence = new_seq.copy()
            new_seq.clear()

        # answer += sum(last_values)
        new_sum = 0
        for value in reversed(first_values):
            new_sum = value - new_sum

        # print(first_values)
        answer += new_sum
        last_values.clear()
        first_values.clear()

    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
