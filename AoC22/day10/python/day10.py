import numpy as np

with open('input.txt', 'r') as f:
    lines = [x.strip('\n') for x in f.readlines()]

vals = []
x_val = 1
during = 1
after = 1

crt = np.array([['.' for i in range(40)] for j in range(6)])

for line in lines:
    if line != 'noop':
        amt = line.split(' ')[1]
        x_val += int(amt)
        after = x_val
        vals.append((during, after))

    vals.append((during, after))
    during = after

print(sum([vals[i - 1][0] * i for i in range(20, 221, 40)]))

sprite = 1

for i in range(len(vals) - 1):
    pixel = i % 40
    row = i // 40

    if (sprite - 1 <= pixel <= sprite + 1):
        crt[row][pixel] = '#'

    sprite = vals[i + 1][0]

for line in crt:
    print(''.join(line))
