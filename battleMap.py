#coding=utf-8


import reversi as ree
import copy
import AI.aiV0 as ai1
import AI.aiV0 as ai2


def run(times):
    stat = {
        "Xwin": 0,
        "Owin": 0,
        "Tie": 0
    }
    for i in range(times):
        re = ree.reversi()
        while 1:
            # re.show()
            tempRe = copy.deepcopy(re)
            if re.turn == 0:
                nextMove = ai1.next(tempRe)
            else:
                nextMove = ai2.next(tempRe)
            result = re.moveByTuple(nextMove)
            if result == 0:
                if re.winner == "X":
                    stat["Xwin"] += 1
                elif re.winner == "O":
                    stat["Owin"] += 1
                elif re.winner == "Tie":
                    stat["Tie"] += 1
                break
    print stat


times = input("Times: ")
run(times)
