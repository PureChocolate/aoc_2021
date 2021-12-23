import math 
#with open("18.txt", "r") as f: data = [a.strip() for a in f.readlines()]
data = []
data.append("[[[[4,3],4],4],[7,[[8,4],9]]]")
data.append("[1,1]")

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
    print("Main", number, depth)
    for a in range(len(number)):
        if not type(number[a]) == list and depth >= 4:
            print("Poggers")
            print(number, depth, number[a])
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

def reduceS(num,depth,done):
    print("Main", num, depth)
    for a in range(len(num)):
        if num[a] == "[":
            depth += 1
            if depth > 4:
                print("Poggers")
                print(num[a:],depth,num[a + 1])
                bIndex = a
                while True:
                    if num[bIndex] == "]":
                        break
                    bIndex += 1
        elif num[a] == "]": depth -= 1
        elif num[a] == ",": continue
        else:
            bIndex = a
            while True:
                if num[bIndex] == "," or num[bIndex] == "]":
                    break
                bIndex += 1
            n = int(num[a:bIndex])
            if n >= 10:
                temp1 = num[:a]
                n1 = str(math.floor(n/2))
                n2 = str(math.ceil(n/2))
                num = num[:a] + n1 + "," + n2 + num[bIndex:]
                a = 0
    return False
        

def runNumS(data):
    cur = "[" + data[0] + ","
    for a in range(1,len(data)):
        cur += data[a] + "]"
        print(cur)
        while True:
            if not reduceS(cur,0,False): break
    


#parse(data)
#runNum(data)
print(type((1,2,3)))
runNumS(data)
#for a in data:
#    print(a)
#print(addnum(start,data[0]))
    
