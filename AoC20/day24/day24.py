direction_dict = {'ne': (1, 0, -1), 'e': (1, -1, 0), 'se': (0, -1, 1), 'sw': (-1, 0, 1), 'w': (-1, 1, 0), 'nw': (0, 1, -1)}

def read_directions(directions: str, grid):
    coordinates = [0, 0, 0]
    direct = ''
    for i, direction in enumerate(directions):
        if direction == 'n' or direction == 's':
            direct = direction
            continue
        else:
            direct = direct + direction
            coordinates = [sum(x) for x in zip(coordinates, direction_dict[direct])]
            direct = ''

    return coordinates

def check_neighbors(grid: list, coordinates: list) -> int:
    neighbors = [[sum(x) for x in zip(coordinates, direction_dict[direct])] for direct in direction_dict.keys()]
    return neighbors

def rolling(grid: list, rounds: int) -> list:
    black_tiles = grid

    for i in range(rounds):
        help_grid = []
        for tile in grid:
            neighbors = check_neighbors(grid, tile)
            if num_nbr =

def do_dirs(grid: list, directions: list) -> list:
    for directions in tile_directions:
        coordinates = read_directions(directions, grid)
        if coordinates in grid:
            grid.remove(coordinates)
        else:
            grid.append(coordinates)

    return grid

with open('input.txt') as f:
    tile_directions = [l.strip('\n') for l in f.read().split('\n')]
    grid = do_dirs([], tile_directions)

    rolling(grid, 2)

    print(len(grid))
