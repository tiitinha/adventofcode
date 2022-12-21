from copy import deepcopy
import re

ops = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '/': lambda x, y: x / y,
    '-': lambda x, y: x - y,
    '=': lambda x, y: (x, y)
}

def calculate(monke: str, monkes: dict) -> int:
    monkedict = deepcopy(monkes)
    op = monkedict[monke]

    if isinstance(op, int):
        return op

    if op.isnumeric():
        return int(op)

    first, math_op, second = op.split(' ')

    first_val = calculate(first, monkedict)
    second_val = calculate(second, monkedict)

    monkedict[first] = first_val
    monkedict[second] = second_val

    res = ops[math_op](first_val, second_val)

    return res
    

with open('input.txt', 'r') as f:
    monkes = {x: y for (x, y) in [x.strip().split(': ') for x in f.readlines()]}
    
    monkes2 = deepcopy(monkes)
    monkes2['root'] = re.sub('[\+\-\*\/]', '=', monkes['root'])

    lbound = 0
    ubound = 10_000_000_000_000

    while True:
        mid_point = int((ubound + lbound) // 2)

        monkes2['humn'] = mid_point

        res = calculate('root', monkes2)

        print(res)

        if res[0] > res[1]:
            lbound = mid_point
        elif res[0] < res[1]:
            ubound = mid_point
        else:
            print(mid_point)
            break


print(calculate('root', monkes))
# print(calculate('root', monkes2))
