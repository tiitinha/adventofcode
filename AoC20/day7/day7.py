import re
from collections import defaultdict


def main():
    bags = defaultdict(set)

    with open('input7.txt') as f:
        file = [line.rstrip() for line in f]
        for line in file:
            parent, children = line.split('contain')
            patt = re.compile('(\s*)bag[s]*(\s*)|(\s*)\d+(\s*)|(\s*)\.(\s*)')
            parent = patt.sub('', parent)
            children = children.split(',')
            for bag in children:
                if not 'no other' in bag:
                    newBag = patt.sub('', bag.strip())
                    bags[newBag].add(parent)

    def findParents(findBag):
        contained = bags[findBag]
        if len(contained) == 0:
            return contained
        return contained.union(c2 for c in contained for c2 in findParents(c))

    print(len(findParents('shiny gold')))

if __name__ == "__main__":
    main()
