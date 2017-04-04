#coding=utf-8
import reversi as ree
import random
times = input("Times:")
stat = {
    "Xwin": 0,
    "Owin": 0,
    "Tie": 0
}
for i in range(times):
    re = ree.reversi()
    while 1:
        # re.show()
        legalList = re.findLegal()
        # re.showLegal()
        randomNextMove = random.choice(legalList)
        x = randomNextMove[0]
        y = randomNextMove[1]
        result = re.move(x, y)
        if result == 0:
            if re.winner == "X":
                stat["Xwin"] += 1
            elif re.winner == "O":
                stat["Owin"] += 1
            elif re.winner == "Tie":
                stat["Tie"] += 1
            break
print stat
