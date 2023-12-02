import re
import numpy as np

with open('../input.txt') as f:
    input = [x.strip() for x in f.readlines()]

rule_dict = {
    'red': 12,
    'green': 13,
    'blue': 14
}

id_sum = 0
game_sum = 0

def is_possible_game(game_data):

    cube_draws = [x.strip() for x in game_data[1].split(';')]

    for draw in cube_draws:

        cubes = [x.strip() for x in draw.split(',')]

        for cube in cubes:

            amt, color = cube.split(' ')

            max_val = rule_dict[color]

            #print(amt, color, max_val)

            if int(amt) > max_val:
                return False

    return True

def min_cube_amt(game_data):
    cubes = re.findall('([0-9]+)\s{1}(red|blue|green)', game_data)
    min_cubes = {'red': -1, 'green': -1, 'blue': -1}
    
    for cube in cubes:
        amt, color = cube
        min_cube_amt = min_cubes[color]

        #print(amt, color)

        if min_cube_amt == -1 or min_cube_amt <= int(amt):
            min_cubes[color] = int(amt)
        
    return np.prod(np.fromiter(min_cubes.values(), dtype=int))


for i, game in enumerate(input):
    game_data = game.split(':')

    id_sum += is_possible_game(game_data) * (i + 1)

    game_sum += min_cube_amt(game)


    

print(id_sum)
print(game_sum)
