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

def calc_vis_trees(row, col, lines):
    count = 0

with open('input.txt', 'r') as f:
    lines = [[int(z) for z in a] for a in [[*y] for y in [x.strip() for x in f.readlines()]]]

vis = (len(lines) - 1) * 4

for row in range(1, len(lines) - 1):
    for col in range(1, len(lines[0]) -1):

        vis += check_if_vis(row, col, lines)

print(vis)
