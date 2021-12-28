import re
import time

def timetable_solver(timestamp, buses):
    earliest_timestamp = [(bus - (timestamp % bus)) for bus in buses]
    waiting_time = min(earliest_timestamp)
    return buses[earliest_timestamp.index(waiting_time)] * waiting_time

def challenge_solver(buses):
    first = int(buses[0][1])
    i = 1
    found = False
    ismod = False
    mod = 0
    checkmod = 0

    while (not found):
        found = False
        for bus in buses[1:]:
            while (not ismod):

                checkmod = i * first + mod
                bus_value = int(bus[1])
                bus_index = bus[0]

                ismod = (checkmod % bus_value) == (bus_value - bus_index % bus_value)

                if ismod:
                    mod = checkmod
                    first *= bus_value
                    i = 1
                    ismod = False
                    break
                i += 1

        return checkmod

with open('input2.txt', 'r') as f:
    timestamp, bus_notes = [l.strip() for l in f.readlines()]
    timestamp = int(timestamp)
    buses = re.findall(r'\,*(\d+)\,*', bus_notes)
    buses = [int(b) for b in buses]
    buses2 = list(enumerate(bus_notes.split(',')))
    buses2 = list(filter(lambda x: (x[1] != 'x'), buses2))


result = timetable_solver(timestamp, buses)
result2 = challenge_solver(buses2)

print(result)
print(result2)
