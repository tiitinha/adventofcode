import numpy as np

with open('../input.txt') as f:
    input_data = [[[int(z) for z in y.split(', ')] for y in x.strip().split(' @ ')] for x in f.readlines()]

def form_line(point, velocity):
    a = velocity[1] / velocity[0]
    b = point[1] - point[0] * a

    return a, b

def solve_intercept(line, line_2):
    a_1 = line[0]
    a_2 = line_2[0]
    b_1 = line[1]
    b_2 = line_2[1]

    if (a_1 - a_2 == 0):
        return None
    
    x_res = (b_2 - b_1) / (a_1 - a_2)
    y_res = (a_1 * x_res) + b_1

    return (x_res, y_res)

def in_future(hail_1, hail_2, ic):
    hail_1_future = (np.array(hail_1[0][0][:2]) - np.array(ic)) * np.array(hail_1[0][1][:2])
    hail_2_future = (np.array(hail_2[0][0][:2]) - np.array(ic)) * np.array(hail_2[0][1][:2])

    return all(hail_1_future <= 0) and all(hail_2_future <= 0)

def in_test_zone(ic, test_zone):
    return test_zone[0][0] <= ic[0] <= test_zone[0][1] and test_zone[1][0] <= ic[1] <= test_zone[1][1]

hails = []
count = 0
test_zone_input = ((200000000000000, 400000000000000), (200000000000000, 400000000000000))
test_zone_test = ((7, 27), (7, 27))

for hail in input_data:
    a, b = form_line(hail[0], hail[1])
    hails.append((hail, (a, b)))

for i in range(len(input_data)):
    for j in range(i + 1, len(input_data)):
        hail_1 = hails[i]
        hail_2 = hails[j]
        ic = solve_intercept(hail_1[1], hail_2[1])

        count += 1 if ic and in_future(hail_1, hail_2, ic) and in_test_zone(ic, test_zone_input) else 0

print(count)
