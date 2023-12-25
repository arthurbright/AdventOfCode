line = input().split()
n = int(line[0])
k = int(line[1])
d = int(line[2])


digs = []
ncopy = n
# parse n into digits of base k
while ncopy > 0:
    digs.append(ncopy % k)
    ncopy = ncopy//k


if len(digs) <= d + 1:
    # easy case, just infect one digit per day
    print(sum(digs))
else:
    # do one digit per day until the last day; cram the rest in
    ans = 0
    for i in range(d):
        ans += digs[i]
    for i in range(d, len(digs)):
        ans += digs[i] * int(k**(i - d))
    print(ans)