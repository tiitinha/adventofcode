with open("../input.txt") as f:
    input_data = [[int(y) for y in x.strip().split(',')] for x in f.readlines()]

print(input_data)
