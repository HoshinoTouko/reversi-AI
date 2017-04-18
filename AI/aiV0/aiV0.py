import random


def next(reMap):
    legalList = reMap.findLegal()
    return random.choice(legalList)


def info():
    return "AI v0, return a random result"
