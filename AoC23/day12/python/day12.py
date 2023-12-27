with open('../input.txt') as f:
    input_data = [x.strip().split(' ') for x in f.readlines()]


for data, groups in input_data:
    numbers = [int(x) for x in groups.split(',')]
    
    
