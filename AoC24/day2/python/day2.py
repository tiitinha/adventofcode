import numpy as np

with open('../test.txt') as f:
    levels = [[int(j) for j in i] for i in [x.strip().split(' ') for x in f.readlines()]]

count = 0
count2 = 0
for level in levels:
    differences = np.diff(level)
    if ((np.all(differences >= 1) & np.all(differences <= 3)) | (np.all(differences <= -1) & np.all(differences >= -3))):
        count += 1
    
    level_len = len(differences)
    masked_1 = differences[np.logical_and(differences >= 1, differences <= 3)]
    masked_2 = differences[np.logical_and(differences <= -1, differences >= -3)]

    if ((level_len - len(masked_1 <= 1) | (level_len - len(masked_2) <= 1))):
        count2 += 1
        print("safe", level)

    print(level, differences, level_len, masked_1, masked_2)

print(count, count2)
