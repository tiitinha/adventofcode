import numpy as np

with open('../test.txt') as f:
    input_data = np.array([[y for y in x.strip()] for x in f.readlines()])

distances = [float('inf') for y in range(len(input_data)) for x in range(len(input_data[0]))]


def get_neighbors(y, x):
    possible_neighbors = [(y + j, x + i) for j in range(-1, 2) for i in range(-1, 2) if y + j >= 0 and y + j < len(input_data) and x + i >= 0 and x + i < len(input_data[0]) and input_data[y + j][x + i] == '.']
    return possible_neighbors

start = np.argwhere(input_data == 'S')[0]

print(start)

q = [start]
visited = set()

while q:
    next = q.pop(0)
    
    print('next: ', next)
    
    visited.add((next[0], next[1]))

    neighbors = get_neighbors(next[0], next[1]) 

    print('neighbors: ', neighbors)

    q.extend(neighbors)

    if len(visited) >= 20:
        break
