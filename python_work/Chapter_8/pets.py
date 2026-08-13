def describe_pet(animal_type, pet_name):
        """Display information about a pet"""
        print(f"\nI have a {animal_type}.")
        print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('willie', 'dog')
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