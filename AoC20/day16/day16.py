import re
from collections import defaultdict

def invalid_values(legit_values: set, values: list) -> list:
    invalids = []
    for value in values:
        if value not in legit_values:
            invalids.append(value)

    return invalids

def ticket_validity(valid_values: set, ticket_values: list) -> bool:
    for value in ticket_values:
        if not all([tick_val in valid_values for tick_val in ticket_values]):
            return False
    return True

def get_valid_tickets(valid_values: set, ticks: list) -> list:
    valid_tickets = []
    for ticket in ticks:
        if ticket_validity(valid_values, ticket):
            valid_tickets.append(ticket)

    return valid_tickets

def get_valid_values(info: list) -> dict:
    valid_ranges = defaultdict(list)
    for line in info:
        rule_name = re.search(r'(\w*\s*\w*)', line)[0]
        values = re.findall(r'(\d*\-\d*)', line)
        for value in values:
            valid_ranges[rule_name].append(list(map(lambda x: int(x), re.findall(r'(\d+)', value))))
    return valid_ranges

def set_of_valids(valid_values: dict) -> set:
    valids = set()
    for rule_range in valid_values.values():
        for value_range in rule_range:
            for num in range(value_range[0], value_range[1] + 1):
                valids.add(num)

    return valids

def fits_rule(rules: dict, ticks: list) -> list:
    rule_fitters = defaultdict(list)
    width = len(ticks[0])
    height = len(ticks)

    for rule in rules:
        for x in range(width):
            help_fitters = []
            for y in range(height):
                if ticks[y][x] in range(rules[rule][0][0], rules[rule][0][1] + 1) or ticks[y][x] in range(rules[rule][1][0], rules[rule][1][1] + 1):
                    help_fitters.append([x, y])
            if len(help_fitters) == height:
                rule_fitters[rule].append(x)
    return rule_fitters

def diff(l1, l2):
    li_diff = [i for i in l1 + l2 if i not in l1 or i not in l2]
    return li_diff

def elimination(values: dict) -> dict:
    helper_dict = defaultdict(list)

    for key, val in values.items():
        if len(val) > 1:
            helper_dict[key].extend(diff(prev, val))
        else:
            helper_dict[key].append(val[0])
        prev = val
    return helper_dict

def part2(values: dict, own_tick: list) -> int:
    aggregate = 1

    for key, val in values.items():
        if 'departure' in key:
            print(val[0])
            print(own_tick)
            aggregate *= own_tick[val[0]]

    return aggregate


with open('input.txt') as f:
    data = [l.split('\n') for l in f.read().split('\n\n')]

    info = data[0]
    own_ticket = [int(x) for x in data[1][1].split(',')]
    other_tickets = [[int(n) for n in y] for y in [a.split(',') for a in data[2][1:]]]
    flat_tix = [value for sublist in other_tickets for value in sublist]

legit_range = get_valid_values(info)
legit_set = set_of_valids(legit_range)

invalid_value_list = invalid_values(legit_set, flat_tix)

valid_tickets_list = get_valid_tickets(legit_set, other_tickets)

valueses = fits_rule(legit_range, valid_tickets_list)

sorted_vals = dict(sorted(valueses.items(), key = lambda k : len(k[1])))

eliminated = elimination(sorted_vals)

print(part2(eliminated, own_ticket))
