from collections import defaultdict, deque
from functools import cache
import functools
import math
import copy

file = open("in", "r")

total = 0

workflows = {}
parts = []

c_to_index = {"x": 0, "m": 1, "a": 2, "s": 3}
swap = False
for line in file:
    words = line.split()

    if len(words) == 0:
        swap = True
        continue
    
    if not swap:
        # read workflows
        wf = []

        workflow = words[0]
        name = workflow.split("{")[0]
        steps = workflow.split("{")[1]
        steps = steps.split("}")[0]
        steps = steps.split(",")
        for step in steps:
            if ":" in step:
                c = step[0]
                sign = step[1]
                rest = step[2:]
                num = int(rest.split(":")[0])
                dest = rest.split(":")[1]
                wf.append((c_to_index[c], sign, num, dest))
            else:
                workflows[name] = (wf, step)
        

    else:
        #read inputs
        inp = words[0][1:-1].split(",")
        k = [int(i[2:]) for i in inp]
        parts.append(k)


# for part in parts:
#     cur = "in"
#     while cur != "R" and cur != "A":
#         steps, final = workflows[cur]
#         exited = False
#         for step in steps:
#             c, sign, val, next = step
#             if (part[c_to_index[c]] < val) ==  (sign == "<"):
#                 cur = next
#                 exited = True
#                 break
#         if not exited:
#             cur = final
#     if cur == "A":
#         # print(part)
#         total += sum(part)

todo = deque()
visited = set()
todo.append(("in", [(1, 4000), (1, 4000), (1, 4000), (1, 4000)]))

def intersect(a, b):
    a1, a2 = a
    b1, b2 = b

    if a1 > b2 or b1 > a2: return None
    return (max(a1, b1), min(a2, b2))

def cpy(t):
    # t2 = (0, 0, 0, 0)
    # for i in range(4):
    #     t2[i] = (t[i][0], t[i][1])
    # return t2
    return t[0:4]

total = 0
while len(todo) > 0:
    name, ivs = todo.popleft()
    if name == "A":
        gaps = [i[1] - i[0] + 1 for i in ivs]
        #print(gaps)
        total += gaps[0] * gaps[1] * gaps[2] * gaps[3]
        continue
    if name == "R":
        continue

    #split inv
    steps, final = workflows[name]
    illegal = False
    for step in steps:
        c, sign, num, next = step
        if sign == "<":
            goal = (1, num - 1)
            opp = (num, 4000)
        else:
            goal = (num + 1, 4000)
            opp = (1, num)
        gg = intersect(ivs[c], goal)
        oo = intersect(ivs[c], opp)

        if gg:
            ivs2 = cpy(ivs)
            ivs2[c] = gg
            todo.append((next, ivs2))
            print(goal)
        if oo:
            ivs2 = cpy(ivs)
            ivs2[c] = oo
            ivs = cpy(ivs2)
        if not oo:
            illegal = True
    if not illegal:
        todo.append((final, ivs))




# for name in workflows:
#     steps, final = workflows[name]
#     adj.add

print(total)



file.close()