import numpy as np

next_letter = {
    'X': 'M',
    'M': 'A',
    'A': 'S'
}

directions = [(-1, -1), (1, -1), (-1, 1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]


with open('../input.txt') as f:
    input = np.array([list(x.strip()) for x in f.readlines()])
    width = len(input[0]) - 1
    height = len(input) - 1


def is_possible(x, y, dir):
    new_x = x + 3 * dir[0]
    new_y = y + 3 * dir[1]

    return (0 <= new_x <= width) & (0 <= new_y <= width)

def check_text(x, y, dir):
    new_x = x + dir[0]
    new_y = y + dir[1]

    if input[new_y][new_x] != 'M':
        return False

    new_x += dir[0]
    new_y += dir[1]

    if input[new_y][new_x] != 'A':
        return False

    new_x += dir[0]
    new_y += dir[1]

    if input[new_y][new_x] != 'S':
        return False

    new_x += dir[0]
    new_y += dir[1]

    return True

def get_neighbors(x, y):
    count = 0
    value = input[y][x]

    if value == 'S':
        return 1

    x_vals = [x + i for i in range(-1, 2) if (x + i >= 0) & (x + i < len(input[0]))]
    y_vals = [y + i for i in range(-1, 2) if (y + i >= 0) & (y + i < len(input))]

    neighbors = [(i, j) for i in x_vals for j in y_vals if (input[j][i] == next_letter[value]) & (not(i == x & y == j))]

    for neighbor in neighbors:
        count += get_neighbors(neighbor[0], neighbor[1])

    return count

count = 0

for j in range(len(input)):
    for i in range(len(input[0])):
        if input[j][i] == 'X':
            for direction in directions:
                if (is_possible(i, j, direction)):
                    valid = check_text(i, j, direction)

                    if valid:
                        count += 1

print(count)
