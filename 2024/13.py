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
        
################### read in file input as a grid
iii = 0
xa = 0
xb = 0
ya = 0
yb = 0
dx = 0
dy = 0
for line in file:
    words = line.split()
    if iii % 4 == 3: 
        iii += 1
        continue
    if iii % 4 == 0:
        xa = int(words[2][2:-1])
        ya = int(words[3][2:])
    elif iii % 4 == 1:
        xb = int(words[2][2:-1])
        yb = int(words[3][2:])
    else:
        dx = int(words[1][2:-1])
        dy = int(words[2][2:])
        # print(xa, ya, xb, yb, dx, dy)
        # print(iii)
        minpress = 4000000
        dx += 10000000000000
        dy += 10000000000000

        if xa * yb == xb * ya:
            xa = max(xa, xb)
            ya = max(ya, yb)
            # print(xa, ya, xb, yb, dx, dy)
            if dx % xa == 0 and dy % ya == 0:
                total += 3 * dx//xa + dy//ya
        else:
            print(xa, ya, xb, yb, dx, dy)
            det = xa * yb - xb * ya
            sx = yb * dx - xb * dy
            sy = 0 - ya * dx + xa * dy
            print(det, sx, sy)
            if sx % det == 0 and sy % det == 0 and sx * det >= 0 and sy * det >= 0:
                total += 3 * sx//det + sy//det

        # for i in range(101):
        #     for j in range(101):
        #         # if iii == 2 and i == 80 and j == 40:
        #             # print(xa, ya, xb, yb, dx, dy)
        #             # print(i * xa + j * xb, )
        #         if i * xa + j * xb == dx and i * ya + j * yb == dy:
        #             # print("hi")
        #             minpress = min(minpress, 3 * i + j)
        # if minpress == 4000000:
        #     pass
        # else:
        #     total += minpress

    iii += 1
print(total)
file.close()