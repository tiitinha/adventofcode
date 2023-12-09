import re

with open('../test3.txt') as f:
    instructions, nodes = f.read().strip().split('\n\n')
    nodes = [re.findall('([A-Z0-9]{3})', x) for x in nodes.split('\n')]
    node_dict = {y[0]: y[1:] for y in nodes}

def part1():
    current_node = 'AAA'
    step_count = 0
    instruction_index = 0

    while True:
        instruction = instructions[instruction_index]

        instruction_index = 0 if instruction_index == len(instructions) - 1 else instruction_index + 1

        step_count += 1
        side = 0 if instruction == 'L' else 1

        next_node = node_dict[current_node][side]


        if next_node == 'ZZZ':
            break

        current_node = next_node

    print(step_count)

def part2():
    starting_nodes = [x[0] for x in nodes if x[0][2] == 'A']
    print(starting_nodes)
    length_idx = []

    for node in starting_nodes:
        instr = 0
        history = []
        cur = node
        length = 0

        while True:
            instruction = instructions[instr]
            instr = 0 if instr == len(instructions) - 1 else instr

            side = 0 if instr == 'L' else 1

            next_node = node_dict[cur][side]

            try:
                idx = history.index((instr, next_node))
            except:
                idx = -1

            if idx != -1:
                print(f'FOUND: {length}, {idx}')
                length_idx.append((length, idx))
                break

            length += 1

            history.append((instr, next_node))

            cur = next_node

part2()
