import numpy as np

with open('input.txt', 'r') as f:

    lines = np.array([x.strip().split(',') for x in f.readlines()]).astype(int)

print(lines)

dirs = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]

max_x = max(x[0] for x in lines)
max_y = max(x[1] for x in lines)
max_z = max(x[2] for x in lines)
min_x = min(x[0] for x in lines)
min_y = min(x[1] for x in lines)
min_z = min(x[2] for x in lines)


