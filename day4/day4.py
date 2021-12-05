import re
with open("in2.txt", "r") as f: data = f.readlines()
if data[-1] != "\n": data.append("\n")



nums = data[0].split("\n")[0]
nums = nums.split(",")
numi = []
for a in nums:
    numi.append(int(a))

markedBoard = {}

counter = 0
data = data[2:]
for a in range(len(data)):
    data[a] = data[a].split("\n")[0]
    data[a] = re.split(r'\s+',data[a])
    temp  = []
    for x in data[a]:
        if x is not "": temp.append(int(x))
    data[a] = temp

# print(data)
counter = 0
boards = []
cBoard = []
for a in data:
    if a != []: cBoard.append(a)
    else:
        markedBoard[counter] = []
        boards.append(cBoard)
        cBoard = []
        counter += 1

def bingoCounter(board,markBoard):
    count = 0
    for r in range(len(board)):
        count = 0
        for k in range(len(board[r])):
                check = board[r][k] in markBoard
                if check: count += 1
        if count is (len(board)): return True

    count = 0
    for r in range(len(board)):
        count = 0
        for k in range(len(board[r])):
                check = board[k][r] in markBoard
                if check: count += 1
        if count is len(board): return True
    return False

def bingo(board, markBoard):
    num = 0
    match = bingoCounter(board,markBoard)
    if match:
        for x in board:
            for u in x:
                if u in markBoard:
                    print("(" + str(u) + ")",end=" ")
                else : print(u,end= " ")

            print("\n")
        for a in board:
            for x in a:
                if x not in markBoard: num += x
        print(num)
        return (True, num)
    return (False, 0)

def run(numi,boards,markedBoard):
    won = 0
    needWon = len(boards)
    lastWon = []
    for a in range(len(numi)):
        for x in range(len(boards)):
            for n in boards[x]:
                for c in n:
                    if c == numi[a]: markedBoard[x].append(c)
            for n in boards[x]:
                for c in n:
                    if c in markedBoard[x]:
                        print("(" + str(c) + ")",end=" ")
                    else : print(c,end= " ")

                print("\n")
            print("^^^^^^^^^^^^^^^^^^")
            store = bingo(boards[x], markedBoard[x])
            if store[0]: 
                # lastWon = [store[1], a]
                # won += 1
                # if won == needWon:
                return lastWon[0] * lastWon[1]
                # print(str(store[1]) + "..." + str(a))
                # return a * store[1]
        print(str(a) + "...." + str(numi[a]))
        print("---------------------------------")
    # return lastWon[0] * lastWon[1]
        
        
print(run(numi,boards,markedBoard))