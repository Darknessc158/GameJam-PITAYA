class Plateformedisplay:
    def __init__(self, x, y, long, larg, type):
        self.x = x
        self.y = y
        self.long = long
        self.larg = larg
        self.type = type

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_long(self):
        return self.long

    def get_larg(self):
        return self.larg

    def get_position(self):
        return (self.x, self.y)

    def set_position(self, x, y):
        self.x += x
        self.y += y

    def get_type(self):
        return self.type

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y