import numpy as np
from collections import defaultdict
from itertools import combinations

def get_antinodes(point_1, point_2, distance):
    first = (point_1[0] + distance[0], point_1[1] + distance[1])
    second = (point_2[0] + distance[0], point_2[1] + distance[1])

def get_distance(point_1, point_2):
    y = abs(point_1[0] - point_2[0])
    x = abs(point_1[1] - point_2[1])
    return (y, x)

def points_on_same_line(point_1, point_2):
    return True

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

    for comb in combs:
        if points_on_same_line(comb[0], comb[1]):
            distance = get_distance(comb[0], comb[1])
            antinodes = get_antinodes(comb[0], comb[1], distance)

