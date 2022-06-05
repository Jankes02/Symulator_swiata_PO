import math


class Punkt:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __eq__(self, drugi):
        return self.x == drugi.x and self.y == drugi.y

    def odleglosc_do(self, drugi):
        return math.sqrt((self.y - drugi.y) ** 2 + (self.x - drugi.x) ** 2)

    def to_string(self):
        return "(" + str(self.y) + "," + str(self.x) + ")"
