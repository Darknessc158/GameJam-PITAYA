import statistics
# from statistics import mean #importer juste une fonction
from random import shuffle

def main(): #Definition d'une fonction
   """
   # print("Hello") #Fin de fonction avec deux sauts de ligne
   # print("YO 2eme ligne")

   #creation de variables
   userName = "Momi"
   age = 19
   wallet = 125.7
   is_happy = True

   print(userName, age)
   age = 25
   print("Nouvel age :", age)
   age += 1 #incremente de 1
   print("Salut " + userName + ", vous avez " + str(age) + " ans.")


#Input clavier
   #attention à bien convertir les types à chaque fois
   note1 = int(input("Entrer la permiere note"))
   note2 = int(input("Entrer la deuxieme note"))
   note3 = int(input("Entrer la troisieme note"))
   moy = (note1+note2+note3)/3
   print("La moyenne des notes est égale à " + str(moy))


wallet = 5000
computer_price = 1200
#comparator == != < > <= >=
# can use and et or

#condition ternaire
text = ("L'achat est possible","Achat impossible")[computer_price == 1000]
print(text)

if computer_price <= wallet and computer_price >= 1000:
   print("Le prix de l'ordi est inférieur à " + str(wallet))
   wallet -= computer_price
else:
   print("Non, Le prix est sup  la t'es ser")

#systeme de verif de mdp avec condition if elif else
password = input("Entrez votre mdp")
password_length = len(password)
if password_length <= 8:
   print("mot de passe trop court")
elif  6 < password_length <= 8:
   print("entre 6 et 8 inclus")
else:
   print("mot de passe valide")


#les listes
online_players = ["Graven","Anana","CleyMax","Kola"]
#getter
print(online_players[0])
print(online_players[len(online_players) - 1])
#Modifier
online_players[0] = "Momi"
print(online_players)
#ajout en milieu de la liste
online_players.insert(1,"BernardGamer")
print(online_players)
online_players[2:4] = ["JOJO","PAUL"]
print(online_players)
#Ajout a la fin de la liste
online_players.append("Gameurdernier")
online_players.extend(["yoo","slt"])
print(online_players)
#Delete
del online_players[1]
#online_players.pop[1]
online_players.remove("JOJO")
online_players.clear() # vide tout
#exemple
notes = [8, 12, 13, 20, 10, 2]
#module python statistics
result = statistics.mean(notes) #fonction deja toute faite
print("La moyenne de l'eleve est de {}".format(result))
print(notes)
shuffle(notes)
print(notes)
#input de liste
text = input("Entrez une chaine (email-pseudo-motdepasse)").split("-")
print(text)
print("Salut {} ton mot de passe{}".format(text[0],text[1]))


#Les Boucles

#boucle for
for i in range(1, 6):
   print("Vous etes le client n°{}".format(i))

emails = ["oui@gmail","hackeur@gmail.fr","non@gmail.com","mdr@gmail.fr","fraudeur@hot.fr"]
blacklist = ["hackeur@gmail.fr","fraudeur@hot.fr"]
#boucle for each
for email in emails:

   if email in blacklist:
      print("Email {} interdit ! envoi impossible ...".format(email))
      break #permet de stoper la boucle

   print("Email envoyé à : ", email)

#boucle while
salary = 1500
while salary < 2000:
   salary += 120
   print("Votre salaire actuel est de ", salary, "$")
print("Salaire final : ",salary)

#Autre boucle while
suscribers_count = 2500
months = 0
while months <= 24:
   suscribers_count *= 1.10 #augmentation de 10% par mois
   print("Vous avez actuellement {} abonnés.".format(suscribers_count))
   months += 1
"""


if __name__ == '__main__':
   main()
