class Animal():

    # Characteristics
    def __init__(self, name, eyes = 2, health = 100): #runs only once when you initialise an object # can't be edited when called
        self.name = name
        self.number_eyes = eyes
        self.alive = True
        self.numer_animal_eaten = 0
        self.age = 0
        self.health = health



    # Behaviours

    def eat(self, food):
        return f'NOM NOM NOM {food}'

    def sleep(self):
        return 'zZzzzzzz'

    def hunt(self):
        return 'ATAAAAAAACCCCCCKKKKK'

    def potty(self):
        return '0_0'

    def play(self):
        return 'XD Rawr'

# Let create an object of class animal
    # initialising an object

#my_animal = Animal() # This is where I create an instance of class animal

# print(my_animal)
# print(type(my_animal))