def placeSearchAlgo(file = 'input5.txt'):

    data = open(file)

    seatIds = []
    binaryDict = {'low': ['F', 'L'], 'high': ['B', 'R']}

    for line in data:
        row = binarySearchAlgo(128, line[:7], binaryDict)
        col = binarySearchAlgo(8, line[7:], binaryDict)

        seatId = (row - 1) * 8 + (col - 1)
        seatIds.append(seatId)

    return seatIds


def binarySearchAlgo(max, string, rules):
    lowerBound = 0
    higherBound = max

    for char in string:
        if char in rules['low']:
            higherBound = lowerBound + (higherBound - lowerBound) / 2
        elif char in rules['high']:
            lowerBound += (higherBound - lowerBound) / 2

    return higherBound

def freeSeat(seatIds):
    for i in range(0, 127 * 8):
        if i not in seatIds and (i + 1) in seatIds and (i - 1) in seatIds:
            return i


seatIds = placeSearchAlgo()
seatIds.sort()
print(seatIds)
print(freeSeat(seatIds))
