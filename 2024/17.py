from collections import defaultdict, deque
from functools import cache
import functools
import math
file = open("in", "r")
total = 0
grid = []

def print_grid():
    for row in grid:
        print("".join(row))
        
########### read in file input as a grid
A = 0
B = 0
C = 0

def combo(i):
    global A
    global B
    global C
    if i <= 3: return i
    elif i == 4: return A
    elif i == 5: return B
    elif i == 6: return C
    elif i == 7: raise ValueError("im fat")

reg = -1
inps = ""
for line in file:
    reg += 1
    words = line.split()
    if reg == 0:
        A = int(words[-1])
    elif reg == 1:
        B = int(words[-1])
    elif reg == 2:
        C = int(words[-1])
    elif reg == 3:
        continue
    else:
        inps = line
        goal = [2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0]
        goal2 = []
        for i in goal:
            goal2.append(i ^ 3)
        # print(goal2)
        start = 0
        # 4 = 325
        # 1 = 33333...132
        # 2 = 651
        # 3 = 530
        digs = [0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for ii in range(len(digs)):
            v = digs[ii]
            start += v * 8**ii
        t = 1
        diggy = 15
        stay = 0
        output = [0 for i in range(len(goal))]
        while output != goal:
            # print(diggy)
            if diggy < 0:
                print(digs)
                break
            if digs[diggy] == 8:
                digs[diggy] = 0
                diggy += 1
                digs[diggy] = digs[diggy] + 1
                stay = 0
                continue
            elif output[diggy] == goal[diggy]:
                diggy -= 1
                stay = 0
                continue
            else:
                digs[diggy] = (digs[diggy] + 1)
                stay += 1

            start = 0
            for ii in range(len(digs)):
                start += digs[ii] * (8 ** ii)
            for AA in range(start, start + 1):
                A = AA
                output = []
                outs = ""
                nums = line.split(",")
                nums = [int(c) for c in nums]
                IP = 0
                while IP < len(nums):
                    if nums[IP] == 0:
                        A = math.trunc(A / (2 ** combo(nums[IP + 1])))
                        IP += 2
                    elif nums[IP] == 1:
                        B = B ^ nums[IP + 1]
                        IP += 2
                    elif nums[IP] == 2:
                        B = combo(nums[IP + 1]) % 8
                        IP += 2
                    elif nums[IP] == 3:
                        if A == 0:
                            IP += 2
                            pass
                        else:
                            IP = nums[IP + 1]
                    elif nums[IP] == 4:
                        B = B ^ C
                        IP += 2
                    elif nums[IP] == 5:
                        output.append(combo(nums[IP + 1]) % 8)
                        outs += str(output[-1]) + ","
                        IP += 2
                    elif nums[IP] == 6:
                        B = math.trunc(A / (2 ** combo(nums[IP + 1])))
                        IP += 2
                    elif nums[IP] == 7:
                        C = math.trunc(A / (2 ** combo(nums[IP + 1])))
                        IP += 2
                print(digs, outs)
                # if inps == outs[0:-1]:
                #     print(start)
# print(start)
print(start)
outs = outs[:-1]
print(len(output))
file.close()