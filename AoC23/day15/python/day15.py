import re

with open('../input.txt') as f:
    input_data = f.read().strip('\n').split(',')
    print(input_data)
    pt2_input = [re.findall('[A-Za-z]+|[=|-]|[0-9]+', x) for x in input_data]
    print(pt2_input)

total = 0

def hash_value(input):
    current_val = 0

    for char in input:
        ascii_val = ord(char)
        current_val += ascii_val
        current_val *= 17
        current_val %= 256

    return current_val

for line in input_data:
    current_value = hash_value(line)

    total += current_value

print(total)

boxes = [{} for _ in range(256)]

for expression in pt2_input:
    hash_val = hash_value(expression[0])
    
    if expression[1] == '=':
        boxes[hash_val][expression[0]] = int(expression[2])

    if expression[1] == '-':
        boxes[hash_val].pop(expression[0], None)


total2 = 0

for i, box in enumerate(boxes):
    for j, focal in enumerate(box.values()):
        total2 += (i + 1) * (j + 1) * focal

print(total2)
