from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")

total = 0

stones = []
        
## read in file input as a grid
for line in file:
    word = line.strip()
    pos = word.split('@')[0].split(",")
    vel = word.split('@')[1].split(",")

    realpos = [int(i.strip()) for i in pos]
    realvel = [int(i.strip()) for i in vel]

    stones.append((realpos, realvel))

def ix(a1, b1, c1, a2, b2, c2):
    if a1 * b2 - a2 * b1 == 0:
        if a1 * c2 == a2 * c1:
            #print("PARR", a1, b1, c1, a2, b2, c2)
            return (0, 0)
        return None
    det = a1 * b2 - a2 * b1

    return ((b1 * c2 - b2 * c1)/det, (a2 * c1 - a1 * c2)/det)

def tostandard(x, y, vx, vy):
    return (vy, -vx, -vy * x + vx * y)


LOW = 200000000000000
HIGH = 400000000000000
def intersect(ii, jj, xoff, yoff):
    p1, vv1 = ii
    p2, vv2 = jj

    v1 = [vv1[0] + xoff, vv1[1] + yoff]
    v2 = [vv2[0] + xoff, vv2[1] + yoff]



    a1, b1, c1 = tostandard(p1[0], p1[1], v1[0], v1[1])
    a2, b2, c2 = tostandard(p2[0], p2[1], v2[0], v2[1])

    ixx = ix(a1, b1, c1, a2, b2, c2)
    if ixx is not None:
        if ((v1[0] > 0) == (ixx[0] > p1[0]))  and ((v2[0] > 0) == (ixx[0] > p2[0])):
            if LOW <= ixx[0] <= HIGH and LOW <= ixx[1] <= HIGH:
                return ixx
            return ixx


    return 0

LOWV = -219
HIGHV = -209

LOWV2 = 163
HIGHV2 = 173
ints = 10
# -214 168

# 172543224455736.0, 348373777394510.0 , 148125938782131
print(172543224455736 + 348373777394510 + 148125938782131)

#t = 154588043705
# with thing 176253337504656, 321166281702430, 134367602892386 @ 190, 8, 338
#t = 499903573610
# with thing 230532038994496, 112919194224200, 73640306314241 @ 98, 303, 398

XPOS = 172543224455736
YPOS = 348373777394510
XSOL = -214
YSOL = 168


    


goodx = None
goody = None
maxx = 0
minn = 300 * 300
intersections = set()
# for xoff in range(LOWV, HIGHV, (HIGHV - LOWV)//ints):
#     for yoff in range(LOWV2, HIGHV2, (HIGHV2 - LOWV2)//ints):
for xoff in [XSOL]:
    for yoff in [YSOL]:
        totx = 0
        toty = 0
        cnt = 0
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                ixx = intersect(stones[i], stones[j], xoff, yoff)
                if ixx:
                    intersections.add(ixx)
                    cnt += 1
                    totx += ixx[0]
                    toty += ixx[1]
        if cnt > maxx:
            maxx = cnt
            goodx = xoff
            goody = yoff


print(maxx, goodx, goody)
iii = 0
for k in intersections:
    print(k)
    iii += 1
    if iii == 10:
        break

print(len(intersections))


def dist(c1, c2):
    return ((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2 + (c1[2] - c2[2])**2)**0.5

def normalize(v):
    norm = dist(v, [0, 0, 0])
    return [i/norm for i in v]

def add(a, b, c):
    return [a[i] + b[i] * c for i in range(3)]

def neg(v):
    return [-i for i in v]

def dot(v1, v2):
    return abs(sum([v1[i] * v2[i] for i in range(len(v1))]))

# low = 0
# high = 10000000000
# minn = 999999999999999999999999
# t = -1
# for mid in range(0, 100):
#     p1, v1 = stones[0]
#     p2, v2 = stones[1]
#     p3, v3 = stones[2]

#     p1 = add(p1, v1, mid)
#     p2 = add(p2, v2, mid)
#     p3 = add(p3, v3, mid)

#     d1 = add(p1, p2, -1)
#     d2 = add(p2, p3, -1)
#     score = min(dist(normalize(d1), normalize(d2)), dist(normalize(neg(d1)), normalize(d2)))
#     print()
#     if score < minn:
#         minn = score
#         t = mid


file.close()