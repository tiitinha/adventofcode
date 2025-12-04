import re
from collections import defaultdict
from operator import itemgetter

with open('../input.txt') as f:
    initials, mapping = f.read().strip().split('\n\n')
    initials = [x.split(': ') for x in initials.split('\n')]
    mapping_list = [re.split('\s+->\s+|\s+', x) for x in mapping.split('\n')]

memory_mapping = defaultdict(None)

def map_exists(mapping):
    return memory_mapping.get(mapping[0]) != None and memory_mapping.get(mapping[2]) != None

for initial in initials:
    memory_mapping[initial[0]] = int(initial[1])

while True:
    if not mapping_list:
        break

    mapping = mapping_list.pop(0)

    if map_exists(mapping):
        first = bool(memory_mapping[mapping[0]])
        second = bool(memory_mapping[mapping[2]])
        destination = mapping[3]
        operator = mapping[1]

        if operator == 'AND':
            memory_mapping[destination] = first & second
        if operator == 'OR':
            memory_mapping[destination] = first | second
        if operator == 'XOR':
            memory_mapping[destination] = first ^ second
    else:
        mapping_list.append(mapping)

bits = [(k, v) for (k, v) in memory_mapping.items() if k.startswith('z')]

sorted_bits = sorted(bits, key=itemgetter(0))

binary = []
for bit in sorted_bits:
    if bit[1]:
        binary.insert(0, '1')
    else:
        binary.insert(0, '0')


binary_num = ''.join(binary)
print(int(binary_num, 2))
