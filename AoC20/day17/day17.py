import numpy as np

def run_cycle(inputdata, layers: int):
    cubexet = []

    for x in range(len(inputdata)):
        for y in range(len(inputdata[0])):
            for z in range(layers):
                count_neighbors((x, y, z), inputdata)
    return cubexet

def count_neighbors(coordinates, space):
    count = 0
    for x in range(coordinates[0] - 1, coordinates[0] + 2):
        for y in range(coordinates[1] - 1, coordinates[1] + 2):
            for z in range(coordinates[2] - 1, coordinates[2] + 2):
                if not (x == coordinates[0] and y == coordinates[1] and z == coordinates[2]):
                    count += space[x][y][z] == '#'

    return count

with open('input.txt') as f:
    # vedä np arrayn sisään toi
    inputdata = [l.strip('\n') for l in f.read().split('\n')]

print(inputdata)
run_cycle(inputdata, 1)
