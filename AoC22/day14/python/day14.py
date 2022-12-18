def sand_drop(rocks: set) -> tuple:
    x, y = 500, 0
    return (x, y)

with open('input.txt', 'r') as f:
    rules = [[[int(c) for c in y.split(',')] for y in z] for z in [x.strip().split(' -> ') for x in f.readlines()]]


rocks = set()

for rule in rules:
    for i in range(1, len(rule)):
        p1, p2 = (rule[i - 1], rule[i])
        x1, y1 = (p1[0], p1[1])
        x2, y2 = (p2[0], p2[1])

        xrange = range(x1, x2 + 1) if x2 >= x1 else range(x2, x1 + 1)
        yrange = range(y1, y2 + 1) if y2 >= y1 else range(y2, y1 + 1)

        rocks.update({(x, y) for x in xrange for y in yrange})


bottom_depth = max([x[1] for x in rocks])
original_rocks = rocks.copy()

def part1(rockset: set, bottom_depth: int) -> int:
    sand_count = 0

    while True:
        x, y = 500, 0
        sand_count += 1

        for r in range(bottom_depth + 2):
            if r == bottom_depth:
                return sand_count - 1

            if (x, r + 1) not in rocks:
                continue

            if (x - 1, r + 1) not in rocks:
                x -= 1
                continue

            if (x + 1, r + 1) not in rocks:
                x += 1
                continue

            rockset.add((x, r))
            break

def part2(rockset: set, bottom_depth: int) -> int:
    sand_count = 0

    while True:
        x, y = 500, 0
        sand_count += 1

        for r in range(bottom_depth + 1):
            if r == bottom_depth:
                rockset.add((x, r))
                break

            if (x, r + 1) not in rocks:
                continue

            if (x - 1, r + 1) not in rocks:
                x -= 1
                continue

            if (x + 1, r + 1) not in rocks:
                x += 1
                continue

            rockset.add((x, r))
            break

        if (500, 0) in rocks:
            return sand_count, rocks


print(part1(rocks, bottom_depth))
p2, sands = part2(rocks, bottom_depth + 1)
print(len(sands) - len(original_rocks))
