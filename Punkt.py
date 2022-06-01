import math


class Punkt:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def odleglosc_do(self, drugi):
        return math.sqrt((self.y - drugi.y) ** 2 + (self.x - drugi.x) ** 2)

    def to_string(self):
        return "(" + self.y + "," + self.x + ")"
