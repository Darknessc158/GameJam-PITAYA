class Plateforme:
    def __init__(self, x, y, isDangerous):
        self.x = x
        self.y = y
        self.isDangerous=isDangerous

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_isDangerous(self):
        return self.isDangeous

    def set_x(self, x):
        self.x=x

    def set_y(self, y):
        self.y=y

    def set_isDangerous(self, isDangerous):
        self.isDangeous=isDangerous

    """ 
    def get_damage_amount(self):
        return self.damage
    """