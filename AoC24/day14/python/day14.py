import re
from collections import Counter
from operator import mul
from functools import reduce
import numpy as np

width = 101
height = 103
mid_width = width // 2
mid_height = height // 2

def outlier(vars_x, vars_y, var_x, var_y):
    avg_x = np.mean(vars_x)
    avg_y = np.mean(vars_y)

    if abs(var_x - avg_x) / var_x >= 1 and abs(var_y - avg_y) / var_y >= 1:
        return True

def move(position, velocity, rounds):
    new_x = (position[0] + velocity[0] * rounds) % width
    new_y = (position[1] + velocity[1] * rounds) % height

    return (new_x, new_y)

def quadrant_check(position):
    if position[0] < mid_width and position[1] < mid_height:
        return 1
    if position[0] > mid_width and position[1] < mid_height:
        return 2
    if position[0] < mid_width and position[1] > mid_height:
        return 3
    if position[0] > mid_width and position[1] > mid_height:
        return 4

    return 0

with open('../input.txt') as f:
    robots = [[y.split(',') for y in z] for z in [re.findall('\-*\d+\,\-*\d+', x) for x in f.readlines()]]

end_pos_set = []

for robot in robots:
    position = (int(robot[0][0]), int(robot[0][1]))
    velocity = (int(robot[1][0]), int(robot[1][1]))

    end_pos = move(position, velocity, 100)

    end_pos_set.append(end_pos)

end_quadrants = [quadrant_check(pos) for pos in end_pos_set]

quadrant_count = Counter(end_quadrants)
del quadrant_count[0]

print(reduce(mul, quadrant_count.values(), 1))

rnds = 1
vars_x = []
vars_y = []
while True:
    positions = []
    for robot in robots:
        position = (int(robot[0][0]), int(robot[0][1]))
        velocity = (int(robot[1][0]), int(robot[1][1]))

        pos = move(position, velocity, rnds)
        positions.append(pos)

    var_x = np.var([x[0] for x in positions])
    var_y = np.var([x[1] for x in positions])

    vars_x.append(var_x)
    vars_y.append(var_y)

    if outlier(vars_x, vars_y, var_x, var_y):
        break

    rnds += 1

print(rnds)
print(vars_x[-1], vars_y[-1])


