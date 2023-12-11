import numpy as np
from copy import copy

direction_map = {
    '|': ((1, 0), (-1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((0, 1), (-1, 0)),
    'J': ((-1, 0), (0, -1)),
    '7': ((1, 0), (0, -1)),
    'F': ((0, 1), (1, 0)),
    '.': ((0, 0), (0, 0))
}

def is_valid_point(y, x, ylen, xlen):
    return y >= 0 and y < ylen and x >= 0 and x < xlen
    

def get_pipe_end_points(y, x):
    pipe_part = maze[y][x]
    directions = direction_map[pipe_part]
    end_points = [(y + d[0], x + d[1]) for d in directions]
    #print('ends: ', end_points)
    return end_points

def pt1(maze, start):
    neighbors = [(start[0] + y, start[1] + x) for y, x in [(y, x) for y in range(-1, 2) for x in range(-1, 2) if abs(x) != abs(y)] if is_valid_point(start[0] + y, start[1] + x, len(maze), len(maze[0]))]
    points = []


    for neighbor in neighbors:
        end_points = get_pipe_end_points(neighbor[0], neighbor[1])
        if start in end_points:
            points.append(neighbor)

    rounds = 1
    previous_first_point = start
    previous_second_point = start

    while points[0] != points[1]:
        temp_prev_first = points[0]
        temp_prev_second = points[1]
        points[0] = [x for x in get_pipe_end_points(points[0][0], points[0][1]) if x != previous_first_point][0]
        previous_first_point = temp_prev_first
        points[1] = [x for x in get_pipe_end_points(points[1][0], points[1][1]) if x != previous_second_point][0]
        previous_second_point = temp_prev_second
        rounds += 1

        if maze[points[0][0]][points[0][1]] == 'S':
            break

    print(rounds)


with open('../input.txt') as f:
    maze = np.array([[y for y in x.strip()] for x in f.readlines()])

y, x = [i for j in np.where(maze == 'S') for i in j]


pt1(maze, (y, x))
