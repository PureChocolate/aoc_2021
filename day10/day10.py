with open("in.txt", "r") as f : data = [a.rstrip() for a in f.readlines()]

char = {"(": (")",1), "[": ("]",2) , "{": ("}",3),"<":(">",4)}
# lis = [0,0,0,0]
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
        lis.reverse()
        for x in lis:
            data[a] += char[x][0]
            scoreC = (scoreC * 5) + char[x][1]
        scoreCl.append(scoreC)
print(score)
scoreCl.sort()
print(scoreCl[int(len(scoreCl)/2)])
# print(new)
        


# print(char)