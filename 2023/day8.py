from collections import defaultdict
import itertools
import functools
import math
file = open("in", "r")

total = 0

lines = iter(file)

instr = next(lines).split()[0]
print(instr)
ins = instr
temp = next(lines)

graph = {}
cur = []

while(line := next(lines, None)):

    words = line.split()
    a = words[0]
    b = words[1]
    c = words[2]

    if a[2] == 'A':
        cur.append(a)

    graph[a] = (b, c)

total = 0
ind = 0

factors = []

repeats = []
goodinds = [[] for i in cur]
curcopy = [i for i in cur]

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

goodss = []
lcms = [61, 59, 79, 47, 53, 73]
ind = -1
for curr in cur:
    ind += 1
    og = curr
    total = 0
    goods = []
    prevtotal = 0
    while True:
        c = instr[total % len(instr)]
        if og[2] == "Z":
            goods.append((total - prevtotal)//lcms[ind])
            prevtotal = total
        if len(goods) > 40:
            goodss.append(goods)
            break
        

        if c == "L":
            for i in range(len(cur)):
                og = graph[og][0]
        else:
            for i in range(len(cur)):
                og = graph[og][1]

        total += 1

for i in goodss:
    print(i)
# add back to the iterator
#lines = itertools.chain(["hi there"], lines)




file.close()