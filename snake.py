from const import *

class Snake:
    def __init__(self, x:int, y:int, length:int=0):
        self.x = x
        self.y = y
        self.length = length
        self.body = []