
raw_data = ""

with open("input") as f: 
    raw_data = f.read()

lines = raw_data.split("\n")

def pos_key(p):
    return p[0] * 1000 + p[1]

def in_bounds(w, h, p):
    if (p[0] < 0 or p[0] >= w) or (p[1] < 0 or p[1] >= w):
        return False
    return True

def rotate_look(l):
    if l == [-1, 0]:
        return [0, 1]
    if l == [0, 1]:
        return [1, 0]
    if l == [1, 0]:
        return [0, -1]
    if l == [0, -1]:
        return [-1, 0]
    return [0, 0]

pos = []
visited = {}
grid = []
# out_grid = [] # uncomment out_grid to create visualization
for idx, line in enumerate(lines):

    if "^" in line:
        pos.append(idx)
        pos.append(line.index("^"))
        visited[pos_key(pos)] = True

    grid.append(list(line))
    # out_grid.append(list(line))


width = len(grid[0])
height = len(grid)

look = [-1, 0]

debug_counter = 10
while in_bounds(width, height, pos):
    
    # if not debug_counter == 0:
    #     print(pos)
    #     debug_counter -= 1

    visited[pos_key(pos)] = True
    # out_grid[pos[0]][pos[1]] = "X"
    
    next_pos = [sum(x) for x in zip(pos, look)]

    if grid[next_pos[0]][next_pos[1]] == "#":
        look = rotate_look(look)
    else:
        pos = next_pos

# print(pos)
print(len(visited))

# # To write the resulting path for visualization
# with open('output', 'w') as file:
#
#    for line in out_grid:
#         file.write(''.join(line))
#         file.write("\n")
