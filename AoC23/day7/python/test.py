from collections import Counter
cards = 'J23456789TQKA'

def get_type(hand):
    jokers = hand.count('J')
    hand = [c for c in hand if c != 'J']
    counts = sorted(Counter(hand).values(), reverse=True)

    print(counts)
    print(hand)
    print(Counter(hand).most_common())

    if not counts:
        counts = [0]
    if counts[0] + jokers == 5:
        return 6
    if counts[0] + jokers == 4:
        return 5
    if counts[0] + jokers == 3 and counts[1] == 2:
        return 4
    if counts[0] + jokers == 3:
        return 3
    if counts[0] == 2 and (jokers or counts[1] == 2):
        return 2
    if counts[0] == 2 or jokers:
        return 1
    return 0

print(get_type('33J21'))