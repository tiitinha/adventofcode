def calculate(input_array: list, aim_enabled: bool):

    depth = 0
    horizontal = 0
    aim = 0

    for dir, amt in input_array:
        if dir == 'forward':
            horizontal += amt
            if aim_enabled:
                depth += aim * amt
        elif dir == 'up':
            if aim_enabled:
                aim -= amt
            else:
                depth -= amt
        elif dir == 'down':
            if aim_enabled:
                aim += amt
            else:
                depth += amt

    return horizontal * depth

with open('input.txt', 'r') as file:
    input_data = [(x, int(y)) for x, y in [x.strip().split(' ') for x in file.readlines()]]


print(calculate(input_data, False))
print(calculate(input_data, True))
