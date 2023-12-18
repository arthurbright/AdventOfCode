from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")

total = 0

inn = []
        
m = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U"
}
## read in file input as a grid
for line in file:
    words = line.split()
    dir = words[0]
    dist = int(words[1])
    color = words[2]

    dist2 = color[2:-2]
    realdist = int(dist2, 16)
    realdir = m[color[-2]]
    inn.append((realdir, realdist, color))
    #inn.append((dir, dist, color))

minr = 999999999999999999999999999999
minc = 9999999999999999999999999999999
maxr = -9999999999999999999999999999999
maxc = -9999999999999999999999999999999

wall = set()
curr = 0
curc = 0

def updateOpts():
    global minr
    global minc
    global maxr
    global maxc
    minr = min(minr, curr)
    minc = min(minc, curc)
    maxr = max(maxr, curr)
    maxc = max(maxc, curc)

walls = []
downs = set()
importants = []
for dir, dist, color in inn:
    oldr, oldc = curr, curc
    if dir == "R":
        # for i in range(0, dist + 1):
        #     wall.add((curr, curc + i))
        curc += dist
    elif dir == "D":
        downs.add((oldr, oldc))
        #print((oldr, oldc))
        # for i in range(0, dist + 1):
        #     wall.add((curr + i, curc))
        curr += dist
    elif dir == "U":
        
        # for i in range(0, dist + 1):
        #     wall.add((curr - i, curc))
        curr -= dist
        downs.add((curr, curc))
    elif dir == "L":
        # for i in range(0, dist + 1):
        #     wall.add((curr, curc - i))
        curc -= dist
    if oldc == curc:
        walls.append((min(oldr, curr) + 1, oldc, max(oldr, curr) - 1, curc))
    else:
        walls.append((oldr, oldc, curr, curc))
    importants.append(oldr)
    importants.append(oldr + 1)
    importants.append(oldr - 1)
    importants.append(curr)
    importants.append(curr + 1)
    importants.append(curr - 1)
    updateOpts()
print(maxr, minr, maxc, minc)
importants.sort()

def vertical(w):
    r1, c1, r2, c2 = w
    if c1 == c2: return True
    return False

def get_intersect(r):
    sects = []
    for wall in walls:
        r1, c1, r2, c2 = wall
        if vertical(wall):
            if min(r1, r2) <= r <= max(r1, r2):
                sects.append((c2, "pass"))
        else:
            # hor wall
            #print(wall)
            assert r1 == r2
            if r1 == r:
                sects.append((min(c1, c2), "chunkstart"))
                sects.append((max(c1, c2), "chunkend"))
    return sects


total = 0
nummm = 0
found = set()

stash = 0
prevr = minr - 1
for r in importants:
    total += (r - prevr) * stash
    prevr = r

    nummm += 1
    inside = False
    prev = -1
    acc = 0

    lll = sorted(get_intersect(r))
    #print(lll)
    intersections = iter(lll)
    

    while intss := next(intersections, None):
        c, t = intss
        if t == "pass":
            inside = not inside
            if inside:
                prev = c
            else:
                acc += c - prev + 1
        elif t == "chunkstart":
            int2 = next(intersections)
            c2, t2 = int2
            #print(t2)
            assert t2 == "chunkend"
            if ((r, c) in downs) == ((r, c2) in downs):
                if inside:
                    pass
                else:
                    acc += c2 - c + 1
            else:
                if inside:
                    acc += c2 - prev + 1
                else:
                    prev = c
                inside = not inside
    stash = acc
    #print(acc)
    # if acc not in found:
    #     found.add(acc)
        
    #     print(acc, lll)
print(total)
    
            
            

    
        

exit()
def out(r, c):
    if r < minr - 1 or c < minc - 1 or r > maxr + 1 or c > maxc + 1:
        return True
    return False

todo = deque()
visited = set()

for r in range(minr, maxr + 1):
    todo.append((r, minc - 1))
    todo.append((r, maxc + 1))
    visited.add((r, minc - 1))
    visited.add((r, maxc + 1))
for c in range(minc, maxc + 1):
    todo.append((minr - 1, c))
    todo.append((maxr + 1, c))
    visited.add((minr - 1, c))
    visited.add((maxr + 1, c))

def getNext(r, c):
    return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

total = 0
while len(todo) > 0:
    cur = todo.popleft()
    total += 1

    for next in getNext(*cur):
        # if next == (3, 0):
        #     print("HIIII")
        if next not in visited and not out(*next) and next not in wall:
            visited.add(next)
            todo.append(next)
print(total)


print((maxr - minr + 3) * (maxc - minc + 3) - total)

# for r in range(minr - 1, maxr + 2):
#     s = ""
#     for c in range(minc - 1, maxc - 202):
#         if (r, c) in visited:
#             s += "O"
#         elif (r, c) in wall:
#             s += "#"
#         else:
#             s += "."
#     print(s)

file.close()