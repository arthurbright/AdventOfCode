from collections import defaultdict, deque
import itertools
import functools
import math


file = open("in", "r")

total = 0

lines = iter(file)
while(line := next(lines, None)):

    words = iter(line.split())

    while(word := next(words, None)):
        print(word)

    #add back to the iterator
    #words = itertools.chain(["hi"], words)

# add back to the iterator
#lines = itertools.chain(["hi there"], lines)




file.close()