with open("in.txt", "r") as f: nums = f.read().splitlines()

def get(a, data):
    cNum = []
    for x in data:
        cNum.append(x[a])
    return cNum

def counts(data):
    gamma = []
    for a in range(len(data[0])):
        gamma.append(get(a,data))
    return gamma

def part1(data,eps):
    gamma = counts(data)    
    gammaBit = ''
    for a in gamma:
        c0 = 0
        c1 = 0
        for x in a:
            if x == '0': c0 += 1
            elif x == '1': c1 += 1        
        if eps is 0:
            if c0 > c1: gammaBit += '0'
            else: gammaBit += '1'
        else:
            if c0 < c1: gammaBit += '0'
            else: gammaBit += '1'

    return int(gammaBit,2)

def oxyNum(data,second):
    cCounts = counts(data)    
    track = data[:]
    trackL = []

    for pos in range(len(data[0])):
        c0 = 0
        c1 = 0
        for x in cCounts[pos]:
            if x == '0': c0 += 1
            elif x == '1': c1 += 1
        if second is 0:
            if c0 > c1: 
                for n in track:
                    if n[pos] == '0': trackL.append(n)
            else:
                for n in track:
                    if n[pos] == '1': trackL.append(n)
        else:
            if c1 < c0: 
                for n in track:
                    if n[pos] == '1': trackL.append(n)
            else:
                for n in track:
                    if n[pos] == '0': trackL.append(n) 
        track = trackL[:]
        if len(track) == 1: break
        trackL = []
        cCounts = counts(track)

    return int(trackL[0],2)

def part2(data):
    return oxyNum(data,0) * oxyNum(data,1)

print(part2(nums), part1(nums,0) * part1(nums,1))