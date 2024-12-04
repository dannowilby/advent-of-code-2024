
# M M
#  A
# S S

data = ""

with open("input") as f: 
    data = f.read()

lines = data.split("\n")

grid = []

for line in lines:
    grid.append(list(line))

w = len(grid)
h = len(grid[0])

result = 0

for x in range(w):
    for y in range(h):
        
        if x == 0 or x == w - 1:
            continue
        if y == 0 or y == h - 1:
            continue

        if grid[x][y] == "A":
            
            score = 0
            
            if grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S":
                score += 1
            if grid[x - 1][y - 1] == "S" and grid[x + 1][y + 1] == "M":
                score += 1

            if grid[x + 1][y - 1] == "M" and grid[x - 1][y + 1] == "S":
                score += 1
            if grid[x + 1][y - 1] == "S" and grid[x - 1][y + 1] == "M":
                score += 1

            if score == 2:
                result += 1

print(result)