import math

raw_data = ""

with open("input") as f: 
    raw_data = f.read()

stones = list(map(int, raw_data.split(" ")))

def blink(stones):

    next_stones = []
    for stone in stones:

        a = str(stone)
        b = len(a)
    
        if stone == 0:
            next_stones.append(1)
        elif b % 2 == 0:
            c = b // 2
            stone1 = int(a[:c])
            stone2 = int(a[c:])
            next_stones.append(stone1)
            next_stones.append(stone2)
        else:
            next_stones.append(2024 * stone)

    return next_stones

for i in range(25):
    stones = blink(stones)

print(len(stones))