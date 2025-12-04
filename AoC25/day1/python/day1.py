import math

with open("../test2.txt") as f:
    input_data = [(x[0], int(x[1:])) for x in f.readlines()]

current_value = 50
zero_count = 0
zero_count_2 = 0

for direction, val in input_data:
    clicks = math.copysign(1, ord(direction) - ord('R')) * val
    current_value += clicks
    zeros = int(abs(current_value // 100))

    if current_value < 0 and current_value % 100 == 0:
        zero_count_2 += 1

    current_value %= 100
   
    if current_value == 0:
        zero_count += 1
        
    zero_count_2 += zeros
    
print(zero_count, zero_count_2)
# 6671 (too low), 6779 (too high)
