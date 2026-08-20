class User:
    """Gives description of user"""

    def __init__(self, first_name, last_name):
        """Initialize user descriptions"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Print user discription"""
        print(
            f"First name: {self.first_name}"
            f"Last name: {self.last_name}"
            )

    def greet_user(self):
        """Greet the user"""
        print(f"Welcome {self.first_name} {self.last_name}!")

user_01 = User("Richard", "Dawkins")

user_01.describe_user()
user_01.greet_user()