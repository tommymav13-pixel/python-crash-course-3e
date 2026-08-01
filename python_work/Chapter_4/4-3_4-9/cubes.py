# list of cubes using a for loop
cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)    
print(cubes)

# List of cubes using list comprehension
cube = [value ** 3 for value in range(1, 11)]
print(cube)