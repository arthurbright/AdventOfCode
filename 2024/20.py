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
        
############ read in file input as a grid
rr = 0

sx = 0
sy = 0
fx = 0
fy = 0
for line in file:
    words = line.split()
    word = words[0]

    row = [c for c in word]
    if "S" in row:
        sx = rr
        sy = row.index("S")
    if "E" in row:
        fx = rr
        fy = row.index("E")

    grid.append(row)
    rr += 1

rows = len(grid)
cols = len(grid[0]) 

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
todo = deque()
todo.append((sx, sy))
visited = set()
visited.add((sx, sy))
dists = {}
dists[(sx, sy)] = 0
while len(todo) > 0:
    x, y = todo.popleft()
    for dx, dy in dirs:
        nx = dx + x
        ny = dy + y
        if grid[nx][ny] != "#" and (nx, ny) not in visited:
            todo.append((nx, ny))
            visited.add((nx, ny))
            dists[(nx, ny)] = 1 + dists[(x, y)]


todo = deque()
todo.append((fx, fy))
visited = set()
visited.add((fx, fy))
dists2 = {}
dists2[(fx, fy)] = 0
while len(todo) > 0:
    x, y = todo.popleft()
    for dx, dy in dirs:
        nx = dx + x
        ny = dy + y
        if grid[nx][ny] != "#" and (nx, ny) not in visited:
            todo.append((nx, ny))
            visited.add((nx, ny))
            dists2[(nx, ny)] = 1 + dists2[(x, y)]

ddd = defaultdict(int)
shortest = dists[(fx, fy)]
total = 0
for i in range(rows):
    print(i)
    for j in range(cols):
        if grid[i][j] == "#":
            continue
        checks = set()
        for t in range(1, 21): # 1... 21
            for k in range(t + 1): #0... t
                for a in [(i + k, j + t - k), (i - k, j + t - k), (i - k, j - t + k), (i + k, j - t + k)]:
                    checks.add(a)
        
        for ii, jj in list(checks):
            if ii < 0 or jj < 0 or ii >= rows or jj >= cols:
                continue
            if grid[ii][jj] == "#":
                continue
            # if i > ii or j > jj:
            #     continue
            
            anss = []
            for (x, y) in [(i, j), (ii, jj)]:
                mins1 = 999999999
                minf1 = 999999999
                for di, dj in dirs:
                    i1 = x + di
                    j1 = y + dj
                    if i1 < 0 or j1 < 0 or i1 >= rows or j1 >= cols:
                        continue
                    elif grid[i1][j1] != "#":
                        mins1 = min(mins1, dists[(i1, j1)] + 1)
                        minf1 = min(minf1, dists2[(i1, j1)] + 1)

                if grid[x][y] != "#":
                    mins1 = min(mins1, dists[(x, y)])
                    minf1 = min(minf1, dists2[(x, y)])
                anss.append(mins1)
                anss.append(minf1)

            a, b, c, d = anss
            t = abs(ii - i) + abs(jj - j)
            comp = min(a + d + t, b + c + t)
            if shortest -50 >= comp:
                ddd[shortest - comp] += 1
            if comp <= shortest - 100:
                total += 1

aaa = [(k, ddd[k]//2) for k in ddd]
aaa.sort()
print(aaa)


print(total, total//2)
file.close()