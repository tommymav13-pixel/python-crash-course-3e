plaatsen = ['Barcelona', 'Amsterdam', 'New York', 'Tokyo', 'London']
print("Original list:")
print(plaatsen) 

print("\nHere is the sorted list:")
print(sorted(plaatsen)) 

print("\nHere is the original list again:")
print(plaatsen)

print("\nHere is the sorted list in reverse order:")
print(sorted(plaatsen, reverse=True))

print("\nHere is the original list again:")
print(plaatsen) 

print("\nHere is the list in reverse order:")
plaatsen.reverse()
print(plaatsen)

print("\nHere is the list in reverse alphabetical order:")
plaatsen.sort(reverse=True)
print(plaatsen) 

print("\nHere is the list in alphabetical order:")
plaatsen.sort()
print(plaatsen) 

print(f"\nThere are {len(plaatsen)} places in the list.")   