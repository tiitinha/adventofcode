import re

maps = []
with open('../input.txt') as f:
    input_data = [x for x in f.read().strip().split('\n\n')]
    seeds = [int(x) for x in re.findall('([0-9]+)', input_data[0])]

    for input in input_data[1:]:
        mapping = input.split('\n')
        formatted_mapping = [z.split(' ') for y in [x.split('\n') for x in mapping[1:]] for z in y]
        maps.append(formatted_mapping)

seeds = [int(x) for x in seeds]
lowest_list = []

for seed in seeds:
    new_seed = seed
    for map in maps:
        for rng in map:
            source_start = int(rng[1])
            dest_start = int(rng[0])
            rng_width = int(rng[2])

            offset = dest_start - source_start

            if source_start <= new_seed < source_start + rng_width:
                new_seed = new_seed + offset
                break

    lowest_list.append(new_seed)

print(min(lowest_list))
