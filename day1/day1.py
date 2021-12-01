with open("in.txt", "r") as f: data = [int(n) for n in f.readlines()]

prev = data[0]
count = 0
for num in data:
    if prev < num: count += 1
    prev = num
print(count)

# part 2
track = data[:3]
preW = sum(track)
count = 0
for num in data[3:]:
    track.pop(0)
    track.append(num)
    s = sum(track)
    if preW < s: count += 1
    preW = s

print(count)