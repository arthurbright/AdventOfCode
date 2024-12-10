from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")

total = 0

locs = defaultdict(list)

grid = []
def print_grid():
    for row in grid:
        print("".join(row))
        
## read in file input as a grid
rr = 0
for line in file:
    words = line.split()
    word = words[0]

    row = [c for c in word]
    grid.append(row)
    cc = 0
    for c in row:
        if c != ".":
            locs[c].append((rr, cc))
        cc += 1
    rr += 1


rows = len(grid)
cols = len(grid[0])

goods = set()
for c in locs:
    lis = locs[c]
    for x, y in lis:
        for x1, y1 in lis:
            if (x, y) == (x1, y1):
                continue
            aa, bb = x, y
            dx = x - x1
            dy = y - y1

            
            while aa >= 0 and bb >= 0 and aa < rows and bb < cols:
                goods.add((aa, bb))
                aa += dx
                bb += dy

            aa, bb = x, y
            while aa >= 0 and bb >= 0 and aa < rows and bb < cols:
                goods.add((aa, bb))
                aa -= dx
                bb -= dy

    
print(len(goods))

file.close()