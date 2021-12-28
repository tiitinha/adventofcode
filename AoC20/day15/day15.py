from collections import defaultdict
from copy import deepcopy
import time

real_input = [11, 18, 0, 20, 1, 7, 16]
testinput = [0, 3, 6]
testinput2 = [1, 3, 2]

def game(inputdata, top):
    stack = {val: index for index, val in enumerate(inputdata, start = 1)}

    all_numbers = deepcopy(inputdata)
    num = 0

    start = len(inputdata) + 1

    for i in range(start, top):
        all_numbers.append(num)
        if num in stack.keys():
            next_num = i - stack[num]
            stack[num] = i
            num = next_num
        else:
            stack[num] = i
            num = 0
    return num

start = time.perf_counter()
print(game(real_input, 30000000))
end = time.perf_counter()
print(end - start)
