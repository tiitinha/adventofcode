import numpy as np
import re
from operator import mul
from functools import reduce
from math import prod

with open("../input.txt") as f:
    data = f.readlines()
    
numbers = np.array([[int(y) for y in re.findall(r'\d+', x)] for x in data[:-1]])
operations = re.findall(r'[*+]', data[-1])

result = 0

for i, column in enumerate(numbers.T):
    operation = operations[i]
    
    if operation == "*":
        result += reduce(mul, column, 1)

    if operation == "+":
        result += reduce(lambda x, y: x + y, column)

raw = [reversed(list(row.rstrip("\n"))) for row in data]
zipped = zip(*raw)
current_ops = []

result_2 = 0

for row in zipped:
    if (''.join(row).strip() == ''):
        continue
    if (row[-1] == ' '):
        current_ops.append(int(''.join(row)))
    else:
        current_ops.append(int(''.join(row[:-1])))
    if (row[-1] == '+'):
        result_2 += sum(current_ops)
        current_ops = []
    if (row[-1] == '*'):
        result_2 += prod(current_ops)
        current_ops = []

print(result_2)

