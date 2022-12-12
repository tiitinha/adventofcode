import numpy as np
from collections import deque

def get_height_val(c: str) -> int:
    if c == 'S':
        return ord('a')

    if c == 'E':
        return ord('z')

    return ord(c)

def get_next_possible_nodes(current: tuple, m: list) -> list:
    x = current[0]
    y = current[1]

    possible = []
    dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    for d in dirs:
        temp_x = x - d[0]
        temp_y = y - d[1]

        if (0 <= temp_x < len(m[0])) and (0 <= temp_y < len(m)) and (m[temp_y][temp_x] - m[y][x]) <= 1:
            possible.append((temp_x, temp_y))

    return possible

def bfs(start: tuple, end: tuple, m: list) -> int:
    explored = np.zeros((len(m), len(m[0])))
    count = 0

    queue = deque([start])

    dist = np.zeros((len(m), len(m[0])))

    rnd = 0

    while queue:
        current = queue.popleft()

        explored[current[1]][current[0]] = 1

        if current == end:
            return dist[end[1]][end[0]]

        neighbors = get_next_possible_nodes(current, m)

        for neighbor in neighbors:
            if explored[neighbor[1]][neighbor[0]] == 0 and neighbor not in queue:
                queue.append(neighbor)

                dist[neighbor[1]][neighbor[0]] = dist[current[1]][current[0]] + 1

    return dist[end[1]][end[0]]

def find_point(point: str, m: list) -> tuple:
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == point:
                return (x, y)

def find_points(starts: list, m: list) -> list:
    points = []

    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] in starts:
                points.append((x, y))

    return points

with open('input.txt', 'r') as f:
    heightmap_raw = [[*y] for y in [x.strip() for x in f.readlines()]]
    heightmap = np.array([[get_height_val(y) for y in x] for x in heightmap_raw])

start = find_point('S', heightmap_raw)
starts = find_points(['S', 'a'], heightmap_raw)
end = find_point('E', heightmap_raw)

print(bfs(start, end, heightmap))

results = [bfs(x, end, heightmap) for x in starts]
print(min([y for y in results if y != 0]))
