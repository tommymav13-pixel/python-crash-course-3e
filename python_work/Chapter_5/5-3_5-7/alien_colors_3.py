# Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
alien_color = ['green', 'yellow', 'red']
# Write 3 versions of this program, making sure each message is printed for a 
# different color alien.
# Version 1: Green alien
alien_colors = ['green']
if 'green' in alien_colors:
    print("You earned 5 points!")
elif 'yellow' in alien_colors:
    print("You earned 10 points!")
elif 'red' in alien_colors:
    print("You earned 15 points!")
else:
    print("No points earned.") 

# Version 2: Yellow alien
alien_colors = ['yellow']
if 'green' in alien_colors:
    print("You earned 5 points!")
elif 'yellow' in alien_colors:
    print("You earned 10 points!")
elif 'red' in alien_colors:
    print("You earned 15 points!")
else:
    print("No points earned.")

# Version 3: Red alien
alien_colors = ['red']
if 'green' in alien_colors:
    print("You earned 5 points!")
elif 'yellow' in alien_colors:
    print("You earned 10 points!")
elif 'red' in alien_colors:
    print("You earned 15 points!")
else:
    print("No points earned.")

