with open('input.txt', 'r') as f:
    rules = [[[int(c) for c in y.split(',')] for y in z] for z in [x.strip().split(' -> ') for x in f.readlines()]]


max_x = rules[0][0][0]
max_y = rules[0][0][1]
min_x = rules[0][0][0]
min_y = rules[0][0][1]

for rule in rules:
    for pair in rule:
        max_x = pair[0] if pair[0] > max_x else max_x
        max_y = pair[1] if pair[1] > max_y else max_y
        min_x = pair[0] if pair[0] < min_x else min_x
        min_y = pair[1] if pair[1] < min_y else min_y

print(max_x, max_y, min_x, min_y)
