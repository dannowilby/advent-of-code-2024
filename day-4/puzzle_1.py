
# S  S  S
#  A A A
#   MMM
# SAMXMAS
#   MMM
#  A A A
# S  S  S

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
        if grid[x][y] == "X":
            up = x - 3 < 0
            down = x + 3 >= w
            left = y - 3 < 0
            right = y + 3 >= h

            # search right
            if (not right) and (grid[x][y + 1] == "M" and grid[x][y + 2] == "A" and grid[x][y + 3] == "S"):
                result += 1
            
            # search left
            if (not left) and (grid[x][y - 1] == "M" and grid[x][y - 2] == "A" and grid[x][y - 3] == "S"):
                result += 1

            # search up
            if (not up) and (grid[x - 1][y] == "M" and grid[x - 2][y] == "A" and grid[x - 3][y] == "S"):
                result += 1

            # search down
            if (not down) and (grid[x + 1][y] == "M" and grid[x + 2][y] == "A" and grid[x + 3][y] == "S"):
                result += 1
            
            # search diagonal 1
            if (not (left) and not (up)) and (grid[x - 1][y - 1] == "M" and grid[x - 2][y - 2] == "A" and grid[x - 3][y - 3] == "S"):
                result += 1
            
            # search diagonal 2
            if (not (right) and  not (up)) and (grid[x - 1][y + 1] == "M" and grid[x - 2][y + 2] == "A" and grid[x - 3][y + 3] == "S"):
                result += 1

            # search diagonal 3
            if (not (left) and not (down)) and (grid[x + 1][y - 1] == "M" and grid[x + 2][y - 2] == "A" and grid[x + 3][y - 3] == "S"):
                result += 1

            # search diagonal 4
            if (not (right) and not (down)) and (grid[x + 1][y + 1] == "M" and grid[x + 2][y + 2] == "A" and grid[x + 3][y + 3] == "S"):
                result += 1

print(result)