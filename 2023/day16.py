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

tests = [(r, 0, 0, 1) for r in range(rows)] + [(r, cols - 1, 0, -1) for r in range(rows)] + [(0, c, 1, 0) for c in range(cols)] + [(rows - 1, c, -1, 0) for c in range(cols)]
maxx = 0
for test in tests:
    todo = deque()
    visited = set()

    todo.append(test)

    def out(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return True
        return False


    while len(todo) > 0:
        r, c, vr, vc = todo.popleft()
        if out(r, c):
            continue

        if (r, c, vr, vc) in visited:
            continue
        visited.add((r, c, vr, vc))
        


        if grid[r][c] == ".":
            todo.append((r + vr, c + vc, vr, vc))
        elif grid[r][c] == "|":
            if vc == 0:
                todo.append((r + vr, c + vc, vr, vc))
            else:
                todo.append((r + 1, c, 1, 0))
                todo.append((r - 1, c, -1, 0))
        elif grid[r][c] == "-":
            if vr == 0:
                todo.append((r + vr, c + vc, vr, vc))
            else:
                todo.append((r, c + 1, 0, 1))
                todo.append((r, c - 1, 0, -1))
        elif grid[r][c] == "\\":
            todo.append((r + vc, c + vr, vc, vr))
        elif grid[r][c] == "/":
            todo.append((r - vc, c - vr, -vc, -vr))
    
    
    
    v = set()
    for s in visited:
        r, c, _, _ = s
        v.add((r, c))
    maxx = max(maxx, len(v))

print(maxx)
file.close()