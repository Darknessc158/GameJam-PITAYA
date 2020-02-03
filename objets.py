#Importation de la class player fichier model
from model.player import Player
from model.plateforme import Weapon

knife = Weapon("Couteau", 3)


player1 = Player("Jojo", 23, 4)
player2 = Player("Bob", 20, 4)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())

print("Bienvenue au joueur", player1.pseudo, "/ Points de vie:", player1.health, "/ Attaque:", player1.attack)
print("Bienvenue au joueur", player2.pseudo, "/ Points de vie:", player2.health, "/ Attaque:", player2.attack)

print(player1.get_weapon())
print(player1.get_attack())
player1.set_weapon(knife)
print(player1.get_weapon().get_name())
print(player1.get_attack())