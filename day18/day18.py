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

def explode(number):
    number = 1

def splitNum(number):
    number = 1

def reduce(number,depth):
    for a in number:
        if type(a) == list and depth >= 4:
            number = explode(a)
        elif type(a) == list: reduce(a,depth+1)
        elif a >= 10: number = splitNum(a)

def runNum(data):
    cur = data[0]
    for a in range(1, len(data)):
        cur = addnum(cur,data[a])
        reduce(cur,1)
    


parse(data)
runNum(data)
print(type((1,2,3)))
#print(addnum(start,data[0]))
    
