# To make parsing easier, a custom separator is added between the rules and the prints

import math

data = ""

with open("input") as f: 
    data = f.read()

lines = data.split("separator")

raw_rules = lines[0].split("\n")
raw_prints = lines[1].split("\n")

rules = {}
for rule in raw_rules:
    if rule == "":
        continue;

    v = rule.split("|")
    before = int(v[0])
    after = int(v[1])
    if before in rules:
        rules[before].append(after)
    else:
        rules[before] = [after]

prints = []
for p in raw_prints:
    if p == "":
        continue;

    prints.append(list(map(int, p.split(","))))


def is_valid(rules, p):
    valid = True

    for idx, x in enumerate(p):
        for idy, y in enumerate(p):
            if idy <= idx:
                continue

            # if reverse of two values is a rule, then the sequence is invalid
            if y in rules and x in rules[y]:
                valid = False

    return valid

# get only the valid midpoint values
pre_result = 0
for p in prints:
    if not is_valid(rules, p):
        continue
    mid_point = math.floor(len(p) / 2)
    pre_result += p[mid_point]

# sort the invalid
for p in prints:
    t = p[:]
    while not is_valid(rules, p):
        for idx, x in enumerate(p):
            for idy, y in enumerate(p):
                if idy <= idx:
                    continue

                # if an invalid pair is found, flip them
                # then start the check over
                if y in rules and x in rules[y]:
                    t1 = x
                    t2 = y
                    p[idx] = t2
                    p[idy] = t1
                    break
            else:
                continue
            break

# get total result now that all sequences are valid
result = 0
for p in prints:
    if not is_valid(rules, p):
        continue
    mid_point = math.floor(len(p) / 2)
    result += p[mid_point]

print(pre_result, result)
print(result - pre_result)