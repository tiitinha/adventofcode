import re
import cmath
import numpy as np
import math

with open('../inpt.txt') as f:
    raw_input = f.readlines()

    time = [int(x) for x in re.findall('([0-9]+)', raw_input[0])]
    distance = [int(x) for x in re.findall('([0-9]+)', raw_input[1])]

def calc_res(race_time, race_distance):
    
    discriminant = (race_time ** 2) - (4 * 1 * (race_distance))

    sol_1 = math.floor((race_time - cmath.sqrt(discriminant)).real / (2 * 1))
    sol_2 = math.ceil((race_time + cmath.sqrt(discriminant)).real / (2 * 1))

    ans = sol_2 - sol_1 - 1
    
    return ans

result = 1

for race in range(len(time)):
    possibilities = 0
    race_time = time[race]
    race_distance = distance[race]

    ans = calc_res(race_time, race_distance)

    result *= ans

print(result)

pt2_time = int(''.join([str(x) for x in time]))
pt2_dist = int(''.join([str(x) for x in distance]))

race_time_2 = calc_res(pt2_time, pt2_dist)

print(race_time_2)
