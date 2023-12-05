import numpy as np
from collections import defaultdict

with open('../input.txt') as f:
    input_data = np.asarray([[y for y in x.strip()] for x in f.readlines()])

current_part = ''
parts = []

gears = defaultdict(list)

def create_neighbors(y, x):
    x_dir = []
    if x == 0:
        x_dir.extend([0 ,1])
    elif x == len(input_data[0]) - 1:
        x_dir.extend([-1, 0])
    else:
        x_dir.extend([-1, 0, 1])
    

    y_dir = []

    if y == 0:
        y_dir.extend([0 ,1])
    elif y == len(input_data) - 1:
        y_dir.extend([-1, 0])
    else:
        y_dir.extend([-1, 0, 1])

    neighbors = [(y + y_diff, x + x_diff) for y_diff in y_dir for x_diff in x_dir]

    return neighbors


def check_if_valid(y, x):
    directions = create_neighbors(y, x)

    for coordinate in directions:
        y_val, x_val = coordinate
        value = input_data[y_val][x_val]

        if not value.isdigit() and not value == '.':
            return True

    return False

def check_if_gear(y, x):
    directions = create_neighbors(y, x)

    for coordinate in directions:
        y_val, x_val = coordinate
        value = input_data[y_val][x_val]

        if value == '*':
            return (y_val, x_val)
    
    return False

for j in range(len(input_data)):
    is_valid_part = False
    is_gear = False
    for i in range(len(input_data[j])):
        if not input_data[j][i].isdigit():
            if is_valid_part and current_part != '':
                parts.append(current_part)
            if is_gear and current_part != '':
                gears.setdefault(f'{is_gear}', []).append(current_part)    
            current_part = ''
            is_valid_part = False
            is_gear = False
            continue
        
        if input_data[j][i].isdigit():
            is_valid_part = is_valid_part if is_valid_part else check_if_valid(j, i)
            is_gear = is_gear if is_gear else check_if_gear(j, i)

        current_part += input_data[j][i]

    if is_valid_part:
        parts.append(current_part)
        current_part = ''

    if is_gear and current_part != '':
        gears.setdefault(f'{is_gear}', []).append(current_part)

pt1 = sum([int(x) for x in parts])
print(parts)
print(pt1)

#for key, value in gears.items():
#    print(key, value)

gear_lists = [x for x in gears.values() if len(x) == 2]
print(sum([int(x[0]) * int(x[1]) for x in gear_lists]))
