
strategies = {
    'X': {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    },
    'Y': {
        'A': 'A',
        'B': 'B',
        'C': 'C'
    },
    'Z': {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }
}

strategy_pts = {
    'A': 1,
    'B': 2,
    'C': 3
}

result_pts = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

with open('input.txt') as f:
    rounds = [x for x in f.readlines()]

points = 0

for round in rounds:
    p1, res = round.split()

    p2_choice = strategies[res][p1]

    points += strategy_pts[p2_choice] + result_pts[res]

print(points)
