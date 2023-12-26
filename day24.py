from collections import defaultdict

from aocd import get_data
from aocd.post import submit


class Line:
    def __init__(self, x, y, z, vx, vy, vz):
        self.point_one = (x, y, z)
        self.point_two = (x + vx, y + vy, z + vz)
        self.going_right = x + vx > x
        self.going_up = y + vy > y
        self.A = self.point_two[1] - self.point_one[1]
        self.B = self.point_one[0] - self.point_two[0]
        self.C = self.A * self.point_one[0] + self.B * self.point_one[1]

    def check_future(self, x, y):
        if self.going_right and self.going_up:
            if x >= self.point_two[0] and y >= self.point_two[1]:
                return True
        elif self.going_right:
            if x >= self.point_two[0] and y <= self.point_two[1]:
                return True
        elif self.going_up:
            if x <= self.point_two[0] and y >= self.point_two[1]:
                return True
        else:
            if x <= self.point_two[0] and y <= self.point_two[1]:
                return True

        return False


def get_intersection(line_one: Line, line_two: Line):
    d = (line_one.A * line_two.B) - (line_two.A * line_one.B)
    if d == 0:
        return None

    x = (line_two.B * line_one.C - line_one.B * line_two.C) / d
    y = (line_one.A * line_two.C - line_two.A * line_one.C) / d

    if line_one.check_future(x, y) and line_two.check_future(x, y):
        return x, y

    return None


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    answer = 0
    lines = []
    for line in data:
        parts = [x for x in line.split(' ') if x != '']
        x = int(parts[0].removesuffix(','))
        y = int(parts[1].removesuffix(','))
        z = int(parts[2])
        vx = int(parts[4].removesuffix(','))
        vy = int(parts[5].removesuffix(','))
        vz = int(parts[6])

        lines.append(Line(x, y, z, vx, vy, vz))

    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            intersection = get_intersection(lines[i], lines[j])
            if intersection:
                if 400000000000000 >= intersection[0] >= 200000000000000 and 400000000000000 >= intersection[1] >= 200000000000000:
                    answer += 1
    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
