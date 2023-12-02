mapping_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
mapping_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
mapping = mapping_nums + mapping_words

with open('../input.txt') as f:
    lines = f.readlines()

res_1, res_2 = 0, 0

for line in lines:
    first, last = 0, 0

    for i in range(len(line)):
        if first == 0 and line[i].isdigit():
            first = line[i]
        if last == 0 and line[-i - 1].isdigit():
            last = line[-i - 1]

    res_1 += int(f'{first}{last}')

    lowest, highest = len(line), -1
    lowest_val, highest_val = 0, 0

    for num in mapping:
        first_idx = line.find(num)
        last_idx = line.rfind(num)

        if first_idx >= 0 and first_idx < lowest:
            lowest = first_idx
            lowest_val = mapping.index(num) + 1
            lowest_val = lowest_val if lowest_val < 10 else lowest_val - 9
        
        if last_idx >= 0 and last_idx > highest:
            highest = last_idx
            highest_val = mapping.index(num) + 1
            highest_val = highest_val if highest_val < 10 else highest_val - 9

    res_2 += int(str(lowest_val) + str(highest_val))


print(res_1, res_2)
