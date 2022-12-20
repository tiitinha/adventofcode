import re

def is_possible(x, y):
    for sx, sy, d in sensors:
        if manhattan_dist((sx, sy), (x, y)) <= d and (x, y) not in beacons:
            return False

    return True

def manhattan_dist(a: tuple, b: tuple) -> int:
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def part1(j: int):
    count = 0
    lower = min(x - d for x, _, d in sensors)
    upper = max(x  +d for x, _, d in sensors)

    for i in range(lower, upper):
        if not is_possible(i, j) and (i, j) not in beacons:
            count += 1

    return count

with open('input.txt', 'r') as f:
    lines = [[int(y) for y in z] for z in [re.findall(r'\w+\=([\-]?\d+)', x) for x in f.readlines()]]

sensors = set()
sensors2 = set()
beacons = set()
radius = {(a, b): manhattan_dist((a, b), (c, d)) for (a, b, c, d) in lines}

for line in lines:
    sx, sy = line[0], line[1]
    bx, by = line[2], line[3]

    d = manhattan_dist((sx, sy), (bx, by))

    sensors.add((sx, sy, d))
    sensors2.add((sx, sy))
    beacons.add((bx, by))

print(part1(2000000))

acoeffs, bcoeffs = set(), set()

for (x, y), r in radius.items():
    acoeffs.add(y - x + r + 1)
    acoeffs.add(y - x - r - 1)
    bcoeffs.add(x + y + r + 1)
    bcoeffs.add(x + y - r - 1)

ubound = 4000000

for a in acoeffs:
    for b in bcoeffs:
        point = ((b - a) // 2, (a + b) // 2)
        if all(0 < coordinate < ubound for coordinate in point):
            if all(manhattan_dist(point, center) > radius[center] for center in radius.keys()):
                print(4000000 * point[0] + point[1])

