from collections import defaultdict
with open("in.txt", "r") as f: rD =  [[*map(lambda x: [int(x),0], s.strip())] for s in f.readlines()]
data = rD.copy()
rDC = rD.copy()
print("parsed: ")

def flash(flashes,flasesCur,data,r,c):
    stack = []
    flashes += 1
    flasesCur += 1
    data[r][c][0] = 0
    data[r][c][1] = 1
    # dones.append((r,c))
    stack.append((r,c))
    while(len(stack) > 0):
        n = stack.pop(0)
        u = [[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[1,1],[1,-1],[-1,1]]
        for x in u:
            ra = n[0]+ x[0]
            cc = n[1] + x[1]            
            if 0 <= ra < len(data) and 0 <= cc < len(data[r]):
                if data[ra][cc][1] == 0:                   
                    data[ra][cc][0] += 1
                    if data[ra][cc][0] > 9:
                        flashes += 1
                        flasesCur += 1
                        data[ra][cc][0] = 0
                        data[ra][cc][1] = 1
                        stack.append((ra,cc))
    return (flashes,flasesCur)

def run(data):
    steps = 100
    step = 0
    flashes = 0
    flasesCur = 0
    while(True):
        flasesCur = 0
        for r in range(len(data)):
            for c in range(len(data[r])):
                if data[r][c][1] == 0: data[r][c][0] += 1
                if data[r][c][0] > 9:
                    x = flash(flashes,flasesCur, data,r,c)
                    flashes = x[0]
                    flasesCur = x[1]
        for r in range(len(data)):
            for c in range(len(data[r])):
                data[r][c][1] = 0
        steps -= 1
        step += 1
        if flasesCur == len(data) * len(data[0]):
            print(step)
            break
        if steps == 0: print("P1:", flashes)


run(rD)