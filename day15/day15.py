from collections import defaultdict
from os import system
import heapq as heap, sys
with open("in2.txt","r") as f: s = [a.strip("\n") for a in f.readlines()]
data = []
for a in s:
    temp = []
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    for x in a:
        temp.append(int(x))
    # for x in temp:
    #     u = x + 1 if x < 9 else 1
    #     temp1.append(u)
    # for x in temp1: temp.append(x)
    # for x in temp1:
    #     u = x + 1 if x < 9 else 1
    #     temp2.append(u)
    # for x in temp2: temp.append(x)
    # for x in temp2:
    #     u = x + 1 if x < 9 else 1
    #     temp3.append(u)
    # for x in temp3: temp.append(x)
    # for x in temp3:
    #     u = x + 1 if x < 9 else 1
    #     temp4.append(u)
    # for x in temp4: temp.append(x)
    data.append(temp)
datax = data.copy()
# for r in range(len(data)):
#     for c in range(len(data[r])):

# print(data)


def travel(r,c,data):
    parentsMap = {}
    visi = set()
    pq = []
    weight = defaultdict(lambda: float('inf'))
    weight[(r,c)] = 0
    heap.heappush(pq, (0,(r,c)))
    while pq:
        _, point = heap.heappop(pq)
        visi.add(point)
        u = [[0,-1],[0,1],[-1,0],[1,0]]
        for x in u:
            rr = point[0] + x[0]
            cc = point[1] + x[1]    
            if 0 <= rr < len(data) and 0 <= cc < len(data[rr]):                
                if (rr,cc) in visi: continue
                nCost = weight[point] + data[rr][cc]
                if weight[(rr,cc)] > nCost:
                    parentsMap[(rr,cc)] = (r,c)
                    weight[(rr,cc)] = nCost
                    heap.heappush(pq,(nCost, (rr,cc)))

    print(weight[(len(data)-1, len(data[0])-1)])


travel(0,0,data)


# print(data)