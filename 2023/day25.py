from collections import defaultdict, deque
from functools import cache
import functools
import math
import random

file = open("in", "r")

total = 0

graph = defaultdict(list)
        
## read in file input as a grid
for line in file:
    words = line.split()
    src = words[0][0:-1]
    print(src)

    for i in range(1, len(words)):
        dest = words[i]
        graph[src].append(dest)
        graph[dest].append(src)

# 3321 edges

# todo = deque()
# visited = set()

START = "mmh"
# START = "jqt"
# todo.append(START)
# visited.add(START)

# prevs = {}
# while len(todo) > 0:
#     cur = todo.popleft()
#     for next in graph[cur]:
#         if next not in visited:
#             visited.add(next)
#             todo.append(next)
#             prevs[next] = cur

END = "jlb"

edges = defaultdict(int)
def addedge(a, b):
    if a < b:
        edges[(a, b)] += 1
    else:
        edges[(b, a)] += 1

nodes = [k for k in graph.keys()]
for i in range(1000):
    a = random.randint(0, len(nodes) - 1)
    b = a
    while b == a:
        b = random.randint(0, len(nodes) - 1)
    
    start = nodes[a]
    end = nodes[b]
    #find shortest path

    todo = deque()
    visited = set()
    prevs = {}

    todo.append(start)
    visited.add(start)

    while len(todo) > 0:
        cur = todo.popleft()
        if cur == end:
            break
        for next in graph[cur]:
            if next not in visited:
                visited.add(next)
                todo.append(next)
                prevs[next] = cur
    
    # back trace
    cc = end
    while cc != start:
        p = prevs[cc]
        addedge(cc, p)
        cc = p

#print(edges)
arr = [(edges[k], k) for k in edges.keys()]
arr.sort()
print(arr)

forb = [('rcn', 'xkf'), ('dht', 'xmv'), ('cms', 'thk')]
todo = deque()
visited = set()
todo.append(start)
visited.add(start)
found = 0
while len(todo) > 0:
    cur = todo.popleft()
    found += 1
    for next in graph[cur]:
        if (next, cur) in forb or (cur, next) in forb:
            continue
        if next not in visited:
            visited.add(next)
            todo.append(next)

print(f"REACHABLE: {found} out of {len(nodes)}")

print(767 * (1475 - 767))
file.close()