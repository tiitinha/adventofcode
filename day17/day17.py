import re

with open('input.txt', 'r') as file:
    x, y = [[int(y) for y in z] for z in [x.split('..') for x in re.findall('(\d{2}...\d{2})', file.read())]]
    print(y)


def get_max_y(y_vel) -> int:

    jump_size = abs(max(y_vel)) - 1
    return (jump_size * (jump_size + 1)) / 2

print(get_max_y(y))
