import numpy as np

next_letter = {
    'X': 'M',
    'M': 'A',
    'A': 'S'
}

def get_neighbors(x, y, value, input):
    x_vals = [x + i for i in range(-1, 2) if (x + i >= 0) & (x + i < len(input[0]))]
    y_vals = [y + i for i in range(-1, 2) if (y + i >= 0) & (y + i < len(input))]

    print(x, y, value)

    return [(i, j) for i in x_vals for j in y_vals if (input[j][i] == next_letter[value]) & (not(i == x & y == j))]

with open('test.txt') as f:
    input = np.array([list(x.strip()) for x in f.readlines()])

count = 0

for j in range(len(input)):
    for i in range(len(input[0])):
        if input[j][i] == 'X':
            vals = get_neighbors(i, j, input[j][i], input)
            print(vals)
