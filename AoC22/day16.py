import re

class Valve:
    def __init__(self, name, flow_rate, destinations, isopen):
        self._name = name
        self._flow_rate = flow_rate
        self._destinations = destinations
        self._isopen = isopen

    @property
    def destinations(self):
        return self._destinations

    @property
    def flow_rate(self):
        return self._flow_rate
    
    @property
    def isopen(self):
        return self._isopen
    
    @isopen.setter
    def state(self):
        self._isopen = not self._isopen
    
    def __str__(self):
        return f'{self._name}: {self._flow_rate}, destinations: {self._destinations}'

with open('test.txt', 'r') as f:

    lines = [x.strip() for x in f.readlines()]

valves = []

for line in lines:
    start_valve = re.search(r'\s([A-Z]{2})\s', line).group(1)
    flow_rate = int(re.search(r'(\d+)', line).group(1))
    destinations = [x for x in re.findall(r'([A-Z]{2})', line) if x != start_valve]
    valve = Valve(start_valve, flow_rate, destinations, False)

    valves.append(valve)

current_pressure_released = 0
total_pressure_released = 0    

for i in range(30):

    total_pressure_released += current_pressure_released
