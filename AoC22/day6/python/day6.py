def read_markers(string, n):
    for i in range((n - 1), len(string)):
        chars = string[i - (n - 1) : i + 1]

        uniques = set(chars)

        if len(uniques) == n:
            return i + 1


with open('input.txt', 'r') as f:
    inputstream = f.read().strip('\n')

test = 'nppdvjthqldpwncqszvftbrmjlhg'
test2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

print(read_markers(inputstream, 4))
print(read_markers(inputstream, 14))
