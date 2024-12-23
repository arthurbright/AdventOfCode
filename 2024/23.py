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
        
adj = defaultdict(set)
players = set()
############################ read in file input as a grid
for line in file:
    line = line.strip()
    words = line.split("-")
    a = words[0]
    b = words[1]
    adj[a].add(b)
    adj[b].add(a)
    players.add(a)
    players.add(b)

players = list(players)
# print(players)
ll = len(players)
# print(ll)

# MAX SIZE = 83
# TOTAL PLAYERS = 520
def cliquee(p):
    pass
cliques = []
for i in range(ll):
    # print(i)
    for j in range(i + 1, ll):
        for k in range(j + 1, ll):
            ii = players[i]
            jj = players[j]
            kk = players[k]
            # if ii[0] == "t" or jj[0] == "t" or kk[0] == "t":
            if True:
                if ii in adj[jj] and jj in adj[kk] and kk in adj[ii]:
                    # total += 1
                    cliques.append([i, j, k])

while True:
    new_cliques = []
    for clique in cliques:
        k = max(clique)
        for p in range(k + 1, ll):
            if all([players[p] in adj[players[i]] for i in clique]):
                clique_ = clique.copy()
                clique_.append(p)
                new_cliques.append(clique_)
    if len(new_cliques) == 0:
        print("FINAL", cliques)
        break
    cliques = new_cliques
    print(i)

ans = cliques[0]
print(len(ans))
names = [players[i] for i in ans]
names.sort()
print(",".join(names))
file.close()