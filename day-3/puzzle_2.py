
import re

data = ""

with open('input') as f: 
    data = f.read()

regex = re.compile("(mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\))")
occurences = regex.findall(data)

result = 0
do = True
for occurence in occurences:
    match occurence:
        case "do()": 
            do = True
        case "don't()":
            do = False
        case _:
            line = occurence.removeprefix("mul(")
            line = line.removesuffix(")")
            nums = list(map(int, line.split(",")))
            if do:
                result += nums[0] * nums[1]

print(result)