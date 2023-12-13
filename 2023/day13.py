from collections import defaultdict, deque
from functools import cache
import itertools
import functools
import math


file = open("in", "r")

total = 0

lines = iter(file)

def findpre(gridd, rows, cols):
    ans = []
    for r in range(1, rows):
        # try row\
        good = True
        for i in range(0, rows):

            if r - 1 - i < 0 or r + i >= rows: 
                break
            if gridd[r - i  - 1] != gridd[r + i]:
                good = False
                break
        if good:
           # print(f"r: {r}") 
            ans.append(100 * r)

    grid2 = [[gridd[r][c] for r in range(rows)] for c in range(cols)]
    for c in range(1, cols):
        good = True
        for i in range(0, cols):
            if c - 1 - i < 0 or c + i >= cols:
                break
            if grid2[c - 1 - i] != grid2[c + i]:
                good = False
                break

        if good:
           # print(f"c: {c}") 
            ans.append(c)
    return ans
    raise Exception("NO MIRROR FOUND")


def flip(s):
    if s == ".":
        return "#"
    return "."

grid = []
while(line := next(lines, None)):

    words = line.split()
    if len(words) == 0:
        #LOGIC
        rows = len(grid)
        cols = len(grid[0])
        oldans = findpre(grid, rows, cols)[0]
        cnt = 0
        found = False
        for i in range(rows):
            for j in range(cols):
                #flip
                gridd = [[e for e in row] for row in grid]
                gridd[i][j] = flip(grid[i][j])
                try:
                    a = findpre(gridd, rows, cols)
                    #print(len(a))
                    if len(a) > 1 and not found:
                        #print(a)
                        total += sum(a) - oldans
                        found = True
                    if len(a) == 1 and a[0] != oldans and not found:
                        found = True
                        total += a[0]
                   
                    
                except Exception:
                    pass
                
        
        # print(total)

        # reset
        grid = []
        continue

    word = words[0]
    row = [c for c in word]
    grid.append(row)

    #add back to the iterator
    #words = itertools.chain(["hi"], words)

# add back to the iterator
#lines = itertools.chain(["hi there"], lines)


print(total)

file.close()