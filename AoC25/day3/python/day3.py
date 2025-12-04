with open("../test.txt") as f:
    batteries = [x.strip() for x in f.readlines()]

joltage = 0

for battery in batteries:
    battery_vals = [int(x) for x in battery]
    largest_val = max(battery_vals)
    max_index = battery_vals.index(largest_val)

    if (max_index == len(battery_vals) - 1):
        second_val = max(battery_vals[:-1])
        joltage += second_val * 10 + largest_val
    else:
        second_val= max(battery_vals[max_index + 1:])
        joltage += largest_val * 10 + second_val

print(joltage)
