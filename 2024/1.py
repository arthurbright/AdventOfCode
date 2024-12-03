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


aa = []
bb = []

dd = defaultdict(int)
## read in file input as a grid
for line in file:
    words = line.split()
    a = int(words[0])
    b = int(words[1])
    dd[b] += 1
    aa.append(a)
    bb.append(b)

aa.sort()
bb.sort()

diff = 0
for a in aa:
    diff += a * dd[a]


    
print(diff)

file.close()