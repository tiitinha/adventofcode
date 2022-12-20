import re

with open('input.txt', 'r') as f:
    blueprints = [list(map(int, re.findall(r'(\d+)', x))) for x in f.readlines()]

for blueprint in blueprints:
    id_num, ore_robot, clay_robot, obsidian_robot_ore, obsidian_robot_clay, geode_robot_ore, geode_robot_obsidian = blueprint

