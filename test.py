#coding=utf-8
import reversi as ree

re = ree.reversi()
while 1:
    re.show()
    re.showLegal()
    legalList = re.findLegal()
    x = input("x: ")
    y = input("y: ")
    if (x, y) in legalList:
        re.showReversi(x, y)
        result = re.move(x, y)
    else:
        print "illegal, please reinput"
        continue
    if result == 0:
        break

raw_input()
