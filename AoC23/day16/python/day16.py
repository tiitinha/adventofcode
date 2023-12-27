import numpy as np

with open('../test.txt') as f:
    input_data = np.array([[y for y in x.strip()] for x in f.readlines()])

collider_mapper = {
    '|': np.array([[1, 0], [-1, 0]]),
    '-': np.array([[0, 1], [0, -1]]),
    '/': np.array([[0, -1], [1, 0]]),
    '\\': np.array([[0, 1], [-1, 0]])
}

beams = []
visited = []

#beams.append()

print(input_data)


while beams:
    beam = beams.pop(0)

    new_visited, new_beams = get_new_beams_and_visited(beam)

    visited.extend(new_visited)
    beams.extend(new_beams)

print(len(visited))
