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

@cache
def pow(n):
    if n == 0: return 1
    return 2 * pow(n - 1)

def has(r):
    acc = 0
    for i, a in enumerate(r):
        if a == "O":
            acc += pow(i) 
    return acc
def hash(g):
    return tuple(has(r) for r in g)
#spin
NUM = 4000000000
seen = {}
found = False
for cycle in range((NUM - 440) % 36 + 440 + 36):
#for cycle in range(NUM):
    grid2 = []
    rows = len(grid)
    cols = len(grid[0])
    total = 0
    # north
    for c in range(cols):
        #print(total)
        cnt = 0
        col = [grid[r][c] for r in range(rows)]
        str = "".join(col)
        ll = rows

        newrow = []
        wordss = str.split("#")
        for i, seg in enumerate(wordss):
            nums = seg.count("O")
            for ii in range(nums):
                total += ll - ii
            ll -= len(seg) + 1
            if i != 0:
                newrow += ["#"]
            newrow += ["O"] * nums
            newrow += ["."] * (len(seg) - nums)

        grid2.append(list(reversed(newrow)))
    if not found and cycle % 4 == 0 and hash(grid2) in seen:
        #grid = grid2
        #print_grid()
        # print(hash(grid))
        print(f"last seen: {seen[hash(grid2)]}")
        print(f"current seen: {cycle}")
        print(total)
        print("SEEN")
        found = True
    elif cycle % 4 == 0:
        seen[hash(grid2)] = cycle
    grid = grid2
    # print_grid()
    # print(total)

#print_grid()
total = 0
rows = len(grid)
cols = len(grid[0])
print(rows)
for i, r in enumerate(grid):
    total += (rows - i) * r.count("O")

print(total)

file.close()