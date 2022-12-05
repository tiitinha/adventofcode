import re
import copy

def move(n, origin, destination, stacks):

    for i in range(n):
        first = stacks[origin - 1].pop()
        stacks[destination - 1].append(first)

    return stacks

def movept2(n, origin, destination, stacks_pt2):
    to_be_moved = []

    if n < len(stacks_pt2[origin - 1]):
        to_be_moved.extend(stacks_pt2[origin - 1][-n:])
        del stacks_pt2[origin - 1][-n:]
    else:
        to_be_moved.extend(stacks_pt2[origin - 1])
        stacks_pt2[origin - 1].clear()

    stacks_pt2[destination - 1].extend(to_be_moved)

    return stacks_pt2

with open('input.txt', 'r') as f:
    stacks_raw, raw_instructs = f.read().split('\n\n')

    instructs = [re.findall(r'(\d+)', x) for x in raw_instructs.strip('\n\n').split('\n')]

stacks = [ [] for _ in range(9)]

for line in stacks_raw.split('\n')[:-1]:
    for i in range(0, 9):
        char = line[1 + i * 4]
        if char != ' ':
            stacks[i].insert(0, char)

stacks_pt2 = copy.deepcopy(stacks)

for n, o, d in instructs:
    stacks = move(int(n), int(o), int(d), stacks)
    stacks_pt2 = movept2(int(n), int(o), int(d), stacks_pt2)

res = ''
res_pt2 = ''

for s in stacks:
    res += s[len(s) - 1]

for s2 in stacks_pt2:
    if len(s2) > 0:
        res_pt2 += s2[len(s2) - 1]

print(res)
print(res_pt2)
