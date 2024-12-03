from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")

total = 0
enabled = True

def proc(line):
    global enabled
    cnt = 0
    s = len(line)
    for i in range(len(line) - 7):
        if(line[i:i + 4] == "mul(" and enabled):
            com = line.find(",", i)
            close = line.find(")", i)
            if com == -1: continue
            if close == -1: continue
            if com > close: continue

            try:
                a = int(line[i + 4:com])
                b = int(line[com + 1:close])
            except:
                continue
                
            cnt += a * b
        if(line[i:i + 4] == "do()"):
            enabled = True
        if(line[i:i + 7] == "don't()"):
            enabled = False
    return cnt

grid = []
def print_grid():
    for row in grid:
        print("".join(row))
        
## read in file input as a grid
for line in file:
    words = line.split()
    total += proc(line)

    
    
print(total)

file.close()