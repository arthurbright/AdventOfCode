from collections import defaultdict, deque
from functools import cache
import functools
import math
import heapq
file = open("in", "r")
total = 0
grid = []

    

def print_grid():
    for row in grid:
        print("".join(row))
        
########################## read in file input as a grid
for line in file:
    words = line.split()
    word = words[0]

    row = [c for c in word]
    grid.append(row)

rows = len(grid)
cols = len(grid[0])

sx = rows - 2
sy = 1
fx = 1
fy = cols - 2

visited = set()
todo = []
todo.append((0, sx, sy, 0, 1))
heapq.heapify(todo)
dists = {}
dists[(sx, sy, 0, 1)] = 0

prev = {}
ooga = defaultdict(list)
opt = 9999999999
while len(todo) > 0:
    dist, x, y, dx, dy = heapq.heappop(todo)
    if (x, y, dx, dy) in visited:
        continue
    dists[(x, y, dx, dy)] = dist
    visited.add((x, y, dx, dy))
    if dist > opt:
        continue
    if (x, y) == (fx, fy):
        opt = dist
    if (x, y, dx, dy) == (8, 5, -1, 0) or (x, y, dx, dy) == (7, 4, 0, 1):
        print(x, y, dx, dy, dist)
        

    if grid[x + dx][y + dy] != "#" and (x + dx, y + dy, dx, dy) not in visited:
       heapq.heappush(todo, (dist + 1, x + dx, y + dy, dx, dy))
       next = (x + dx, y + dy, dx, dy)
       ooga[next].append((dist + 1, x, y, dx, dy))
       if next not in dists or dist + 1 < dists[next]:
           prev[next] = [(x, y, dx, dy)]
       elif next in dists and dist + 1 == dists[next]:
           prev[next].append((x, y, dx, dy))
    if (x, y, dy, -dx) not in visited:
        heapq.heappush(todo, (dist + 1000, x, y, dy, -dx))
        next = (x, y, dy, -dx)
        ooga[next].append((dist + 1000, x, y, dx, dy))
        if next not in dists or dist + 1000 < dists[next]:
           prev[next] = [(x, y, dx, dy)]
        elif next in dists and dist + 1000 == dists[next]:
           prev[next].append((x, y, dx, dy))
    if (x, y, -dy, dx) not in visited:
        heapq.heappush(todo, (dist + 1000, x, y, -dy, dx))
        next = (x, y, -dy, dx)
        ooga[next].append((dist + 1000, x, y, dx, dy))
        if next not in dists or dist + 1000 < dists[next]:
           prev[next] = [(x, y, dx, dy)]
        elif next in dists and dist + 1000 == dists[next]:
           prev[next].append((x, y, dx, dy))


total = 0
tododo = deque()

if (fx, fy, 0, 1) in dists and dists[(fx, fy, 0, 1)] == opt:
    tododo.append((fx, fy, 0, 1))
elif (fx, fy, -1, 0) in dists and dists[(fx, fy, -1, 0)] == opt:
    tododo.append((fx, fy, -1, 0))

vis = set()
while len(tododo) > 0:
    cur = tododo.popleft()
    x, y, _, _ = cur
    vis.add((x, y))
    grid[x][y] = "O"
    if (x, y) == (sx, sy):
        continue
    # print(ooga[cur])
    # print(dists[cur])
    for dist, xx, yy, dx, dy in ooga[cur]:
        if dist == dists[cur]:
            tododo.append((xx, yy, dx, dy))


print_grid()
print(len(vis))
file.close()