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

def proc(row):
    row2 = []
    for i in row:
        ll = len(str(i))
        if i == 0:
            row2.append(1)
        
        elif ll % 2 == 0:
            # print(str(i), ll)
            row2.append(int(str(i)[0:ll//2]))
            row2.append(int(str(i)[ll//2:]))
        else:
            row2.append(i * 2024)
    return row2

@cache
def procc(i, itr):
    if itr == 0: return 1
    ll = len(str(i))
    if(i == 0): return procc(1, itr - 1)
    if ll % 2 == 0:
        return procc(int(str(i)[0:ll//2]), itr - 1) + procc(int(str(i)[ll//2:]), itr - 1)
    else:
        return procc(i * 2024, itr - 1)
        
## read in file input as a grid
for line in file:
    words = line.split()
    

    row = [int(c) for c in words]
    for k in row:
        total += procc(k, 75)

    print(total)
    


file.close()