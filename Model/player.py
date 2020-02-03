class Player:
    def __init__(self, health, x, y, fuel):
        self.x = x  # position x
        self.y = y  # position y
        self.health = health  # Vie du joueur 1 ou 0
        self.fuel = fuel  # quantite de fuel du jetpack du joueur

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_health(self):
        return self.health

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_health(self, health):
        self.health = health

    def set_fuel(self, fuel):
        self.fuel = fuel
