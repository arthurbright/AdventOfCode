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
    
    
print(total)

file.close()