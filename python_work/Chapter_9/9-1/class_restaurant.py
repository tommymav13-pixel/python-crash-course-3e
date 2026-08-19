class Restaurant:
    """A simple attempt to model information about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the restaurant description."""
        print(
            f"The restaurant's name is {self.restaurant_name.title()} "
            f"and serves {self.cuisine_type.title()} cuisine."
        )

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.restaurant_name.title()} is now open!")


my_restaurant = Restaurant("IDA", "japanese")

print(f"My favourite restaurant is {my_restaurant.restaurant_name}!")
print(f"They serve {my_restaurant.cuisine_type} cuisine.")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()