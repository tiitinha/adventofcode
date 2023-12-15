import numpy as np
import time

with open('../input.txt') as f:
    input_data = np.array([[y for y in x.strip()] for x in f.readlines()])

rolling_rocks = []
solid_rocks = []
length = len(input_data)

def get_northest_possible_point(stone):
    x_axis = stone[1]
    y_value = stone[0]

    if y_value == 0:
        return stone

    while True:
        if y_value == 0 or (y_value - 1, x_axis) in solid_rocks or (y_value - 1, x_axis) in new_rolling_rock_points:
            break
        y_value -= 1
    return (y_value if y_value >= 0 else 0, x_axis)


for i in range(len(input_data.T)):
    for j in range(len(input_data.T[0])):
        input = input_data[j][i]

        if input == 'O':
            rolling_rocks.append((j, i))

        if input == '#':
            solid_rocks.append((j, i))


new_rolling_rock_points = []

start = time.time()
for stone in rolling_rocks:
    new_position = get_northest_possible_point(stone)

    new_rolling_rock_points.append(new_position)
end = time.time()

print(end-start)

result = sum([length - x[0] for x in new_rolling_rock_points])
print(result)
