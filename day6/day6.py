with open("in2.txt", "r") as f: data = [int(a) for a in f.read().split(",")]
total = len(data)
fishes = {}
for a in range(9):
    fishes[a] = 0
for a in data:
    fishes[a] += 1

days = 10000
while(days > 0):
    hold = fishes[0]
    for a in range(0, 8):
        fishes[a] = fishes[a+1]
    fishes[6] += hold
    fishes[8] = hold
    days -= 1
sum = 0
for k, v in fishes.items():
    sum += v
# print(fishes)
print(sum)