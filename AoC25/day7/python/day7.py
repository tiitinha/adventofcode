import numpy as np
from collections import defaultdict

with open("../input.txt") as f:
    tachyon_map = np.array([[y for y in x.strip()] for x in f.readlines()])
    
beams = set(zip(*np.where(tachyon_map == 'S')))
start = list(beams)[0]
splitters = list(zip(*np.where(tachyon_map == '^')))
width = len(tachyon_map[0]) - 1
height = len(tachyon_map) - 1

beam_dict = defaultdict(int)
beam_dict[start] += 1

print(beam_dict)

splits = 0
splits_2 = 0

for row in range(len(tachyon_map) - 1):
    next_beams = defaultdict(int)
    for current_beam in beam_dict.keys():
        cell_below = (current_beam[0] + 1, current_beam[1])
        if (tachyon_map[cell_below[0]][cell_below[1]] == "^"):
            left_beam = (cell_below[0], cell_below[1] - 1)
            right_beam = (cell_below[0], cell_below[1] + 1)

            splits += 1
            splits_2 += beam_dict[current_beam]

            next_beams[left_beam] += beam_dict[current_beam]
            next_beams[right_beam] += beam_dict[current_beam]
        else:
            next_beams[cell_below] += beam_dict[current_beam]
            
    beam_dict = next_beams

print(splits, splits_2)
