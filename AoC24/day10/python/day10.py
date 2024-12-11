import numpy as np

with open('../test1.txt') as f:
    topographic_map = np.array([[int(y) for y in x.strip()] for x in f.readlines()])

print(topographic_map)
