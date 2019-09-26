from animal_class import *
class Reptile(Animal): # Inheritance
    # This code (next 4 lines) is only needed if you want to override the inherited parameters
    def __init__(self, name, number_hearts, camo, eyes = 2,  health = 100): #default argument has to come last i.e something thats specified
        super().__init__(name, eyes = 2, health = 100) #this re-adds all the previous parameters
        self.number_hearts = number_hearts
        self.camo = camo

    def eat(self, food = 'bugs'): #Method of polymorphism to override original method eat()
        return f'Waiiiit for iiittttt, annnnnd POUNCE! NOM NOM NOM {food}'

    def seek_heat(self): #adding new method to reptile class only
        return 'Hmmmm its a bit chilly, wheres the sun at? Why did I sit at the back'