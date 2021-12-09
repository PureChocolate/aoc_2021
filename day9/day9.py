from collections import defaultdict
import time
with open("in.txt", "r") as f : data = [a.strip("\n") for a in f.readlines()]
start = time.time()
d = {}
hmap = defaultdict(lambda: 10, d)
r = 0
for a in data:
    c = 0
    for x in a: 
        hmap[(r,c)] = int(x)
        c += 1
    r += 1
print("parser: " + str((time.time() - start)* 1000))


def basin(r,c,hmap,visited):
    tot = 0
    if hmap[(r,c)] < 9 and visited[(r,c)] == 0:
        visited[(r,c)] = 1
        tot += 1 + basin(r-1,c,hmap,visited) + basin(r+1,c,hmap,visited) + basin(r,c-1,hmap,visited) + basin(r,c+1,hmap,visited)
    return tot

start = time.time()
lowP =[]
visited = defaultdict(lambda: 0)
size = []

for r in range(len(data)):
    for c in range(len(data[r])):
        b = basin(r,c,hmap,visited)
        if b > 0: size.append(b)
        if hmap[(r,c)] < hmap[(r,c-1)] and hmap[(r,c)] < hmap[(r-1,c)] and hmap[(r,c)] < hmap[(r+1,c)] and hmap[(r,c)] < hmap[(r,c+1)]: lowP.append(hmap[(r,c)]+1)

size.sort()

print(size[-1] * size[-2] * size[-3])
print(sum(lowP))
print("p1/p2: " + str((time.time() - start)* 1000))