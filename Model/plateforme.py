class Plateforme:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, x, y, isPoison):
        self.x = x
        self.y = y
        self.poison=isPoison

    # instance method
    def description(self):
        return "Platefome x: {}   y: {}  Poison: {} ".format(self.x, self.y, self.poison)


# Instantiate the Dog object
mikey = Plateforme(8, 6, True)

# call our instance methods
print(mikey.description())
