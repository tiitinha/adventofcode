import math

def numcat(a,b):
    return int(math.pow(10,(int(math.log(b,10)) + 1)) * a + b)

with open('../input.txt') as f:
    calibrations = [x.strip().split(': ') for x in f.readlines()]

def evaluate(inputs):
    interim_results = set()
    interim_results.add(inputs[0])

    for input in inputs[1:]:
        next_results = set()
        for res in interim_results:
            plus = res + input
            mul = res * input
            concat = int(str(res) + str(input))
            next_results.add(plus)
            next_results.add(mul)
            next_results.add(concat)

        interim_results = next_results

    return interim_results

total = 0
for calibration in calibrations:
    result = int(calibration[0])
    inputs = [int(x) for x in calibration[1].split(' ')]

    possible_results = evaluate(inputs)

    if result in possible_results:
        total += result

print(total)
