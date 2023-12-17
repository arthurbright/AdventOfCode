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

    row = [int(c) for c in word]
    grid.append(row)

rows = len(grid)
cols = len(grid[0])

import heapq
todo = []
dists = defaultdict(lambda: 999999999999)
visited = set()
starts = [(i, 0, 1) for i in range(4, 11)] + [(0, i, 0) for i in range(4, 11)]

def out(r, c):
    if r < 0 or c < 0 or r >= rows or c >= rows:
        return True
    return False

def dist(r, c, r2, c2):
    if c == c2:
        return sum([grid[i][c] for i in range(min(r, r2), max(r, r2) + 1)]) - grid[r][c]
    elif r == r2:
        return sum([grid[r][i] for i in range(min(c, c2), max(c, c2) + 1)]) - grid[r][c]
    else:
        raise Exception("ILLEGAL DIST")
    
for i in starts:
    dists[i] = dist(0, 0, i[0], i[1])
    heapq.heappush(todo, (dists[i], i))

def neighbors(r, c, dir):
    n = []
    if dir == 0:
        return [(r + i, c, 1) for i in range(4, 11)] + [(r - i, c, 1) for i in range(4, 11)]
    else:
        return [(r, c + i, 0) for i in range(4, 11)] + [(r, c - i, 0) for i in range(4, 11)]

while len(todo) > 0:
    val, cur = heapq.heappop(todo)
    visited.add(cur)
    

    r, c, dir = cur
    if r == rows - 1 and c == cols - 1:
        print(dists[cur])
        break

    for next in neighbors(r, c, dir):
        r2, c2, _ = next
        if out(r2, c2): continue
        if next not in visited and dists[cur] + dist(r, c, r2, c2) < dists[next]:
            dists[next] = dists[cur] + dist(r, c, r2, c2)
            heapq.heappush(todo, (dists[next], next))
    
file.close()