import numpy as np
import math

def manhattan_dist(coordinates):
    return sum(abs(coordinates))

def rotate_vector(vector, direction, degrees):
    rotation = 0
    if direction == 'L':
        rotation = degrees
    elif direction == 'R':
        rotation = 360 - degrees

    a = int(math.cos(math.radians(rotation)))
    b = -int(math.sin(math.radians(rotation)))
    c = int(math.sin(math.radians(rotation)))
    d = int(math.cos(math.radians(rotation)))

    rotator = np.array([[a, b], [c, d]])

    rotated_vector = vector.dot(rotator)
    return rotated_vector

def execute_instructions(instructions):
    movs = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    orient = 'E'
    directs = ['N', 'E', 'S', 'W']
    cur_coordinates = np.array([0, 0])
    dirs = {'N': np.array([1, 0]), 'W': np.array([0, -1]), 'S': np.array([-1, 0]), 'E': np.array([0, 1])}
    cur_direction = dirs['E']

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1])

        if direction in ['N', 'W', 'S', 'E']:
            cur_coordinates += dirs[direction] * distance
            movs[direction] += distance
        elif direction in ['L', 'R']:
            cur_direction = rotate_vector(cur_direction, direction, distance)
            if direction == 'R':
                turns = int(distance/90)
                orient = directs[(directs.index(orient) + turns) % len(directs)]
            if direction == 'L':
                turns = int(distance/90)
                orient = directs[directs.index(orient) - turns]
        elif direction == 'F':
            cur_coordinates += cur_direction * distance
            movs[orient] += distance

    #return np.array([movs['N'] - movs['S'], movs['E'] - movs['W']])

    return cur_coordinates

def execute_instructions_waypoint(instructions):
    cur_coordinates = np.array([0, 0])
    dirs = {'N': np.array([1, 0]), 'W': np.array([0, -1]), 'S': np.array([-1, 0]), 'E': np.array([0, 1])}
    waypoint = np.array([1, 10])

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1])

        if direction in ['N', 'W', 'S', 'E']:
            waypoint += dirs[direction] * distance
        elif direction in ['L', 'R']:
            waypoint = rotate_vector(waypoint, direction, distance)
        elif direction == 'F':
            cur_coordinates += waypoint * distance

    return cur_coordinates


with open('input.txt') as f:
    instructions = [(l[0], l[1:]) for l in f.read().split('\n')]

executed = execute_instructions(instructions)
waypoint_ver = execute_instructions_waypoint(instructions)
dist = manhattan_dist(executed)
pt2 = manhattan_dist(waypoint_ver)
print(executed)
print(dist)
print(pt2)
