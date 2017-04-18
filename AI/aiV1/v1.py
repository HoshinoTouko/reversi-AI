import random


def next(reMap):
    legalList = reMap.findLegal()
    return random.choice(legalList)


def info():
    return "AI v1, return the max quality node"
