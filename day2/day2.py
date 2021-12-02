with open("in.txt", "r") as f: data = f.read().splitlines()

pos = depth = aim = 0
for a in data:
    s = a.split(" ")
    if s[0] == "forward": 
        pos += int(s[1])
        depth += aim * int(s[1])
    elif s[0] == "up":
        aim -= int(s[1])
    elif s[0] == "down":
        aim += int(s[1])

print(depth * pos)