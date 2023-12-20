from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")

total = 0

broads = []
flipflops = defaultdict(list)
conjs = defaultdict(list)
states = {}
sources = defaultdict(dict)

        
## read in file input as a grid
for line in file:
    words = line.split("=")
    word = words[0]

    parts = word.split("->")
    p1 = parts[0].strip()
    p2 = parts[1].strip()

    if p1 == "broadcaster":
        pps = p2.split(",")
        for dest in pps:
            dest2 = dest.strip()
            broads.append(dest2)
    elif p1[0] == "%":
        #flipflop
        name = p1[1:]
        pps = p2.split(",")
        for dest in pps:
            name2 = dest.strip()
            flipflops[name].append(name2)
            states[name] = False
            states[name2] = False
            sources[name2][name] = False
        
    elif p1[0] == "&":
        #conjuction
        name = p1[1:]
        pps = p2.split(",")
        for dest in pps:
            name2 = dest.strip()
            conjs[name].append(name2)
            states[name] = False
            states[name2] = False
            sources[name2][name] = False
        
todo = deque()

PUSHES = 100000
highs = 0
lows = 0

cnt = 0
ks = defaultdict(list)

for push in range(PUSHES):
    lows += 1 # button
    for i in broads:
        todo.append((i, False, "broadcaster"))

    
    #bfs
    while len(todo) > 0:
        state, high, prev = todo.popleft()
        if state == "cs" and high:
            if prev not in ks or len(ks[prev]) <= 2:
                ks[prev].append(push)
                cnt += 1
        if cnt == 12:
            print(ks)
            exit()
        if state == "rx" and not high:
            print(push + 1)
            exit()
        #print(prev, high, state)
        if high:
            highs += 1
        else:
            lows += 1

        if state in flipflops.keys():
            if high:
                # do nothing
                pass
            else:
                states[state] = not states[state]
                for dest in flipflops[state]:
                    todo.append((dest, states[state], state))
        elif state in conjs:
            sources[state][prev] = high
            alltrue = all([v for v in sources[state].values()])
            
            if alltrue:
                for dest in conjs[state]:
                    todo.append((dest, False, state))
            else:
                for dest in conjs[state]:
                    todo.append((dest, True, state))


print(ks)
file.close()