import re

count = 0

with open('input.txt', 'r') as f:
    for line in f:
        bits = re.findall('(\d+)-(\d+)\s(\w):\s(\w*)', line)
        firstValue = int(bits[0][0]) - 1
        secondValue = int(bits[0][1]) - 1
        ruleChar = bits[0][2]
        password = bits[0][3]

        if ((password[firstValue] == ruleChar) ^ (password[secondValue] == ruleChar)):
            count += 1

print(count)