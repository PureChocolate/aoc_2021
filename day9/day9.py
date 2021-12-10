from collections import defaultdict
import time
start = time.time()
with open("bigboy2.txt", "r") as f : data = [[*map(int, a.rstrip())] for a in f.readlines()]

print("parser/ map grid to dict: " + str(time.time() - start))

def basin(ps,data):   
    start = time.time()
    visited = defaultdict(lambda: 0) 
    size = []
    for a in ps:
        stack = []
        # print(ps[1][0], ps[1][1])
        stack.append((a[1][0], a[1][1]))
        tot = 0
        while(len(stack) > 0):
            n = stack.pop(-1)
            u = [[0,0],[0,-1],[0,1],[-1,0],[1,0]]
            for x in u:
                r = n[0]+ x[0]
                c = n[1] + x[1]
                if 0 <= r < len(data) and 0 <= c < len(data[n[0]]):
                    if data[r][c] < 9 and visited[(r,c)] == 0:
                        tot += 1
                        visited[(r,c)] = 1
                        stack.append((r,c))
        size.append(tot)
    size.sort()
    print(size[-3] * size[-1] * size[-2])
    print("p2: " + str(time.time() - start))

def run(data):
    start = time.time()
    lowP =[]
    for ra in range(len(data)):
        for cc in range(len(data[ra])):
            c = data[ra][cc]
            l = [[0,-1],[0,1],[-1,0],[1,0]]
            pos = False
            for a in l:
                if 0 <= (ra + a[0]) < len(data) and 0 <= (cc + a[1]) < len(data[ra]):
                    if not c < data[ra+a[0]][cc+a[1]]:
                        pos = False
                        break
                    else: 
                        pos = True
            if pos: lowP.append([c,(ra,cc)])
    print(sum([a[0]+1 for a in lowP]))
    print("p1: " + str(time.time() - start))
    return lowP

basin(run(data),data)