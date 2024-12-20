import numpy as np
import math
import heapq
from itertools import count

with open('../input.txt') as f:
    byte_data = np.array([[int(y) for y in x.strip().split(',')] for x in f.readlines()])

directions = [np.array([x, y]) for x in range(-1, 2) for y in range(-1, 2) if abs(x) != abs(y)]
cost = 1
size = 71
byte_size = 1024
start = np.array([0, 0])
end = np.array([size - 1, size - 1])

input_data = np.full((size, size), 0)
dist_array = np.full((size, size), math.inf)
visited = np.full((size, size), 0)
visited[start[0]][start[1]] = 1
tiebreaker = count()
heap = [(0, next(tiebreaker), start)]
dist_array[start[0]][start[1]] = 0

for byte in byte_data[:byte_size]:
    visited[byte[1]][byte[0]] = 2

def can_move(point):
    if np.any(point < 0) or np.any(point >= size) or input_data[point[0]][point[1]] or visited[point[0]][point[1]]:
        return False

    return True

def get_neighbors(point):
    potential_neighbors = [(point + direction) for direction in directions]
    neighbors = [x for x in potential_neighbors if can_move(x)]
    return neighbors

while not len(heap) == 0:
    node = heapq.heappop(heap)
    neighbors = get_neighbors(node[2])
    
    for neighbor in neighbors:
        dist = node[0] + cost
        coords = neighbor
        if dist <= dist_array[coords[0]][coords[1]] and visited[coords[0]][coords[1]] == 0:
            dist_array[coords[0]][coords[1]] = dist
            new_node = (dist, next(tiebreaker), coords)
            heapq.heappush(heap, new_node)
            visited[coords[0]][coords[1]] = 1


print(dist_array[end[0]][end[1]])
print(dist_array)
