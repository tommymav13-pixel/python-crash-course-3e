# Glossary
glossary = {
    'variable': 'A named storage location in memory.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A control structure that repeats a block of code.',
    'list': 'An ordered collection of items.',
    'dictionary': 'A collection of key-value pairs.',
    'key': 'An item in a dictionary that is paired with a value.',
    'value': 'An item in a dictionary that is paired with a key.',
    'set': 'A collection in which each item must be unique.',
    'boolean': 'A value that is either True or False.',
    'string': "A sequence of characters, usually used to represent text such as"
    " words or sentences."

}

# 6-4
for word, definition in glossary.items():
    print(f"{word.title()}: {definition}")

