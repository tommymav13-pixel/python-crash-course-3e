person_01 = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 30,
        'city': 'New York'
}

# Create two more dictionaries with people
person_02 = {
        'first_name':'Jack',
        'last_name': 'Black',
        'age': 34,
        'city': 'Los Angeles'
}

person_03 = {
        'first_name': 'Anna',
        'last_name': 'Stone',
        'age': 27,
        'city': 'Manhatten'
}

# store dictionaries in list called people
people = [person_01, person_02, person_01]

for person in people:
        print(person['first_name'])
        print(person['last_name'])
        print(person['age'])
        print(person['city'])
        print()
