from itertools import combinations

with open("../input.txt") as f:
    input_data = [[int(y) for y in x.split(',')] for x in f.readlines()]


all_pairs = combinations(input_data, 2)

largest = 0
largest_pair = ()

for first, second in all_pairs:
    area = abs(first[0] - second[0] + 1) * abs(first[1] - second[1] + 1)
    if area > largest:
        largest = area
        largest_pair = (first, second)

print(largest, largest_pair)
