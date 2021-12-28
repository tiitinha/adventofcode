import numpy as np

with open('input.txt', 'r') as file:
    cavern_map = np.array([[int(y) for y in x] for x in file.read().strip().split('\n')])


def find_smallest_sum_path(cavern_map: list) -> list:

    height = len(cavern_map)
    width = len(cavern_map[0])

    tc = np.array([[0 for x in range(width)] for x in range(height)])

    tc[0][0] = cavern_map[0][0]

    for i in range(1, height):
        tc[i][0] = tc[i - 1][0] + cavern_map[i][0]

    for j in range(1, width):
        tc[0][j] = tc[0][j - 1] + cavern_map[0][j]

    for i in range(1, height):
        for j in range(1, width):
            tc[i][j] = min(tc[i - 1][j], tc[i][j - 1]) + cavern_map[i][j]


    return tc

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

def get_best_path_sum(best_path: list) -> int:
    return best_path[len(best_path) - 1][len(best_path[0]) - 1] - best_path[0][0]

best_path = find_smallest_sum_path(cavern_map)

print(get_best_path_sum(best_path))

larger_map = copy_map(cavern_map, 5)
larger_map_best_path = find_smallest_sum_path(larger_map)

print(get_best_path_sum(larger_map_best_path))


