with open('input.txt', 'r') as file:
    data = [x.strip('\n').split(' -> ') for x in file.readlines()]


def draw(data: list, size: int) -> list:
    oceanfloor = [[0 for x in range(size)] for y in range(size)]

    for row in data:

        start = [int(x) for x in row[0].split(',')]
        end = [int(x) for x in row[1].split(',')]

        if start[0] == end[0]:
            s = min(start[1], end[1])
            e = max(start[1], end[1])
            for i in range(s, e + 1):
                oceanfloor[i][start[0]] += 1
        elif start[1] == end[1]:
            s = min(start[0], end[0])
            e = max(start[0], end[0])
            for i in range(s, e + 1):
                oceanfloor[start[1]][i] += 1

    return oceanfloor

def calculate(table: list) -> int:

    counter = 0

    for x in range(len(table)):
        for y in range(len(table[0])):
            if table[x][y] > 1:
                counter += 1

    return counter


table = draw(data, 1000)
result = calculate(table)
