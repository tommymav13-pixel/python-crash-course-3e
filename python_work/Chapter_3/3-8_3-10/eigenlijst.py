# bedenk een lijst met talen en gebruik alle functies uit het hoofdstuk om de lijst te bewerken en te printen.
talen = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby']
print("Original list:")
print(talen)

print("\nHere is the sorted list:")
print(sorted(talen))

print("\nHere is the original list again:")
print(talen)

print("\nHere is the sorted list in reverse order:")
print(sorted(talen, reverse=True))

print("\nHere is the original list again:")
print(talen)

print("\nHere is the list in reverse order:")
talen.reverse()
print(talen)

print("\nHere is the list in reverse alphabetical order:")
talen.sort(reverse=True)
print(talen)

print("\nHere is the list in alphabetical order:")
talen.sort()
print(talen)

print(f"\nThere are {len(talen)} languages in the list.")
