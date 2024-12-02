import numpy as np

with open('./input.txt') as f:
    levels = [[int(j) for j in i] for i in [x.strip().split(' ') for x in f.readlines()]]

count = 0
count2 = 0
for level in levels:
    differences = np.diff(level)
    diff2 = np.array([level[i] - level[i - 2] for i in range(2, len(level))])
    if ((np.all(differences >= 1) & np.all(differences <= 3)) | (np.all(differences <= -1) & np.all(differences >= -3))):
        count += 1
        count2 += 1
        print(level, "safe")
    elif (((sum(diff2 < 1) + sum(diff2 > 3) + sum(diff2 == 0) <= 1)) | (sum(diff2 > -1) + sum(diff2 < -3) + sum(diff2 == 0) <= 1)):
        count2 += 1
        print(level, "safe, rmv")
    

print(count, count2)
