def solve(coords: list, iterations: int = 1):
    idx = [i for i in range(len(coords))]

    for i in idx * iterations:
        idx.pop(j := idx.index(i))
        idx.insert((j + coords[i]) % len(idx), i)

    return idx


with open('input.txt', 'r') as f:
    coordinates = [int(x.strip()) for x in f.readlines()]

pt1 = solve(coordinates, 1)

zero_pos = pt1.index(coordinates.index(0))
pt1_sol = sum(coordinates[pt1[(zero_pos + p) % len(coordinates)]] for p in [1000, 2000, 3000])

print(pt1_sol)

pt2_coords = [x * 811589153 for x in coordinates]

pt2 = solve(pt2_coords, 10)
zero_pt2 = pt2.index(pt2_coords.index(0))
pt2_sol = sum(pt2_coords[pt2[(zero_pt2 + p) % len(coordinates)]] for p in [1000, 2000, 3000])

print(pt2_sol)
