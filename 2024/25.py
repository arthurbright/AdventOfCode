from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
rows = 0
cols = 0
def in_bounds(r, c):
    global rows
    global cols
    return r >= 0 and c >= 0 and r < rows and c < cols

total = 0
grid = []
def print_grid():
    for row in grid:
        print("".join(row))
        
keys = []
locks = []
grid = []
############################ read in file input as a grid
for line in file:
    line = line.strip()
    if len(line) == 0:
        # save grid
        levels = []
        if grid[0][0] == ".":
            for i in range(5):
                for j in range(7):
                    if grid[j][i] == "#":
                        levels.append(6 - j)
                        break
                    
            keys.append(levels)
        else:
            for i in range(5):
                for j in range(7):
                    if grid[j][i] == ".":
                        levels.append(j - 1)
                        break
            locks.append(levels)
        grid = []
    else:
        row = [c for c in line]
        grid.append(row)

# print(keys)
# print(locks)

for key in keys:
    for lock in locks:
        good = True
        for i in range(5):
            if key[i] + lock[i] >= 6:
                good = False
                break
        if good:
            total += 1

print(total)
file.close()