with open('../input.txt') as f:
    input_data = [x.strip().split(' ') for x in f.readlines()]


for data, numbers in input_data:
    print(data, numbers)
