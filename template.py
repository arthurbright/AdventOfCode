from collections import defaultdict, deque
import functools
import math

file = open("in", "r")

total = 0

for line in file:
    words = line.split()
    print(words)
    
    
print(total)

file.close()