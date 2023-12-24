from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")

total = 0

bricks = []
## read in file input as a grid
for line in file:
    words = line.split("~")
    e1 = words[0].strip()
    e2 = words[1].strip()
    
    a1 = [int(k) for k in e1.split(",")]
    a2 = [int(k) for k in e2.split(",")]

    if a1[2] > a2[2]:
        bricks.append((a2, a1))
    else:
        bricks.append((a1, a2))

def cmp(b1, b2):
    return b1[0][2] - b2[0][2]

bricks.sort(key=functools.cmp_to_key(cmp))

def collide(i, j):
    b1 = bricks[i]
    b2 = bricks[j]
    
    # same plane
    planes = [0, 1, 2]
    others = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    for d in planes:
        if b1[0][d] == b2[0][d]:
            good = True
            for d2 in others[d]:
                if min(b1[0][d2], b1[1][d2]) > max(b2[0][d2], b2[1][d2]):
                    good = False
                if min(b2[0][d2], b2[1][d2]) > max(b1[0][d2], b1[1][d2]):
                    good = False
            if good:
                return True
    return False

#if brick i collides with any below it
def collides(i):
    return [j for j in range(i) if collide(i, j)]
    
def fall(brick, k):
    return ([brick[0][0], brick[0][1], brick[0][2] + k], [brick[1][0], brick[1][1], brick[1][2] + k])

def above_ground(brick):
    if min(brick[0][2], brick[1][2]) > 0: return True
    return False

supportedby = defaultdict(list)
supports = defaultdict(list)

for i in range(len(bricks)):
    print(f"Progress: {i}")
    # fall a brick, and see what it rests on
    while(True):
        bricks[i] = fall(bricks[i], -1)
        if not above_ground(bricks[i]):
            bricks[i] = fall(bricks[i], 1)
            #print(f"Brick {i} hit the ground at {bricks[i]}")
            break
        col = collides(i)
        if len(col) > 0:
            if i == 1:
                #print(f"HERE: {bricks}, {col}")
                pass
            for dep in col:
                supportedby[i].append(dep)
                supports[dep].append(i)
            bricks[i] = fall(bricks[i], 1)
            #print(f"Brick {i} hit bricks {col} and sits at {bricks[i]}")
            break



total = 0
for i in range(len(bricks)):
    acc = -1
    todo = deque()
    fallen = set()
    todo.append(i)
    fallen.add(i)

    scount = {k:len(supportedby[k]) for k in supportedby}

    while len(todo) > 0:
        cur = todo.popleft()
        acc += 1

        for top in supports[cur]:
            if top in fallen:
                continue
            scount[top] -= 1
            #print(f"{cur}, {top}, {scount[top]}")
            if scount[top] == 0:
                fallen.add(top)
                todo.append(top)
            
    print(f"{acc}: {fallen}")
    #print(scount)
    total += acc

print(total)


file.close()