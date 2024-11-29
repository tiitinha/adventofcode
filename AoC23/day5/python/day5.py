import re
import numpy as np

maps = []
with open('../test.txt') as f:
    input_data = [x for x in f.read().strip().split('\n\n')]
    seeds = [int(x) for x in re.findall('([0-9]+)', input_data[0])]

    for input in input_data[1:]:
        mapping = input.split('\n')
        formatted_mapping = [z.split(' ') for y in [x.split('\n') for x in mapping[1:]] for z in y]
        maps.append(formatted_mapping)

    seed_ranges = []

    i = 0

    while i < len(seeds) - 1:
        seed_range = (seeds[i], seeds[i + 1])
        seed_ranges.append(seed_range)

        i += 1

    print(seed_ranges)

def get_mapped_value(value, rng):
    source_start = int(rng[1])
    dest_start = int(rng[0])
    rng_width = int(rng[2])

    offset = dest_start - source_start

    if source_start <= value < source_start + rng_width:
        return value + offset

    return None

def part1(seeds):
    seeds = [int(x) for x in seeds]
    lowest = np.inf

    for seed in seeds:
        new_seed = seed
        for map in maps:
            for rng in map:
                new_seed_val = get_mapped_value(new_seed, rng)

                if new_seed_val:
                    break
            if not new_seed_val:
                new_seed_val = new_seed
        
            new_seed = new_seed_val

        lowest = new_seed if new_seed < lowest else lowest

def part2()

print(part1(seeds))

