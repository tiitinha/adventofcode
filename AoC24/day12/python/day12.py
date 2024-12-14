import numpy as np

with open('../input.txt') as f:
    input_data = np.array([[y for y in x.strip()] for x in f.readlines()])

print(input_data)
