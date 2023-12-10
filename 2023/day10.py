from collections import defaultdict, deque
import functools
import math

file = open("in", "r")

total = 0

grid = []

startr = -1
startc = -1

row = 0
for line in file:
    words = line.split()
    word = words[0]

    roww = []
    col = 0
    for c in word:
        roww.append(c)
        if c == "-" or c == "F" or c == "L" or c == "S": 
            roww.append("-")
        else:
            roww.append(".")
        if c == "S":
            startr = row
            startc = col
        col += 2
    
    grid.append(roww)
    roww2 = []
    for c in roww:
        if c == "|" or c == "7" or c == "F" or c == "S":
            roww2.append("|")
        else:
            roww2.append(".")

    grid.append(roww2)
    row += 2

#print(grid)

def getNexts(r, c):
    if grid[r][c] == "S":
        return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        #return [(r + 1, c)]
    if grid[r][c] == ".":
        return []
    elif grid[r][c] == "F":
        return [(r + 1, c), (r, c + 1)]
    elif grid[r][c] == "7":
        return [(r + 1, c), (r, c - 1)]
    elif grid[r][c] == "J":
        return [(r - 1, c), (r, c - 1)]
    elif grid[r][c] == "L":
        return [(r - 1, c), (r, c + 1)]
    elif grid[r][c] == "|":
        return [(r - 1, c), (r + 1, c)]
    elif grid[r][c] == "-":
        return [(r, c + 1), (r, c - 1)]
    else:
        raise Exception(f"unkonw char:  {grid[r][c]}")

# try start directions
def tryNav():
    visited = set()
    visited.add((startr, startc))

    dists = {}
    dists[(startr, startc)] = 0
    #bfs
    todo = deque()
    todo.append((startr, startc))
    maxx = 0

    ends = []
    while(len(todo) > 0):
        #print(todo)
        rr, cc = todo.popleft()
        maxx = max(maxx, dists[(rr, cc)])
        #print(rr, cc)

        foundnext = 0
        for next in getNexts(rr, cc):
            nextr, nextc = next
            if nextr < 0 or nextc < 0 or nextr >= row or nextc >= col:
                continue
            if (rr, cc) in getNexts(nextr, nextc) and next not in visited:
                visited.add(next)
                dists[next] = dists[(rr, cc)] + 1
                todo.append(next)
                foundnext += 1
            #print(foundnext)
        if foundnext == 0:
            ends.append((rr, cc))
    return (ends, dists)


ends, dists = tryNav()
print(ends)
for i in ends:
    for j in ends:
        if i != j and j in getNexts(*i) and i in getNexts(*j):
            #print(max(dists[i], dists[j]))
            pass
    

status = [[0 for i in range(col)] for j in range(row)]

# BFS status Wall
todo = deque()
visited = set()
visited.add(ends[0])
todo.append(ends[0])

status[startr][startc] = 2
while len(todo) > 0:
    cur = todo.popleft()
    status[cur[0]][cur[1]] = 2
    for next in getNexts(*cur):
        if next not in visited and next != (startr, startc):
            visited.add(next)
            todo.append(next)

total = 0
todo = deque()
visited = set()

for i in range(row):
    if status[i][0] != 2:
        todo.append((i, 0))
        visited.add((i, 0))
    if status[i][col - 1] != 2:
        todo.append((i, col - 1))
        visited.add((i, col - 1))

for i in range(col):
    if status[0][i] != 2:
        todo.append((0, i))
        visited.add((0, i))
    if status[row - 1][i] != 2:
        todo.append((row - 1, i))
        visited.add((row - 1, i))
    
def fil(p):
    r, c = p
    return r >= 0 and c >= 0 and r < row and c < col
def getAdjs(r, c):
    cand = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    cand = list(filter(fil, cand))
    return cand

while len(todo) > 0:
    cur = todo.popleft()
    status[cur[0]][cur[1]] = 1
    for next in getAdjs(*cur):
        if next not in visited and status[next[0]][next[1]] != 2:
            visited.add(next)
            todo.append(next)

total = 0
statuss = [[str(i) for i in row] for row in status]
for i in range(row):
    #print("".join(statuss[i]))
    for c in range(col):
        
        if status[i][c] == 0 and i % 2 == 0 and c % 2 == 0:
            total += 1

print(total)
    

file.close()