class Connect4Game:
    def __init__(self, height=7, width=7, n_players=2):
        self.height = height
        self.width = width
        self.n_players = n_players
        self.board = self.empty_board()

    def checkwin(self):
        board = self.board
        bricks = [(x,y) for x in range(len(board)) for y in range(len(board[x]))]
        for i in bricks:
            for j in [(1,0),(0,1),(1,1),(-1,1)]:
                if self.checkline(i[0],i[1],j[0],j[1],board[i[0]][i[1]]) >=4:
                    return board[i[0]][i[1]]
        return None

    def checkline(self, x, y, dx, dy, p):
        board = self.board
        if 0<=x<len(board) and 0<=y<len(board[x]) and board[x][y] == p:
            return 1 + self.checkline(x+dx,y+dy,dx,dy,p)
        else:
            return 0

    def print_board(self):
        board = self.board
        w = self.width
        h = self.height
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

    def move(self, p, col):
        board = self.board
        w = self.width
        h = self.height
        if 0<=col<w and len(board[col])<h:
            board[col].append(p)

    def empty_board(self):
        return [[] for i in range(self.width)]

    def is_full(self):
        return all([len(col) >= self.height for col in self.board])

if __name__ == '__main__':
    game = Connect4Game()
    game.print_board()
    win = None
    while win == None:
        for i in range(1,game.n_players+1):
            prompt = ""
            while prompt == "":
                prompt = input("player"+str(i)+"> ")
            game.move(i, int(prompt))
            game.print_board()
            win = game.checkwin()
            if win != None:
                print("player "+str(i)+" wins!")
                break
