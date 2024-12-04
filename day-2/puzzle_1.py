
data = []

with open('input', 'r') as file:
    lines = file.readlines()
    for line in lines:
        nums = line.split(" ")
        data.append(list(map(lambda x: int(x.removesuffix("\n")), nums)))

results = 0

for x in data:

    if len(x) < 2:
        results += 1
        continue

    safe = True

    # check if the difference is within 3
    for y in range(len(x) - 1):
        if abs(x[y] - x[y + 1]) > 3:
            safe = False
    
    # check if they are all increasing or decreasing
    if not (all(i < j for i, j in zip(x, x[1:])) or all(i > j for i, j in zip(x, x[1:]))):
        safe = False

    if safe:
        results += 1

print(results)