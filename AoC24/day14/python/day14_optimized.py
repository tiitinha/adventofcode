import re
from collections import Counter
from operator import mul
from functools import reduce
from statistics import variance

width, height = 101, 103
mid_width, mid_height = width // 2, height // 2

def outlier(vars_x, vars_y, var_x, var_y):
    avg_x = np.mean(vars_x)
    avg_y = np.mean(vars_y)

    if abs(var_x - avg_x) / var_x >= 1 and abs(var_y - avg_y) / var_y >= 1:
        return True

def move(position, velocity, rounds):
    new_x = (position[0] + velocity[0] * rounds) % width
    new_y = (position[1] + velocity[1] * rounds) % height

    return (new_x, new_y)

def simulate(t, robots):
    xs, ys = zip(*[((x + t * vx) % width, (y + t * vy) % height) for (x, vx, y, vy) in robots])

    return xs, ys

def quadrant_check(position):
    if position[0] < mid_width and position[1] < mid_height:
        return 1
    if position[0] > mid_width and position[1] < mid_height:
        return 2
    if position[0] < mid_width and position[1] > mid_height:
        return 3
    if position[0] > mid_width and position[1] > mid_height:
        return 4

with open('../input.txt') as f:
    robots = [[int(y) for y in re.findall(r'(-?\d+)', x)] for x in f.readlines()]

end_pos_set = []

for robot in robots:
    print(robot)
    position = (robot[0], robot[1])
    velocity = (robot[2], robot[3])

    end_pos = move(position, velocity, 100)
    print(end_pos)

    end_pos_set.append(end_pos)

end_quadrants = [quadrant_check(pos) for pos in end_pos_set]

quadrant_count = Counter(end_quadrants)
del quadrant_count[None]
print(reduce(mul, quadrant_count.values(), 1))

best_x, best_xvar, best_y, best_yvar = 0, 1000, 0, 1000
for t in range(max(width, height)):
    xs, ys = simulate(t, robots)

    if (xvar := variance(xs)) < best_xvar:
        best_x, best_xvar = t, xvar
    
    if (yvar := variance(ys)) < best_yvar:
        bext_y, best_yvar = t, yvar

part_2 = best_x + (((pow(width, -1, height) * (best_y - best_x)) % height) * width)
print(part_2)


