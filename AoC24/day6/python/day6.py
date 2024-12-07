import numpy as np

rot_right = np.array([[0, 1], [-1, 0]])

with open('../input.txt') as f:
    map_input = np.array([[z for z in y] for y in [x.strip() for x in f.readlines()]])

width = len(map_input[0]) - 1
height = len(map_input) - 1

guard_location = np.argwhere(map_input == '^')[0]
obstacles = np.argwhere(map_input == '#')

def can_move_forward(location, direction):
    potential_next = location + direction

    x_legit = (0 <= potential_next[1] <= width)
    y_legit = (0 <= potential_next[0] <= height)

    if (x_legit and y_legit and map_input[potential_next[0]][potential_next[1]] != '#'):
        return True

    return False

def can_turn_right(location, direction):
    new_direction = np.dot(rot_right, direction)
    potential_next = location + new_direction

    x_legit = (0 <= potential_next[1] <= width)
    y_legit = (0 <= potential_next[0] <= height)

    if (x_legit and y_legit and map_input[potential_next[0]][potential_next[1]] == '.'):
        return True

    return False

direction = np.array([-1, 0])
visited = set()
visited.add((guard_location[0], guard_location[1]))

while True:
    if can_move_forward(guard_location, direction):
        guard_location += direction
    elif can_turn_right(guard_location, direction):
        direction = np.dot(rot_right, direction)
        guard_location += direction
    else:
        break

    visited.add((guard_location[0], guard_location[1]))

print(len(visited))
