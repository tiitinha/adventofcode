from collections import defaultdict
import re
import copy

def mask_on(mask: str, value: int) -> int:
    binary_value = list(format(value, '036b'))

    for i, binary in enumerate(mask):
        if binary != 'X':
            binary_value[i] = mask[i]

    int_value = int(''.join(binary_value), 2)

    return int_value

def mask_on_two(mask: str, value: int) -> list:
    binary_value = list(format(value, '036b'))

    binary_values = []
    ready_vals = []

    ekses = [i for (i, b) in enumerate(mask) if b == 'X']
    ones = [i for (i, b) in enumerate(mask) if b == '1']

    for i, bit in enumerate(binary_value):
        if i in ones:
            binary_value[i] = '1'

    binary_values.append(binary_value)


    for i, bit in enumerate(binary_value):
        helper_values = []
        if i in ekses:
            for binray in binary_values:
                temp_binary1 = copy.deepcopy(binray)
                temp_binary2 = copy.deepcopy(binray)

                temp_binary1[i] = '0'
                temp_binary2[i] = '1'

                helper_values.append(temp_binary1)
                helper_values.append(temp_binary2)

                ready_vals.append(int(''.join(temp_binary1), 2))
                ready_vals.append(int(''.join(temp_binary2), 2))

        binary_values.extend(helper_values)

    return ready_vals



with open('input.txt', 'r') as f:
    values = defaultdict()
    values2 = defaultdict()

    for line in f:
        if 'mask' in line:
            mask = re.sub(r'\s', '', line.split("=")[1])
        else:
            address, value = re.findall(r'\[(\d*)\]\s=\s(\d*)', line)[0]
            #values[address] = mask_on(mask, int(value))
            address_list = mask_on_two(mask, int(address))

            for address in address_list:
                values2[address] = int(value)

    print(sum(values2.values()))
