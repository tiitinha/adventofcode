import re

maps = {}

with open('../input.txt') as f:
    input_data = [x for x in f.read().split('\n\n')]
    seeds = [int(x) for x in re.findall('([0-9]+)', input_data[0])]
    for input in input_data[1:]:
        mapping = input.split('\n')
        name = mapping[0]
        formatted_mapping = [x.split('\n') for x in mapping[1:]]
        maps[name] = formatted_mapping

print(seeds)
print(maps)
