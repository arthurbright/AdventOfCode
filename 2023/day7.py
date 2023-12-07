from collections import defaultdict
import functools
file = open("in", "r")


pairs = []
order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

tot = 0
for line in file:
    tot += 1
    words = line.split()
    hand = words[0]
    bid = words[1]

    count = [0 for i in range(13)]
    jokers = hand.count("J")
    for i in range(12):
        count[i] = hand.count(order[i])

    count.sort(reverse=True)
    count[0] += jokers
    
    pairs.append((count, int(bid), hand))
    
mapp = defaultdict(lambda: [])
pairs.sort()
for ppp in pairs:
    count, bid, hand = ppp
    cnt = ""
    for i in count:
        cnt = cnt + chr(i)
    mapp[cnt].append((hand, bid))

total =0
ind = 1

def cpmp(item1, item2):
    for i in range(5):
        if order.index(item1[0][i]) < order.index(item2[0][i]):
            return 1
        elif order.index(item1[0][i]) > order.index(item2[0][i]):
            return -1
    return 0

for k in mapp:
    mapp[k].sort(key=functools.cmp_to_key(cpmp))
    for pp in mapp[k]:
        hand, bid = pp
        print(f"{hand}: {ind}")
        total += ind * bid
        ind += 1

print(total)
    

file.close()