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

pos1 = {}
pos1["7"] = (0, 0)
pos1["8"] = (0, 1)
pos1["9"] = (0, 2)
pos1["4"] = (1, 0)
pos1["5"] = (1, 1)
pos1["6"] = (1, 2)
pos1["1"] = (2, 0)
pos1["2"] = (2, 1)
pos1["3"] = (2, 2)
pos1["0"] = (3, 1)
pos1["A"] = (3, 2)
pos1[" "] = (3, 0)

pos2 = {}
pos2["^"] = (0, 1)
pos2["A"] = (0, 2)
pos2["<"] = (1, 0)
pos2["v"] = (1, 1)
pos2[">"] = (1, 2)
pos2[" "] = (0, 0)

def shortests(pos, a, b):
    x1, y1 = pos[a]
    x2, y2 = pos[b]
    
    if x2 >= x1:
        s1 = "v" * (x2 - x1)
    else:
        s1 = "^" * (x1 - x2)
    if y2 >= y1:
        s2 = ">" * (y2 - y1)
    else:
        s2 = "<" * (y1 - y2)

    if (x1, y2) == pos[" "]:
        return [s1 + s2]
    elif (x2, y1) == pos[" "]:
        return [s2 + s1]

    return [s2 + s1, s1 + s2]

@cache
def shorter(a, b, num_left):
    if num_left == 1:
        return len(shortests(pos2, a, b)[0]) + 1
    else:
        cand = shortests(pos2, a, b)
        # print(cand)
        ans = 999999999999999999999999999999
        for c in cand:
            c = "A" + c + "A"
            acc = 0
            for i in range(1, len(c)):
                acc += shorter(c[i - 1], c[i], num_left - 1)
            ans = min(ans, acc)
        return ans

# v<<A
#  >vA
#  <A
#  A
#  >>^A

def proc(row):
    best = [row]
    for dicc in [pos1, pos2]:
        new_best = []
        for path in best:
            temp = [""]
            for i in range(1, len(path)):
                newer_s = []
                nexts = shortests(dicc, path[i - 1], path[i])
                for k in temp:
                    for kk in nexts:
                        newer_s.append(k + kk + "A")
                temp = newer_s
            new_best.extend(temp)
        minl = min([len(s) for s in new_best])
        best = [("A" + k) for k in new_best if len(k) == minl]
        # print(best)

    ans = 999999999999999999999999999999
    for path in best:
        t = ""
        for i in range(1, len(path)):
            nexts = shortests(dicc, path[i - 1], path[i])
            t +=  nexts[0] + "A"
        ans = min(ans, len(t))
    
    # print(ans)
    return ans

def proc2(row):
    best = row
    for dicc in [pos1, pos2, pos2]:
        path = ""
        for i in range(1, len(best)):
            nexts = shortests(dicc, best[i - 1], best[i])
            path +=  nexts[0] + "A"
        best = "A" + path
        print(best)
    print(len(best), best)
    return len(best)
        
def proc3(row):
    path = row
    t = [""]
    for i in range(1, len(path)):
        newt = []
        nexts = shortests(pos1, path[i - 1], path[i])
        for k in t:
            for kk in nexts:
                newt.append(k + kk + "A")
        t = newt
    # print(t)
    
    minn = 9999999999999999999999999999
    for opt in t:
        opt = "A" + opt
        # print(opt)
        acc = 0
        for i in range(1, len(opt)):
            acc += shorter(opt[i - 1], opt[i], 25)
        minn = min(minn, acc)
    
    # print(ans)
    return minn

############################ read in file input as a grid
for line in file:
    words = line.split()
    word = words[0]

    l = proc3("A" + word)
    print(word, l, int(word[:-1]))
    total += l * int(word[:-1])

print(total)
file.close()

# print("================TESTING")
# tester = "A<A^A>^^AvvvA"
# tot = 0
# for i in range(1, len(tester)):
#     k = shorter(tester[i - 1], tester[i], 1)
#     print(k)
#     tot += k
# print(tot)
# A  v<<A   
#  >vA
#  <A
#  A
#  >>^A