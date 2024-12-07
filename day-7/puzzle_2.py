
import itertools as it
import operator as op

raw_data = ""

with open("input") as f: 
    raw_data = f.read()

# Test data:
# raw_data = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

lines = raw_data.split("\n")

def concat(x, y):
    return int(str(x) + str(y))

result = 0
for line in lines:

    [test_value, values] = line.split(":")

    test_value = int(test_value)
    values = list(map(int, values[1:].split(" ")))

    l = len(values) - 1
    acc = values[0]

    possible = False
    
    for c in it.product([op.add, op.mul, concat], repeat=l):

        acc = values[0]

        for i in range(len(c)):
            acc = c[i](acc, values[i + 1])
        
        if acc == test_value:
            possible = True
            break
        

    if possible:
        result += test_value

print(result)