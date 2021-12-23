import math 
with open("C:/AoC_2021/test.txt", "r") as f: data = [a.strip() for a in f.readlines()]
#data = []#data[:2]
#data.append("[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")
#data.append("[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]")
#data.append("[[[[4,3],4],4],[7,[[8,4],9]]]")
#data.append("[1,1]")
#data.append("[2,2]")
#data.append("[3,3]")
#data.append("[4,4]")
#data.append("[5,5]")
#data.append("[6,6]")


def printer(num,i):
    for a in range(len(num)):
        if i == a:
            print("(" + num[a] + ")",end="")
        else: print(num[a], end="")
    print("")
        

def makeLists(num,i):
    #print("Num: ", num, i, len(num))
    #printer(num,i)
    li = []
    while i < len(num):
        if num[i] == "[":
            u = makeLists(num,i+1)
            li.append(u[0])
            #print("I BEFORE:",i)
            i = u[1]
            #print("I AFTER:", i)
        elif num[i] == "]": break
        elif num[i] == ",":
            i += 1
            continue
        else:
            #print("Hit num: ", num[i])
            li.append(int(num[i]))
        i += 1
    #print("RETURNED:",li, i)      
    return (li,i)

def addnum(num,num2):
    li = []
    li.append(num)
    li.append(num2)
    return li

def parse(data):
    for a in range(len(data)):
        data[a] = makeLists(data[a],1)[0]
        print(data[a])

def explode(number,org):
    number = 1

def splitNum(number,org):
    number = 1

def reduce(number,depth,done,org):
    print("Main", number)
    for a in range(len(number)):
        if not type(number[a]) == list and depth >= 4:
            print("Exploding ", number, depth, number[a])
            explode(number[a],org)
            if depth > 0: return True
            a = 0
        elif type(number[a]) == list:
            if reduce(number[a],depth+1,False,org) and depth  == 0:
                a = 0
        elif a >= 10:
            number[a] = splitNum(number[a],org)
            if depth > 0: return True
            a = 0
    return False

def runNum(data):
    cur = data[0]
    for a in range(1, len(data)):
        cur = addnum(cur,data[a])
        while True:
            if not reduce(cur,0,False, cur): break

def explodeS(sNum,addN,left):
    #print("ADDING EXPLODE")
    #print(sNum,"----","BLAH",left)
    if left:
        for a in range(len(sNum)-1,0,-1):
            if not sNum[a] in ["[","]",","]:
                bIndex = a
                while True:
                    if sNum[bIndex] in ["]",",","["]:
                        break
                    bIndex -= 1
                nUp = str(int(sNum[bIndex+1:a+1]) + addN)
                #print("FirstNum: ", nUp)
                sNum = sNum[:bIndex+1] + nUp + sNum[a+1:]
                #print(sNum, "WOOOO")
                return sNum
        sNum = sNum
        return sNum
    else:
        #print("ADDED RIGHT")
        for a in range(len(sNum)):
            if not sNum[a] in ["[","]",","]:
                bIndex = a
                while True:
                    if sNum[bIndex] in ["]",",","["]:
                        break
                    bIndex += 1
                nUp = str(int(sNum[a:bIndex]) + addN)
                sNum = sNum[:a] + nUp + sNum[bIndex:]
                return sNum
        return sNum            
            

def reduceS(num,depth):
    limit = len(num)
    a = 0
    while a < limit:
        #print("CUR NUM: ", num)
        if num[a] == "[":
            depth += 1
            if depth >= 5:
                if num[a+1] not in ["]",",","["]:
                    print("----------")
                    bIndex = a
                    while True:
                        if num[bIndex] == "]":
                            break
                        bIndex += 1
                    nExp = num[a+1:bIndex].split(",")                    
                    print("Poggers", num[a:bIndex],"Depth: ", depth)
                    #print(nExp,num[a:])
                    front = num[:a]
                    #print(front)
                    rest  = num[bIndex+1:]
                    #print(a,bIndex)
                    #print(rest)
                    front = explodeS(front,int(nExp[0]),True)
                    #print(front)
                    rest = "0" + explodeS(rest, int(nExp[1]),False)
                    #print(rest)
                    num = front + rest
                    #print(num, "go gog ")
                    a = -1
                    limit = len(num)
                    depth = 0
                    continue
        elif num[a] == "]": depth -= 1
        elif num[a] == ",": m = 0
        else:
            #print("hitnum",depth)
            bIndex = a
            while True:
                if num[bIndex] == "," or num[bIndex] == "]":
                    break
                bIndex += 1
            n = int(num[a:bIndex])
            if n >= 10:
                print("---------------")
                print(num)
                print("SPLITTING", n)
                front = num[:a]
                rest = num[bIndex:]
                n1 = str(math.floor(n/2))
                n2 = str(math.ceil(n/2))
                num = front +"[" + n1 + "," + n2 + "]" + rest
                a = -1
                limit = len(num)
                depth = 0
                print("DONE DONE DONE SPLIT:", num)
        a += 1
    return num
        

def runNumS(data):
    cur = data[0]
    for a in range(1,2):#len(data)):
        cur = "[" + cur + "," + data[a] + "]"
        #print(cur)
        cur = reduceS(cur,0)
        print(cur)
    


#parse(data)
#runNum(data)
print(type((1,2,3)))
runNumS(data)
#for a in data:
#    print(a)
#print(addnum(start,data[0]))
    
