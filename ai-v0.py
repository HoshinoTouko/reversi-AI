#coding=utf-8
import reversi as ree
import random
m = input("Mode: 0.EvE 1.PvE 2.EvP")
while 1:
    re = ree.reversi()
    while m == 0:
        re.show()
        legalList = re.findLegal()
        randomNextMove = random.choice(legalList)
        x = randomNextMove[0]
        y = randomNextMove[1]
        result = re.move(x, y)
        if result == 0:
            break
    while m == 1:
        re.show()
        legalList = re.findLegal()
        re.showLegal()
        if re.turn == 0:
            x = input("x: ")
            y = input("y: ")
        else:
            randomNextMove = random.choice(legalList)
            x = randomNextMove[0]
            y = randomNextMove[1]
        result = re.move(x, y)
        if result == 0:
            break
    while m == 2:
        re.show()
        legalList = re.findLegal()
        re.showLegal()
        if re.turn == 1:
            x = input("x: ")
            y = input("y: ")
        else:
            randomNextMove = random.choice(legalList)
            x = randomNextMove[0]
            y = randomNextMove[1]
        result = re.move(x, y)
        if result == 0:
            break
    m = input("Mode: 0.EvE 1.PvE 2.EvP")
    if m not in (0, 1, 2):
        break
