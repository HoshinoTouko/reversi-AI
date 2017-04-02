#coding=utf-8


class reversi:
    def __init__(self):
        self.map = [[0] * 8 for i in range(8)]
        self.turn = 0 # 0 means black, 1 means white
        self.move(3, 3)
        self.move(3, 4)
        self.move(4, 4)
        self.move(4, 3)

    def move(self, x, y):
        if self.turn == 0:
            self.map[y][x] = 1
        else:
            self.map[y][x] = 2
        self.next()

    def next(self):
        self.turn = (self.turn + 1) % 2

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
