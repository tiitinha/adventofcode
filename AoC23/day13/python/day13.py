import numpy as np

def convert(data):
    output = []
    for char in data:
        if char == '#':
            output.append(1)
        else:
            output.append(0)
    return output

with open('../test.txt') as f:
    input_data = [np.array(([convert(z) for z in y] for y in [x.strip().split('\n')])) for x in f.read().split('\n\n')]

def check_horizontal_mirroring(pattern):
    return 0

def check_vertical_mirroring(pattern):
    return 0


number_sum = 0

print(input_data)
