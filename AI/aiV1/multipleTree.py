#coding=utf-8


class node:

    def __init__(self, data):
        self._data = data
        self._children = []

    def addChildren(self, node):
        self._children.append(node)

    def addChildrens(self, nodes):
        for node in nodes:
            self._children.append(node)

    def getData(self):
        return self._data

    def getChildren(self):
        return self._children

    def go(self, data):
        for child in self._children:
            if child.getdata() == data:
                return child
        return None


class tree:

    def __init__(self):
        self._head = node('header')

    def linkHead(self, node):
        self._head.add(node)
