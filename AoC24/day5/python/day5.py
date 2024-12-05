from collections import defaultdict
from functools import cmp_to_key

def follows_rules(value, next_vals, rules):
    for val in next_vals:
        if value in rules[val]:
            return False

    return True

def update_follows_rules(update, rules):
    for i in range(len(update)):
        next_vals = update[i + 1:]
        value = update[i]
        if not follows_rules(value, next_vals, rules):
            return False

    return True

with open('../input.txt') as f:
    rules, updates = f.read().split('\n\n')

rules = [[int(y) for y in z] for z in [x.split('|') for x in rules.split('\n')]]
rule_dict = defaultdict(list)

def comparator(x, y):
    if y in rule_dict[x]:
        return -1

    if x in rule_dict[y]:
        return 1

    return 0

for rule in rules:
    first, second = rule
    rule_dict[first].append(second)

updates = [[int(x) for x in z] for z in [y.split(',') for y in updates.strip().split('\n')]]

sum = 0
sum2 = 0
for update in updates:
    if update_follows_rules(update, rule_dict):
        sum += update[len(update) // 2]
    else:
        reordered_update = sorted(update, key = cmp_to_key(comparator))
        sum2 += reordered_update[len(reordered_update) // 2]

print(sum)
print(sum2)
