import time
import numpy as np
# start = time.process_time()
with open("in2.txt", "r") as f: data = [int(a) for a in f.read().split(",")]
total = len(data)
fishes = np.array([0,0,0,0,0,0,0,0,0],dtype=object)
for a in data: fishes[a] += 1
# print("Parser: " + str(time.process_time() - start))

start = time.process_time()
days = 9999999
while(days > 0):
    fishes = np.roll(fishes,-1)
    fishes[6] = np.add(fishes[6],fishes[8],dtype=object)
    # hold = fishes[0]
    # for a in range(0, 8):
    #     fishes[a] = fishes[a+1]
    # fishes[6] = sum([fishes[6],hold])
    # fishes[8] = hold
    days -= 1
tot = sum(fishes)
print(str(tot)[:9])
print("Calc " + str(time.process_time() - start))