from collections import Counter
import copy

card_strengths = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
card_strengths.reverse()


card_strengths2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
card_strengths2.reverse()

with open('../input.txt') as f:
    hands = [x.strip().split(' ') for x in f.readlines()]
    hands2 = copy.deepcopy(hands)


def hand_strength(hand, pt2):
    # get all hands from five of kind to high

    card_count = Counter(hand[0])
    most_common = card_count.most_common()
    jcount = hand[0].count('J') if pt2 else 0

    if len(most_common) == 1:
        return 7
    if most_common[0][1] + jcount == 5:
        return 6
    if most_common[0][1] + jcount == 4:
        return 5
    if most_common[0][1] + jcount == 3:
        if most_common[1][1] == 2:
            return 4
        return 3
    if most_common[0][1] + jcount == 2:
        if most_common[1][1] == 2:
            return 2
        return 1
    return 0

hands.sort(key=lambda hand: (hand_strength(hand, False), [card_strengths.index(card) for card in hand[0]]))
hands2.sort(key=lambda hand: (hand_strength(hand, True), hand[0].count('J'), sorted([card_strengths2.index(card) for card in hand[0]])))
#print(hands)
#print(hands2)

for hand in hands2[-10:]:
    print(hand)
    print(hand_strength(hand, True))
    print([card_strengths2.index(card) for card in hand[0]])
    print(hand[0].count('J'))

print(sum([(i + 1) * int(x[1]) for i, x in enumerate(hands)]))
print(sum([(i + 1) * int(x[1]) for i, x in enumerate(hands2)]))


