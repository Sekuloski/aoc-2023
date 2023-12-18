from matplotlib import patches
from matplotlib.path import Path
from shapely import BufferCapStyle
from shapely.geometry.polygon import Polygon
from aocd import get_data
from aocd.post import submit
import matplotlib.pyplot as plt



def area_of_polygon(vertices):
    area = 0.0
    for i in range(len(vertices) - 1):  # Subtract 1 to skip the duplicated first/last vertex
        x_i, y_i = vertices[i]
        x_next, y_next = vertices[i + 1]
        area += (x_i * y_next - x_next * y_i)
    return abs(area) / 2.0


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    start = (0, 0)
    path_coords = [start]

    max_x = 0
    min_x = 90
    max_y = 0
    min_y = 90

    for code in [line.split(' ')[-1][2:-1] for line in data]:
        direction = code[-1]
        steps = int(code[:-1], 16)
        match direction:
            case '0':
                new_coords = (1, 0)
            case '1':
                new_coords = (0, -1)
            case '2':
                new_coords = (-1, 0)
            case _:
                new_coords = (0, 1)
    #
    # for direction, steps in [line.split(' ')[:-1] for line in data]:
    #     match direction:
    #         case 'R':
    #             new_coords = (1, 0)
    #         case 'D':
    #             new_coords = (0, -1)
    #         case 'L':
    #             new_coords = (-1, 0)
    #         case _:
    #             new_coords = (0, 1)

        start = (start[0] + new_coords[0] * int(steps), start[1] + new_coords[1] * int(steps))
        path_coords.append(start)

        max_x = max(max_x, start[0])
        min_x = min(min_x, start[0])

        max_y = max(max_y, start[1])
        min_y = min(min_y, start[1])

    path = Path(path_coords)
    fig, ax = plt.subplots()
    patch = patches.PathPatch(path, facecolor='cyan', lw=2)
    ax.add_patch(patch)
    ax.set_xlim(min_x - 1, max_x + 1)
    ax.set_ylim(min_y - 2, max_y + 2)
    plt.show()

    polygon = Polygon(path.vertices)

    buffer_distance = 0.5
    expanded_polygon = polygon.buffer(buffer_distance, cap_style=BufferCapStyle.flat, join_style=BufferCapStyle.flat)
    expanded_coords = list(expanded_polygon.exterior.coords)

    path = Path(expanded_coords)
    fig, ax = plt.subplots()
    patch = patches.PathPatch(path, facecolor='cyan', lw=2)
    ax.add_patch(patch)
    ax.set_xlim(min_x - 1, max_x + 1)
    ax.set_ylim(min_y - 2, max_y + 2)
    plt.show()

    answer = int(area_of_polygon(expanded_coords))
    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
