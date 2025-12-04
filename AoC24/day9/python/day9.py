with open('../test.txt') as f:
    data = [int(x) for x in f.read().strip()]
files = []
frees = []

def get_last_not_empty(lst):
    for i in range(1, len(lst)):
        if lst[-i] != '.':
            return len(lst) - i

for i in range(0, len(data) - 1, 2):
    files.append(data[i])
    frees.append(data[i + 1])

memory_space = []
idx = 0

for i, val in enumerate(data):
    if i % 2 == 0:
        memory_space.extend([idx] * val)
        idx += 1
    else:
        memory_space.extend(['.'] * val)

first_empty = memory_space.index('.')
dots = memory_space.count('.')
last_not_empty = get_last_not_empty(memory_space)

#print(memory_space, first_empty, dots)
#print(len(memory_space) - dots)

while first_empty != (len(memory_space) - dots):
    movable = memory_space[last_not_empty]
    memory_space[last_not_empty] = '.'
    memory_space[first_empty] = movable

    first_empty = memory_space.index('.')
    last_not_empty -= 1

checksum = 0
for i, val in enumerate(memory_space):
    if val == '.':
        break
    
    checksum += i * val

print(checksum)
