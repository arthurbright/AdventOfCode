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

def inn(r, c):
    if r < 0 or c < 0 or r >= rows or c >= rows:
        return False
    return True

def getnexts(r, c):
    nexts = []
    # if inn(r + 1, c) and grid[r + 1][c] == 'v':
    #     nexts.append((r + 2, c, 2))
    # if inn(r - 1, c) and grid[r - 1][c] == '^':
    #     nexts.append((r - 2, c, 2))
    # if inn(r, c + 1) and grid[r][c + 1] == '>':
    #     nexts.append((r, c + 2, 2))
    # if inn(r, c - 1) and grid[r][c - 1] == '<':
    #     nexts.append((r, c - 2, 2))
    for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if inn(rr, cc) and grid[rr][cc] != '#':
            nexts.append((rr, cc))
    return nexts

keypoints = set([(0, 1), (rows - 1, cols - 2)])
for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        if grid[r][c] != "#":
            acc = 0
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if grid[rr][cc] != "#":
                    acc += 1
            if acc > 2:
                keypoints.add((r, c))
# print(len(keypoints))

#construct a graph
graph = {k:{} for k in keypoints}

for start in keypoints:
    #bfs
    todo = deque()
    visited = set()
    dists = defaultdict(int)

    todo.append(start)
    visited.add(start)
    dists[start] = 0

    while len(todo) > 0:
        cur = todo.popleft()
        if cur in keypoints and cur != start:
            graph[start][cur] = dists[cur]
            graph[cur][start] = dists[cur]
            continue
        for next in getnexts(*cur):
            if next not in visited:
                visited.add(next)
                todo.append(next)
                dists[next] = dists[cur] + 1

# find longest path from endpoints
ans = 0

point_to_ind = {}
ctnt = 0
for p in keypoints:
    point_to_ind[p] = ctnt
    ctnt += 1

@cache
def solve(cur, bitset):
    if cur == (0, 1):
        return 0
    m = -99999999999999999999
    curbit = 1 << point_to_ind[cur]
    for next in graph[cur]:
        ind = point_to_ind[next]
        if (bitset & (1 << ind)) == 0:
            # print(cur, next, bitset, point_to_ind[cur], curbit)
            m = max(m, solve(next, bitset | curbit) + graph[cur][next])
    return m
    

print(solve((rows - 1, cols - 2), 0))
# print(solve((2, 1), 0))


file.close()