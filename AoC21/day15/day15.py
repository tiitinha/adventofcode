import numpy as np
import math
from copy import deepcopy

with open('input.txt', 'r') as file:
    cavern_map = np.array([[int(y) for y in x] for x in file.read().strip().split('\n')])


def find_smallest_sum_path(cavern_map: list) -> list:

    height = len(cavern_map)
    width = len(cavern_map[0])

    tc = np.array([[int(math.pow(2, 31)) for x in range(width)] for x in range(height)])

    tc[0][0] = 0

    for i in range(0, height):
        for j in range(0, width):
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if is_valid((j + a), (i + b), height, width) and abs(a) != abs(b):
                        value = tc[j][i] + cavern_map[j + a][i + b]
                        tc[j + a][i + b] = value if tc[j + a][i + b] > value else tc[j + a][i + b]


    return tc

def is_valid(x: int, y: int, rows: int, cols: int):
    return x >= 0 and x < cols and y >= 0 and y < colsdef create_larger_map():
    map = np.array(lines)
    for i in range(4):
        new_part = lines
        for a in range(len(lines)):
            for b in range(len(lines[0])):
                new_part[a][b] += 1
                if (new_part[a][b] > 9):
                    new_part[a][b] = 1
        map = np.concatenate((map, np.array(new_part)), axis=0)
    new_part = deepcopy(map)
    for i in range(4):
        for a in range(len(new_part)):
            for b in range(len(new_part[0])):
                new_part[a][b] += 1
                if (new_part[a][b] > 9):
                    new_part[a][b] = 1
        map = np.concatenate((map, np.array(new_part)), axis=1)
    return map

def copy_map(cavern_map: list, copies: int) -> list:

    height = len(cavern_map)
    width = len(cavern_map[0])

    copied_map = np.zeros((height * copies, width * copies))

    for i in range(copies):
        for j in range(copies):
            for x in range(height):
                for y in range(width):
                    copied_map[(i * height) + x][(j * width) + y] = (cavern_map[x][y] + i + j) % 9 if (cavern_map[x][y] + i + j) % 9 != 0 else 9

    return copied_map

def create_larger_map(lines: list, rounds):
    map = np.array(lines)
    for i in range(rounds):
        new_part = lines
        for a in range(len(lines)):
            for b in range(len(lines[0])):
                new_part[a][b] += 1
                if (new_part[a][b] > 9):
                    new_part[a][b] = 1
        map = np.concatenate((map, np.array(new_part)), axis=0)
    new_part = deepcopy(map)
    for i in range(rounds):
        for a in range(len(new_part)):
            for b in range(len(new_part[0])):
                new_part[a][b] += 1
                if (new_part[a][b] > 9):
                    new_part[a][b] = 1
        map = np.concatenate((map, np.array(new_part)), axis=1)
    return map

def get_best_path_sum(best_path: list) -> int:
    return best_path[len(best_path) - 1][len(best_path[0]) - 1] - best_path[0][0]

best_path = find_smallest_sum_path(cavern_map)

print(get_best_path_sum(best_path))

larger_map = copy_map(cavern_map, 5)
larger_map_best_path = find_smallest_sum_path(larger_map)

print(get_best_path_sum(larger_map_best_path))
