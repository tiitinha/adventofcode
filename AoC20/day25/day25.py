def encrypt(public_key: int) -> int:
    value = 1
    loop_size = 0
    subject_num = 7

    while value != public_key:
        value *= subject_num
        value %= 20201227
        loop_size += 1

    return loop_size

def transform(public_key: int, loop_size) -> int:
    value = 1
    for i in range(loop_size):
        value *= public_key
        value %= 20201227

    return value

with open('input.txt') as f:
    card_public, door_public = [int(l.strip('\n')) for l in f.read().split('\n')]

    print(card_public, door_public)

loop_size = encrypt(card_public)
transformed = transform(door_public, loop_size)

print(loop_size, transformed)
