import numpy as np

with open('../test.txt') as f:
    input_data = np.array([[y for y in x.strip()] for x in f.readlines()])

print(input_data)

start_point = (0, np.where(input_data[0] == '.')[0][0])


print(start_point)
