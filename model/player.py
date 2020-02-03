class Player:
    #constructor
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur", pseudo, "/ Points de vie:", health, "/ Attaque:", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        if self.weapon == None:
            return self.attack
        else:
            return self.attack + self.weapon.get_damage_amount()

    def get_weapon(self):
        return self.weapon

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        target_player.damage(self.get_attack())

    def set_weapon(self, weapon):
        self.weapon = weapon