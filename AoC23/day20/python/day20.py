from collections import defaultdict

with open('../test.txt') as f:
    instr = {(y[0][1:] if len(y[0]) < 10 else y[0]): {'out': y[1].split(', '), 'state': 0 if y[0][0] == '%' else None, 'pulse': 0, 'type': y[0][0] if y[0][0] == '%' or y[0][0] == '&' else None} for y in [x.strip().split(' -> ') for x in f.readlines()]}

inputs = defaultdict(list)
outputs = defaultdict(list)

def check_conjunction(module):
    module_inputs = inputs[module]
    module_input_pulses = map(lambda x: x['pulse'], module_inputs)

    return all(module_input_pulses)

def check_flip_flop(module):
    module_inputs[module]
    module_input_pulses = map(lambda x: x['pulse'], module_inputs)

    return any(module_input_pulses)

for inst, vals in instr.items():
    #print(vals)
    outputs[inst] = vals['out']
    
    for val in vals['out']:
        inputs[val].append(inst)

instr['button'] = {'out': 'broadcaster', 'type': None, 'state': 0}

modules = []
highs = 0
lows = 0

for i in range(1):
    print(i)

    next = instr['button']['out']

    modules.append(next)

    while modules:
        print('queue', modules)
        next_name = modules.pop(0)
        next = instr[next_name]

        if next['type'] == '&':
            if check_conjunction(next):
                next['pulse'] = 0
            else:
                next['pulse'] = 1

        if next['type'] == '%':
            if check_filp_flop(next):
                next['state']: 1
                next['pulse']: 

        print(next_name, next)

        modules.extend(next['out'])

        if next_name == 'inv':
            break



