import numpy as np

with open('../input.txt') as f:
    input = np.array([list(x.strip()) for x in f.readlines()])

print(input)
