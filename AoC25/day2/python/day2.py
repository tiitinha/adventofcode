with open("../input.txt") as f:
    ranges = [(x.split("-")) for x in f.read().strip().split(",")]

res = 0
    
for min_val, max_val in ranges:
    for value in range(int(min_val), int(max_val) + 1):
        if len(str(value)) % 2 != 0:
            continue

        midpoint = len(str(value)) // 2
        first_half = str(value)[:midpoint]
        second_half = str(value)[midpoint:]

        if (first_half == second_half):
            res += value
        
print(res)

## part 2 --> find repeating pattern, must be of the same pattern --> lossless compression?
