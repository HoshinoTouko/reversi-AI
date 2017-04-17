#coding=utf-8


class reversi:
    def __init__(self):
        self.map = [[0] * 8 for i in range(8)]
        self.turn = 0  # 0 means black, 1 means white
        self.winner = ""
        self.map[3][3] = 1
        self.map[4][3] = 2
        self.map[4][4] = 1
        self.map[3][4] = 2

    def move(self, x, y):
        legalList = self.findLegal()
        if (x, y) in legalList:
            reversiPieces = self.findReversi(x, y)
            self.setP((x, y), self.turn)
            for reversiPiece in reversiPieces:
                self.setP(reversiPiece, self.turn)
            self.next()
        # Check who win
        legalList = self.findLegal()
        if len(legalList) == 0:
            self.next()
            legalList = self.findLegal()
            if len(legalList) == 0:
                data = self.countMap()
                if data[0] > data[1]:
                    # print "X win"
                    self.winner = "X"
                elif data[0] == data[1]:
                    # print "Tie"
                    self.winner = "Tie"
                elif data[0] < data[1]:
                    # print "O win"
                    self.winner = "O"
                return 0
            else:
                return 1
        else:
            return 1

    def moveByTuple(self, t):
        return self.move(t[0], t[1])

    def setP(self, (x, y), turn):
        self.map[y][x] = turn + 1

    def countMap(self):
        black = 0
        white = 0
        for y in self.map:
            for x in y:
                if x == 1:
                    black += 1
                elif x == 2:
                    white += 1
        return (black, white, 64-black-white)

    def next(self):
        self.turn = (self.turn + 1) % 2

    def showLegal(self):
        print self.findLegal()

    def findLegal(self):
        # First step
        result = []
        nowMove = self.turn + 1
        nextMove = (self.turn + 1) % 2 + 1
        for y in range(8):
            for x in range(8):
                # If the position is not blank, pass it
                if self.map[y][x] != 0:
                    continue
                isLegal = False
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        # 1st. step:
                        # The piece must next to an another colour piece
                        try:
                            if self.map[y+i][x+j] != nextMove:
                                continue
                        except:
                            continue
                        # 2nd. step:
                        # Try that if the piece can 'eat' some another colour piece
                        tempx = x
                        tempy = y
                        while 1:
                            tempx += j
                            tempy += i
                            try:
                                nowPiece = self.map[tempy][tempx]
                            except:
                                break
                            try:
                                if nowPiece == nowMove:
                                    isLegal = True
                                    break
                                elif nowPiece == nextMove:
                                    continue
                                elif nowPiece == 0:
                                    break
                            except:
                                break
                if isLegal:
                    result.append((x, y))
        return result

    def showReversi(self, x, y):
        print self.findReversi(x, y)

    def findReversi(self, x, y):
        result = []
        nowMove = self.turn + 1
        nextMove = (self.turn + 1) % 2 + 1
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                # 1st. step:
                # The piece must next to an another colour piece
                tempResult = []
                try:
                    if self.map[y+i][x+j] != nextMove:
                        continue
                except:
                    continue
                # 2nd. step:
                # Try that if the piece can 'eat' some another colour piece
                tempx = x
                tempy = y
                isLegal = False
                while 1:
                    tempx += j
                    tempy += i
                    try:
                        nowPiece = self.map[tempy][tempx]
                    except:
                        break
                    # print (tempx, tempy),
                    try:
                        if nowPiece == nowMove:
                            # print "now"
                            isLegal = True
                            break
                        elif nowPiece == nextMove:
                            # print "next"
                            tempResult.append((tempx, tempy))
                            continue
                        elif nowPiece == 0:
                            # print "0"
                            break
                    except:
                        break
                if isLegal:
                    for tt in tempResult:
                        result.append(tt)
        return result

    def show(self):
        print " ",
        for i in range(8):
            print i,
        print ""
        j = 0
        for y in self.map:
            print j,
            for x in y:
                if x == 0:
                    print "-",
                elif x == 1:
                    print "X",
                elif x == 2:
                    print "O",
            j += 1
            print ""
        print "================="
