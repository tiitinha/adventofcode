with open("../input.txt") as f:
    fresh, available = f.read().strip().split("\n\n")
    fresh = sorted([tuple(int(y) for y in x.split("-")) for x in fresh.split("\n")])
    available = [int(x) for x in available.split("\n")]

fresh_count = 0

ranges = []
current_low = fresh[0][0]
current_high = fresh[0][1]

for low, high in fresh[1:]:
    if current_low <= low <= current_high:
        current_high = max(high, current_high)
        continue

    ranges.append([current_low, current_high])
    current_low = low
    current_high = high
ranges.append([current_low, current_high])

available_range = 0

for low, high in ranges:
    available_range += high - low + 1
    for ingredient in available:
        if low <= ingredient <= high:
            fresh_count += 1

print(fresh_count)
print(available_range)
