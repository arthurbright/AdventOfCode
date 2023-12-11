from collections import defaultdict, deque
import functools
import math

file = open("in", "r")

total = 0

grid = []
galaxies = []
for line in file:
    words = line.split()
    word = words[0]

    row = [c for c in word]
    grid.append(row)

rows = len(grid)
cols = len(grid[0])

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "#":
            galaxies.append((i, j))

emptyRows = []
emptyCols = []

for i in range(rows):
    a = True
    for j in range(cols):
        if grid[i][j] == "#":
            a = False
            break

    if a:
        emptyRows.append(i)

for i in range(cols):
    a = True
    for j in range(rows):
        if grid[j][i] == "#":
            a = False
            break
    if a:
        emptyCols.append(i)

for i in emptyCols:
    print(i)

total = 0
for gg in range(len(galaxies)):
    g = galaxies[gg]
    r1, c1 = g
    for gg2 in range(gg + 1, len(galaxies)):
        g2 = galaxies[gg2]
        r2, c2 = g2
        temp = abs(r2 - r1) + abs(c2 - c1)
        for r in range(min(r1, r2), max(r1, r2)):
            if r in emptyRows:
                temp += 1000000 - 1
        for c in range(min(c1, c2), max(c1, c2)):
            if c in emptyCols:
                temp += 1000000 - 1
        total += temp
        #print(g, g2, temp)



    
print(total)

file.close()