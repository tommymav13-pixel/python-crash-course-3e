import pets_to_import
pets_to_import.describe_pet(animal_type='hamster', pet_name='harry')

from pets_to_import import describe_pet
describe_pet('willie', 'dog')

from module_name import function_name as fn
import module_name as mn
from module_name import *




describe_pet('cat', 'sheba')

# Order Matters in Positional Arguments. The order of Keyword arguments doesn't
# matters

# Equivalent Function Calls
# A dog named Willie.
describe_pet('dog', 'willie')
describe_pet('dog', pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')