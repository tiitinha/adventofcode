import re
from math import lcm, prod
from copy import deepcopy

def operate(old_val: int, operation: str) -> int:

    a, op, second = operation.lstrip().split(' ')

    if op == '+':
        if second == 'old':
            new_val = old_val + old_val
        else:
            new_val = old_val + int(second)
    else:
        if second == 'old':
            new_val = old_val * old_val
        else:
            new_val = old_val * int(second)

    return new_val

def run_rounds(n: int, monkeys: dict, div: bool = True) -> dict:

    modulo = lcm(*[monkey['test'] for monkey in monkeys])

    for i in range(n):

        for monkey in monkeys:
            while monkey['starting_items']:
                old_val = monkey['starting_items'].pop()
                new_val = operate(old_val, monkey['operation'])

                new_val = new_val // 3 if div else new_val % modulo

                throw_dest = monkey[new_val % monkey['test'] == 0]

                monkeys[throw_dest]['starting_items'].append(new_val)

                monkey['inspections'] += 1

    return monkeys

with open('input.txt', 'r') as f:
    lines = f.read().split('\n\n')

monkeys = [{} for _ in range(len(lines))]

for i, monkey in enumerate(lines):
    monkey_lines = monkey.split('\n')

    monkeys[i]['starting_items'] = [int(x) for x in re.findall(r'(\d+)', monkey_lines[1])]

    monkeys[i]['operation'] = monkey_lines[2].split('=')[1]
    monkeys[i]['test'] = int(re.search(r'(\d+)', monkey_lines[3]).group())
    monkeys[i][True] = int(re.search(r'(\d+)', monkey_lines[4]).group())
    monkeys[i][False] = int(re.search(r'(\d+)', monkey_lines[5]).group())
    monkeys[i]['inspections'] = 0

monkeys2 = deepcopy(monkeys)

pt_1_monkeys = run_rounds(20, monkeys)

vals = list(map(lambda x: x['inspections'], pt_1_monkeys))
vals.sort(reverse = True)
print(vals[0] * vals[1])


pt_2_monkeys = run_rounds(10000, monkeys2, False)

vals2 = list(map(lambda x: x['inspections'], pt_2_monkeys))
vals2.sort(reverse = True)
print(vals2)
print(vals2[0] * vals2[1])
