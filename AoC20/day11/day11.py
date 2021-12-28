import numpy as np
import copy
import time

def timer(func):
    def wrap(*args, **kwargs):
        start = time.process_time()
        ret = func(*args, **kwargs)
        end = time.process_time()
        print(end - start)
        return ret
    return wrap


def load_data(inputFile):
    with open(inputFile) as f:
        array = np.array([list(l.strip('\n')) for l in f])

    return array

def get_seats(list_of_seats):
    helper_seats = copy.deepcopy(list_of_seats)
    changed = 0
    ibound = list_of_seats.shape[0]
    jbound = list_of_seats.shape[1]

    for x, y in np.ndindex(list_of_seats.shape):
        seat = list_of_seats[x, y]
        neighbor_count = get_neighbors(list_of_seats, x, y, ibound, jbound, 1)

        if neighbor_count == 0 and seat == 'L':
            helper_seats[x, y] = '#'
            changed += 1
        elif neighbor_count >= 4 and seat == '#':
            helper_seats[x, y] = 'L'
            changed += 1

    if changed == 0:
        return (helper_seats == '#').sum()
    else:
        return get_seats(helper_seats)

def get_neighbors(seats, x, y, ibound, jbound, rng):
    count = 0
    for i in range(x - rng, x + rng + 1):
        for j in range(y - rng, y + rng + 1):
            if (x == i and y == j):
                continue
            if ((i >= 0 and j >= 0) and (i < ibound  and j < jbound)):
                count += seats[i, j] == '#'
    return count

def get_neighbors_diag(seats, x, y, ibound, jbound):
    pass

def get_neighbors_row(seats, x, y, ibound, jbound):
    pass

def get_neighbors_col(seat, x, y, ibound, jbound):
    pass

def check_all_directions(seats, x, y):
    pass


data = load_data('input.txt')
start = time.process_time_ns()
occupied_seats = get_seats(data)
end = time.process_time_ns()
print(occupied_seats)
print(end - start)
