import numpy as np

directions = [np.array([x, y]) for x in range(-1, 2) for y in range(-1, 2) if abs(x) != abs(y)]

with open('../test2.txt') as f:
    topographic_map = np.array([[int(y.replace('.', '-1')) for y in x.strip()] for x in f.readlines()])

def is_valid(point, previous):

    if np.any(point < 0) or np.any(point >= len(topographic_map)):
        return False

    value = topographic_map[point[0]][point[1]]
    previous_value = topographic_map[previous[0]][previous[1]]

    if value - previous_value == 1:
        #print(previous, previous_value, point, value)
        return True

    return False

def get_neighbors(point):
    value = topographic_map[point[0]][point[1]]
    neighbors = []

    for direction in directions:
        potential = point + direction
        if is_valid(potential, point):
            neighbors.append(np.array(potential))

    return neighbors

def find_path(point, visited):
    cnt = 0
    if topographic_map[point[0]][point[1]] == 9 and visited[point[0]][point[1]] == 0:
        cnt += 1
        visited[point[0]][point[1]] = 1
        return cnt, visited

    visited[point[0]][point[1]] = 1

    neighbors = get_neighbors(point)
    
    for neighbor in neighbors:
        count_val, visited = find_path(neighbor, visited)
        cnt += count_val

    return cnt, visited

zeros = [x for x in np.where(topographic_map == 0)]
starts = [(x[0], x[1]) for x in zip(zeros[0], zeros[1])]

count = 0
for start in starts:
    visited = np.full((len(topographic_map), len(topographic_map)), 0)
    count_val, visited = find_path(start, visited)
    count += count_val

print(count)
