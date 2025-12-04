import numpy as np

def map_key(key_input):
    return []

def map_lock(lock_input):
    return []

with open('../input.txt') as f:
    input_data = [x.split('\n') for x in f.read().strip().split('\n\n')]

keys = []
locks = []

for input_map in input_data:
    input_array = np.array([[y for y in x] for x in input_map])
    print(input_array)
    if np.all(input_array[0] == '#'):
        key = map_key(input_array)
        keys.append(key)
    else:
        lock = map_lock(input_array)
        locks.append(lock)
