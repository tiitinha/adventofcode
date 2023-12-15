with open('../input.txt') as f:
    input_data = f.read().strip('\n').split(',')

print(input_data)

total = 0

for line in input_data:
    print(line)
    current_value = 0
    for char in line:
        ascii_val = ord(char)
        current_value += ascii_val
        current_value *= 17
        current_value %= 256

    print(current_value)
    total += current_value

print(total)
