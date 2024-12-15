import numpy as np



movement_map = {
    '^': np.array([-1, 0]),
    '<': np.array([0, -1]),
    'v': np.array([1, 0]),
    '>': np.array([0, 1])
}

with open('../input.txt') as f:
    area_map, instructions = f.read().split('\n\n')

area_map = np.array([[y for y in x] for x in area_map.split()])
instructions = [movement_map[x] for x in instructions.replace('\n', '')]

def can_move(pos, direction):
    next_pos = pos + direction

    if area_map[pos[0]][pos[1]] == '.' or area_map[next_pos[0]][next_pos[1]] == '#':
        return False

    if area_map[next_pos[0], next_pos[1]] == '.' or can_move(next_pos, direction):
        current_block = area_map[pos[0]][pos[1]]
        area_map[pos[0]][pos[1]] = '.'
        area_map[next_pos[0]][next_pos[1]] = current_block
        return True

initial_robot_pos = np.array(list(zip(*np.where(area_map == '@')))[0])

for instruction in instructions:
    can_move(initial_robot_pos, instruction)
    initial_robot_pos = (list(zip(*np.where(area_map == '@')))[0])

boxes = list(zip(*np.where(area_map == 'O')))

summa = 0

for box in boxes:
    x = box[1]
    y = box[0]

    summa += y * 100 + x

print(summa)
