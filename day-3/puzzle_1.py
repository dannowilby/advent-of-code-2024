
import re

data = ""

with open('input') as f: 
    data = f.read()

regex = re.compile("mul\([0-9]+,[0-9]+\)")
occurences = regex.findall(data)

result = 0
for occurence in occurences:
    line = occurence.removeprefix("mul(")
    line = line.removesuffix(")")
    nums = list(map(int, line.split(",")))
    result += nums[0] * nums[1]

print(result)