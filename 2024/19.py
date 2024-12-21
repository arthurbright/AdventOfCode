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
ll = 0
towels = []

def possible(row):
    global towels
    le = len(row)
    
    poss = [0 for i in range(le)]
    for i in range(le):
        s = row[:i + 1]
        if s in towels:
            poss[i] = 1
            # print(i)
        # print(s, s in towels)
        if True:
            for j in range(1, i + 1):
                # print(row[j:i + 1], row[:i + 1])
                if row[j:i + 1] in towels:
                    # print(row[j:i + 1], row[:i + 1], poss[i], row[:i + 1])
                    poss[i] += poss[j - 1]
    # print(poss)
    return poss[le - 1]   



for line in file:
    words = line.split()
    # word = words[0]

    if ll == 0:
        towels = line.strip().split(", ")
    elif ll >= 2:
        # print(line[:-1])
        line = line.strip()
        print(line, possible(line))
        total += possible(line)
    ll += 1
    
    
print(total)

file.close()