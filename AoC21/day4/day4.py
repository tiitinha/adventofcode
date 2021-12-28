import re
import time

with open('input.txt', 'r') as file:
    inputdata = [x.strip() for x in file.read().split('\n\n')]

    numbers = [int(x) for x in inputdata[0].split(',')]

    tables = [[[int(x) for x in row.split()] for row in t.split('\n')] for t in inputdata[1:]]


def get_table_score(numbers: list, table: list) -> int:

    bingocheck = [[0 for x in range(len(table[0]))] for y in range(len(table))]

    for i, number in enumerate(numbers):
        for j, row in enumerate(table):
            if number in row:
                bingocheck[j][row.index(number)] = 1
            if all(x == 1 for x in bingocheck[j]):
                filtered_table = [x for x in [num for sublist in table for num in sublist] if x not in numbers[:i + 1]]

                return sum(filtered_table) * number, number, i, filtered_table
            for col in range(len(table[0])):

                column = [y[col] for y in bingocheck]

                if all(x == 1 for x in column):
                    filtered_table = [x for x in [num for sublist in table for num in sublist] if x not in numbers[:i + 1]]

                    return sum(filtered_table) * number, number, i, filtered_table


def test(numbers: list, tables: list):
    print(get_table_score(numbers, tables[2]))

def solve(numbers: list, tables: list) -> list:
    results = []

    for table in tables:
        results.append(get_table_score(numbers, table))

    return results

results = solve(numbers, tables)


a1 = min(results, key = lambda x: x[2])[0]
a2 = max(results, key = lambda x: x[2])[0]


print(a1, a2)
