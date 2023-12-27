from heapq import heappush, heappop
from collections import defaultdict

from aocd import get_data
from aocd.post import submit


def dijkstra(grid):
    visited = set()
    priority_queue = [(0, 0, 0, (0, 0), 0)]

    while priority_queue:
        distance, y, x, prev_direction, steps = heappop(priority_queue)

        if y == len(grid) - 1 and x == len(grid[y]) - 1:
            return distance

        if (y, x, prev_direction, steps) in visited:
            continue

        visited.add((y, x, prev_direction, steps))

        # Continue straight
        if steps < 10 and (x, y) != (0, 0):
            new_y = y + prev_direction[1]
            new_x = x + prev_direction[0]
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[new_y]):
                heappush(priority_queue, (distance + grid[new_y][new_x], new_y, new_x, prev_direction, steps + 1))

        # Turn
        if steps >= 4 or (x, y) == (0, 0):
            for new_direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_y = y + new_direction[1]
                new_x = x + new_direction[0]
                if new_direction != prev_direction and new_direction != (-prev_direction[0], -prev_direction[1]):
                    if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[new_y]):
                        heappush(priority_queue, (distance + grid[new_y][new_x], new_y, new_x, new_direction, 1))


def main():
    data = get_data(day=17).split('\n')
    # data = open('test').read().split('\n')

    answer = 0
    graph = defaultdict(dict)

    for y in range(len(data)):
        for x in range(len(data[y])):
            position = (x, y)
            for neighbor in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                neighbor = (x + neighbor[0], y + neighbor[1])

                if 0 > neighbor[0] or neighbor[0] >= len(data[0]):
                    continue
                if 0 > neighbor[1] or neighbor[1] >= len(data):
                    continue

                graph[position][neighbor] = int(data[neighbor[1]][neighbor[0]])

    test_data = []
    for i in range(len(data)):
        test_data.append([])
        for x in data[i]:
            test_data[i].append(int(x))

    answer = dijkstra(test_data)
    print(answer)
    submit(answer, day=17)


if __name__ == '__main__':
    main()
