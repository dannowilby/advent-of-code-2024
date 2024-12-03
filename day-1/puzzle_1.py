
list1 = []
list2 = []

with open('input', 'r') as file:
    lines = file.readlines()
    for line in lines:
        nums = line.split("   ")
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

list1.sort();
list2.sort();

result = [abs(x - y) for x, y in zip(list1, list2)]

print(sum(result))