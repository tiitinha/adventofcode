def countTrees(right, down):
    index = 0
    treeCount = 0

    f = [l.strip('\n') for l in open('input3.txt').readlines()]

    for i in range(0, len(f), down):
        line = f[i]
        rowLength = len(line)

        if index > rowLength - 1:
            index -= rowLength
        charCheck = line[index]

        if (charCheck == '#'):
            treeCount += 1

        index += right
    return treeCount

first = countTrees(1, 1)
second = countTrees(5, 1)
third = countTrees(7, 1)
fourth = countTrees(1, 2)
fifth = countTrees(3, 1)

print(f'{first}, {second}, {third}, {fourth}')

print(first * second * third * fourth * fifth)



