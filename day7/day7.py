import time
with open("in.txt", "r") as f: data = [int(a) for a in f.read().split(",")]
start = time.process_time()
dist = min(map(lambda a: sum(list(map(lambda x: sum(range(1,abs(x-a) +1)),data))), range(len(data))))
print("Done: " + str(time.process_time() - start))
print(dist)