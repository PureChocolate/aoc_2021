with open("in.txt", "r") as f: rD =  [[*map(lambda x: int(x), s.strip())] for s in f.readlines()]

def run(data):
    steps = 0
    flashes = 0
    while(True):
        flasesCur = 0
        done = []
        for r in range(len(data)):
            for c in range(len(data[r])):
                if data[r][c] == 9:
                    stack = []
                    flashes += 1
                    flasesCur += 1
                    data[r][c] = 0
                    done.append((r,c))
                    stack.append((r,c))
                    while(len(stack) > 0):
                        n = stack.pop(0)
                        u = [[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[1,1],[1,-1],[-1,1]]
                        for x in u:
                            ra = n[0]+ x[0]
                            cc = n[1] + x[1]                                
                            if 0 <= ra < len(data) and 0 <= cc < len(data[r]):
                                if (ra,cc) not in done:  data[ra][cc] += 1
                                if data[ra][cc] > 9 and (ra,cc) not in done:
                                    flashes += 1
                                    flasesCur += 1
                                    data[ra][cc] = 0
                                    done.append((ra,cc))
                                    stack.append((ra,cc))
                else: 
                    if (r,c) not in done: data[r][c] += 1
        if flasesCur == len(data) * len(data[0]):
            print(steps)
            break
        steps += 1
    print(flashes)

run(rD)