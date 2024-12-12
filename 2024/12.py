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

areas = defaultdict(int)
perims = defaultdict(int)
        
#################### read in file input as a grid
for line in file:
    words = line.split()
    word = words[0]

    row = [c for c in word]
    grid.append(row)

rows = len(grid)
cols = len(grid[0])

visited = set()
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(rows):
    for j in range(cols):
        if (i, j) in visited:
            continue
        c = grid[i][j]
        area = 0
        perim = 0
        todo = deque()
        sides = set()
        todo.append((i, j))
        visited.add((i, j))
        while len(todo) > 0:
            a, b = todo.popleft()
            area += 1
            for dx, dy in dirs:
                nx = a + dx
                ny = b + dy
                if not (nx >= 0 and ny >= 0 and nx < rows and ny < cols) or grid[nx][ny] != c:
                    if (a + dy, b + dx, nx + dy, ny + dx) in sides: 
                        if (a - dy, b - dx, nx - dy, ny - dx) in sides:
                            perim -= 1
                    else:
                        if(a - dy, b - dx, nx - dy, ny - dx) in sides:
                            pass
                        else:
                            perim += 1
                    sides.add((a, b, nx, ny))

                    
                if nx >= 0 and ny >= 0 and nx < rows and ny < cols and (nx, ny) not in visited and grid[nx][ny] == c:
                    visited.add((nx, ny))
                    todo.append((nx, ny))
        print(c, area, perim)
        total += area * perim

        

print(total)
file.close()