def bit_calculator(input_array: list, length: int) -> tuple:
    result = [0] * length

    for i in range(len(input_array)):
        for j in range(0, length):
            if input_array[i][j] == '0':
                result[j] -= 1
            else:
                result[j] += 1

    binary = ''.join(['1' if x >= 0 else '0' for x in result])
    bitwise_xor = ''.join(['0' if x >= 0 else '1' for x in result])

    return binary, bitwise_xor

def pt1(input_array: list, length: int) -> int:
    binary, bitwise_xor = bit_calculator(input_array, length)

    first = int(binary, 2)
    second = int(bitwise_xor, 2)

    return first * second


def pt2(input_array: list, length: int) -> int:
    first, second = bit_calculator(input_array, length)

    print(first, second)

    result = bitfilter(input_array, first, 0, True)[0]
    result2 = bitfilter(input_array, second, 0, False)[0]

    print(result, result2)

    fin = int(result, 2) * int(result2, 2)

    return fin

def bitfilter(input_array: list, filter: str, index: int, oxy: bool) -> str:

    templist = []
    result = []

    if len(input_array) > 1:
        for i, x in enumerate(input_array):

            if x[index] == filter[index]:
                templist.append(x)

        if oxy:
            filter = bit_calculator(templist, len(input_array[0]))[0]
        else:
            filter = bit_calculator(templist, len(input_array[0]))[1]

        result =  bitfilter(templist, filter, index + 1, oxy)
    else:
        result = input_array

    return result

with open('input.txt', 'r') as file:
    input_data = [x.strip() for x in file.readlines()]

print(pt1(input_data, len(input_data[0])))
print(pt2(input_data, len(input_data[0])))
