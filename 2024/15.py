from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")
total = 0
grid = []
def print_grid():
    for row in grid:
        print("".join(row))
        

x = -1
y = -1

def move(m):
    global grid
    
    global x
    global y
    rows = len(grid)
    cols = len(grid[0])
    # print(m)
    if m == "^":
        dx, dy = -1, 0
    elif m == ">":
        dx, dy = 0, 1
    elif m == "v":
        dx, dy = 1, 0
    elif m == "<":
        dx, dy = 0, -1
    
    tx = x
    ty = y
    if dx == 0:
        while tx >= 0 and ty >= 0 and tx < rows and ty < cols and grid[tx][ty] != ".":
            if grid[tx][ty] == "#":
                break
            tx += dx
            ty += dy
        if grid[tx][ty] == "#" or not (tx >= 0 and ty >= 0 and tx < rows and ty < cols):
            # do nothing
            pass
        else:
            #shift
            if dy < 0:
                last = "["
            else: last = "]"
            while ty != y:
                grid[x][ty] = last
                last = "[" if last == "]" else "]"
                ty -= dy
            grid[x][y] = "."
            grid[x + dx][y + dy] = "@"
            x += dx
            y += dy
        print(x, y)
    else:
        #dy = 0
        pushing = [y]
        grid2 = [[x for x in row] for row in grid]

        push = True
        goodd = False
        tx += dx
        while tx >= 0 and tx < rows:
            newpushing = []
            for yy in pushing:
                if grid[tx][yy] == "#":
                    push = False
                    break
                elif grid[tx][yy] == "[":
                    newpushing.append(yy)
                    newpushing.append(yy + 1)
                    grid2[tx][yy] = grid[tx - dx][yy]
                    if yy + 1 in pushing:
                        grid2[tx][yy + 1] = grid[tx - dx][yy + 1]
                    else:
                        grid2[tx][yy + 1] = "."
                elif grid[tx][yy] == "]":
                    newpushing.append(yy)
                    newpushing.append(yy - 1)
                    grid2[tx][yy] = grid[tx - dx][yy]
                    if yy - 1 in pushing:
                        grid2[tx][yy - 1] = grid[tx - dx][yy - 1]
                    else:
                        grid2[tx][yy - 1] = "."
                elif grid[tx][yy] == ".":
                    # do nothing?
                    grid2[tx][yy] = grid[tx - dx][yy]
            pushing = list(set(newpushing))
            if len(newpushing) == 0:
                goodd = True
                break

            if push == False:
                break
            tx += dx
        
        if push == False:
            return
        elif goodd == True:
            # print("GOOD")
            grid2[x][y] = "."
            x += dx
            grid = grid2
        # if grid[tx][ty] == "#" or not (tx >= 0 and ty >= 0 and tx < rows and ty < cols):
        #     # do nothing
        #     pass
        # else:
        #     #shift
        #     last = "["
        #     while ty != y:
        #         grid[x][ty] = last
        #         last = "[" if last == "]" else "]"
        #         ty -= dy
        #         grid[x][i]
        #     grid[x][y] = "."
        #     grid[x + dx][y + dy] = "@"
        #     x += dx
        #     y += dy
        
        
######### read in file input as a grid

rrr = 0
gridd = True
for line in file:
    if line[0] == "a":
        gridd = False
        continue

    if gridd:
        # print(line)
        words = line.split()
        word = words[0]
        row = ""
        for c in word:
            if c == ".": row += ".."
            elif c == "#": row += "##"
            elif c == "@": row += "@."
            else: row += "[]"
        row = [c for c in row]
        grid.append(row)
        if "@" in row:
            x = rrr
            y = row.index("@")
        rrr += 1
    else:
        words = line.split()
        for c in words[0]:
            move(c)

rows = len(grid)
cols = len(grid[0])
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "[":
            total += 100 * row + col

print_grid()
print(total)
file.close()