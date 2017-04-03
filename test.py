#coding=utf-8
import reversi as re

re = re.reversi()
while 1:
    re.show()
    re.showLegal()
    legalList = re.findLegal()
    x = input("x: ")
    y = input("y: ")
    if (x, y) in legalList:
        re.showReversi(x, y)
        re.move(x, y)
    else:
        print "illegal, please reinput"
        continue

raw_input()
