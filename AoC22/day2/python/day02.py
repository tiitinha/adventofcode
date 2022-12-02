
points = {'rock': 1,
        'paper': 2,
        'scissors': 3,
        'win': 6,
        'draw': 3,
        'loss': 0}

strategies_pt1 = {'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissors'}

def check_outcome(player_1, player_2):
    if player_1 == 'rock' and player_2 == 'scissors':
        return 0
    if player_1 == 'rock' and player_2 == 'rock':
        return 3
    if player_1 == 'rock' and player_2 == 'paper':
        return 6
    if player_1 == 'paper' and player_2 == 'scissors':
        return 6
    if player_1 == 'paper' and player_2 == 'rock':
        return 0
    if player_1 == 'paper' and player_2 == 'paper':
        return 3
    if player_1 == 'scissors' and player_2 == 'scissors':
        return 3
    if player_1 == 'scissors' and player_2 == 'rock':
        return 6
    if player_1 == 'scissors' and player_2 == 'paper':
        return 0

with open('input.txt', 'r') as f:
    rounds = [x for x in f.readlines()]

round_points = []

# Part 1

for rnd in rounds:
    player_1, player_2 = rnd.split()
    p1_strat = strategies[player_1]
    p2_strat = strategies[player_2]

    pts = points[p2_strat] + check_outcome(p1_strat, p2_strat)
    round_points.append(pts)

print(sum(round_points))

# Part 2


