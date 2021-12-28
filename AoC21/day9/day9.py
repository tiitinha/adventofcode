with open('input.txt', 'r') as file:
    heightmap = [[int(y) for y in x.strip()] for x in file.readlines()]

def get_lowpoints(heightmap: list) -> list:

    lowpoints = []
    width = len(heightmap[0]) - 1
    height = len(heightmap) - 1

    for i, row in enumerate(heightmap):
        for j, col in enumerate(row):
            current = heightmap[i][j]
            if i == 0 and j == 0:
                if heightmap[i + 1][j] > current and heightmap[i][j + 1] > current:
                    lowponts.append(current)
            elif i == 0 and j < width:
                if heightmap[i][j + 1] > current and heightmap[i + 1][j] > current and heightmap[i][j - 1] > current:
                    lowpoints.append(current)
            elif i == 0 and j == width:
                if heightmap[i + 1][j] > current and heightmap[i][j - 1] > current:
                    lowpoints.append(current)
            elif i < height and j == 0:
                if heightmap[i - 1][j] > current and heightmap[i][j + 1] > current and heightmap[i + 1][j] > current:
                    lowpoints.append(current)
            elif i == height and j == 0:
                if heightmap[i - 1][j] > current and heightmap[i][j + 1] > current:
                    lowpoints.append(current)
            elif i == height and j < width:
                if heightmap[i - 1][j] > current and heightmap[i][j - 1] > current and heightmap[i][j + 1] > current:
                    lowpoints.append(current)
            elif i == height and j == width:
                if heightmap[i][j - 1] > current and heightmap[i - 1][j] > current:
                    lowpoints.append(current)
            elif i < height and j == width:
                if heightmap[i - 1][j] > current and heightmap[i + 1][j] > current and heightmap[i][j - 1] > current:
                    lowpoints.append(current)
            elif 0 < i < height and 0 < j < width:
                if heightmap[i - 1][j] > current and heightmap[i][j - 1] > current and heightmap[i + 1][j] > current and heightmap[i][j + 1] > current:
                    lowpoints.append(current)

    return lowpoints

def calc_risk(lowpoints: list) -> int:
    risk = sum([x + 1 for x in lowpoints])

    print(risk)

lowpoints = get_lowpoints(heightmap)
calc_risk(lowpoints)
