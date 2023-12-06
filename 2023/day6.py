from collections import defaultdict
file = open("in", "r")

total = 0
first = True
times = []
records = []
for line in file:
    words = line.split()[1:]
    if first:
        first = False
        times = [int(i) for i in words]
    else:
        records = [int(i) for i in words]

total = 1
for i in range(len(times)):
    time = times[i]
    record = records[i]
    cnt = 0
    for hold in range(0, time):
        if (time - hold) * hold > record:
            cnt += 1
    total *= cnt
    
    
    
print(total)

file.close()