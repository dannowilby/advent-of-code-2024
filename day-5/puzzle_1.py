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

result = 0

n_valid = 0
n_invalid = 0
for p in prints:
    valid = True

    for idx, x in enumerate(p):
        for idy, y in enumerate(p):
            if idy <= idx:
                continue
            
            # if reverse of two values is a rule, then the sequence is invalid
            if y in rules and x in rules[y]:
                valid = False
    
    if valid:
        n_valid += 1
        mid_point = math.floor(len(p) / 2)
        result += p[mid_point]
    else:
        n_invalid += 1

print(n_valid, n_invalid)
print(result)