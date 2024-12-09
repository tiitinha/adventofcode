import numpy as np
from collections import defaultdict
from itertools import combinations

with open('../test.txt') as f:
    antenna_map = np.array([list(x.strip()) for x in f.readlines()])

antenna_dict = defaultdict(list)

for j, row in enumerate(antenna_map):
    for i, cell in enumerate(row):
        if cell != '.':
            antenna_dict[cell].append((j, i))


for antenna in antenna_dict.keys():
    antennas = antenna_dict[antenna]
    
    combs = list(combinations(antennas, 2))

    print(combs)

