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
        
## read in file input as a grid
for line in file:
    words = line.split()
    word = words[0]

    row = [c for c in word]
    grid.append(row)

rows = len(grid)
cols = len(grid[0])

def good(a, b, c, d):
    if(a == "X" and b == "M" and c == "A" and d == "S"): return True
    if(a == "S" and b == "A" and c == "M" and d == "X"): return True
    return False

def good2(a, b, c, d, e):
    if(a == "M" and b == "S") or (a == "S" and b == "M"):
        return ((c == "M" and d == "S") or (c == "S" and d == "M")) and e == "A"
    return False
    
# for i in range(rows):
#     for j in range(cols):
#         if(i >= 3) and good(grid[i][j], grid[i - 1][j], grid[i - 2][j], grid[i - 3][j]):
#             total += 1
#         if(j >= 3) and good(grid[i][j], grid[i][j - 1], grid[i][j - 2], grid[i][j - 3]):
#             total += 1
#         if (i >= 3) and j >= 3:
#             if good(grid[i][j], grid[i - 1][j - 1], grid[i - 2][j - 2], grid[i - 3][j - 3]):
#                 total += 1
#             if good(grid[i - 3][j], grid[i - 2][j - 1], grid[i - 1][j - 2], grid[i][j - 3]):
#                 total += 1

for i in range(rows):
    for j in range(cols):
        if (i >= 2) and j >= 2:
            if good2(grid[i][j], grid[i - 2][j - 2], grid[i - 2][j], grid[i][j - 2], grid[i - 1][j - 1]):
                total += 1
    
    
print(total)

file.close()