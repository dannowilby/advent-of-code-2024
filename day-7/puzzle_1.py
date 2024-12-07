
import itertools as it
import operator as op
import math

raw_data = ""

with open("input") as f: 
    raw_data = f.read()

lines = raw_data.split("\n")

result = 0
for line in lines:

    [test_value, values] = line.split(":")

    test_value = int(test_value)
    values = list(map(int, values[1:].split(" ")))

    l = len(values) - 1
    acc = values[0]

    possible = False
    
    for c in it.product([op.add, op.mul], repeat=l):

        for i in range(len(c)):
            acc = c[i](acc, values[i + 1])

        if acc == test_value:
            possible = True
        
        acc = values[0]

    if possible:
        result += test_value

print(result)

