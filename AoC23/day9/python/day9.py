with open('../input.txt') as f:
    input_data = [[int(z) for z in y] for y in [x.strip().split() for x in f.readlines()]]

def calculate_diff(line):
    diffs = []

    for i in range(1, len(line)):
        diffs.append(line[i] - line[i - 1])

    return diffs

def calculate_diffs(line):
    diffs = []
    new_diff = line

    while not all(diff == 0 for diff in new_diff):
        new_diff = calculate_diff(new_diff)

        diffs.append(new_diff)

    return diffs

def calculate_next_value(diffs):
    diffs[len(diffs) - 1].append(0)

    for i in range(len(diffs) - 2, -1, -1):
        diff= diffs[i]
        new_value = diff[len(diff) - 1] + diffs[i + 1][len(diffs[i + 1]) - 1]
        diff.append(new_value)


    return diffs

def calculate_previous_value(diffs):
    diffs[len(diffs) - 1].insert(0, 0)

    for i in range(len(diffs) - 2, -1, -1):
        diff = diffs[i]
        new_value = diff[0] - diffs[i + 1][0]
        diff.insert(0, new_value)

    return diffs

history_sum = 0
history_sum2 = 0

for line in input_data:
    dataset = []
    dataset.append(line)
    result = calculate_diffs(line)
    dataset.extend(result)

    new_data = calculate_next_value(dataset)
    new_value = new_data[0][len(new_data[0]) - 1]

    new_data_2 = calculate_previous_value(dataset)
    new_value_2 = new_data_2[0][0]

    history_sum += new_value
    history_sum2 += new_value_2


print(history_sum)
print(history_sum2)
