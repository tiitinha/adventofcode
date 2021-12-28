import re

def evaluate_expression(expression: str):
    #splitted = re.findall(r'([\w\*\+\(\)])', expression.strip(" "))
    splitted = re.split(r'[\(\)]', expression)



    return expression

def evaluate_input(expressions: list) -> list:
    ready_exp = []
    for expression in expressions:
        print(expression)
        ready_exp.append(evaluate_expression(expression))

    return expressions

with open('input2.txt') as f:
    calcs = [l.strip('\n') for l in f]

evaluate_input(calcs)
