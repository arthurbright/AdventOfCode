from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
rows = 0
cols = 0
def in_bounds(r, c):
    global rows
    global cols
    return r >= 0 and c >= 0 and r < rows and c < cols

total = 0
grid = []
def print_grid():
    for row in grid:
        print("".join(row))
        
def mix(n, cur):
    return n ^ cur

def prune(cur):
    return cur % 16777216

score = defaultdict(int)

def proc_one(num):
    num = mix(num, num * 64)
    num = prune(num)
    num = mix(num, (num//32))
    num = prune(num)
    num = mix(num, num * 2048)
    num = prune(num)
    return num

@cache
def proc(num, iter):
    diffs = []
    seen = set()
    for i in range(iter):
        last = num % 10
        num = proc_one(num)
        cur = num % 10

        diffs.append(cur - last)
        if len(diffs) >= 4:
            tup = (diffs[-4], diffs[-3], diffs[-2], diffs[-1])
            if tup not in seen:
                seen.add(tup)
                if tup == (-2, 1, -1, 3):
                    print(num % 10)
                score[tup] += num % 10
    return num
    
############################ read in file input as a grid
for line in file:
    words = line.split()
    word = words[0]
    # print(word)
    num = int(word)
    ans = proc(num, 2000)
    total += ans

maxx = 0
win = (0, 0, 0, 0)
for k in score:
    if score[k] > maxx:
        maxx = score[k]
        win = k
print(maxx, win)
file.close()