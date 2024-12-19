import numpy as np
import math
import heapq
from itertools import count

turn_left = np.array([[0, 1], [-1, 0]])
turn_right = np.array([[0, -1], [1, 0]])
direction = np.array([0, 1])
cost = 1001

with open('../input.txt') as f:
    input_data = np.array([[y for y in x.strip()] for x in f.readlines()])

def can_move(point):
    if input_data[point[0]][point[1]] == '#':
        return False

    return True

def get_neighbors(point, direction):
    potential_neighbors = [((point + direction), 1, direction), ((point + np.dot(direction, turn_left)), cost, np.dot(direction, turn_left)), ((point + np.dot(direction, turn_right)), cost, np.dot(direction, turn_right))]

    return [x for x in potential_neighbors if can_move(x[0])]

start = np.array([y for x in np.where(input_data == 'S') for y in x])
end = np.array([y for x in np.where(input_data == 'E') for y in x])

dist_array = np.full((len(input_data), len(input_data[0])), math.inf)
visited = np.full((len(input_data), len(input_data[0])), 0)
visited[start[0]][start[1]] = 1
tiebreaker = count()
heap = [(0, next(tiebreaker), start, direction)]
dist_array[start[0]][start[1]] = 0

while not len(heap) == 0:
    node = heapq.heappop(heap)
    neighbors = get_neighbors(node[2], node[3])
    
    for neighbor in neighbors:
        direction = neighbor[2]
        dist = node[0] + neighbor[1]
        coords = neighbor[0]
        if dist <= dist_array[coords[0]][coords[1]] and visited[coords[0]][coords[1]] == 0:
            dist_array[coords[0]][coords[1]] = dist
            new_node = (dist, next(tiebreaker), coords, direction)
            heapq.heappush(heap, new_node)
            visited[coords[0]][coords[1]] = 1


print(dist_array[end[0]][end[1]])

#print(visited)
