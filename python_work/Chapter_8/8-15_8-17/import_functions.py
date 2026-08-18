# Here we import an entire module
import pets_to_import

pets_to_import.describe_pet(animal_type='hamster', pet_name='harry')

# Here we import a specific function
from pets_to_import import describe_pet

describe_pet('willie', 'dog')

# Here we use fn as an alias of the function
from pets_to_import import describe_pet as fn

fn('cat', 'sheba')

# Here we import the entire module as an alias
import pets_to_import as mn

mn.describe_pet('dog', 'willie')
mn.describe_pet('dog', pet_name='willie')

# This is importing all functions in a Module
from pets_to_import import *

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')