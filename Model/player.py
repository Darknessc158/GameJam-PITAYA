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

    def get_fuel(self):
        return self.fuel

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def movePositCourante(self, x, y):
        self.x += x
        self.y += y
        print("La position courante du joueur x : ", self.x, " y : ", self.y)
        return (self.x, self.y)

    def set_health(self, health):
        self.health = health

    def set_fuel(self, fuel):
        self.fuel = fuel

    def full_fuel(self): #rechage à 100 le fuel (max)
        self.fuel = 100


    def collision_test(rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list


    def move(rect, movement, tiles):
        collision_types = {'top': False, 'bottom': False,
                        'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types
