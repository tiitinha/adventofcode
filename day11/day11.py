import numpy as np

with open('test.txt', 'r') as file:
    initial_state = np.array([[int(y) for y in x.strip()] for x in file.readlines()])

    print(initial_state)


def run_round(state: list) -> list:

