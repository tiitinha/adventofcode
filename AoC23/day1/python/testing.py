with open('../input.txt') as f:
    strings = f.read().split('\n')

digit_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8' ,'9']
result1, result2 = 0, 0
for string in strings:
    first, last = 0, 0

    for i in range(len(string)):
        if first == 0 and string[i].isdigit():
            first = string[i]
        if last == 0 and string[-i-1].isdigit():
            last = string[-i-1]
    result1 += int(first+last)

    lowest, highest = float('inf'), -1
    lowest_digit, highest_digit = 0, 0
    for digit_string in digit_strings:
        first_index = string.find(digit_string)
        try:
            last_index = string.rindex(digit_string)
        except:
            last_index = highest
        if (first_index >= 0 and first_index < lowest):
            lowest = first_index
            lowest_digit = digit_strings.index(digit_string) + 1
            lowest_digit = lowest_digit if lowest_digit <= 9  else lowest_digit - 9
        if (last_index >= 0 and last_index > highest):
            highest = last_index
            highest_digit = digit_strings.index(digit_string) + 1
            highest_digit = highest_digit if highest_digit <= 9  else highest_digit - 9

    result2 += int(str(lowest_digit) + str(highest_digit))

print(result1, result2)