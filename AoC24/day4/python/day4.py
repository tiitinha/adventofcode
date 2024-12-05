import numpy as np

next_letter = {
    'X': 'M',
    'M': 'A',
    'A': 'S'
}

mas_mapping = {
    'M': 'S',
    'S': 'M'
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

def mas_possible(x, y):
    return (0 <= x - 1 <= width) & (0 <= x + 1 <= width) & (0 <= y - 1 <= height) & (0 <= y + 1 <= height)

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

def check_mas(x, y):
    not_allowed = ['X', 'A']
    upper_left = input[y - 1][x - 1]
    lower_left = input[y + 1][x - 1]
    upper_right = input[y - 1][x + 1]
    lower_right = input[y + 1][x + 1]

    if (upper_left in not_allowed) | (lower_left in not_allowed) | (upper_right in not_allowed) | (lower_right in not_allowed):
        return False

    return (mas_mapping[upper_left] == lower_right) & (mas_mapping[lower_left] == upper_right)

count = 0
count2 = 0

for j in range(len(input)):
    for i in range(len(input[0])):
        if input[j][i] == 'X':
            for direction in directions:
                if (is_possible(i, j, direction)):
                    valid = check_text(i, j, direction)

                    if valid:
                        count += 1

        if (input[j][i] == 'A') & mas_possible(j, i):
            valid = check_mas(i, j)

            if valid:
                count2 += 1



print(count)
print(count2)
