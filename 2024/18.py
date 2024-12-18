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

DIM = 71
LIM = 1024
grid = [["." for i in range(DIM)] for i in range(DIM)]
##################### read in file input as a grid
ii = 0
for line in file:
    words = line.split(",")
    x = int(words[0])
    y = int(words[1])
    grid[x][y] = "#"
    ii += 1
    print(ii)
    # if ii == LIM:
    #     break

    todo = deque()
    visited = set()
    visited.add((0, 0))
    todo.append((0, 0))

    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    dists = {}
    dists[(0, 0)] = 0
    while len(todo) > 0:
        x, y = todo.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < DIM and ny >= 0 and ny < DIM and (nx, ny) not in visited and grid[nx][ny] != "#":
                visited.add((nx, ny))
                todo.append((nx, ny))
                dists[(nx, ny)] = dists[(x, y)] + 1

    # print(dists[(DIM - 1, DIM - 1)])
    if((DIM - 1, DIM - 1)) not in visited:
        print(line)
        break
# print_grid()
file.close()