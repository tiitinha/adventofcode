with open('../test.txt') as f:
    data = [int(x) for x in f.read().strip()]

files = []
frees = []

for i in range(0, len(data) - 1, 2):
    files.append(data[i])
    frees.append(data[i + 1])

for i in range(len(files)):
    print(files[i], frees[i])
