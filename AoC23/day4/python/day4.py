import re
import math

with open('../input.txt') as f:
    cards = [x.strip() for x in f.readlines()]


res_sum = 0

for card in cards:
    splitted = card.split(':')
    winning, elfs = splitted[1].split('|')
    winning = re.findall('([0-9]+)', winning)
    elfs = re.findall('([0-9]+)', elfs)

    elfs_winning = [value for value in winning if value in elfs]

    points = math.pow(2, len(elfs_winning) - 1) if len(elfs_winning) > 0 else 0

    res_sum += points

print(res_sum)
