import re
import numpy as np

with open('test.txt', 'r') as file:
    raw_coordinates, raw_folds = file.read().split('\n\n')

coordinates = [[int(y) for y in z] for z in [x.split(',') for x in raw_coordinates.split('\n')]]
folds = [z.split('=') for z in [re.search(r'([x|y]=\d)', x).group() for x in raw_folds.strip().split('\n')]]

def get_max_coordinates(coordinates: list) -> tuple:
    max_x = 0
    max_y = 0

    for coordinate in coordinates:
        x, y = coordinate

        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y

    return max_x, max_y

def draw_paper(coordinates: list) -> list:

    max_x, max_y = get_max_coordinates(coordinates)

    table = np.array([['.' for y in range(max_y)] for x in range(max_x)])

    for coordinate in coordinates:
        table[coordinate[0] - 1, coordinate[1] - 1] = '#'

    return(table)


def fold(folds: list, paper: list) -> int:
    for fold in folds:
        axis = fold[0]
        coordinate = int(fold[1])

        if axis == 'x':
            folded_to = paper[0:coordinate, :]
            folded_on = np.flipud(paper[coordinate + 1:, :])
        else:
            folded_to = paper[:, 0:coordinate]
            folded_on = np.fliplr(paper[:, coordinate + 1:])

        if len(folded_to) > len(folded_on):
            pass


paper = draw_paper(coordinates)

fold(folds, paper)
