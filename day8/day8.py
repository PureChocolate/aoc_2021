import time
with open("in2.txt", "r") as f: data = [ a.split(" | ") for a in f.readlines()]

nums = [2,4,3,7]
corrected = ""

counter = 0
tot = 0
start = time.time()
maxT = 0.000000000000
for a in data:
    starti = time.time()
    c = a[0].split(" ")
    c.sort(key=lambda s: len(s))
    # print(c)-
    s = list(map(lambda x: set(x), c))
    clock0 = s[3].intersection(s[4],s[5]).intersection(s[1])
    clock1 = s[6].intersection(s[7],s[8]).symmetric_difference(s[9]).intersection(s[0])
    clock2 = s[6].intersection(s[7],s[8]).intersection(s[0])
    clock3 = s[3].intersection(s[4],s[5]).difference(s[1]).difference(s[2]) #.intersection(s[6].intersection(s[7],s[8])).symmetric_difference(s[1]).symmetric_difference(s[0])
    clock4 = s[6].intersection(s[7],s[8]).symmetric_difference(s[9]).difference(s[2])
    clock5 = s[3].intersection(s[4],s[5]).symmetric_difference(s[9]).symmetric_difference(s[0]).intersection(s[2])
    clock6 = s[3].intersection(s[4],s[5]).intersection(s[2])
    # clock = ''.join(clock)
    # print(clock)
    
    check = [0,0,0,0,0,0,0,0,0,0]
    check[0] = clock0.union(clock1,clock2,clock3,clock4,clock5)
    check[1] = clock1.union(clock2)
    check[2] = clock0.union(clock1,clock3,clock4,clock6)
    check[3] = clock0.union(clock1,clock2,clock3,clock6)
    check[4] = clock1.union(clock2,clock5,clock6)
    check[5] = clock0.union(clock5,clock6,clock2,clock3)
    check[6] = clock0.union(clock4,clock2,clock3,clock5,clock6)
    check[7] = clock0.union(clock1,clock2)
    check[8] = clock0.union(clock4,clock2,clock3,clock5,clock6,clock1)
    check[9] = clock0.union(clock1,clock2,clock3,clock5,clock6)
    # check = list(map(lambda x: ''.join(str(x)), check))
    # print(time.time() - starti)
    # if maxT < t: maxT = t
    startg = time.time()
    n = [x.strip("\n") for x in a[1].split(" ")]
    # print(check)
    wires = list(map(lambda x: set(x),n))
    # for x in n:
    #     u = set(x)
        # print(u)
    h = list(map(lambda a: str(check.index(a)),wires))
    x = "".join(h)

    # print(x)
    # for a in range(len(wires)):
    #     h += str(check.index(wires[a]))
    # print(h)

        # print(u)
        # print(check)
        # if u in check:
        #     h += str(check.index(u))
    tot += int(x)
    # print(time.time() - startg)

    # shol = ""
    # for x in c:
    #     if len(x) in nums: 
    #         lenx = len(x)
    #         if lenx == 7: 
    #             shol += "8"
    #         elif lenx == 3: 
    #             shol += "7"
    #         elif lenx == 4: 
    #             shol += "4"
    #         else: 
    #             clock[1] += x[0]
    #             clock[2] += x[1]
    #         counter += 1
    #     else: 
    #         if len(x) == 6:
    #             # 0, 9, 6
    #             c = 0
    #         elif len(x) == 5:
    #             # 2, 3, 5
    #             p = 0

    #         shol += x
    # tot += int(shol)

        


print(str(time.time() - start))
# print("Max Time per build clock: " + str(t))
# print(counter)
print(tot)
# print(data)