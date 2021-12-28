from collections import deque

def game(player1, player2):
    cont = True

    p1_hands = []
    p2_hands = []

    p1_hands.append(player1)
    p2_hands.append(player2)

    while cont:

        p1_cards = len(player1)
        p2_cards = len(player2)

        player1_card = player1.popleft()
        player2_card = player2.popleft()

        if p1_cards >= player1_card and p2_cards >= player2_card:
            game(player1, player2)
        else:
            if player1_card < player2_card:
                player2.extend([player2_card, player1_card])
            elif player1_card > player2_card:
                player1.extend([player1_card, player2_card])
            elif player1_card == player2_card:
                pass

        if p1_cards in p1_hands or p2_cards in p2_hands:
            return player1

        p1_hands.append(player1)
        p2_hands.append(player2)


        if len(player1) == 0:
            return player2
        elif len(player2) == 0:
            return player1

def calc_points(cards):
    points = 0
    i = 1

    while len(winning) > 0:
        point = winning.pop()
        points += i * point
        i += 1

    return points

with open('input.txt') as f:
    data = f.read().split('\n\n')
    player1 = deque([int(x) for x in data[0].split('\n')[1:]])
    player2 = deque([int(x) for x in data[1].split('\n')[1:]])

winning = game(player1, player2)

print(calc_points(winning))
