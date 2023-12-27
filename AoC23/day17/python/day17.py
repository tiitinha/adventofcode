import numpy as np

with open('../test.txt') as f:
    input_data = np.array([[int(y) for y in x.strip()] for x in f.readlines()])

print(input_data)

def get_neighbors(current_point, count_to_current_dir, direction):
    pass

count_to_current_dir = 0
direction = (0, 1)

while current_point != finnish:
    neighbors = get_neighbors(current_point, count_to_current_dir, direction)

current_point = (0, 0)
visited = [(0, 0)]
finnish = (len(input_data) - 1, len(input_data[0] - 1))

result = sum([input_data[y][x] for y, x in path])

print(result)
