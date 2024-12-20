import numpy as np

rot_right = np.array([[0, 1], [-1, 0]])

with open('../input.txt') as f:
    map_input = np.array([[z for z in y] for y in [x.strip() for x in f.readlines()]])

width = len(map_input[0]) - 1
height = len(map_input) - 1

guard_location = np.argwhere(map_input == '^')[0]
obstacles = np.argwhere(map_input == '#')

def check_obstacle(location, direction, visited):
    next_dir = np.dot(rot_right, direction)
    next_loc = (location[0], location[1])

    while can_move_forward(next_loc, next_dir):
        next_loc += next_dir
        if (next_loc[0], next_loc[1], next_dir[0], next_dir[1]) in (visited):
            return True

    return False

def can_move_forward(location, direction):
    potential_next = location + direction

    x_legit = (0 <= potential_next[1] <= width)
    y_legit = (0 <= potential_next[0] <= height)

    if (x_legit and y_legit and map_input[potential_next[0]][potential_next[1]] != '#'):
        return True

    return False

def can_turn_right(location, direction):
    new_direction = np.dot(direction, rot_right)
    potential_next = location + new_direction

    x_legit = (0 <= potential_next[1] <= width)
    y_legit = (0 <= potential_next[0] <= height)

    if (x_legit and y_legit and map_input[potential_next[0]][potential_next[1]] == '.'):
        return True

    return False

def is_going_out(guard_location, direction):
    next_location = guard_location + direction

    return (next_location[0] < 0) | (next_location[0] > height) | (next_location[1] < 0) | (next_location[1] > width)

direction = np.array([-1, 0])
visited = set()
visited_dir = set()
visited.add((guard_location[0], guard_location[1]))
visited_dir.add((guard_location[0], guard_location[1], direction[0], direction[1]))
visited_obstacles = set()
count = 0

while True:
    if check_obstacle(guard_location, direction, visited_dir):
        count += 1
    if is_going_out(guard_location, direction):
       break 
    elif can_move_forward(guard_location, direction):
        guard_location += direction
    elif can_turn_right(guard_location, direction):
        direction = np.dot(rot_right, direction)
        guard_location += direction


    visited.add((guard_location[0], guard_location[1]))
    visited_dir.add((guard_location[0], guard_location[1], direction[0], direction[1]))

print(len(visited))
print(count)
