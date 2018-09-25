def checkwin(board):
    bricks = [(x,y) for x in range(len(board)) for y in range(len(board[x]))]
    for i in bricks:
        for j in [(1,0),(0,1),(1,1),(-1,1)]:
            if checkline(i[0],i[1],j[0],j[1],board[i[0]][i[1]]) >=4:
                return board[i[0]][i[1]]
    return 0

def checkline(x,y,dx,dy,p):
    if 0<=x<len(board) and 0<=y<len(board[x]) and board[x][y] == p:
        return 1 + checkline(x+dx,y+dy,dx,dy,p)
    else:
        return 0

def printboard(w,h,board):
    out = ""
    for y in range(h):
        for x in range(w-1,-1,-1):
            if x>=len(board) or y>=len(board[x]):
                out = ". " + out
            else:
                out = str(board[x][y]) + " " + out
        out = "\n" + out
    out += "\n"+"--"*w + "\n"
    for i in range(1,w+1):
        out+=str(i)+" "
    print(out)

def move(p,col,w,h,board):
    if 0<=col-1<w and len(board[col-1])<h:
        board[col-1].append(p)

board = [[],[],[],[],[],[],[]]
players = 2
height = 7
width = 7

printboard(width,height,board)
win = 0
while win == 0:
    for i in range(1,players+1):
        prompt = ""
        while prompt == "":
            prompt = input("player"+str(i)+"> ")
        move(i,int(prompt),width,height,board)
        printboard(width,height,board)
        win = checkwin(board)
        if win!=0:
            print("player "+str(i)+" wins!")
            break
