from functools import reduce

with open('input.txt', 'r') as file:
    heightmap = [[int(y) for y in x.strip()] for x in file.readlines()]

def get_lowpoints(heightmap: list) -> list:

    lowpoints = []
    coords = []
    width = len(heightmap[0]) - 1
    height = len(heightmap) - 1

    for i, row in enumerate(heightmap):
        for j, col in enumerate(row):
            current = heightmap[i][j]
            current_coords = [i, j]
            if i == 0 and j == 0:
                if heightmap[i + 1][j] > current and heightmap[i][j + 1] > current:
                    lowpoints.append(current)
                    coords.append(current_coords)
            elif i == 0 and j < width:
                if heightmap[i][j + 1] > current and heightmap[i + 1][j] > current and heightmap[i][j - 1] > current:
                    lowpoints.append(current)
                    coords.append(current_coords)
            elif i == 0 and j == width:
                if heightmap[i + 1][j] > current and heightmap[i][j - 1] > current:
                    lowpoints.append(current)
                    coords.append(current_coords)
            elif i < height and j == 0:
                if heightmap[i - 1][j] > current and heightmap[i][j + 1] > current and heightmap[i + 1][j] > current:
                    lowpoints.append(current)
                    coords.append(current_coords)
            elif i == height and j == 0:
                if heightmap[i - 1][j] > current and heightmap[i][j + 1] > current:
                    lowpoints.append(current)
                    coords.append(current_coords)
            elif i == height and j < width:
                if heightmap[i - 1][j] > current and heightmap[i][j - 1] > current and heightmap[i][j + 1] > current:
                    lowpoints.append(current)
                    coords.append(current_coords)
            elif i == height and j == width:
                if heightmap[i][j - 1] > current and heightmap[i - 1][j] > current:
                    lowpoints.append(current)
                    coords.append(current_coords)
            elif i < height and j == width:
                if heightmap[i - 1][j] > current and heightmap[i + 1][j] > current and heightmap[i][j - 1] > current:
                    lowpoints.append(current)
                    coords.append(current_coords)
            elif 0 < i < height and 0 < j < width:
                if heightmap[i - 1][j] > current and heightmap[i][j - 1] > current and heightmap[i + 1][j] > current and heightmap[i][j + 1] > current:
                    lowpoints.append(current)
                    coords.append(current_coords)

    return lowpoints, coords

def calc_risk(lowpoints: list) -> int:
    risk = sum([x + 1 for x in lowpoints])

    print(risk)

def calculate_basins(lowpoints: list) -> list:
    basins = []
    for point in lowpoints:
        basins.append(get_basin(heightmap, point))

    return basins

def neigh_filter(neighbors: list, points: list) -> list:
    neighs = []

    for neighbor in neighbors:
        if points[neighbor[0]][neighbor[1]] != 9:
            neighs.append(neighbor)

    return neighs

def get_basin(points: list, low_point: list) -> list:
    dekki = [low_point]
    visited = []
    basin = []

    while dekki:
        point = dekki.pop()
        neighbors = get_neighbors(points, point[0], point[1])

        neighbors = neigh_filter(neighbors, heightmap)

        dekki.extend([x for x in neighbors if x not in visited])
        visited.append(point)

        if point not in basin:
            basin.append(point)

    return basin

def get_neighbors(points: list, x: int, y: int) -> list:
    neighbors = []

    if x == 0 and y == 0:
        if points[x][y + 1] > points[x][y]:
            neighbors.append([x, (y + 1)])
        if points[x + 1][y] > points[x][y]:
            neighbors.append([(x + 1), y])
    elif x == 0 and y > 0 and y < len(points[0]) - 1:
        if points[x][y - 1] > points[x][y]:
            neighbors.append([x, (y - 1)])
        if points[x + 1][y] > points[x][y]:
            neighbors.append([(x + 1), y])
        if points[x][y + 1] > points[x][y]:
            neighbors.append([x, (y + 1)])
    elif x > 0 and x < len(points) - 1 and y == 0:
        if points[x - 1][y] > points[x][y]:
            neighbors.append([(x - 1), y])
        if points[x + 1][y] > points[x][y]:
            neighbors.append([(x + 1), y])
        if points[x][y + 1] > points[x][y]:
            neighbors.append([x, (y + 1)])
    elif x == len(points) - 1 and y == 0:
        if points[x - 1][y] > points[x][y]:
            neighbors.append([(x - 1), y])
        if points[x][y + 1] > points[x][y]:
            neighbors.append([x, (y + 1)])
    elif x > 0 and x < len(points) - 1 and y > 0 and y < len(points[0]) - 1:
        if points[x - 1][y] > points[x][y]:
            neighbors.append([(x - 1), y])
        if points[x][y - 1] > points[x][y]:
            neighbors.append([x, (y - 1)])
        if points[x + 1][y] > points[x][y]:
            neighbors.append([(x + 1), y])
        if points[x][y + 1] > points[x][y]:
            neighbors.append([x, (y + 1)])
    elif x == 0 and y == len(points[0]) - 1:
        if points[x][y - 1] > points[x][y]:
            neighbors.append([x, (y - 1)])
        if points[x + 1][y] > points[x][y]:
            neighbors.append([(x + 1), y])
    elif x > 0 and x < len(points) - 1 and y == len(points[0]) - 1:
        if points[x - 1][y] > points[x][y]:
            neighbors.append([(x - 1), y])
        if points[x][y - 1] > points[x][y - 1]:
            neighbors.append([x, (y - 1)])
        if points[x + 1][y] > points[x][y]:
            neighbors.append([(x + 1), y])
    elif x == len(points) - 1 and y == len(points[0]) - 1:
        if points[x - 1][y] > points[x][y]:
            neighbors.append([(x - 1), y])
        if points[x][y - 1] > points[x][y]:
            neighbors.append([x, (y - 1)])
    elif x == len(points) - 1 and y > 0 and y < len(points[0]):
        if points[x - 1][y] > points[x][y]:
            neighbors.append([(x - 1), y])
        if points[x][y - 1] > points[x][y]:
            neighbors.append([x, (y - 1)])
        if points[x][y + 1] > points[x][y]:
            neighbors.append([x, (y + 1)])

    return neighbors

def calc_basin_len(basins: list) -> list:
    basin_lengths = [len(x) for x in basins]

    print(sorted(basin_lengths))

    return reduce(lambda x, y: x * y, sorted(basin_lengths)[-3:], 1)

lowpoints, coords = get_lowpoints(heightmap)
calc_risk(lowpoints)

basins = calculate_basins(coords)

result2 = calc_basin_len(basins)
print(result2)
