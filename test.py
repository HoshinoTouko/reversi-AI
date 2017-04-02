#coding=utf-8
import reversi as re

re = re.reversi()
while 1:
    re.show()
    x = input("x: ")
    y = input("y: ")
    re.move(x, y)

raw_input()
