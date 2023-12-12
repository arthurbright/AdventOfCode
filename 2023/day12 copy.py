from collections import defaultdict, deque
import functools
from functools import cache
import math

file = open("in", "r")

total = 0

s = []
arr = []
def check(st, arr):
    s = "".join(st)
    a = [len(k) for k in s.split(".") if len(k) != 0]
    return a == arr

numleft = []

@cache
def getNum2(si, arri, cont, offset = 0):
    if len(s) == si or len(arr) == arri:
        if len(s) == si and len(arr) > arri:
            return 0
        if len(s) ==  si and len(arr) == arri:
            return 1
        return all(c == "." or c == "?" for c in s[si:])

    if numleft[si] < sum(arr[arri:]) + offset:
        return 0
    
    if s[si] == ".":
        if cont:
            if arr[arri] + offset == 0:
                return getNum2(si + 1, arri + 1, False)
            else:
                return 0
        else:
            return getNum2(si + 1, arri, False)
    if s[si] == "#":
        if arr[arri] + offset == 0: return 0
        # arr[arri] -= 1
        k = getNum2(si + 1, arri, True, offset - 1)
        # arr[arri] += 1
        return k
    
    if s[si] == "?":
        if cont:
            if arr[arri] + offset == 0:
                return getNum2(si + 1, arri + 1, False)
            #arr[arri] -= 1
            k =  getNum2(si + 1, arri, True, offset - 1) # use hashtag
            #arr[arri] += 1
            return k
        else:
            k = getNum2(si + 1, arri, False, offset)

            #arr[arri] -= 1
            k += getNum2(si + 1, arri, True, offset - 1)
            #arr[arri] += 1
            return k
                
            


    

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

    getNum2.cache_clear()
    a= getNum2(0, 0, False)

    total += a
    i += 1
    print(f"{i}: {a}")

    
    
print(total)

file.close()