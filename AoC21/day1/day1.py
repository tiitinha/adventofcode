def counter(indexes: int, input_data: list):

    prev = sum(input_data[:indexes])
    count = 0

    for index in range(indexes - 1, len(input_data)):
        summation = sum(input_data[index : index + indexes])

        if summation > prev:
            count += 1

        prev = summation

    return count


def part1(input_list: list):
    print(counter(1, input_list))

def part2(input_list: list):
    print(counter(3, input_list))

list_input = []

with open(f'input.txt', 'r') as file:
    list_input = [int(x) for x in file.readlines()]

part1(list_input)
part2(list_input)
