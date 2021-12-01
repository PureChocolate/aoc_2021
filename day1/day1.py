#Read the file and store as ints
with open("in.txt", "r") as f: data = [int(n) for n in f.readlines()]

#First value as data
prev = data[0]
count = 0

#Part 1: go through each data and check if next num is greater than last
for num in data:
    if prev < num: count += 1
    prev = num
print(count)

#Part 2: track the first 3 nums at start and sum them
track = data[:3]
preW = sum(track)
count = 0

#Go through rest of the nums and slide values down one at a time and 
#Sum them up again to compare to previous sum for tracked values
for num in data[3:]:
    track.pop(0)
    track.append(num)
    s = sum(track)
    if preW < s: count += 1
    preW = s

print(count)