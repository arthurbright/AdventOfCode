from collections import defaultdict, deque
import functools
import math

file = open("in", "r")

total = 0

s = []
arr = []
def check(st, arr):
    s = "".join(st)
    a = [len(k) for k in s.split(".") if len(k) != 0]
    return a == arr

# print(check(['#', '.', '#', '.', '#', '#', '#'], [1, 1, 3]))

# def getNum(s, arr):
#     todo = deque()
#     todo.append(s)
#     tot = 0
#     while(len(todo) > 0):
#         cur = todo.popleft()
#         #print(todo)
#         try:
#             ind = cur.index("?")
#             curc = [c for c in cur]
#             curc2 = [c for c in cur]
#             curc[ind] = "."
#             todo.append(curc)
#             curc2[ind] = "#"
#             todo.append(curc2)
#             #print(todo)
#         except Exception:
#             # if cur == ['#', '.', '#', '.', '#', '#', '#']:
#             #     print("HI")
#             #     print(arr)
#             #     print(check(cur, arr))
#             if check(cur, arr):
#                 # print("".join(cur))
#                 # print("GOT")
#                 tot += 1
#             continue
    
#     return tot

numleft = []

def getNum2():
    todo = deque()
    todo.append((0, 0, False, 0))
    tt = 0
    its = 0
    cache = dict()
    while len(todo) > 0:
        si, arri, cont, offset = todo.popleft()
        pp = (si, arri, cont, offset)
        if pp in cache:
            tt += cache[pp]
            continue
        cache[pp]
        
        its += 1
        if (its % 10000000 < 10): print(len(todo))
        if len(s) == si or len(arr) == arri:
            if len(s) == si and len(arr) > arri:
                continue
            if len(s) ==  si and len(arr) == arri:
                tt += 1
                continue
            tt +=  all(c == "." or c == "?" for c in s[si:])
            continue

        if numleft[si] < sum(arr[arri:]) + offset:
            continue
        
        if s[si] == ".":
            if cont:
                if arr[arri] + offset == 0:
                    todo.append((si + 1, arri + 1, False, 0))
                    continue
                else:
                    continue
            else:
                todo.append((si + 1, arri, False, 0))
                continue
        if s[si] == "#":
            if arr[arri] + offset == 0: continue
            todo.append((si + 1, arri, True, offset - 1))
            continue
        
        if s[si] == "?":
            if cont:
                if arr[arri] + offset == 0:
                    todo.append((si + 1, arri + 1, False, 0))
                    continue # use dot
                todo.append((si + 1, arri, True, offset - 1)) # use hashtag
                continue
            else:
                todo.append((si + 1, arri, False, offset))

                todo.append((si + 1, arri, True, offset - 1))
    return tt
                
            


    

## read in file input as a grid
i = 0
for line in file:
    words = line.split()
    wwwww = words[0] + "?" + words[0] + "?" + words[0] + "?" + words[0] + "?" + words[0] + "."
    #print(wwwww)
    s = [c for c in wwwww]
    #s = [c for c in words[0]] + ["."]


    arr = [int(c) for c in words[1].split(",")] * 5
    #arr = [int(c) for c in words[1].split(",")]
    #print(nums)


    #make numleft
    numleft = [0]
    for c in reversed(wwwww):
        if c == "#" or c == "?":
            numleft.append(numleft[len(numleft) - 1] + 1)
        else:
            numleft.append(numleft[len(numleft) - 1])
    numleft.reverse()
    #print(numleft)

    a= getNum2()
    total += a
    i += 1
    print(f"{i}: {a}")

    
    
print(total)

arr = [c for c in "???.###???."]
arr2 = [int(c) for c in "1,1,3,1,1".split(",")]
# print(getNum2(["?", "?", "?", ".", "#", "#", "."], [1, 1, 2], False))
# print(getNum2(arr, arr2, False))

file.close()