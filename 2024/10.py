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

for i in range(rows):
    for j in range(cols):
        counts = [[0 for i in range(cols)] for j in range(rows)]
        if grid[i][j] != 0: continue
        todo = deque()
        visited = set()
        visited.add((i, j))
        todo.append((i, j))
        counts[i][j] = 1
        score = 0
        # print(i, j)
        visited.add((i, j))
        while len(todo) > 0:
            a, b = todo[0]
            todo.popleft()
            v = grid[a][b]
            # print(a, b, v)
            if v == 9:
                score += counts[a][b]
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = a + dx, b + dy
                if nx >= 0 and ny >= 0 and nx < rows and ny < cols and grid[nx][ny] == v + 1:
                    counts[nx][ny] += counts[a][b]
                if nx >= 0 and ny >= 0 and nx < rows and ny < cols and grid[nx][ny] == v + 1 and not (nx, ny) in visited:
                    todo.append((nx, ny))
                    visited.add((nx, ny))
                

        total += score
        print(counts)

    
print(total)
file.close()