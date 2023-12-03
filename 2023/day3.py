from collections import defaultdict
rows = 140
cols = 140 + 2
grid = [[-2 for i in range(cols)]]
gears = defaultdict(int)
gearr = defaultdict(lambda: 1)
with open("in", "r") as file:

    total = 0
    
    c = 0
    for line in file:
        row = [-2]
        for c in line[:-1]:
            if ord(c) >= ord("0") and ord(c) <= ord("9"):
                row.append(int(c))
            elif c == "*":
                row.append(-1)
            else:
                row.append(-2)
        row.append(-2)
        grid.append(row)
    grid.append([-2 for i in range(cols)])


    for r in range(1, len(grid) - 1):
        acc = 0
        lenn = 0
        for c in range(1, cols):
            if(grid[r][c] >= 0):
                acc = acc * 10 + grid[r][c]
                lenn += 1
            else:
                #scan surroundings
                if lenn == 0: continue
                good = False
                for rr in range(r - 1, r + 2):
                    for cc in range(c - lenn - 1, c + 1):
                        #print("gay")
                        if grid[rr][cc] == -1 and (rr != r or cc == c - lenn - 1 or cc == c):
                            good = True
                            print((rr, cc))
                            gears[(rr, cc)] += 1
                            gearr[(rr, cc)] *= acc

                if good: total += acc
                acc = 0
                lenn = 0

    total = 0
    for gear in gears:
        if(gears[gear] == 2):
            print(gear)
            print(gearr[gear])
            total += gearr[gear]

    print(total)