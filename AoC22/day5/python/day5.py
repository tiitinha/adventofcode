import re

def move(n, origin, destination, stacks):

    for i in range(n):
        first = stacks[origin - 1].pop()
        stacks[destination - 1].append(first)

    return stacks

def movept2(n, origin, destionation, stacks):
    pass

with open('input.txt', 'r') as f:
    stacks_raw, raw_instructs = f.read().split('\n\n')

    instructs = [re.findall(r'(\d+)', x) for x in raw_instructs.strip('\n\n').split('\n')]

stacks = [ [] for _ in range(9)]

for line in stacks_raw.split('\n')[:-1]:
    for i in range(0, 9):
        char = line[1 + i * 4]
        if char != ' ':
            stacks[i].insert(0, char)

for n, o, d in instructs:
    stacks = move(int(n), int(o), int(d), stacks)

res = ''

for s in stacks:
    res += s[len(s) - 1]

print(res)
