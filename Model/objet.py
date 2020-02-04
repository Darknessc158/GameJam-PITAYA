
class Objet:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_name(self):
        return self.name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def add_position(self, x, y):
        self.x += x
        self.y += y


class Carburant(Objet):
    def __init__(self, name, x, y, quantite):
        super().__init__(self, name, x, y)
        self.quantite = quantite

    def get_quantite(self):
        return self.quantite

    def set_quantite(self, quantite):
        self.quantite = quantite

class Ennemi(Objet):
    def __init__(self, name, x, y, recul):
        super().__init__(self, name, x, y)
        self.recul = recul

    def get_recul(self):
        return self.quantite

    def set_recul(self, recul):
        self.recul = recul