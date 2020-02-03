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

class Warrior(Player): # Warrior(Player, ?, ?) Pour plusieurs heritage
    #constructor
    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3
        print("Bienvenue au guerrier", pseudo, "/ Points de vie:", health, "/ Attaque:", attack)

    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        super().damage(damage) #utilisation de la fonction damage du player

    def blade(self):
        self.armor = 3
        print("Les points d'armure sont rechargés")

    def get_armor_point(self):
        return self.armor


player1 = Player("Graven", 20, 2)
player1.damage(3)

warrior = Warrior("DarkWarrior", 30, 4)
warrior.damage(4)
print("Bienvenue au guerrier", warrior.pseudo, "/ Points de vie:", warrior.health, "/ Attaque:", warrior.attack, "/ Armure:", warrior.armor)
warrior.damage(4)
print("Bienvenue au guerrier", warrior.pseudo, "/ Points de vie:", warrior.health, "/ Attaque:", warrior.attack, "/ Armure:", warrior.armor)
warrior.damage(4)
print("Bienvenue au guerrier", warrior.pseudo, "/ Points de vie:", warrior.health, "/ Attaque:", warrior.attack, "/ Armure:", warrior.armor)
warrior.damage(4)
print("Bienvenue au guerrier", warrior.pseudo, "/ Points de vie:", warrior.health, "/ Attaque:", warrior.attack, "/ Armure:", warrior.armor)

if issubclass(Warrior, Player):
    print("Le guerrier est bien une spécialisation de Player")