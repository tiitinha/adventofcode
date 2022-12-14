import ast
from itertools import zip_longest
from functools import cmp_to_key

with open('test.txt', 'r') as f:
    data = [list(map(eval, x.split())) for x in f.read().strip().split('\n\n')]


def compare(a, b):
    if a is None:
        return -1
    if b is None:
        return 1
    if isinstance(a, int) and isinstance(b, int):
        return -1 if a < b else 1 if b < a else 0
    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])

    for x, y in zip_longest(a, b):
        res = compare(x, y)

        if res == 0:
            continue
        return res

    return 0

part_1_count = 0

for i, (a, b) in enumerate(data):
    if compare(a, b) < 0:
        part_1_count += i + 1

print(part_1_count)

flattened_list = [message for pair in data for message in pair]
flattened_list.extend([[[2]], [[6]]])
flattened_list.sort(key = cmp_to_key(compare))
print((flattened_list.index([[2]]) + 1) * (flattened_list.index([[6]]) + 1))
