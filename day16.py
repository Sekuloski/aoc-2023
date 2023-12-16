import itertools
from collections import defaultdict
from itertools import repeat
from multiprocessing import Pool

from aocd import get_data
from aocd.post import submit

data = get_data().split('\n')
# data = open('test').read().split('\n')
mapping = {
        '/': {
            # Heading Right
            (1, 0): (0, -1),
            # Heading Left
            (-1, 0): (0, 1),
            # Heading Up
            (0, -1): (1, 0),
            # Heading Down
            (0, 1): (-1, 0)
        },
        '|': {
            # Heading Right
            (1, 0): ((0, -1), (0, 1)),
            # Heading Left
            (-1, 0): ((0, -1), (0, 1)),
        },
        '\\': {
            # Heading Right
            (1, 0): (0, 1),
            # Heading Left
            (-1, 0): (0, -1),
            # Heading Up
            (0, -1): (-1, 0),
            # Heading Down
            (0, 1): (1, 0)
        },
        '-': {
            # Heading Up
            (0, -1): ((-1, 0), (1, 0)),
            # Heading Down
            (0, 1): ((-1, 0), (1, 0))
        }
    }


def main():
    possible_beams = []
    for i in range(len(data[0])):
        if i == 0:
            possible_beams.append([i, 0, (0, 1)])
            possible_beams.append([i, 0, (1, 0)])
        elif i == len(data[0]) - 1:
            possible_beams.append([i, 0, (0, 1)])
            possible_beams.append([i, 0, (-1, 0)])
        else:
            possible_beams.append([i, 0, (0, 1)])

    for i in range(len(data[0])):
        if i == 0:
            possible_beams.append([i, len(data[0]) - 1, (0, -1)])
            possible_beams.append([i, len(data[0]) - 1, (1, 0)])
        elif i == len(data[0]) - 1:
            possible_beams.append([i, len(data[0]) - 1, (0, -1)])
            possible_beams.append([i, len(data[0]) - 1, (-1, 0)])
        else:
            possible_beams.append([i, len(data[0]) - 1, (0, -1)])

    for i in range(len(data)):
        if i == 0:
            possible_beams.append([0, i, (0, 1)])
            possible_beams.append([0, i, (1, 0)])
        elif i == len(data) - 1:
            possible_beams.append([0, i, (0, -1)])
            possible_beams.append([0, i, (1, 0)])
        else:
            possible_beams.append([0, i, (1, 0)])

    for i in range(len(data)):
        if i == 0:
            possible_beams.append([len(data) - 1, i, (0, 1)])
            possible_beams.append([len(data) - 1, i, (-1, 0)])
        elif i == len(data) - 1:
            possible_beams.append([len(data) - 1, i, (0, -1)])
            possible_beams.append([len(data) - 1, i, (-1, 0)])
        else:
            possible_beams.append([len(data) - 1, i, (-1, 0)])

    pool = Pool()
    answer = max(pool.map(process_beams, possible_beams))

    print(answer)
    submit(answer)


def process_beams(beams):
    beams = [beams, ]
    beams_to_remove = []
    field_crossed = [''.join(repeat('.', len(data[0])))] * len(data)
    DP = []
    while True:
        # [print(x) for x in field_crossed]
        [beams.remove(beam) for beam in beams_to_remove]
        beams_to_remove = []

        if len(beams) == 0:
            break

        for beam_i in range(len(beams)):
            beam_x, beam_y, beam_direction = beams[beam_i]
            if beams[beam_i] in DP:
                beams_to_remove.append(beams[beam_i])
                continue
            else:
                DP.append(beams[beam_i].copy())

            if 0 > beam_x or len(data[0]) <= beam_x or 0 > beam_y or len(data) <= beam_y:
                beams_to_remove.append(beams[beam_i])
                continue

            string_list = list(field_crossed[beam_y])
            string_list[beam_x] = '#'
            field_crossed[beam_y] = "".join(string_list)

            mirror = data[beam_y][beam_x]
            if mirror in mapping:
                if mirror in ('-', '|'):
                    if beam_direction in mapping[mirror]:
                        beam_direction_1, beam_direction_2 = mapping[mirror][beam_direction]
                        beams.append(
                            [
                                beams[beam_i][0] + beam_direction_2[0],
                                beams[beam_i][1] + beam_direction_2[1],
                                beam_direction_2
                            ]
                        )

                        beams[beam_i][2] = beam_direction_1
                        beams[beam_i][0] += beam_direction_1[0]
                        beams[beam_i][1] += beam_direction_1[1]
                    else:
                        beams[beam_i][0] += beam_direction[0]
                        beams[beam_i][1] += beam_direction[1]
                else:
                    beams[beam_i][2] = mapping[mirror][beam_direction]
                    beams[beam_i][0] += beams[beam_i][2][0]
                    beams[beam_i][1] += beams[beam_i][2][1]
            else:
                beams[beam_i][0] += beam_direction[0]
                beams[beam_i][1] += beam_direction[1]
    # [print(x) for x in field_crossed]
    answer = sum([x.count('#') for x in field_crossed])
    return answer


if __name__ == '__main__':
    main()
