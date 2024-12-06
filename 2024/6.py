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
## read in file input as a grid
for line in file:
    words = line.split()
    word = words[0]

    row = [c for c in word]
    if "^" in row:
        y= row.index("^")
        x = len(grid)
    grid.append(row)

rows = len(grid)
cols = len(grid[0])

xx = x
yy = y
    
k = set()
dir = (-1, 0)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for tx in range(rows):
    print(tx)
    for ty in range(cols):
        if grid[tx][ty] == "#" or grid[tx][ty] == "^": continue

        grid[tx][ty] = "#"
        seen = set()
        cnt = 0
        x = xx
        y = yy
        dir = (-1, 0)
        while (x >= 0) and (y >= 0) and x < rows and y < rows:
            if ((dir, x, y)) in seen:
                total += 1
                break
            seen.add((dir, x, y))
            nx = x + dir[0]
            ny = y + dir[1]

            if (nx >= 0) and (ny >= 0) and nx < rows and ny < rows and grid[nx][ny] == "#":
                dir = dirs[(dirs.index(dir) + 1) % 4]
            else:
                x, y = nx, ny
        grid[tx][ty] = "."
    
print(total)

file.close()