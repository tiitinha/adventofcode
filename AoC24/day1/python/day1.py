
with open('input.txt') as f:
    input = [x.strip().split() for x in f.readlines()]

first = []
second = []
for row in input:
    first.append(int(row[0]))
    second.append(int(row[1]))

first.sort()
second.sort()

total_sum = 0
similarity_score = 0

for a, b in zip(first, second):
    total_sum += abs(a - b)

for a in first:
    count = second.count(a)
    similarity_score += a * count

print(total_sum)
print(similarity_score)
