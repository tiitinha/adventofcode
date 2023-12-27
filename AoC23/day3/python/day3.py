import numpy as np
from collections import defaultdict
import math

with open('../input.txt') as f:
    input_data = np.asarray([[y for y in x.strip()] for x in f.readlines()])

current_part = ''
parts = []

gears = defaultdict(list)

def create_neighbors(y, x):
    neighbors = [(y + y_diff, x + x_diff) for y_diff in range(-1, 2) for x_diff in range(-1, 2) if (y + y_diff < len(input_data) and y + y_diff >= 0) and (x + x_diff < len(input_data[0]) and x + x_diff >= 0)]

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
                gears.setdefault(is_gear, []).append(int(current_part))    
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

    if is_gear != False and current_part != '':
        #print(is_gear, current_part)
        gears.setdefault(is_gear, []).append(int(current_part))


    current_part = ''

pt1 = sum([int(x) for x in parts])
#print(parts)
print(pt1)

#for key, value in gears.items():
#    print(key, value)

gear_lists = [x for x in gears.values() if len(x) == 2]
print(sum([math.prod([int(y) for y in x]) for x in gear_lists]))
