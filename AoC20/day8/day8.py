import re
import copy

def getInstructions():
    instructions = []
    with open('input.txt') as f:
        inputData = [l.strip('\n\n') for l in f.readlines()]
        for line in inputData:

            regex = re.match(r'(\w{3})\s*([+-])(\d+)', line)
            command, sign, value = regex[1], regex[2], regex[3]
            instructions.append([command, sign, value])

    return instructions


def findInfiniteLoop(vals):
    visited = [0 for i in range(len(vals))]
    index = 0
    acc = 0
    while True:
        if visited[index]:
            break

        visited[index] = 1

        command, sign, value = vals[index]

        if command == 'nop':
            index += 1
        elif command == 'acc':
            if sign == '+':
                acc += int(value)
            else:
                acc -= int(value)
            index += 1
        elif command == 'jmp':
            if sign == '+':
                index += int(value)
            else:
                index -= int(value)
        if index >= len(visited) - 1:
            return [acc, True]
    return [acc, False]

def getSwitchedCommands(instructions):
    mappedInstructions = list(map(lambda inst: inst[0], instructions))
    for i, command in enumerate(mappedInstructions):
        vals = copy.deepcopy(instructions)
        if command == 'jmp':
            vals[i][0] = 'nop'
            result = findInfiniteLoop(vals)
            if True in result:
                return result

        elif command == 'nop':
            vals[i][0] = 'jmp'
            result = findInfiniteLoop(vals)
            if True in result:
                return result
        vals = []

    return [0, False]

instructions = getInstructions()
#print(findInfiniteLoop(instructions))

print(getSwitchedCommands(instructions))

