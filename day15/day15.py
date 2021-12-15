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
    for x in temp:
        u = x + 1 if x + 1 < 10 else 11 - x
        temp1.append(u)
    for x in temp1: temp.append(x)
    for x in temp1:
        u = x + 1 if x + 1 < 10 else 11 - x
        temp2.append(u)
    for x in temp2: temp.append(x)
    for x in temp2:
        u = x + 1 if x + 1 < 10 else 11 - x
        temp3.append(u)
    for x in temp3: temp.append(x)
    for x in temp3:
        u = x + 1 if x + 1 < 10 else 11 - x
        temp4.append(u)
    for x in temp4: temp.append(x)
    data.append(temp)
datax = data.copy()
for a in range(1,5):
    for r in range(len(data)):
        temp = []
        for c in range(len(data[r])):
            u = data[r][c] + a if data[r][c] + a < 10  else 11 - data[r][c]
            temp.append(u)
        datax.append(temp)

# for a in datax:
#     print(a)
print(datax[-1])

def travel(r,c,data):
    parents = {}
    visi = set()
    pq = []
    weight = defaultdict(lambda: float('inf'))
    weight[(r,c)] = 0
    heap.heappush(pq, (0,(r,c)))
    while pq:
        _, point = heap.heappop(pq)
        visi.add(point)
        #check valid pos
        u = [[0,-1],[0,1],[-1,0],[1,0]]
        for x in u:
            rr = point[0] + x[0]
            cc = point[1] + x[1]    
            if 0 <= rr < len(data) and 0 <= cc < len(data[rr]):                
                if (rr,cc) in visi: continue #if visited skip
                nCost = weight[point] + data[rr][cc] #get the cost to get to the next point from current
                if nCost < weight[(rr,cc)]:
                    parents[(rr,cc)] = point
                    weight[(rr,cc)] = nCost  #if less update the cost of the point to get there from origin
                    heap.heappush(pq,(nCost, (rr,cc))) # push 

    print(weight[(len(datax)-1, len(datax[0])-1)])
    x = 49
    y = 49
    while(x > 0 and y > 0):
        u = parents[(y,x)]
        print(u, datax[u[0]][u[1]])
        x = u[1]
        y = u[0]
    print(parents[(49,49)])    
    print(parents[(49,48)])
    print(parents[(49,47)])
    print(parents[(49,46)])
    print(parents[(49,45)])
    vals = list(weight.values())
    tot = []
    print(len(datax)-1,len(datax[0])-1)
    for k,v in weight.items():
        if v < float('inf'): 
            if v == 315: 
                print(k, v)
                # tot.append(v)
            # tot.append(v)
    # tot.sort()
    print(tot)

travel(0,0,datax)


# print(data)