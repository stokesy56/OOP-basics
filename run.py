from animal_class import *
from reptile_class import *
import cmath
my_animal = Animal('Ricky',3) # This is where I create an instance of class animal
print(my_animal)
print(type(my_animal))
print(my_animal.eat('taco'))
print(my_animal.sleep())
print((my_animal.potty()))
print(my_animal.name)

my_animal2 = Animal('Jose')
print(my_animal2.name)
print(my_animal2.play())

my_animal3 = Animal('Benjani',45,100)
print(str(my_animal3.number_eyes) + ' ' + my_animal3.name)

my_reptile = Reptile('Ringo', 'green',99,3,'can turn into any colour')
print(my_reptile.name)
print(my_reptile.eat())
print(my_reptile.seek_heat())
print(my_reptile.camo)



