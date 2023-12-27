import re
import numpy as np
import math

with open('../input.txt') as f:
    input_data = [re.findall('[U|D|L|R]|[0-9]+|#[A-Za-z0-9]{6}', x.strip()) for x in f.readlines()]


directions = {
    'U': np.array([1, 0]),
    'D': np.array([-1, 0]),
    'L': np.array([0, -1]),
    'R': np.array([0, 1])
}

directions2 = {
    '3': np.array([1, 0]),
    '1': np.array([-1, 0]),
    '2': np.array([0, -1]),
    '0': np.array([0, 1])
}

current = np.array([0, 0])
visited = []
step_list = []
visited2 = []
step_list2 = []

for input in input_data:
    dir = input[0]
    steps = int(input[1])
    rgb = input[2]

    steps_movement = directions[dir] * steps
    step_list.append(steps_movement)
    current += steps_movement

    visited.append(np.array([current[0], current[1]]))

current = np.array([0, 0])

for input in input_data:
    dir = input[2][6]
    steps = int(input[2][1:6], 16)

    steps_movement = directions2[dir] * steps
    step_list2.append(steps_movement)
    current += steps_movement

    visited2.append(np.array([current[0], current[1]]))

def calculate_solucious(visited, step_list):
    area = 0
    for i in range(1, len(visited)):
        first = visited[i - 1]
        second = visited[i]

        determinant = first[0] * second[1] - first[1] * second[0]

        area += determinant

    area = abs(area) / 2
    boundry = sum([abs(math.sqrt(x[0] ** 2 + x[1] ** 2)) for x in step_list])

    result = (area + boundry) - boundry / 2 + 1

    return result

pt1 = calculate_solucious(visited, step_list)
pt2 = calculate_solucious(visited2, step_list2)

print(pt1, pt2)
