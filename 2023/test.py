from collections import defaultdict
import itertools
import functools
file = open("in2", "r")

total = 0

lines = iter(file)

instr = next(lines).split()[0]
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

for i in cur:
    og = i
    total = 0
    ind = 0
    while True:
        c = instr[ind]
        if c != "R" and c != "L":
            raise 5

        good = True
        for cc in cur:
            if cc[2] != "Z":
                good = False
                break
        if good:
            factors.append(total)
            break

        newcur = []
        for curr in cur:
            if c == "L":
                newcur.append(graph[curr][0])
            else:
                newcur.append(graph[curr][1])
        
        cur = newcur
        ind = (ind + 1) % len(instr)
        total += 1

print(factors)
# add back to the iterator
#lines = itertools.chain(["hi there"], lines)




file.close()