def addition(x, y):
    res = x+y
    return res

def multiplication(x, y):
    res = x*y
    return res

def max(a, b):
    if a > b:
        return a
    else:
        return b

x = input("Choisissez un premier nombre")
y = input("Choisissez un deuxieme nombre")

print("La valeur max est ", max(x,y))
print("Resultat de " + x + " + " + y + " = ", addition(int(x), int(y)))
print("Resultat de " + x + " x " + y + " = ", multiplication(int(x), int(y)))