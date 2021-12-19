with open('test.txt', 'r') as file:
    rawinput = file.readlines()
    data = [a for b in [y.strip().split(' ') for y in [item for subitem in [x.split('|') for x in rawinput] for item in subitem] if '\n' in y] for a in b]
    data2 = [x.strip() for x in rawinput]


def part1(input_array: list) -> int:
    lengths = [len(x) for x in input_array]

    count = 0

    for l in lengths:
        if l == 2 or l == 3 or l == 4 or l == 7:
            count += 1

    print(count)


def part2(input_array: list) -> int:
    for row in input_array:
        left, right = [x.strip().split() for x in row.split('|')]

        numbers = get_nums(left)

        print(numbers)

def check_sub_char(sub: list, sup: list) -> bool:
    return all(x in sup for x in sub)

def char_sub(x: list, y: list) -> list:
    temp = y[:]

    for a in x:
        if a in temp:
            temp.remove(a)
    return temp

def char_add(x: list, y: list) -> list:
    temp = y[:]

    for a in x:
        if a not in temp:
            temp.append(a)

    return sorted(temp)

def get_nums(input_row: list) -> list:

    row = [[y for y in sorted(x)] for x in input_row]

    numbers = [''] * 10

    for num in row:
        if len(num) == 2:
            numbers[1] = num
        elif len(num) == 3:
            numbers[7] = num
        elif len(num) == 4:
            numbers[4] = num
        elif len(num) == 7:
            numbers[8] = num

    for num in row:
        if len(num) == 5:
            if check_sub_char(numbers[1], num):
                numbers[3] = num
            elif check_sub_char(char_sub(numbers[1], numbers[4]), num):
                numbers[5] = num
            else:
                numbers[2] = num

    numbers[6] = char_add(char_sub(numbers[1], numbers[8]), numbers[5])
    numbers[9] = char_add(numbers[1], numbers[5])

    for x in numbers:
        if x not in numbers:
            numbers[0] = x

    return numbers

part1(data)
part2(data2)

