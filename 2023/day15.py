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
        
def hash(s):
    acc = 0
    for c in s:
        val = ord(c)
        acc += val
        acc *= 17
        acc = acc % 256
    return acc
## read in file input as a grid

hashmap = [dict() for i in range(256)]

for line in file:
    words = line.split(",")
    for word in words:
        if "-" in word:
            box = word.split("-")[0]
            if box in hashmap[hash(box)]:
                del hashmap[hash(box)][box]
        else:
            box = word.split("=")[0]
            val = int(word.split("=")[1])
            hashmap[hash(box)][box] = val

total = 0
for i in range(256):
    cnt = 0
    for k in hashmap[i]:
        cnt += 1
        total += (i + 1) * cnt * hashmap[i][k]
#print(hash("HASH"))
    
print(hash("qp"))
print(total)

file.close()