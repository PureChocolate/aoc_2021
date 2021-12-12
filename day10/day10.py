with open("bigboy.txt", "r") as f : data = [a.rstrip() for a in f.readlines()]

char = {"(": (")",1), "[": ("]",2) , "{": ("}",3),"<":(">",4)}
score = 0
scoreCl = []
new =[]
for a in range(len(data)):
    lis = []
    wrong = False
    scoreC = 0
    for c in data[a]:        
        if c == "}":
            if lis[-1] == "{":
                lis.pop()
                continue
            else:
                wrong = True
                score += 1197
                break
        elif c == ")":
            if lis[-1] == "(":
                lis.pop()
                continue
            else:
                wrong = True
                score += 3
                break
        elif c == "]": 
            if lis[-1] == "[":
                lis.pop()
                continue
            else:
                wrong = True
                score += 57
                break
        elif c == ">": 
            if lis[-1] == "<":
                lis.pop()
                continue
            else:
                wrong = True
                score += 25137
                break
        lis.append(c)
    if not wrong:
        for x in range(len(lis)-1,-1,-1):
            scoreC = (scoreC * 5) + char[lis[x]][1]
        scoreCl.append(scoreC)
print(score)
scoreCl.sort()
print(scoreCl[int(len(scoreCl)/2)])