with open("in.txt", "r") as f : data = f.read().strip()
data = "620080001611562C8802118E34"
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
    for a in range(0,len(binary)-4,4):
        print(binary[a:a+4],end=", ")
    print("")
 
def readPacket(binary,versions):
    printer(binary)
    pver = s2Bin(binary[:3])
    versions.append(pver)
    ptype = s2Bin(binary[3:6])
    #print(pver, ptype)
    print(versions)
    num = ""
    readB = 6
    if ptype == 4:
        print("Literal")
        start = 6
        i = 0
        while True:
            s = binary[start:start+5]
            readB += 5
            #print(s)
            #print(s2Bin(num))
            if s[0] == "0":
                num += s[1:]
                return [s2Bin(num),readB]
            num += s[1:]
            start += 5
            i += 1
    else:
        print("Operator")
        if binary[6] == "0":
            nBitP = s2Bin(binary[7:7+15])
            start = 7+15
            while nBitP > 0:
                u = readPacket(binary[start:],versions)
                if len(u) > 0:
                    #print(u)
                    start += u[1]
                    nBitP -= u[1]
                else: break
                    #print(nBitP)
            return []
        elif binary[6] == "1":
            nPackets = s2Bin(binary[7:7+11])
            #print(nPackets)
            start = 7+11
            while nPackets > 0:
                print("Packets Left: ",nPackets)
                u = readPacket(binary[start:],versions)
                if len(u) > 0:
                    start += u[1]
                nPackets -= 1
            return []
            
        
                
                
#print("0",end="")
printer(binary)
versions = []
print(readPacket(binary,versions))
print(sum(versions))
            
 
#print(pver,ptype,num,val)
