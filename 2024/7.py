from collections import defaultdict, deque
from functools import cache
import functools
import math

file = open("in", "r")

total = 0

def concat(a, b):
    return int(str(a) + str(b))

def poss(k, nums):
    if(len(nums) == 1): return nums[0] == k
    if poss(k - nums[-1], nums[0:-1]):
        return True
    if(k % nums[-1] == 0 and poss(k // nums[-1], nums[0:-1])):
        return True
    if(len(nums) > 1):
        # print(k, nums[-1], nums)
        if str(k).endswith(str(nums[-1])):
            # print(k, nums[-1], "hi")
            kk = len(str(nums[-1]))
            if(kk != len(str(k))):
                newk = int(str(k)[:-kk])
                if poss(newk, nums[0:-1]):
                    return True
        # n = concat(nums[-2], nums[-1])
        # nums2 = nums[0:-2].copy()
        # nums2.append(n)
        # print(nums, nums2)
        # return poss(k, nums2)
    
    return False

grid = []
def print_grid():
    for row in grid:
        print("".join(row))
        
## read in file input as a grid
for line in file:
    words = line.split()
    k = int(words[0][0:-1])

    nums = [int(c) for c in words[1:]]
    if(poss(k, nums)):
        print(k)
        total += k

    
    
print(total)

file.close()