# Sorteer een lijst van auto's in alfabetische volgorde en print de gesorteerde lijst.
cars = ['toyota', 'honda', 'ford', 'chevrolet']
cars.sort()
print(cars) 

# Print de lijst van auto's in omgekeerde alfabetische volgorde.
cars.sort(reverse=True)
print(cars) 

# Gebruik de sorted() functie om een lijst van auto's in alfabetische volgorde te printen zonder de originele lijst te veranderen.
cars = ['toyota', 'honda', 'ford', 'chevrolet']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) 

print("\nHere is the original list again:")
print(cars)

# Print de lijst van auto's in omgekeerde volgorde.
cars.reverse()
print(cars)    

# Toon het aantal auto's in de lijst.
print(f"\nThere are {len(cars)} cars in the list.")
    