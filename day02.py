from collections import defaultdict

from aocd import get_data
from aocd.post import submit


def main():
    data = get_data().split('\n')
    # data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split('\n')

    reds = 12
    greens = 13
    blues = 14
    answer = 0

    for line in data:
        max_red = 0
        max_blue = 0
        max_green = 0

        parts = line.split(' ')[2:]
        game_id = line.split(' ')[1].replace(":", '')
        for i in range(0, len(parts) - 1, 2):
            if 'red' in parts[i + 1]:
                max_red = max(int(parts[i]), max_red)

            if 'blue' in parts[i + 1]:
                max_blue = max(int(parts[i]), max_blue)

            if 'green' in parts[i + 1]:
                max_green = max(int(parts[i]), max_green)

        answer += max_red * max_blue * max_green

    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
