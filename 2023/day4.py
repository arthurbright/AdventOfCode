from collections import defaultdict
with open("in", "r") as file:
    total = 0
    
    counts = [1 for i in range(220)]
    lnum = 0
    for line in file:
        words = line.split()[2:]
        win = []
        mine = []
        past = False
        for word in words:
            if word == "|":
                past = True
                continue

            val = int(word)
            if past:
                mine.append(val)
            else:
                win.append(val)
        
        num = 0
        for i in mine:
            if i in win:
                num += 1

        for i in range(lnum + 1, min(lnum + 1 + num, 219)):
            counts[i] += counts[lnum]
        total += num
        lnum += 1


    total = 0
    for i in range(220):
        total += counts[i]
    print(total)