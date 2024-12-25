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
        
defs = {}

def calc(u):
    if type(defs[u]) == list:
        v1, op, v2 = defs[u]
        a1 = calc(v1)
        a2 = calc(v2)
        ans = 0
        if op == "XOR":
            ans = a1 ^ a2
        elif op == "OR":
            ans = a1 | a2
        else:
            ans = a1 & a2
        # defs[u] = ans
        return ans
    else:
        return defs[u]

############################ read in file input as a grid
mode = 0
vars = set()
xors = {}
ands = {}
lookup = {}
for line in file:
    line = line.strip()
    if len(line) == 0:
        mode = 1
        continue
    elif mode == 0:
        words = line.split()
        v = words[0][:-1]
        num = int(words[1])
        defs[v] = num
        vars.add(v)
    else:
        words = line.split()
        v1 = words[0]
        op = words[1]
        v2 = words[2]
        res = words[4]
        vars.add(v1)
        vars.add(v2)
        vars.add(res)
        defs[res] = [v1, op, v2]
        lookup[(v1, op, v2)] = res
        lookup[(v2, op, v1)] = res
        if v1[0] == "y":
            v1, v2 = v2, v1
        if v1[0] == "x" and v2[0] == "y":
            n1 = int(v1[1:])
            n2 = int(v2[1:])
            assert (n1 == n2)
            if op == "XOR":
                xors[n1] = res
            elif op == "AND":
                ands[n1] = res
            else:
                print("EXCEPTION FOUND")



rems = {}
rems[0] = "qvn"
for n in range(1, 44):
    xor = xors[n]
    andd = ands[n]
    rem = rems[n - 1]
    temp1 = "ooga"
    if (xor, "AND", rem) in lookup:
        temp1 = lookup[(xor, "AND", rem)]
    elif  (rem, "AND", xor) in lookup:
        temp1 = lookup[(rem, "AND", xor)]
    else: 
        print("COULD NOT FIND THE AND:", n, xor, rem)

    if (temp1, "OR", andd) in lookup:
        rems[n] = lookup[(temp1, "OR", andd)]
    elif (andd, "OR", temp1) in lookup:
        rems[n] = lookup[(andd, "OR", temp1)]
    else:
        print("COULD NOT FIND THE OR", n, temp1, andd)

    print("XOR", xor, "AND", andd, "rem", rems[n], "temp1", temp1)
    # z[n] = xor XOR rem
    # rem AND xor => temp1
    # temp1 or ands => rem[n]

for exp in range(45):
    x = [0 for i in range(45)]
    y = [0 for i in range(45)]
    x[exp] = 1

    for i in range(45):
        ooga = str(i)
        if len(str(i)) == 1:
            ooga = "0" + ooga
        namex = "x" + ooga
        defs[namex] = x[i]
        namey = "y" + ooga
        defs[namey] = y[i]


    ans = [0 for i in range(100)]
    # for u in vars:
    #     if type(defs[u]) == list:
    #         defs[u] = calc(u)

    for u in vars:
        if u[0] == "z":
            ind = int(u[1:])
            ans[ind] = calc(u)

    mult = 1
    # print(ans[0:10])
    total = 0
    for k in ans:
        total += mult * k
        mult *= 2
    # print(total)
    if total != 2**exp:
        print("wrong", exp, 2**exp, total)
file.close()

# z08 / vvr,  rnq/bkr, z28/tfb, z39/mqh
arr = ["z08", "vvr", "rnq", "bkr", "z28", "tfb", "z39", "mqh"]
arr.sort()
print(",".join(arr))
