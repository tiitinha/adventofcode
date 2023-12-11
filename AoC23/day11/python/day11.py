import numpy as np
from itertools import combinations

def already_checked(galaxy, galaxy2, checked):
    return (galaxy, galaxy2) in checked or (galaxy2, galaxy) in checked

with open('../input.txt') as f:
    input_data = np.array([[z for z in y] for y in [x.strip() for x in f.readlines()]])

galaxies = [(y, x) for x in range(len(input_data[0])) for y in range(len(input_data)) if input_data[y][x] == '#']

rows = [False for _ in range(len(input_data))]
cols = [False for _ in range(len(input_data[0]))]

for i, row in enumerate(input_data):
    rows[i] = all([x == '.' for x in row])

for j, col in enumerate(input_data.T):
    cols[j] =  all([x == '.' for x in col])


def shift_galaxies(galaxies, amt):
    new_galaxies = []
    for galaxy in galaxies:
        # count how may new rows and cols should be added before the galaxy
        rows_added = sum(rows[:galaxy[0]])
        cols_added = sum(cols[:galaxy[1]])

        new_galaxy = (galaxy[0] + rows_added * amt, galaxy[1] + cols_added * amt)
        new_galaxies.append(new_galaxy)

    return new_galaxies

def calc_distances(galaxies):

    dist_sum = 0
    combs = combinations(galaxies, 2)

    for g in combs:
        dist = abs(g[0][0] - g[1][0]) + abs(g[0][1] - g[1][1])
        dist_sum += dist

    print(dist_sum)

pt1 = shift_galaxies(galaxies, 1)
pt2 = shift_galaxies(galaxies, 999999)

calc_distances(pt1)
calc_distances(pt2)
