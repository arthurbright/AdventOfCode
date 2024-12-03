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
        
def safe(row):
    ll = len(row)
    if row[0] < row[1]:
        low = 1
        hi = 3
    else:
        low = -3
        hi = -1
    
    good = True
    for i in range(ll - 1):
        if not (low <= row[i + 1] - row[i] <= hi):
            good = False
            break
    
    return good
    
## read in file input as a grid
for line in file:
    words = line.split()

    row = [int(c) for c in words]
    good = safe(row)
    ll = len(row)
    for i in range(ll):
        cc = row.copy()
        cc.pop(i)
        if safe(cc):
            good = True
    if good:
        total += 1
    
print(total)

file.close()