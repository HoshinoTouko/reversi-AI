import random
import multipleTree as tree
import copy


def calc(node, generation):
    result = []
    reMap = node.getData()["map"]
    if generation == 1:
        legalList = reMap.findLegal()
        if len(legalList):
            for step in legalList:
                thisTurn = reMap.turn
                thatTurn = (thisTurn + 1) % 2
                tempMap = copy.deepcopy(reMap)
                tempMap.moveByTuple(step)
                thisNum = tempMap.count(thisTurn + 1)
                thatNum = tempMap.count(thatTurn + 1)
                score = float(thisNum) / (thisNum + thatNum)
                data = dict()
                data["map"] = tempMap
                data["score"] = score
                data["step"] = step
                tempResult = tree.node(data)
                result.append(tempResult)
        else:
            return None
    return result


def next(reMap):
    # Create a blank tree
    data = dict()
    data["map"] = reMap
    data["score"] = -1
    mTree = tree.node(data)
    mTree.addChildrens(calc(mTree, 1))
    max = 0
    for item in mTree.getChildren():
        nodeData = item.getData()
        # print nodeData
        if nodeData["score"] >= max:
            max = nodeData["score"]
            nextStep = nodeData["step"]
    # print nextStep
    return nextStep


def info():
    return "AI v1, return the max quality node(only 1 layer)"
