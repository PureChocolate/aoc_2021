from collections import defaultdict

with open("in.txt", "r") as f: data = [a.strip("\n") for a in f.readlines()]

rules = defaultdict(lambda: "")
formula = data[0]
for x in data[2:]:
    u = x.split(" -> ")
    rules[u[0]] = u[1]


pairs = defaultdict(lambda: 0)
for i in range(0,len(formula)-1):
    cur = formula[i: i+2]
    pairs[cur] += 1

step = 40
while(step > 0):
    nPair = defaultdict(lambda: 0)
    for k in pairs.keys():
        u = rules[k]
        nPair[k[0] + u] += pairs[k]
        nPair[u + k[1]] += pairs[k]

    pairs = nPair
    step -= 1

oCount = defaultdict(lambda: 0)
for k in pairs.keys():
    if nPair[k] > 1:
        oCount[k[0]] += nPair[k]
    elif nPair[k] > 0:
        oCount[k[0]] += 1

oCount[formula[-1]] += 1
vals = list(oCount.values())
vals.sort()
print(vals[-1] - vals[0])