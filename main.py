from aocd import get_data
from aocd.post import submit


digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def main():
    data = get_data().split('\n')
#     data = """two1nine
# eightwoeight
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".split('\n')

    answer = 0
    first_digit = 0
    first_flag = False
    last_digit = 0
    original = {}

    for line in data:
        print(line)
        text_digits = []

        for digit in digits:
            if digit in line:
                original[line.index(digit)] = digit
                original[line.rindex(digit)] = digit

        text_digits = [x[1] for x in sorted(original.items(), key=lambda x: x[0])]
        print(original)

        if not text_digits:
            for character in line:
                if first_digit == 0 and character.isnumeric():
                    first_digit = character

                if character.isnumeric():
                    last_digit = character

        else:
            for character in line.split(text_digits[0])[0]:
                if not first_flag and character.isnumeric():
                    first_digit = character
                    first_flag = True

            for character in line.split(text_digits[-1])[-1]:
                if character.isnumeric():
                    last_digit = character

        if first_digit == 0:
            first_digit = digits.index(text_digits[0]) + 1

        if last_digit == 0:
            last_digit = digits.index(text_digits[-1]) + 1

        print(text_digits)
        print(first_digit, last_digit)
        print()
        answer += int(str(first_digit) + str(last_digit))
        first_digit = 0
        last_digit = 0
        first_flag = False
        original.clear()

    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
