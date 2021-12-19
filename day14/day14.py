from collections import defaultdict

with open('input.txt', 'r') as file:
    polymer, rules = file.read().split('\n\n')

    rules = {key: value for (key, value) in [x.split(' -> ') for x in rules.strip().split('\n')]}


def polymerize(polymer: str, rules: dict, generations: int) -> dict:

    count = defaultdict()
    letter_count = {x: 0 for x in rules.values()}

    for j in range(len(polymer) - 1):
        pair = polymer[j: j + 2]

        if pair not in count.keys():
            count[pair] = 1
        else:
            count[pair] += 1

    for i in range(generations):
        temp_count = defaultdict()
        temp_letter = {x: 0 for x in rules.values()}

        for j, pair in enumerate(count):
            first = pair[0] + rules[pair]
            second = rules[pair] + pair[1]

            temp_letter[first[0]] += count[pair]
            temp_letter[first[1]] += count[pair]

            if first not in temp_count.keys():
                temp_count[first] = count[pair]
            else:
                temp_count[first] += count[pair]

            if second not in temp_count.keys():
                temp_count[second] = count[pair]
            else:
                temp_count[second] += count[pair]

        count = temp_count
        letter_count = temp_letter

    return(count, letter_count)


pair_count, letter_count = polymerize(polymer, rules, 40)
print(pair_count)
print(max(letter_count.values()) + 1 - min(letter_count.values()))
#element_count(pair_count)

