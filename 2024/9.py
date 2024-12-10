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

def comp(line):
    line = [int(c) for c in line]
    arr = []
    man = []
    ll = len(line)
    used = 0
    for i in range(ll):
        if i % 2 == 0:
            for j in range(line[i]):
                arr.append(i//2)
                man.append(i//2)
                used += 1
        else:
            for j in range(line[i]):
                man.append(-1)
    tot = 0
    ind = 0
    print(man)
    for c in man:
        if c >= 0:
            tot += c * ind
        else:
            if len(arr) > 0:
                tot += arr[-1] * ind
                arr.pop()
        ind += 1
        used -= 1
        if(used == 0): break
    return tot

def comp2(line):
    line = [int(c) for c in line]
    blocks = []
    spaces = []
    spaceb = []
    ll = len(line)
    used = 0
    for i in range(ll):
        if i % 2 == 0:
            blocks.append((i//2, line[i])) #id, count
        else:
            spaces.append(line[i])
            spaceb.append([])
    tot = 0
    ind = 0
    not_blocks = []
    ka = len(blocks) - 1
    for id, size in reversed(blocks):
        # look at previous spaces
        for i in range(ka):
            s = spaces[i]
            if s >= size:
                # print("reducing", i, size, s, id)
                spaces[i] = s - size
                spaceb[i].append((id, size))
                # print(id, size)
                not_blocks.append(id)
                break
        ka -= 1
        # ss = ""
        # for i in range(ll//2):
            
        #     id, size = blocks[i]
        #     ss += str(id) * size
                
        #     for id, size in spaceb[i]:
        #         ss += str(id) * size
        #     ss += "." * spaces[i]
        # print(ss)
    
    # newblocks.reverse()
    # blocks = newblocks
    # print(spaces)
    ss = ""
    for i in range(len(blocks)):
        
        id, size = blocks[i]
        if id in not_blocks:
            ss += "." * size
        else:
            ss += str(id) * size
            
        if i < len(spaceb):
            for id, size in spaceb[i]:
                ss += str(id) * size
            ss += "." * spaces[i]
    print(ss)
    ind = 0
    for i in range(len(blocks)):
        id, size = blocks[i]
        # print(blocks[i])
        if id in not_blocks:
            ind += size
        else:
            for k in range(size):
                tot += ind * id
                ind += 1
            
        if i < len(spaceb):
            for id, size in spaceb[i]:
                # print((id, size))
                for k in range(size):
                    tot += ind * id
                    ind += 1
        if i < len(spaceb):
            ind += spaces[i]

    return tot




## read in file input as a grid
for line in file:
    words = line.split()
    print(comp2(words[0]))
    

file.close()