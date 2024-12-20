import numpy as np


def is_safe(level):
    diffs = np.diff(level)
    return ((np.all(diffs >= 1) & np.all(diffs <= 3)) | (np.all(diffs <= -1) & np.all(diffs >= -3)))

def safe_pt2(level):
    for i in range(0, len(level)):
        subset = level[:i] + level[i + 1:]
        if (is_safe(subset)):
            return True

    return False

with open('../input.txt') as f:
    levels = [[int(j) for j in i] for i in [x.strip().split(' ') for x in f.readlines()]]

count = 0
count2 = 0

for level in levels:

    if (is_safe(level)):
        count += 1
        count2 += 1
    else:
        if safe_pt2(level):
            count2 += 1

print(count, count2)
