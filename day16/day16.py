with open("in.txt", "r") as f : data = f.read().strip()
#data = "A0016C880162017C3686B18A3D4780"
hex2Bin = {"0" : "0000",
"1" : "0001",
"2" : "0010",
"3" : "0011",
"4" : "0100",
"5" : "0101",
"6" : "0110",
"7" : "0111",
"8" : "1000",
"9" : "1001",
"A" : "1010",
"B" : "1011",
"C" : "1100",
"D" : "1101",
"E" : "1110",
"F" : "1111"}
binary = ""
for a in data:
    binary += hex2Bin[a]

def s2Bin(s):
    return int(s,2)

def printer(binary):
    #for a in range(0,len(binary)-4,4):
    #    print(binary[a:a+4],end=", ")
    print(binary)

def readOperator(binary,readB):
    #Extract Option

def readPacket(binary,versions):
    #printer(binary)
    #print(len(binary))
    pver = s2Bin(binary[:3])
    versions.append(pver)
    ptype = s2Bin(binary[3:6])
    #print(pver, ptype)
    #print(versions, pver)
    num = ""
    readB = 6
    if ptype == 4:
        start = 6
        i = 0
        while True:
            s = binary[start:start+5]
            readB += 5
            #print(s)
            #print(s2Bin(num))
            if s[0] == "0":
                num += s[1:]
                #print("Literal", s2Bin(num))
                #print("READ: ", readB)
                return [s2Bin(num),readB]
            num += s[1:]
            start += 5
            i += 1
    elif ptype == 0:
        value = 0
        
    else:
        readB += 1
        if binary[6] == "0":
            #print("Operator0")
            nBitP = s2Bin(binary[7:7+15])
            start = 7+15
            readB += 15
            #print(nBitP)
            while nBitP > 0:
                u = readPacket(binary[start:],versions)
                #if len(u) > 0:
                    #print(u)
                start += u[1]
                readB += u[1]
                nBitP -= u[1]
                    #print(nBitP)
        elif binary[6] == "1":
            #print("Operator1")
            nPackets = s2Bin(binary[7:7+11])
            #print(nPackets)
            start = 7+11
            readB += 11
            #if binary[start] == "0" and binary[start+1] == "0":
            #    start += 2
            while nPackets > 0:
                #print("Packets Left: ",nPackets)
                u = readPacket(binary[start:],versions)
                if len(u) > 0:
                    a = max(u[1],11)
                    start += a
                    readB += a
                    nPackets -= 1
    #print("READ: ", readB)
    return [0,readB]
            
        
                
                
#print("0",end="")
#printer(binary)
versions = []
readPacket(binary,versions)
print(sum(versions))
            

#print(pver,ptype,num,val)
