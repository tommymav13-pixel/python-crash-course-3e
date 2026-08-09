cat = {
    'animal': 'cat',
    'color': 'black',
    'owner': 'Dave',
}

dog = {
    'animal': 'dog',
    'color': 'white',
    'owner': 'rowan',
}

chameleon = {
    'animal': 'chameleon',
    'color': 'green',
    'owner': 'alice',
}

gerbil = {
    'animal': 'gerbil',
    'color': 'brown',
    'owner': 'chantal',
}

pets = [cat, dog, chameleon, gerbil]

for pet in pets:
        print(f'{pet["owner"].title()} owns a',
              pet['color'], 
              pet['animal'])