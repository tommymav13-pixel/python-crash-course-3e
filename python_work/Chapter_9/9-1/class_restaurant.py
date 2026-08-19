class Restaurant:
        """A simple attempt to model information about a restaurant"""

        def __init__(self, name, cuisine):
                """Initialize name and type"""
                self.name = name
                self.cuisine = cuisine

        def describe_restaurant(self):
                """Print restaurant description"""
                print(f"The restaurant's name is {self.name.title()} and has a"
                      f"{self.cuisine} kitchen")

        def open_restaurant(self):
                """Simulate opening the restaurant."""
                print(f"{self.name.title()} is now open!")

my_restaurant = Restaurant("IDA", "japanese")

print(f"My favourite restaurant is {my_restaurant.name}!")
print(f"They have {my_restaurant.cuisine} foods")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
