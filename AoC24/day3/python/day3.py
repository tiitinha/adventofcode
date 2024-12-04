import re

with open('../input.txt') as f:
    instructions = f.read().strip()

muls = [x.group() for x in re.finditer(r'mul\(\d{1,3}\,\d{1,3}\)|(do\(\))|(don\'t\(\))', instructions)]

result = 0
result2 = 0
do = True

for mul in muls:
    if 'do' in mul:
        do = True
    if 'don\'t' in mul:
        do = False
    if 'mul' in mul:
        numbers = re.findall(r'\d+', mul)
        res = int(numbers[0]) * int(numbers[1])
        result += res
        if do:
            result2 += res

print(result)
print(result2)
