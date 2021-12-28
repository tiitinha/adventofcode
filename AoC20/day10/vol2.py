#!/usr/bin/env python

import fileinput
from collections import defaultdict

addapters = [0] + sorted(map(int, fileinput.input('input.txt')))
addapters.append(addapters[-1] + 3)

diffs = defaultdict(int)
counts = defaultdict(int, {0: 1})

print(list(zip(addapters[1:], addapters)))

for a, b in zip(addapters[1:], addapters):
    diffs[a - b] += 1
    # number of ways to reach i'th adapter from previous three possible ones
    counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]
    #print(diffs)
    #print(counts)

print(diffs[1] * diffs[3])
print(counts[addapters[-1]])