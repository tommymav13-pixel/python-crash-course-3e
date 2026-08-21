class User:
    """Represent a user profile."""

    def __init__(
        self,
        first_name,
        last_name,
        user_age,
        user_mail,
        user_github,
    ):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age
        self.user_mail = user_mail
        self.user_github = user_github

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
        print(f"Age: {self.user_age}")
        print(f"Email: {self.user_mail}")
        print(f"GitHub: {self.user_github}")

    def greet_user(self):
        """Print a personalized greeting."""
        print(
            f"Welcome, {self.first_name.title()} "
            f"{self.last_name.title()}!"
        )


user_01 = User(
    "tommy",
    "veenhuizen",
    35,
    "tommy.mav13@gmail.com",
    "tommymav13-pixel",
)

user_01.describe_user()
user_01.greet_user()