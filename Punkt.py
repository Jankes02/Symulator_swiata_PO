class Punkt:

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def to_string(self):
        return "(" + self.y + "," + self.x + ")"
