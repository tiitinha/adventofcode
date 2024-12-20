import numpy as np
from collections import defaultdict

turn_left = np.array([[0, 1], [-1, 0]])
turn_right = np.array([[0, -1], [1, 0]])
forwards = np.array([[1, 0], [0, 1]])

def is_valid(point, track):
    if point[0] < 0 or point[1] < 0 or point[0] >= len(track) or point[1] >= len(track[0]):
        return False

    if track[point[0]][point[1]] == '#':
        return False

    return True

def get_starting_direction(point, track):
    directions = [np.array([1, 0]), np.array([0, 1]), np.array([-1, 0]), np.array([0, -1])]

    for direction in directions:
        next_point = point + direction
        if is_valid(next_point, track):
            return direction

def can_move(point1, point2):
    return (abs(point1[0] - point2[0]) == 0 and abs(point1[1] - point2[1] == 0)) or (abs(point1[0] - point2[0]) == 0 and abs(point1[1] - point2[1]) == 2)

def get_neighbors(point, direction, track):
    directions = [turn_left, turn_right, forwards]
    neighbors = [(point + np.dot(direction, x), np.dot(direction, x)) for x in directions]

    return [x for x in neighbors if is_valid(x[0], track)]

with open('../test.txt') as f:
    racetrack = np.array([[y for y in x.strip()] for x in f.readlines()])

start = np.array(np.argwhere(racetrack == 'S')[0])
end = np.array(np.argwhere(racetrack == 'E')[0])
current_pos = start
direction = get_starting_direction(start, racetrack)
track = []
dist_dict = defaultdict(int)

while np.any(current_pos != end):
    neighbors = get_neighbors(current_pos, direction, racetrack)[0]
    current_pos = neighbors[0]
    direction = neighbors[1]
    
    track.append(current_pos)

for i, point1 in enumerate(track):
    for j, point2 in enumerate(track[i:]):
        distance = abs(i - j)

        if can_move(point1, point2) and distance > 4:
            print(point1, point2)
            dist_dict[distance - 2] += 1

print(dist_dict)
