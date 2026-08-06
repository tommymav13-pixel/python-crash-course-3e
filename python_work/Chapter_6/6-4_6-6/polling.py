favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'dave': 'java',
    'samantha': 'html'
}

take_poll = ['melissa', 'erin']

for person in take_poll:
    if person not in favorite_languages:
        print(f"{person.title()}, please take our poll!")

print()

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")