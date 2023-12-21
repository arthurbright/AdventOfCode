from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")

grid = []
def print_grid():
    for row in grid:
        print("".join(row))
        
startr = 0
startc = 0
## read in file input as a grid
rrr = 0
for line in file:
    words = line.split()
    word = words[0]

    row = [c for c in word]
    for i in range(len(word)):
        if word[i] == "S":
            startr = rrr
            startc = i

    grid.append(row)
    rrr += 1

rows = len(grid)
cols = len(grid[0])

def good(r, c):
    if r < -1 or c < -1 or r > rows or c > cols: return False
    return True

griddy = {}
for r in range(rows):
    griddy[r] = {}
    for c in range(cols):
        griddy[r][c] = grid[r][c]
griddy[-1] = {}
griddy[rows] = {}
for r in range(-1, rows + 1):
    griddy[r][-1] = "."
    griddy[r][cols] = "."
for c in range(-1, cols + 1):
    griddy[-1][c] = "."
    griddy[rows][c] = "."

TOTALDIST = 26501365
#TOTALDIST = 65 * 2 + 3

@cache
def bfs(rr, cc, curdist):
    if curdist > TOTALDIST:
        return 0

    dists = {}
    todo = deque()
    todo.append((rr, cc))
    dists[(rr, cc)] = 0
    total = 0
    while len(todo) > 0:
        
        r, c = todo.popleft()
        if dists[(r, c)] + curdist > TOTALDIST:
            continue

        for next in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            nextr, nextc = next
            if good(nextr, nextc) and (nextr, nextc) not in dists and griddy[nextr][nextc] != "#":
                dists[(nextr, nextc)] = dists[(r, c)] + 1
                todo.append((nextr, nextc))

    for k in dists:
        #print(k, dists[k] + curdist)
        if (curdist + dists[k]) % 2 == 1 and dists[k] + curdist <= TOTALDIST:
            p, q = k
            if p >= 0 and q >= 0 and p < rows and q < cols:
                total += 1
        
    return total

flippy = {
    0: -1,
    -1: 0,
    rows - 1: rows,
    rows: rows - 1,
    startc: startc
}

def get_chunk(chunkr, chunkc):
    rr = None
    cc = None
    if chunkr == 0:
        rr = startr
    elif chunkr > 0:
        rr = -(chunkr % 2)
    else:
        rr = rows - 1 + (chunkr % 2)
    
    if chunkc == 0:
        cc = startc
    elif chunkc > 0:
        cc = -(chunkc % 2)
    else:
        cc = cols - 1 + (chunkc % 2)

    ##toggle
    rr, cc = flippy[rr], flippy[cc]

    distleft =  abs(chunkr * rows + rr - startr) + abs(chunkc * cols + cc - startc)
    ans =  bfs(rr, cc, distleft)
    return ans

# print(get_chunk(1, 1))
# exit()



# positive r
tots = get_chunk(0, 0)
last = (-1, -1)
radius = TOTALDIST//rows + 8 # even
for r in range(radius, 0, -2):
    a = get_chunk(r, 0)
    b = get_chunk(r - 1, 0)
    if (a, b) == last and last != (0, 0):
        tots += (r//2) * (a + b)
        break
    else:
        tots += a + b
        last = (a, b)

last = (-1, -1)
#positive c
for c in range(radius, 0, -2):
    a = get_chunk(0, c)
    b = get_chunk(0, c - 1)
    if (a, b) == last and last != (0, 0):
        tots += (c//2) * (a + b)
        break
    else:
        tots += a + b
        last = (a, b)

#negative r
last = (-1, -1)
for r in range(radius, 0, -2):
    a = get_chunk(-r, 0)
    b = get_chunk(-(r - 1), 0)
    if (a, b) == last and last != (0, 0):
        tots += (r//2) * (a + b)
        break
    else:
        tots += a + b
        last = (a, b)

#negative c
last = (-1, -1)
for c in range(radius, 0, -2):
    a = get_chunk(0, -c)
    b = get_chunk(0, -(c - 1))
    if (a, b) == last and last != (0, 0):
        tots += (c//2) * (a + b)
        break
    else:
        tots += a + b
        last = (a, b)

# pos pos ############################################
last = (-1, -1)
for r in range(radius, 0, -2):
    a = get_chunk(r, 1)
    b = get_chunk(r - 1, 1)

    if (a, b) == last and last != (0, 0):
        for rr in range(1, r + 1):
            if rr % 2 == 0:
                tots += rr * a
            else:
                tots += rr * b
        break
    else:
        tots += a * r + b * (r - 1)
        last = (a, b)

last = (-1, -1)
for r in range(radius, 0, -2):
    a = get_chunk(r, -1)
    b = get_chunk(r - 1, -1)

    if (a, b) == last and last != (0, 0):
        for rr in range(1, r + 1):
            if rr % 2 == 0:
                tots += rr * a
            else:
                tots += rr * b
        break
    else:
        tots += a * r + b * (r - 1)
        last = (a, b)


last = (-1, -1)
for r in range(radius, 0, -2):
    a = get_chunk(-r, 1)
    b = get_chunk(-(r - 1), 1)

    if (a, b) == last and last != (0, 0):
        for rr in range(1, r + 1):
            if rr % 2 == 0:
                tots += rr * a
            else:
                tots += rr * b
        break
    else:
        tots += a * r + b * (r - 1)
        last = (a, b)
    
last = (-1, -1)
for r in range(radius, 0, -2):
    a = get_chunk(-r, -1)
    b = get_chunk(-(r - 1), -1)

    if (a, b) == last and last != (0, 0):
        for rr in range(1, r + 1):
            if rr % 2 == 0:
                tots += rr * a
            else:
                tots += rr * b
        break
    else:
        tots += a * r + b * (r - 1)
        last = (a, b)


print(tots)

file.close()