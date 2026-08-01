# Write a series of conditional tests. Print a statement describing each test 
# and your prediction for the results of each test.
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Create at least 10 tests. Have at least 5 tests evaluate to True and 
# another 5 tests evaluate to False.

# Conditional Test 1
book = 'A Brief History of Time'
print("\nIs book == 'A Brief History of Time'? I predict True.")
print(book == 'A Brief History of Time')

print("\nIs book == 'The Great Gatsby'? I predict False.")
print(book == 'The Great Gatsby')   

# Conditional Test 2
age = 25
print("\nIs age > 18? I predict True.")
print(age > 18)

print("\nIs age < 18? I predict False.")
print(age < 18) 

# Conditional Test 3
temperature = 30   
print("\nIs temperature >= 30? I predict True.")
print(temperature >= 30)   

print("\nIs temperature <= 20? I predict False.")
print(temperature <= 20)

# Conditional Test 4
is_raining = True
print("\nIs it raining? I predict True.")
print(is_raining)

print("\nIs it sunny? I predict False.")
print(not is_raining)  

# Conditional Test 5
fruits = ['apple', 'banana', 'orange'] 
print("\nIs 'banana' in the list of fruits? I predict True.")
print('banana' in fruits)

print("\nIs 'grape' in the list of fruits? I predict False.")
print('grape' in fruits)

# Conditional Test 6 for equality and inequality with strings
language = 'Python'
print("\nIs language == 'Python'? I predict True.")
print(language == 'Python')

print("\nIs language != 'Java'? I predict False.")
print(language != 'Java')

# Conditional Test 7 for equality and inequality with numbers
score = 85
print("\nIs score == 85? I predict True.")
print(score == 85)

print("\nIs score != 90? I predict True.")
print(score != 90)

# Conditional Test 8 for greater than and less than
height = 175
print("\nIs height > 170? I predict True.")
print(height > 170)

print("\nIs height < 160? I predict False.")
print(height < 160)

# Conditional Test 9 for greater than or equal to and less than or equal to
weight = 70
print("\nIs weight >= 70? I predict True.")
print(weight >= 70)

print("\nIs weight <= 60? I predict False.")
print(weight <= 60)

# Conditional Test 10 for checking membership in a list
colors = ['red', 'green', 'blue']
print("\nIs 'green' in the list of colors? I predict True.")
print('green' in colors)

print("\nIs 'yellow' in the list of colors? I predict False.")
print('yellow' in colors)

# Conditional Test 11 using the lower() method
name = 'John'
print("\nIs name == 'john'? I predict True.")
print(name.lower() == 'john')

print("\nIs name == 'Jane'? I predict False.")
print(name.lower() == 'jane')

# Conditional Test 12 using the and keyword
age = 20
print("\nIs age > 18 and age < 30? I predict True.")
print(age > 18 and age < 30)

print("\nIs age < 18 and age > 30? I predict False.")
print(age < 18 and age > 30)

# Conditional Test 13 using the or keyword
temperature = 25
print("\nIs temperature < 20 or temperature > 30? I predict False.")
print(temperature < 20 or temperature > 30)

print("\nIs temperature < 20 or temperature > 20? I predict True.")
print(temperature < 20 or temperature > 20)
