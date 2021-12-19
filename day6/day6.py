with open('input.txt', 'r') as file:
    initial_state = [int(x) for x in file.read().strip('\n').split(',')]

def lanternfish_algo(initial_state: list, days: int) -> int:
    toadd = 0

    for i in range(days):
        toadd = 0
        for j, fish in enumerate(initial_state):
            if fish == 0:
                initial_state[j] = 6
                toadd += 1
            else:
                initial_state[j] = fish - 1

        initial_state.extend([8 for x in range(toadd)])

    print(len(initial_state))

def lanternfish_algo_mint(initial_state: list, days: int) -> int:

    current_state = [0] * 9

    for val in initial_state:
        current_state[val] += 1

    for i in range(days):
        next_round = [0] * 9

        for j, val in enumerate(current_state):
            if j == 0:
                next_round[6] += val
                next_round[8] += val
            else:
                next_round[j - 1] += val

        current_state = next_round

    print(sum(current_state))

#lanternfish_algo(initial_state, 80)
lanternfish_algo_mint(initial_state, 256)
