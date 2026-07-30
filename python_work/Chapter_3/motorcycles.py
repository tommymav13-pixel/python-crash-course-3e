#   Een simpele lijst motorfietsen
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#   Het veranderen van een item in een lijst met behulp van de indexpositie
motorcycles[0] = 'ducati'
print(motorcycles) 

#   Het toevoegen van een item aan het einde van een lijst met behulp van de append() methode
motorcycles.append('bmw')
motorcycles.append('kawasaki')
motorcycles.append('harley-davidson')
motorcycles.append('honda')
print(motorcycles)

#   Het toevoegen van een item op een specifieke positie in een lijst met behulp van de insert() methode
motorcycles.insert(0, 'vespa')
print(motorcycles)

#   Het verwijderen van een item uit een lijst met behulp van de del statement
del motorcycles[0]
del motorcycles[2]
print(motorcycles)

#   Als je een item uit een lijst wilt verwijderen en er later nog iets mee wilt doen, 
# kun je de pop() methode gebruiken.
#   De pop() methode verwijdert het laatste item in een lijst, 
# maar het laat je ook toe om dat item te gebruiken nadat het verwijderd is.
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#   Het verwijderen van een item uit een lijst op basis van de waarde in plaats van de positie
motorcycles.remove('yamaha')
print(motorcycles) 

too_expensive = 'bmw'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.") 