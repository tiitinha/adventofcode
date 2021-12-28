import string

def customs():
    with open('input6.txt') as f:

        file = [group for group in f.read().split('\n\n')]

        count = 0

        for line in file:
            groupPersons = line.split('\n')
            allYes = set(string.ascii_lowercase)
            for person in groupPersons:
                personYes = set()
                for char in person:
                    personYes.add(char)
                allYes = allYes & personYes
            count += len(allYes)
        return count

print(customs())
