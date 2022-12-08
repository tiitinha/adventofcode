import numpy as np

def check_if_vis(row, col, lines):
    # Check up
    if all([lines[x][col] < lines[row][col] for x in range(0, row)]):
        return True

    # Check down
    if all([lines[x][col] < lines[row][col] for x in range(row + 1, len(lines))]):
        return True

    # Check right
    if all([lines[row][x] < lines[row][col] for x in range(col + 1, len(lines[0]))]):
        return True

    # Check left
    if all([lines[row][x] < lines[row][col] for x in range(0, col)]):
        return True

    return False

def calc_scenic_score(row, col, lines):
    scenic_score = 1
    value = lines[row][col]

    count1 = 1 if row > 0 else 0

    for x in range(1, row):
        if lines[row - x][col] >= value or row - x == 0:
            break
        count1 += 1

    scenic_score *= count1
    count2 = 1 if row < len(lines) - 1 else 0

    for x in range(row + 1, len(lines)):
        if lines[x][col] >= value or x == len(lines) - 1:
            break
        count2 += 1

    scenic_score *= count2
    count3 = 1 if col > 0 else 0

    for x in range(1, col):
        if lines[row][col - x] >= value or col - x == 0:
            break
        count3 += 1

    scenic_score *= count3
    count4 = 1 if col < len(lines) - 1 else 0

    for x in range(col + 1, len(lines)):
        if lines[row][x] >= value or x == len(lines) - 1:
            break
        count4 += 1

    scenic_score *= count4

    return scenic_score

with open('input.txt', 'r') as f:
    lines = [[int(z) for z in a] for a in [[*y] for y in [x.strip() for x in f.readlines()]]]

vis = (len(lines) - 1) * 4

for row in range(1, len(lines) - 1):
    for col in range(1, len(lines[0]) -1):

        vis += check_if_vis(row, col, lines)

print(vis)

highest = 0
# trees = np.zeros((len(lines), len(lines[0])))

for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        score = calc_scenic_score(i, j, lines)

        highest = score if score > highest else highest

print(highest)

# print(trees)
