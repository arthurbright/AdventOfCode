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

pre = defaultdict(list)

def good(row):
    global pre
    for i in row:
        if i in pre and i in row:
            ind = row.index(i)
            for p in pre[i]:
                if p in row:
                    k = row.index(p)
                    if(k >= ind):
                        return False
    return True

def fix(row):
    global pre
    for i in row:
        if i in pre and i in row:
            ind = row.index(i)
            for p in pre[i]:
                if p in row:
                    k = row.index(p)
                    if(k >= ind):
                        row[ind], row[k] = row[k], row[ind]
                        return fix(row)
    return row


mode = 0
## read in file input as a grid
for line in file:

    if(line == "\n"):
        mode = 1
        continue

    if(mode == 0):
        words = line.split("|")
        a = int(words[0])
        b = int(words[1])
        pre[b].append(a)
    else:
        words = line.split(",")
        row = [int(c) for c in words]
        if  not good(row):
            row = fix(row)
            total += row[len(row)//2]


    
    
print(total)

file.close()