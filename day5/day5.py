with open("in.txt","r") as f: raw = [[(int(t[0]),int(t[1])) for t in [y.split(",") for y in a.split("\n")[0].split(" -> ")]] for a in f.readlines()]

def update(run,upx,upy,xS,yS,grid):
    counter = 0
    for i in range(run):
        if (xS,yS) in grid:
            grid[(xS,yS)][0] += 1
            if grid[(xS,yS)][1] == 0: 
                counter += 1
                grid[(xS,yS)][1] = 1
        else: grid[(xS,yS)] = [1, 0]
        xS += upx
        yS += upy
    return counter

def run(data,counter):
    grid = {}
    run = 0
    for a in data:
        xS = a[0][0]
        yS = a[0][1]
        xE = a[1][0]
        yE = a[1][1]
        upy = -1 if yS > yE else 0 if yS == yE else 1
        upx = -1 if xS > xE else 0 if xS == xE else 1

        if xS != xE and yS == yE: run = abs(xE - xS) + 1
        elif yS != yE and xS == xE: run = abs(yE - yS) + 1
        elif (xS != xE and yS != yE): run = abs(xE - xS) + 1 
        counter += update(run,upx,upy,xS,yS,grid)

    print(counter)

run(raw,0)