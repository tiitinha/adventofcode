
with open('input.txt') as f:
    lines = [x for x in f.read().split('\n\n')]

calories = []

for x in lines:
    vals = [int(y) for y in x.strip().split('\n')]

    elf_sum = sum(vals)

    calories.append(elf_sum)

calories.sort(reverse = True)

part1_result = max(calories)

part2_result = sum(calories[:3])

print(part1_result)

print(part2_result)
