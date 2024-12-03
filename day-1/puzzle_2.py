
list1 = []
list2 = []

with open('input', 'r') as file:
    lines = file.readlines()
    for line in lines:
        nums = line.split("   ")
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

result = 0

freqs = {}
for value in list2:
    freqs[value] = freqs.get(value, 0) + 1 

for idx, x in enumerate(list1):
    result += freqs.get(x, 0) * x

print(result)