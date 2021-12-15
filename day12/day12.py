from collections import defaultdict, deque
class Cave:
    def __init__(self, name, links,small):
        self.name = name
        self.links = links
        self.small = small

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.links == __o.links

    def nEQ(self,__o: object) -> bool:
        return self.name == __o.name
    
    def printer(self):
        print("( ",self.name,"//",[x.name for x in self.links],"//", self.small,")")

def makeCaves(data,caves):
    si = 0    
    a0 = 0
    a1 = 0
    found = False
    for a in data:
        if a[0] == "start": 
            a0 = 1
        elif a[1] == "start": 
            a1 = 1
        c = Cave(a[0], [], a[0].islower())
        c1 = Cave(a[1], [], a[1].islower())
        same = False
        for u in caves:
            if u == c:
                same = True
                break
        if not same: 
            caves.append(c)
            if a0 and (not found): 
                si = len(caves)-1
                found = True
        
        same = False
        for u in caves:
            if u == c1:
                same = True
                break
        if not same: 
            caves.append(c1)
            if a1 and (not found): 
                si = len(caves)-1
                found = True
    return si

def relate(data,caves):
    for a in data:
        c = Cave(a[0],[],a[0].islower())
        c2 = Cave(a[1],[],a[1].islower())
        for x in caves:
            if x.nEQ(c):
                c = x
            elif x.nEQ(c2):
                c2 = x
        if c2 not in c.links: c.links.append(c2)
        if c not in c2.links: c2.links.append(c)

def TraverseStep(node,visi,path,count,visL):
    # path = path + " " + node.name
    for a in node.links:
        dLower = visi.copy()
        if a.name == "start": continue
        if a.name == "end":
            # path += " end ||"
            # print(path)
            count += 1
        else:
            if a.small:
                if not visL and dLower[a.name] < 2:
                    dLower[a.name] += 1
                    tempL = False
                    if dLower[a.name] == 2:
                        tempL = True
                    count = TraverseStep(a,dLower,path,count,tempL)
                elif visL and dLower[a.name] == 0:
                    dLower[a.name] += 1
                    count = TraverseStep(a,dLower,path,count,visL)             
            else: count = TraverseStep(a,dLower,path,count,visL)
    return count



def traverse(start,p1):
    c = 0
    for x in start.links:
        dLower = defaultdict(lambda: 0)
        if x.small:
            dLower[x.name] += 1
        c = TraverseStep(x,dLower,"Start",c,p1)
    print(c)


with open("in.txt", "r") as f : data = [a.strip().split("-") for a in f.readlines()]
caves = []
si = makeCaves(data,caves)
relate(data,caves)
traverse(caves[si],False)
traverse(caves[si],True)