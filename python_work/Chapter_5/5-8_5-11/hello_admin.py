user_names = ['admin', 'user1', 'user2', 'user3', 'user4']
for name in user_names:
    if name == 'admin':
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

# Assignment 5-10: Checking for an empty list
user_names = []
if not user_names:
    print("We need to find some users!")

# Assignment 5-10: Do the following to create a program that simulates how 
# websites ensure that everyone has a unique username. 

# Make a list of five or more usernames called current_users. 
current_users = ['admin', 'user1', 'user2', 'user3', 'user4']

# Then make another list of five usernames called new_users. 
new_users = ['user5', 'user6', 'admin', 'user7', 'user8']

# Check whether each proposed username is already in use.
# Print an appropriate message for each username.
for new_user in new_users:
    if new_user in current_users:
        print(
            f"Sorry, {new_user} is already taken. " 
            "Please enter a new username."
              )
    else:
        print(f"{new_user} is available.")
 