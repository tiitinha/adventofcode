cups = '137826495'
test_cups = '389125467'
cup_list = [int(x) for x in list(test_cups)]

def get_crab_cups(current_cup, cups: list) -> list:
    if current_cup < len(cups) - 4:
        crab_cups = cups[current_cup + 1: current_cup + 4]
    elif current_cup == len(cups) - 1:
        crab_cups = cups[:3]
    else:
        crab_cups = cups[current_cup + 1:] + cups[:(len(cups) - 1 - current_cup)]

    return crab_cups

def get_destination_cup(current_cup: int, cups: list, crab_cups) -> list:
    if cups[current_cup] - 1 == 0:
        destination_cup = len(cups)
    else:
        destination_cup = cups[current_cup] - 1

    while destination_cup in crab_cups:
        if destination_cup == 1:
            destination_cup = len(cups)
        else:
            destination_cup = destination_cup - 1

    return destination_cup

def move_cups(current_cup: int, cups: list) -> list:
    crab_cups = get_crab_cups(current_cup, cups)
    destination_cup = get_destination_cup(current_cup, cups, crab_cups)
    print(f'denstitan: {destination_cup}')

    if current_cup < len(cups) - 4:
        print(1)
        del cups[current_cup + 1: current_cup + 4]
        destination_index = cups.index(destination_cup)
        cups = cups[:destination_index] + crab_cups + cups[destination_index:]
    elif current_cup == len(cups) - 1:
        print(2)
        del cups [:3]
        cups = crab_cups + cups[3:]
    elif current_cup == len(cups) - 3:
        print(3)
        del cups[:-3]
        cups = cups + crab_cups
    else:
        print(4)
        start_index = len(cups) - current_cup - 1
        del cups[current_cup + 1]
        del cups[start_index:]
        cups = crab_cups[start_index:] + cups + crab_cups[:start_index]

    return cups

def game(cups: list, rounds: int) -> list:
    current_cup = 0

    for i in range(rounds):
        cups = move_cups(current_cup, cups)

        if current_cup == len(cups) - 1:
            current_cup = 0
        else:
            current_cup += 1

        print(cups)

    return cups

print(cup_list)
print(game(cup_list, 10))

