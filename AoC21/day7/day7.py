with open('test.txt', 'r') as file:
    horizontal_positions = [int(x) for x in file.read().split(',')]

def calculate_optimal_position(init_positions: list) -> int:
    minimum = min(init_positions)
    maximum = max(init_positions)



print(calculate_optimal_position(horizontal_positions))
