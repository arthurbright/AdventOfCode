from collections import defaultdict
file = open("in", "r")

total = 0

dictt = {}
seeds = []
newseeds = []
found = {}
first = True
for line in file:
    if first:
        first = False
        words = line.split()[1:]
        for i in range(0, len(words), 2):
            seeds.append((int(words[i]), int(words[i]) + int(words[i + 1]) - 1))
    else:
        words = line.split()
        if len(words) == 2 or len(words) == 0:
            #print(seeds, newseeds)
            if newseeds != []:
                for i in seeds:
                    newseeds.append(i)
                seeds = newseeds
                newseeds = []
        else:
            dest = int(words[0])
            src = int(words[1])
            range = int(words[2])

            ##process seeds
            temp = []
            for seed in seeds:
                start, end = seed
                if src <= start < src + range:
                    if src <= end < src + range:
                        newseeds.append((start - src + dest, end - src + dest))
                    else:
                        newseeds.append((start - src + dest, src + range - 1 - src + dest))
                        temp.append((src + range, end))
                else:
                    if src <= end < src + range:
                        temp.append((start, src - 1))
                        newseeds.append((dest, end - src + dest))
                    else:
                        # slice
                        if end >= src + range and start < src:
                            newseeds.append((dest, dest + range - 1))
                            temp.append((start, src - 1))
                            temp.append((src + range, end))
                        else:
                            temp.append((start, end))
            seeds = temp
            
seeds = sorted(seeds)
print(seeds)
print(seeds[0][0])



file.close()