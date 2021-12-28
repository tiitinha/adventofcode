import re
from collections import defaultdict

with open('input.txt') as f:
    datum = [re.sub('[\(\)]', '', l.strip('\n')) for l in f.read().split('\n')]

    allergen_dict = defaultdict(set)

    for line in datum:
        stuff = line.split('contains')

        ingredients = stuff[0].strip().split(' ')
        allergens = stuff[1].strip().split(', ')

        for allergen in allergens:
            allergen_dict[allergen].update(ingredients)


    print(allergen_dict)
