input = "target area: x=269..292, y=-68..-44"[13:].split(", ")
minX = int(input[0][2:].split("..")[0])
maxX = int(input[0][2:].split("..")[1])
minY = int(input[1][2:].split("..")[0])
maxY = int(input[1][2:].split("..")[1])

print(minX, maxX, minY,maxY)

def inTargetArea(x,y,xV,yV,minX,maxX,minY,maxY):
    mY = 0
    if minY < 0:
        while 0 <= x <= maxX and y >= minY:
            mY = max(mY,y)
            if minX <= x <= maxX and minY <= y <= maxY: return (True,mY)
            x += xV
            y += yV
            if xV < 0: xV += 1
            elif xV > 0: xV -= 1
            yV -= 1
    else:
        if maxY < 0:
            while 0 <= x <= maxX and y >= maxY:
                mY = max(mY,y)
                if minX <= x <= maxX and minY <= y <= maxY: return (True,mY)
                x += xV
                y += yV
                if xV < 0: xV += 1
                elif xV > 0: xV -= 1
                yV -= 1
        else:
            while 0 <= x <= maxX and 0 <= y <= maxY:
                mY = max(mY,y)
                if minX <= x <= maxX and minY <= y <= maxY: return (True,mY)
                x += xV
                y += yV
                if xV < 0: xV += 1
                elif xV > 0: xV -= 1
                yV -= 1
    return (False,-1)
# tests = [(7,2),(6,3),(6,9),(9,0)]
# for a in tests:
#     print(inTargetArea(0,0,a[0],a[1],minX,maxX,minY,maxY))
mY = 0
pos = 0
for x in range(0,maxX+1):
    if minY < 0:
        for y in range(minY,abs(minY)):
            t = inTargetArea(0,0,x,y,minX,maxX,minY,maxY)
            mY = max(t[1],mY)
            if t[0]: pos += 1
    else:
        for y in range(0,maxY*2):
            t = inTargetArea(0,0,x,y,minX,maxX,minY,maxY)
            mY = max(t[1],mY)
            if t[0]: pos += 1
print(mY,pos)
