import numpy

def getData(inputFile):
    with open(inputFile, 'r') as f:
        return sorted([int(joltage.strip('\n')) for joltage in f.read().split('\n')])


def chainOfAdapters(inputList):
    diffs = []
    lastNum = 0
    for n in inputList:
        diffs.append(n - lastNum)
        lastNum = n
    diffs.append(3)
    return diffs

def findArrays(dif):
    temp = []
    mult = []

    for n in dif:
        if n != 3:
            temp.append(n)
        elif n == 3:
            if len(temp) > 3:
                mult.append((len(temp) - 1) * 2 + len(temp) - 3)
            elif len(temp) > 1:
                mult.append((len(temp) - 1) * 2)
            temp = []

    return numpy.prod(mult)

data = getData('input.txt')
dif = chainOfAdapters(data)
part1 = dif.count(1) * dif.count(3)
part2 = findArrays(dif)

print(part1)
print(part2)
