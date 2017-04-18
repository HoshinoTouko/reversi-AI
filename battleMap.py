#coding=utf-8


import reversi as ree
import copy
import AI.aiV1.v1 as oriAi1
import AI.aiV0.aiV0 as oriAi2


def run(times):
    stat = {
        "AI1win": 0,
        "AI2win": 0,
        "Tie": 0
    }
    for i in range(times):
        if i % 2:
            ai1 = oriAi1
            ai2 = oriAi2
        else:
            ai1 = oriAi2
            ai2 = oriAi1
        re = ree.reversi()
        while 1:
            # re.show()
            # raw_input("")
            tempRe = copy.deepcopy(re)
            if re.turn == 0:
                nextMove = ai1.next(tempRe)
            else:
                nextMove = ai2.next(tempRe)
            result = re.moveByTuple(nextMove)
            if result == 0:
                if re.winner == "X":
                    if i % 2:
                        stat["AI1win"] += 1
                    else:
                        stat["AI2win"] += 1
                elif re.winner == "O":
                    if i % 2:
                        stat["AI2win"] += 1
                    else:
                        stat["AI1win"] += 1
                elif re.winner == "Tie":
                    stat["Tie"] += 1 
                break
    print stat
    print "AI1 is " + ai1.info()
    print "AI2 is " + ai2.info()


times = input("Times: ")
run(times)
