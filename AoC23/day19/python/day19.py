import re

pattern1 = re.compile(r'^([^{}]+){([^}]+)}$')

def eval_true(letter, comparator, value):
    #print(letter, value)
    return (letter > value) if comparator == '>' else (letter < value)

def handle_rule(rule, x, m, a, s):
    destination = rules[-1]
    for rule in rules[:-1]:
        rule_raw, rule_dest = rule.split(':')
        xmas = rule_raw[0]
        comparator = rule_raw[1]
        value = int(rule_raw[2:])

        #print(xmas, comparator, value)

        if xmas == 'x':
            letter = x
        elif xmas == 'm':
            letter = m
        elif xmas == 'a':
            letter = a
        elif xmas == 's':
            letter = s

        if eval_true(letter, comparator, value):
            return rule_dest

    return destination

with open('../input.txt') as f:

    workflow, parts = f.read().split('\n\n')

    workflow = {pattern1.match(x).group(1): pattern1.match(x).group(2) for x in workflow.strip().split('\n')}
    parts = [re.findall(r'([0-9]+)', x) for x in parts.strip().split('\n')]

result = 0

for part in parts:
    x, m, a, s = [int(y) for y in part]

    current_flow = workflow['in']
    
    while True:
        rules = current_flow.split(',')

        res = handle_rule(rules, x, m, a, s)
        #print(rules, res)

        if res == 'A':
            result += x + m + a + s
            print(part)
            break
        if res == 'R':
            break

        current_flow = workflow[res]

    #print(result)

print(result)

