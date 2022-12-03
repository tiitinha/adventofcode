
def calc_vals(commons):
    val_sum = 0

    for letter in commons:
        if letter.isupper():
            val_sum += ord(letter) - 64 + 26
        else:
            val_sum += ord(letter) - 96

    return val_sum

with open('input.txt', 'r') as f:
    rucksacks = [x.strip() for x in f.readlines()]

common = []

for rucksack in rucksacks:
    first_compartment = rucksack[: len(rucksack) // 2]
    second_compartment= rucksack[len(rucksack) // 2 :]

    common.extend(list(set(first_compartment) & set(second_compartment)))

pt_1 = calc_vals(common)

group_types = []

for i in range(2, len(rucksacks), 3):
    group_types.extend(list(set(rucksacks[i]) & set(rucksacks[i - 1]) & set(rucksacks[i - 2])))

pt_2 = calc_vals(group_types)

print(pt_1)
print(pt_2)
