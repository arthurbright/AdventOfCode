from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")

total = 0

grid = []
def ff(i):
    if i > 9:
        return "9"
    if i == 0:
        return " "
    return str(i)
def print_grid():
    for row in grid:
        print("".join([str(ff(c)) for c in row]))
        
robs = []
###### read in file input as a grid
for line in file:
    words = line.split()
    position = words[0]
    vel = words[1]

    x = int(position.split(",")[0][2:])
    y = int(position.split(",")[1])

    vx = int(vel.split(",")[0][2:])
    vy = int(vel.split(",")[1])

    robs.append((x, y, vx, vy))

rows = 101
cols = 103
q1, q2, q3, q4 = 0, 0, 0, 0

for s in range(1000):
    # secs = 103 * s - 2
    secs = 8179
    entropy = 0
    grid = [[0 for i in range(cols)] for j in range(rows)]
    for x1, y1, vx, vy in robs:
        x = (x1 + secs * vx) % rows
        y = (y1 + secs * vy) % cols
        if x < rows//2 and y < cols//2:
            q1 += 1
        elif x < rows//2 and y > cols//2:
            q2 += 1
        elif x > rows//2 and y > cols//2:
            q3 += 1
        elif x > rows//2 and y < cols//2:
            q4 += 1
        # print(x, y)
        grid[x][y] += 1
        if(grid[x][y] == 2):
            entropy += 1

    # if entropy >= 30:
    if True:
        print(f"SECS == {secs}")
        print_grid()
        print("==============================================")
# 866
# 763

print(q1, q2, q3, q4)
print(q1 * q2 *q3 * q4)
file.close()