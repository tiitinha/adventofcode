import re
import numpy as np

with open('input.txt', 'r') as file:
    input_data = [x for x in file.read().strip().split('\n')]
    final_input = []

    for row in input_data:
        command, xyz = row.split(' ')
        xyz = [[int(y) for y in z] for z in [re.findall('(-*\d+)', x) for x in xyz.split(',')]]


        final_input.append((command, xyz))


def set_values(cube_array: list, rules: list, val: int):
    for x in range(rules[0][0], rules[0][1] + 1):
        if (abs(x) <= 50):
            for y in range(rules[1][0], rules[1][1] + 1):
                if (abs(y) <= 50):
                    for z in range(rules[2][0], rules[2][1] + 1):
                        if (abs(z) <= 50):
                            cube_array[x + 50][y + 50][z + 50] = val


    return cube_array

def part1(input_data: dict) -> int:
    cube_array = np.zeros((101, 101, 101))

    for row in input_data:
        rules = row[1]
        if row[0] == 'on':
            cube_array = set_values(cube_array, rules, 1)
        else:
            cube_array = set_values(cube_array, rules, 0)

    return cube_array

def count(cube: list) -> int:
    return np.sum(cube)

result = part1(final_input)
print(count(result))
