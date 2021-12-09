import time
import math as m
with open("in.txt", "r") as f: data = [int(a) for a in f.read().split(",")]
start = time.process_time()
dist = min(map(lambda a: sum(list(map(lambda x: int(abs(x-a) *(abs(x-a) +1)/2),data))), range(len(data))))
print("Done: " + str(time.process_time() - start))
print(dist)