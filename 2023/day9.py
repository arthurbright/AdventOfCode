from collections import defaultdict
import functools
import math

file = open("in", "r")

total = 0

def allzero(arr):
    for i in arr:
        if i != 0: return False
    return True

total = 0
for line in file:
    words = line.split()
    vals = [int(word) for word in words]
    diffs = [vals]


    while not allzero(diffs[len(diffs) - 1]):
        last = diffs[len(diffs) - 1]
        next = []
        for i in range(1, len(last)):
            next.append(last[i] - last[i - 1])
        diffs.append(next)
    
    diffs.reverse()
    acc = 0
    for arr in diffs:
        acc = arr[0] - acc
    print(acc)
    total += acc

    
    
print(total)

file.close()