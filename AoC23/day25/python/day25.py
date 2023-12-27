import re

with open('../input.txt') as f:

    input_data = [re.findall('[A-Za-z]{3}', x) for x in f.readlines()]

print(input_data)
