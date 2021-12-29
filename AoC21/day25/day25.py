import numpy as np
import copy

with open('input.txt', 'r') as file:
    initial_map = np.array([[y for y in x] for x in file.read().strip().split('\n')])


def move_east(state: list) -> list:
    count = 0
    nu_state = copy.deepcopy(state)
    for i in range(len(state)):
        for j in range(len(state[0])):
            if j < (len(state[0]) - 1) and state[i][j] == '>' and state[i][j + 1] == '.':
                count += 1
                nu_state[i][j + 1] = '>'
                nu_state[i][j] = '.'
            elif j == (len(state[0]) - 1) and state[i][j] == '>' and state[i][0] == '.':
                count += 1
                nu_state[i][j] = '.'
                nu_state[i][0] = '>'

    return nu_state, count

def move_south(state: list) -> list:
    count = 0

    nu_state = copy.deepcopy(state)
    for i in range(len(state)):
        for j in range(len(state[0])):
            if i < (len(state) - 1) and state[i][j] == 'v' and state[i + 1][j] == '.':
                count += 1
                nu_state[i + 1][j] = 'v'
                nu_state[i][j] = '.'
            elif i == (len(state) - 1) and state[i][j] == 'v' and state[0][j] == '.':
                count += 1
                nu_state[0][j] = 'v'
                nu_state[i][j] = '.'

    return nu_state, count

def part1(init_state: list) -> list:
    round_count = 0
    while True:
        round_count += 1
        init_state, run = move_east(init_state)
        init_state, run_2 = move_south(init_state)


        if run == 0 and run_2 == 0:
            print(round_count)
            break

print(initial_map)
part1(initial_map)

