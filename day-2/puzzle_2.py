
data = []

# get tha data
with open('input', 'r') as file:
    lines = file.readlines()
    for line in lines:
        nums = line.split(" ")
        data.append(list(map(lambda x: int(x.removesuffix("\n")), nums)))


def is_safe(candidate):
    # list of consecutive pairs
    zipped = list(zip(candidate[:-1], candidate[1:]))

    # holy hell, 0 really is smaller than at least 1
    contained_distance = all([(1 <= abs(a - b) <= 3) for (a, b) in zipped])

    increasing = all([a < b for (a, b) in zipped])
    decreasing = all([a > b for (a, b) in zipped])
    
    return contained_distance and (increasing or decreasing)

results = 0

for x in data:

    safe = is_safe(x)
    
    for idx, y in enumerate(x):
        candidate = x[:idx] + x[idx + 1:]

        if is_safe(candidate):
            safe = True

    if safe:
        results += 1

print(results)