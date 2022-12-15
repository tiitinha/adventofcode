import re

def manhattan_dist(a: tuple, b: tuple) -> int:
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def get_closer_points(point: tuple, dist: int) -> list:
    return None

with open('test.txt', 'r') as f:
    lines = [[(c[0], c[1]), (c[2], c[3])] for c in [[int(y) for y in z] for z in [re.findall(r'\w+\=([\-]?\d+)', x) for x in f.readlines()]]]

for signal in lines:
    sensor = signal[0]
    beacon = signal[1]

    dist = manhattan_dist(sensor, beacon)

