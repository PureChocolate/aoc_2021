from collections import defaultdict
with open("in.txt","r") as f: data = [a.strip("\n") for a in f.readlines()]
inst = False
datax = []
data2 = []
grid = defaultdict(lambda: '.')
for x in range(len(data)):
    if inst: 
        u = data[x][11:].split("=")
        data2.append((u[0],int(u[1])))     
    else: 
        if data[x] == '': inst = True
        else: datax.append(data[x])
mX = mY = 0
for a in datax:
    u = a.split(",")
    u[0] = int(u[0])
    u[1] = int(u[1])
    mX= u[0] if u[0] > mX else mX
    mY = u[1] if u[1] > mY else mY
    grid[(u[1],u[0])] = " "

for l in data2:    
    way = l[0]
    line = l[1]
    for i in range(mY+1):
        for j in range( mX+1):
            if way == 'y':
                if grid[(i,j)] == " ":
                    grid[line - (i-line),j] = grid[(i,j)]
            else:
                if grid[(i,j)] == " ":
                    grid[i,line - (j-line)] = grid[(i,j)]                    
    if way == 'y': mY = line-1
    else: mX = line-1

# counter = 0
# for i in range(mY+1):
#     for j in range( mX+1):
#         if grid[(i,j)] == "#": 
#             counter += 1
# print(counter)

for i in range(mY+1):
    for j in range( mX+1):
        if grid[(i,j)] == " ": 
            print(grid[(i,j)],end =" ")
        else: print(".",end =" ")
    print("")