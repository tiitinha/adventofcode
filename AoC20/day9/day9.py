import itertools
import time
from collections import deque

def getValues(inputFile) -> list:
    with open(inputFile) as f:
        lines = [int(l.strip()) for l in f.readlines()]
        return lines

def findTheFailure(numberList: list, preambleLength: int) -> int:
        for i, num in enumerate(numberList[preambleLength:]):
            pairwiseSums = [x + y for x, y in itertools.product(numberList[i:i + preambleLength], numberList[i:i + preambleLength])]
            if num  not in pairwiseSums:
                return num

def findWeakness(numberList: list, failedValue: int) -> tuple:
    rollingSum = 0
    rollingList = deque()
    dataStream = iter(numberList)
    while rollingSum != failedValue or len(rollingList) == 1:
        if rollingSum < failedValue:
            nextNumber = next(dataStream)
            rollingList.append(nextNumber)
            rollingSum += nextNumber
        elif rollingSum > failedValue:
            firstValue = rollingList.popleft()
            rollingSum -= firstValue

    return (min(rollingList) + max(rollingList))

values = getValues('input.txt')

failedValue = findTheFailure(values, 25)

print(failedValue)
print(findWeakness(values, failedValue))
