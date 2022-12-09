import numpy as np

def is_touching(head_pos, tail_pos):
    diff = head_pos - tail_pos

    if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
        return True

    return False

def calc_tail_pos(head_pos, tail_pos):

    if is_touching(head_pos, tail_pos):
        return tail_pos

    diff = head_pos - tail_pos

    if (diff[0] != 0 and diff[1] != 0) or abs(diff[0]) > 1 or abs(diff[1]) > 1:
        x = diff[0] / abs(diff[0]) if diff[0] != 0 else 0
        y = diff[1] / abs(diff[1]) if diff[1] != 0 else 0

        tail_pos += np.array([x, y])

    return tail_pos

with open('input.txt', 'r') as f:
    lines = [x.strip().split(' ') for x in f.readlines()]

dirs = {'R': np.array([1, 0]),
        'L': np.array([-1, 0]),
        'U': np.array([0, 1]),
        'D': np.array([0, -1])}

visited_positions = set()
head_pos = np.zeros(2)
tail_pos = np.zeros(2)

positions = [np.zeros(2) for _ in range(10)]
visited_positions_2 = set()

for line in lines:
    direction, steps = line

    movement = dirs[direction]

    for i in range(int(steps)):

        head_pos += movement
        positions[0] = head_pos

        tail_pos = calc_tail_pos(head_pos, tail_pos)

        # print(f'Head: {head_pos}, tail: {tail_pos}')

        visited_positions.add(str(tail_pos))

        for i in range(1, len(positions)):
            next_knot_pos = calc_tail_pos(positions[i - 1], positions[i])

            positions[i] = next_knot_pos

        visited_positions_2.add(str((positions[9][0], positions[9][1])))

# print(visited_positions)
print(len(visited_positions))
print(len(visited_positions_2))

